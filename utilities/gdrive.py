import os
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

# Authenticate and create client
gauth = GoogleAuth()
gauth.LoadClientConfigFile(os.environ["GOOGLE_CLIENT_CONFIG_FILE_LOC"])
gauth.LocalWebserverAuth()  # opens a browser to log in
drive = GoogleDrive(gauth)

# List files
file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file in file_list:
    print(f"{file['title']} ({file['id']})")

# Upload file
f = drive.CreateFile({'title': 'example.txt'})
f.SetContentFile('example.txt')
f.Upload()

# Download file
f = drive.CreateFile({'id': 'FILE_ID'})
f.GetContentFile('downloaded_example.txt')
