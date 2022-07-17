import os 
import shutil
from shutil import copy2 
from tqdm import tqdm 
import logging 


class backupDirectory(): 
    def __init__(self, directory_txt): 
        with open(directory_txt, 'r') as f: 
            directory_paths = f.read()

        self.directory_txt = directory_txt
        self.directory_list = directory_paths.split("\n")


        # Original Folder: Desitination Folder key value pair 
        self.directorySyntax = {}

        self.filecount = 0 

    def splitDestination(self): 
        for line in self.directory_list: 
            paths = line.split("->")
            if len(paths) != 2:
                raise Exception("{Source -> Destination} syntax is not correct. Please refer to Example.txt")
            self.directorySyntax[paths[0].strip()] = paths[1].strip()


    def copy2_verbose(self, src, dst):
        self.filecount += 1
        copy2(src, dst)

    def countFiles(self):
        count = 0 
        directories = list(self.directorySyntax)
        for d in directories: 
            count += len(os.listdir(d))

        return count 

    def copyDirectory(self): 
        self.splitDestination()
        for dirFolder in tqdm(list(self.directorySyntax), leave=True, desc=f"Backing Up: {self.directory_txt}"):
            new_folder = os.path.split(dirFolder)[-1]
            if os.path.isdir(dirFolder) and os.path.exists(dirFolder): 
                shutil.copytree(dirFolder, fr"{self.directorySyntax[dirFolder]}/{new_folder}", dirs_exist_ok=True)
            
                
    def listDirectoryTxt(self):  
        for dirFolder in self.directory_list:
            print(dirFolder)
