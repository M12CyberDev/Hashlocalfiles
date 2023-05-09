#!/usr/bin/python3

import pandas as pd
import os
import hashlib
from os import walk
from datetime import datetime


#current_path = os.getcwd()
path = 'path'

full_path_list = []
file_size_list = []
filename_list = []
file_creating_timestamp_list = []
hash_list = []

for (dirpath, dirnames, filenames) in walk(path):

    for filename in filenames:
        filename_list.append(filename)
        full_path = os.path.join(dirpath, filename)
        file_size = os.path.getsize(full_path)
        file_timestamp_unix = os.path.getctime(full_path)
        timestamp_create = datetime.fromtimestamp(file_timestamp_unix)
        full_path_list.append(full_path)
        file_size_list.append(file_size)
        file_creating_timestamp_list.append(timestamp_create)

        with open(full_path, 'rb') as file:
            md5hash = hashlib.md5()
            buffer = file.read(4096)

            while buffer:
                md5hash.update(buffer)
                buffer = file.read(4096)

            md5hex = md5hash.hexdigest()
            md5hash = str(md5hex).upper()
            hash_list.append(md5hash)


dict = {'filename': filename_list, 'fullpath': full_path_list, 'filesize': file_size_list, 'timestamp': file_creating_timestamp_list, 'md5hash': hash_list}
df = pd.DataFrame(dict)

print(df)
#df.to_csv('output.csv')

intersection_list = ['']
print(df['md5hash'])

for hash in df['md5hash']:
    if hash in intersection_list:
        print('Match ' + str(hash))
