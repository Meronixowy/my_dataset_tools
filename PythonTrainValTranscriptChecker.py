# https://github.com/Meronixowy
import os

def check_and_save_corrected_file(input_filename, output_filename):
    updated_lines = []
    with open(input_filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split('|')
            wav_path = parts[0]
            if os.path.exists(wav_path):
                updated_lines.append(line)
            else:
                print(f"File '{wav_path}' does not exist. Removing the line.")
    
    with open(output_filename, 'w', encoding='utf-8') as file:
        for line in updated_lines:
            file.write(line)

if __name__ == "__main__":
    input_files = ["list_train.txt", "list_val.txt"]
    output_files = ["list_train.txt", "list_val.txt"]
    
    for input_file, output_file in zip(input_files, output_files):
        check_and_save_corrected_file(input_file, output_file)
        print(f"Processed '{input_file}' and saved corrected version to '{output_file}'.")
