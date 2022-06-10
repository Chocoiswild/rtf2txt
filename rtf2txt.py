
from striprtf.striprtf import rtf_to_text
import os
def convert_rtf_to_txt(filepath: str):
    rtf_name = filepath
    txt_name = f"{rtf_name.split('.')[0]}.txt"

    with open(rtf_name) as rtf_file, open(txt_name, "w") as txt_file:
        #read rtf file to memory
        rtf_text = rtf_file.read()
        #convert rtf text to plaintext
        txt = rtf_to_text(rtf_text, errors="ignore")
        #write plaintext to new .txt file with corresponding name
        for line in txt:
            txt_file.write(line)

def iterate_folder(path: str):
    for item in os.listdir(path):
        itempath = os.path.join(path, item)
        #if it's not a folder, attempt to convert to .txt
        if os.path.isfile(itempath):
            iterate_convert_file(itempath)
        #if it's a folder, iterate through it
        elif os.path.isdir(itempath):
            iterate_folder(itempath)

def iterate_convert_file(path: str):
    #ignore any files which are not .rtf
    if not ".rtf" in path:
        return
    #convert file from rtf to txt
    convert_rtf_to_txt(path)

print("Please write the path of the root folder")
print("This folder should contain other folders")
print("These folders should contain .rtf files you wish to convert to .txt")
target_directory = input("Path: ")

iterate_folder(target_directory)
print("Ding ding ding ding")