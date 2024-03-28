def save_text_to_file(text, file_path):
    try:
        with open(file_path, 'w') as file:
            file.write(text)
        print("Text saved successfully to", file_path)
    except Exception as e:
        print("An error occurred while saving the text:", str(e))

# Example usage:
text_content = "This is the content of the text file."
file_path = "example.txt"
save_text_to_file(text_content, file_path)
