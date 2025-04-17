import os

# Set the directory you want to search in
search_dir = 'C:\\Users\\gowth\\OneDrive\\Desktop'

# Loop through files and find .txt files
for root, dirs, files in os.walk(search_dir):
    for file in files:
        if file.endswith('hi.txt'):
            print(os.path.join(root, file))
