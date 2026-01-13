import string
import os

def analyze_text(input_filename, output_filename):
    line_count = 0
    word_count = 0
    word_frequencies = {}

    try:
        with open(input_filename, 'r', encoding='utf-8') as file:
            for line in file:
                line_count += 1
                clean_line = line.lower().translate(str.maketrans('', '', string.punctuation))
                words = clean_line.split()
                word_count += len(words)
                for word in words:
                    word_frequencies[word] = word_frequencies.get(word, 0) + 1

        with open(output_filename, 'w', encoding='utf-8') as result_file:
            result_file.write(f"Total lines: {line_count}\n")
            result_file.write(f"Total words: {word_count}\n")
            result_file.write("\nWord Frequencies:\n")
            for word, freq in word_frequencies.items():
                result_file.write(f"{word}: {freq}\n")
        
        print(f"Analysis completed. {output_filename}")

    except FileNotFoundError:
        print(f"Error: File {input_filename} not found.")

if __name__ == "__main__":
    base_path = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_path, 'text.txt')
    output_path = os.path.join(base_path, 'analysis.txt')
    
    analyze_text(input_path, output_path)