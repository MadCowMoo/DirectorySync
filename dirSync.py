from shutil import copyfile
import os.path
import os
from os import walk

def doSync(src,dest):
    curFiles = []
    curDirs  = []
    for (dirpath, dirnames, filenames) in walk(src):
        print "starting at " + dirpath
        print "     dirs=" + str(len(dirnames))
        print "     files=" + str(len(filenames))
        for fn in filenames:
            if not os.path.isfile(dest + "/" + fn):
                # copy files from src to dest
                print "copying " + dirpath + "/" + fn + " to " + dest + "/" + fn
                copyfile(src + "/" + fn, dest + "/" + fn)
        for d in dirnames:
            # recurse into subdirs
            newSrcDir = src + "/" + d
            newDestDir = dest + "/" + d
            # if newDestDir does not exist, create newDestDir
            if not os.path.exists(newDestDir):
                os.makedirs(newDestDir) 
            print "Directory: " + dirpath + "/" + d
            doSync(newSrcDir, newDestDir)
        break


doSync("/Users/me/Dev", "/Users/me/CopyDev")