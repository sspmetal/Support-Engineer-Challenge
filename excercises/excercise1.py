from sys import argv
import os


def multi_replace(search, replace, path):

    counter_contents = 0
    counter_names = 0
    filelist = []
    if not os.path.exists(path):
        print ('Path does not exist')
        return False
    for dirpath, dirs, files in os.walk(path):
        for filename in files:
            # replace contents
            indata = open((os.path.join(dirpath, filename)), errors='ignore').read()
            if search in indata:
                new = indata.replace(search, replace)
                output = open(os.path.join(dirpath, filename), "w")
                output.write(new)
                counter_contents += 1
                filelist.append(filename)
    print ('%s files renamed, %s files contents altered' % (counter_names, counter_contents))
    print ('Files that has been altered: ' , filelist)

    return True


script, search_str, replace_str, path_str = argv

multi_replace(search_str, replace_str, path_str)
