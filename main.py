import backup_File
import argparse 

def main(): 
    b1 = backup_File.backupDirectory(args.srcfiles, args.destination)  
    b1.copyDirectory()

    
if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description="Backup directories on the command line")
    parser.add_argument("-s", "--srcfiles", metavar = "srcfiles", type = str, help = "The txt file containing the directories you want to backup")
    parser.add_argument("-d", "--destination", metavar = "destination", type = str, help = "The destination you want to copy the src files to")
    args = parser.parse_args()
    main()