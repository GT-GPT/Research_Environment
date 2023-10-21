#!/bin/bash



descriptor_dir="./descriptors"
#files=($(ls "$descriptor_dir"))
files=("imagenet_object_2_feature_2_detailed.json" "imagenet_object_2_feature_3_detailed.json" "imagenet_object_2_feature_4_detailed.json" "imagenet_object_2_feature_5_detailed.json")

#files=("imagenet_object_2_feature_5.json" "imagenet_object_2_feature_6.json" "imagenet_object_2_feature_7.json")

# Output directory
output_dir="output"

mkdir -p "$output_dir"

for f in "${files[@]}"; do
    # Run Python script with the -f argument and save the output to a file
    python main.py -f "$descriptor_dir/$f" >> "$output_dir/output_231020_entropy_d.txt"
    #python main.py -f "$descriptor_dir/$f" # for checking output in terminal
    echo "Executed 'python main.py -f $f'"
done





