import argparse
from shutil import copyfile
import os.path
import os
from os import walk


parser = argparse.ArgumentParser()
parser.add_argument("-src", "--source-root-dir", help="Source directory")
parser.add_argument("-dest", "--destination-root-dir", help="Destination directory")
parser.add_argument("-m", "--move", help="Files are to be moved rather than copied", action="store_true")
args = parser.parse_args()
src = args.source_root_dir
dest = args.destination_root_dir
isMoveMode = args.move


def doSync(src,dest):
    global isMoveMode
    curFiles = []
    curDirs  = []
    for (dirpath, dirnames, filenames) in walk(src):
        print "starting at " + dirpath
        print "     dirs=" + str(len(dirnames))
        print "     files=" + str(len(filenames))
        for filename in filenames:
            if not os.path.isfile(dest + "/" + filename):
                # copy or move files from src to dest
                messageStart = "moving " if isMoveMode else "copying "
                print messageStart + dirpath + "/" + filename + " to " + dest + "/" + filename
                if isMoveMode:
                    shutil.move(src + "/" + filename, dest + "/" + filename)
                else:
                    copyfile(src + "/" + filename, dest + "/" + filename)
        for curDir in dirnames:
            # recurse into subdirs
            newSrcDir = src + "/" + curDir
            newDestDir = dest + "/" + curDir
            # if newDestDir does not exist, create newDestDir
            if not os.path.exists(newDestDir):
                os.makedirs(newDestDir) 
            print "Directory: " + dirpath + "/" + curDir
            doSync(newSrcDir, newDestDir)
        break


doSync(src, dest)