# https://github.com/Meronixowy
with open('list_val.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

speaker_names = []

for line in lines:
    parts = line.strip().split('|')
    if len(parts) == 3:
        speaker_name = parts[2]
        if speaker_name not in speaker_names:
            speaker_names.append(speaker_name)

updated_data_text = 'speakers: ["{}"]'.format('", "'.join(speaker_names))

with open('speakers_list.txt', 'w', encoding='utf-8') as txt_file:
    txt_file.write(updated_data_text)

print("speakers:", speaker_names)
