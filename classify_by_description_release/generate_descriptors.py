import os
import openai
import json

import itertools

from descriptor_strings import stringtolist, openai_imagenet_classes
from templates import templates

openai.api_key = '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' #FILL IN YOUR OWN HERE

def generate_prompt_zeroshot(category_name):
    return f"""Q: What are useful visual features for distinguishing a {category_name} in a photo?
A: There are several useful visual features to tell there is a {category_name} in a photo:
- """
    
def generate_prompt(category_name: str):
    # you can replace the examples with whatever you want; these were random and worked, could be improved
    return templates['three_shots'] + f"""Q: What are useful visual features for distinguishing a {category_name} in a photo?
A: There are several useful visual features to tell there is a {category_name} in a photo:
- """


# generator 
def partition(lst, size):
    for i in range(0, len(lst), size):
        yield list(itertools.islice(lst, i, i + size))
        
def obtain_descriptors_and_save(filename, class_list):
    responses = {}
    descriptors = {}
    
    prompts = [generate_prompt(category.replace('_', ' ')) for category in class_list]
    
    
    # most efficient way is to partition all prompts into the max size that can be concurrently queried from the OpenAI API
    responses = [openai.Completion.create(model="text-davinci-003",
                                            prompt=prompt_partition,
                                            temperature=0.,
                                            max_tokens=100,
                                            ) for prompt_partition in partition(prompts, 20)]
    response_texts = [r["text"] for resp in responses for r in resp['choices']]
    descriptors_list = [stringtolist(response_text) for response_text in response_texts]
    descriptors = {cat: descr for cat, descr in zip(class_list, descriptors_list)}

    # save descriptors to json file
    if not filename.endswith('.json'):
        filename += '.json'
    with open(filename, 'w') as fp:
        json.dump(descriptors, fp)
    

obtain_descriptors_and_save('imagenet_object_3_simple', openai_imagenet_classes)


