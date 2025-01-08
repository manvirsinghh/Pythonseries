import os

# Define the file path
file_path = 'your_file.txt'  # Replace with your file path

try:
    file_size = os.path.getsize(file_path)  # Get the file size in bytes
    print(f"The size of the file is {file_size} bytes.")
except FileNotFoundError:
    print(f"The file at {file_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
