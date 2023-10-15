#!/bin/bash



descriptor_dir="./descriptors"
files=($(ls "$descriptor_dir"))
#files=("file1" "file2" "file3" "file4" "file5")

# Output directory
output_dir="output"

mkdir -p "$output_dir"

for f in "${files[@]}"; do
    # Run Python script with the -f argument and save the output to a file
    python main.py -f "$descriptor_dir/$f" >> "$output_dir/output_231016.txt"
    echo "Executed 'python main.py -f $f'"
done





