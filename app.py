import os
import yaml
import tabula

config_file = 'config.yaml'

# Get the files and folders from config file
def get_configs():
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
        folders = []
        files = []
        if 'folders' in config:
            folders = config['folders']
        if 'files' in config:
            files = config['files']

        return files, folders


# Get files from directories
def get_all_files(directries):
    if not directries:
        return []
    files_list = []
    for directory in directries:
        for root, dirs, files in os.walk(directory):
            for file in files:
                files_list.append(os.path.join(root, file))
    return files_list

# Parse statement files and print the table
def parse(files, folders = None):
    files += get_all_files(folders)
    print(f'Total files to parse: {len(files)}')
    for f in files:
        print(f'Parsing {f}')
        dfs = tabula.read_pdf(f, stream=True)
        print(dfs[0])

if __name__ == '__main__':
    files, folders = get_configs()
    parse(files, folders)