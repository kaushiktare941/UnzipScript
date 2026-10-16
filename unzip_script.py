import zipfile
import os 

print("Started")

extractionFolder = "" #set directory containing .zip files to be extracted
destinationFolder = "" #set destination directory
dirList = os.listdir(extractionFolder)

for item in dirList:
    print ("Now extracting " + item)
    with zipfile.ZipFile(extractionFolder + "/" + item, 'r') as zipref:
        zipref.extractall(destinationFolder)
    print("Extracted " + item)

print("Completed.")