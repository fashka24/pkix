# PKIX - package installer by simple script

## Example of python installer
```json
{
  "windows": {
    "download": {
      "py.exe": "https://www.python.org/ftp/python/3.13.3/python-3.13.3-amd64.exe"
    },
    "execute": [
      "./py.exe"
    ]
  },
  "unix": {
    "download": {
      "py.tar.xz": "https://www.python.org/ftp/python/3.13.3/Python-3.13.3.tar.xz"
    },
    "execute": [
      "tar -xf py.tar.xz", 
      "cd Python-3.13.3",
      "chmod +x install-sh",
      "./install-sh"
    ]
  }
}
```

## Executing
```shell
python main.py py-installer.pkix.json
```