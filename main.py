import requests
import os
import json
import sys
import subprocess
from colorama import init, Fore, Style

init(autoreset=True)

OS_NAME = "windows" if os.name == "nt" else "unix"

# READ JSON FILE IN INPUT
def read_json(path):
    with open(path, 'r', encoding="utf-8") as json_file:
        loaded_data_from_file = json.load(json_file)
    return loaded_data_from_file

# DOWNLOAD FILE FROM URL
def download_file(url, save_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

    except requests.exceptions.RequestException as e:
        print(f" >> error: {Fore.RED}{e}{Style.RESET_ALL}")

# EXECUTE/PARSE JSON FILE
def exec_file(path):
    print(f" >> start installing script: {Fore.GREEN}{path}{Style.RESET_ALL}")
    parsed_json = read_json(path)

    to_install = parsed_json[OS_NAME]['download']
    to_execute = parsed_json[OS_NAME]['execute']

    for url in to_install:
        print(f" >> downloading: {Fore.CYAN}{url}{Style.RESET_ALL}")
        download_file(to_install[url], url)

    for exc in to_execute:
        x = subprocess.run(exc.split(' '))
        print(f" >> return code: {Fore.MAGENTA}{x.returncode}{Style.RESET_ALL}")

def main():
    args = sys.argv[1::]

    for arg in args:
        exec_file(arg)
        print(f" >> installed: {Fore.GREEN}{arg}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
