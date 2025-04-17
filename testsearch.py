import os

# Replace this with the full path to your test folder
search_dir = r" C:\\Users\\gowth\\OneDrive\\Desktop"  # Or "/home/user/test_folder" for Linux/macOS

for root, dirs, files in os.walk(search_dir):
    for file in files:
        if file.endswith('hi.txt'):
            print(os.path.join(root, file))
            