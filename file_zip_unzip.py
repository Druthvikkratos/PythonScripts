import os
import shutil
import zipfile

def file_zip(file1, file2, folder_name, zip_name):
    # If Folder not available create one
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    #copy files to folder
    shutil.copy(file1, folder_name)
    shutil.copy(file2, folder_name)


    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for root, files in os.walk(folder_name):
            for file in files:
                file_path = os.path.join(root, file)
                #zipf.write(file_path, os.path.realpath(file_path))
                zipf.write(file_path, os.path.relpath(file_path, folder_name))
    print(f"created zip file: {zip_name}")

def unzip(zip_name, extract_folder):
     # If Folder not available create one
    if not os.path.exists(extract_folder):
        os.makedirs(extract_folder)
    
    with zipfile.ZipFile(zip_name, 'r') as zipf:
        zipf.extractall(extract_folder)
        print("Folder unzipped successfull")

fileName1 = 'watermark.pdf'
fileName2 = 'watermarked.pdf'
folderName = 'zipfolder'
zipName = 'zippedFolder.zip'
extractTo = 'unzipped_folder'

#file_zip(fileName1, fileName2, folderName, zipName)
unzip(zipName, extractTo)