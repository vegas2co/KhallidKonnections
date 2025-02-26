def count_words_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        return "File not found!"
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
file_path = "/Users/khallidwilliams/Desktop/Move_Me/2025_Resume.docx"
word_count = count_words_in_file(file_path)
print(f"Total words in file: {word_count}")