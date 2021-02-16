import os
import json

# read the source file location and the file name

src_file = 'text1.json'
src_dir = os.getcwd()
src_file_location = os.path.join(src_dir, src_file)
print(src_file_location)

# read the destination file location and file name while adding md extension

dest_ext = '.md' # declares extension for new file
dest_file = (os.path.splitext(src_file)[0]) + dest_ext # removes extension from source file
dest_file_location = os.path.join(src_dir, dest_file)
print(dest_file_location)

# write the source file contents to destination file

with open(src_file_location, 'r') as f1:
    with open(dest_file_location, 'w') as f2:
        for line in f1:
            f2.write(line)
            