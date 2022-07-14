import os 
import shutil 
from tqdm import tqdm 

class backupDirectory(): 
    def __init__(self, directory_txt, destination): 
        with open(directory_txt, 'r') as f: 
            directory_paths = f.read()

        self.directory_list = directory_paths.split("\n")

        self.destination = destination

    def copyDirectory(self): 
        for dirFolder in tqdm(self.directory_list):
            new_folder = os.path.split(dirFolder)[-1]
            if os.path.isdir(dirFolder): 
                shutil.copytree(dirFolder, rf"{self.destination}\{new_folder}", dirs_exist_ok=True)
                print(rf"{self.destination}\{new_folder} Sucessfully backed up")