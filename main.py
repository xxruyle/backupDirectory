import backup_File
import argparse 

def main(): 
    if args.list: 
        b1 = backup_File.backupDirectory(args.list)  
        b1.listDirectoryTxt()
    else:
        b1 = backup_File.backupDirectory(args.srcfiles)  
        b1.copyDirectory()

    
if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description="Backup directories on the command line")
    parser.add_argument("-s", "--srcfiles", metavar = "srcfiles", type = str, help = "The txt file containing the directories you want to backup")
    parser.add_argument("-d", "--destination", metavar = "destination", type = str, help = "The destination you want to copy the src files to")
    parser.add_argument("-l", "--list", metavar = "txtfile", type = str, help = "List all the included folders of a text file")
    args = parser.parse_args()
    main()