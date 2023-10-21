import numpy as np
from src.dataset_readers.base_dsr import BaseDatasetReader
from src.utils.tokenizer_util import get_tokenizer
import logging
import random
logger = logging.getLogger(__name__)


class InferenceDatasetReader(BaseDatasetReader):

    def __init__(self, index_reader, n_tokens, task_name, model_name, field, dataset_path=None,
                 dataset_split=None, ds_size=None):
        self.tokenizer = get_tokenizer(model_name)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        self.tokenizer.pad_token_id = self.tokenizer.eos_token_id
        self.tokenizer.padding_side = "left"
        self.index_reader = index_reader
        self.n_tokens_in_prompt = n_tokens
        # set truncation to false so that metadata['len'] corresponds to metadata['text']
        self.init_dataset(task_name, field, dataset_path, dataset_split, ds_size, truncation=False)

    def get_ice_prompt(self, entry, prompt_len):
        if 'ctxs' in entry:
            ctx = [self.index_reader[i] for i in entry['ctxs']]

            num_to_replace = int(0.3 * len(ctx))
            indices_to_replace = random.sample(range(len(ctx)), num_to_replace)
            replacement_mapping = {'Yes': 'No', 'No': 'Yes'}
            
            for i in indices_to_replace:
                text = ctx[i]['metadata']['text']
                words = text.split()
                label = words[-1]
                label = replacement_mapping[label]
                words[-1] = label
                ctx[i]['metadata']['text'] = ' '.join(words)
                
                
            ice_prompts_list = [i['metadata']['text'] for i in ctx]
            #print(ctx[0]['metadata']['text'])
            ice_lengths_list = [i['metadata']['len'] for i in ctx]

            trunc_ice_prompts_list = self.truncate(prompt_len, ice_lengths_list, ice_prompts_list)
            ice_separator = self.dataset_wrapper.ice_separator
            ice_prompt = ice_separator.join(trunc_ice_prompts_list) + ice_separator
        else:
            trunc_ice_prompts_list = []
            ice_prompt = ""
        return ice_prompt, trunc_ice_prompts_list

    def __getitem__(self, index):
        entry = self.dataset_wrapper[index]
        prompt_len = self.encoded_dataset[index]['metadata']['len']
        prompt = self.encoded_dataset[index]['metadata']['text']

        ice_prompt, trunc_ice_prompts_list = self.get_ice_prompt(entry, prompt_len)
        # do not use format, as some prompts also contains {xxx} :(
        prompt = prompt.replace("{ice_prompt}", ice_prompt)
        

        entry['prompt'] = prompt + self.dataset_wrapper.a_prefix
        entry['ice_prompts_list'] = trunc_ice_prompts_list

        tokenized_example = self.tokenizer.encode_plus(entry['prompt'], truncation=False, return_tensors='pt',
                                                       add_special_tokens=False)

        return {
            'input_ids': tokenized_example.input_ids[0],
            'attention_mask': tokenized_example.attention_mask[0],
            "metadata": entry
        }

    def __len__(self):
        return len(self.dataset_wrapper)

    def shard(self, accelerator):
        self.dataset_wrapper.dataset = self.dataset_wrapper.dataset.shard(
            num_shards=accelerator.num_processes,
            index=accelerator.process_index
        )
        self.encoded_dataset = self.encoded_dataset.shard(
            num_shards=accelerator.num_processes,
            index=accelerator.process_index
        )
        assert len(self.dataset_wrapper.dataset) == len(self.encoded_dataset)

    def truncate(self, test_input_len, lengths_list, prompts_list):
        max_prompts = np.searchsorted(np.cumsum(lengths_list), self.n_tokens_in_prompt - test_input_len)
        # logger.info(self.n_tokens_in_prompt, max_prompts)
        trunc_prompts_list = prompts_list[:max_prompts][::-1]  # more similar more close
        return trunc_prompts_list

def random_noise(text, replacement_mapping):
    words = text.split()
    
    # Create a list to store the indices of words to replace
    replace_indices = []
    
    # Identify the indices of words to replace
    for i, word in enumerate(words):
        if word in replacement_mapping:
            replace_indices.append(i)
    
    # Calculate the number of occurrences to replace (e.g., 30%)
    num_to_replace = int(0.3 * len(replace_indices))
    indices_to_replace = random.sample(replace_indices, num_to_replace)
    print(replace_indices)
    # Iterate through the selected indices and replace the words
    for index in indices_to_replace:
        words[index] = replacement_mapping[words[index]]
        print(words[index])
    
    new_text = ' '.join(words)
    return new_text