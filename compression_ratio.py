import os


compressed_files = '/home/tanay/Projects/BugBox/compressed_files'
raw_files = '/home/tanay/Projects/BugBox/raw_files'

with open('compression.csv', 'a') as log:
    for file in os.listdir(compressed_files):
        compressed_size = os.stat(compressed_files+'/'+file).st_size
        raw_file_size = os.stat(raw_files+'/'+file).st_size
        data = [file, raw_file_size, compressed_size,
        raw_file_size/compressed_size, (raw_file_size-compressed_size)/raw_file_size]
        data = [str(x) for x in data]
        log.write(','.join(data)+'\n')
