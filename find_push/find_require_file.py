import os 
all_files = []
def load_scan(path): 
    for dirName, subdirList, fileList in os.walk(path): 
        for filename in fileList: 
            if ".txt" in filename.lower(): 
                all_files.append(os.path.join(dirName,filename)) 
        print all_files
        return all_files

input_floder = r'home\allen\myproject_flask\repo\sss'
load_scan(input_floder)