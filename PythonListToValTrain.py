# https://github.com/Meronixowy
# code taken from: https://github.com/Herob527/create_lists_for_tacotron_training
from pathlib import Path
from pydub import AudioSegment
from operator import itemgetter
from os.path import join

datasets_dirs = files = [x for x in Path("./datasets").glob('*') if x.is_dir()]

for dir in datasets_dirs:
    print(dir)
    filename = join(dir, 'list.txt')
    train_file = join(dir, 'list_train.txt')
    val_file = join(dir, 'list_val.txt')
    path_wavs = join(dir, 'wavs')
    validation_share = 10

    files = []

    with open(filename, 'r', encoding='utf8') as list_input:
        for entries in list_input.readlines():
            file, text = entries.split('|')
            length = AudioSegment.from_file(join(dir, file)).duration_seconds
            files.append({'file': file, 'text': text, 'length': length})

    amount_of_files = len(open(filename, 'r', encoding='utf8').readlines())
    validation_data_amount = amount_of_files // validation_share
    train_data_amount = amount_of_files - validation_data_amount

    sorted_files = sorted(files, key=itemgetter('length'), reverse=True)
    train_files = [f"{i['file']}|{i['text'].strip()}\n" for i  in sorted_files[validation_data_amount:]]
    val_files = [f"{i['file']}|{i['text'].strip()}\n" for i  in sorted_files[:validation_data_amount]]

    with open(train_file, 'w', encoding='utf8') as output_train, open(val_file, 'w', encoding='utf8') as output_val:
        output_train.writelines(train_files)
        output_val.writelines(val_files)
