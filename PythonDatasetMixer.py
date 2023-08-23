# https://github.com/Meronixowy
import os
import shutil
import json

main_folder = "datasets"
output_folder = "mixed_datasets"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

wavs_output_folder = os.path.join(output_folder, "wavs")
if not os.path.exists(wavs_output_folder):
    os.makedirs(wavs_output_folder)

folders = [folder for folder in os.listdir(main_folder) if os.path.isdir(os.path.join(main_folder, folder))]

data = {
    'name': '',
    'n_speakers': len(folders),
    'tacotron': '',
    'train_list': '',
    'actors': []
}

for speaker_id, speaker_folder in enumerate(folders):
    speaker_folder_path = os.path.join(main_folder, speaker_folder)
    mixed_list_train = []
    mixed_list_val = []

    list_train_path = os.path.join(speaker_folder_path, "list_train.txt")
    with open(list_train_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            wav_path, text = line.strip().split("|")
            filename = f"{speaker_id}_{os.path.basename(wav_path)}"
            #mixed_list_train.append(f"wavs/{filename}|{text}|{speaker_id}")
            mixed_list_train.append(f"wavs/{filename}|{text}|{speaker_folder}")
            shutil.copy(os.path.join(speaker_folder_path, "wavs", os.path.basename(wav_path)), os.path.join(wavs_output_folder, filename))

    list_val_path = os.path.join(speaker_folder_path, "list_val.txt")
    with open(list_val_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            wav_path, text = line.strip().split("|")
            filename = f"{speaker_id}_{os.path.basename(wav_path)}"
            #mixed_list_val.append(f"wavs/{filename}|{text}|{speaker_id}")
            mixed_list_val.append(f"wavs/{filename}|{text}|{speaker_folder}")
            shutil.copy(os.path.join(speaker_folder_path, "wavs", os.path.basename(wav_path)), os.path.join(wavs_output_folder, filename))

    mixed_list_train_path = os.path.join(output_folder, "list_train.txt")
    with open(mixed_list_train_path, "a", encoding="utf-8") as file:
        file.write("\n".join(mixed_list_train))
        file.write("\n")

    mixed_list_val_path = os.path.join(output_folder, "list_val.txt")
    with open(mixed_list_val_path, "a", encoding="utf-8") as file:
        file.write("\n".join(mixed_list_val))
        file.write("\n")

    actor_data = {
        'id': speaker_id,
        'name': speaker_folder,
        'waveglow': 'Vatras',
        'n_files': len(mixed_list_train) + len(mixed_list_val)
    }
    data['actors'].append(actor_data)

output_json_path = os.path.join(output_folder, "model_info.json")
with open(output_json_path, "w") as json_file:
    json.dump(data, json_file, indent=4)
