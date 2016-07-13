
# coding: utf-8

# In[5]:

import sys
import glob
import re
import time
import os

def Get_Root(arguments) :
    possible_arguments = ["--file","--directory","-f","-d","-m"]
    for arg in possible_arguments :
        arguments = re.sub(arg,"",arguments)
    
    return (arguments.strip())

def List_file(root,_list_mod_info) :
    try :
         
        if os.path.isdir(root) :
           root = root+"\*"
        file_to_print = glob.glob(root)
        for each_file in file_to_print :
            print each_file
            if _list_mod_info :
                st = os.stat(each_file)
                print "modified on:", time.asctime(time.localtime(st.st_mtime))
    except :
        print "\nUnable to process the arguments"

def List_dir(root,_list_mod_info) :
    try :
        all_items = os.listdir(root)
        for item in all_items:
            if os.path.isdir(root+"\\"+item):
               sub_dir = root+"\\"+item
               print(sub_dir)
               if _list_mod_info :
                  st = os.stat(sub_dir)
                  print "modified on:", time.asctime(time.localtime(st.st_mtime))
    except :
        print "\nUnable to process the arguments !"


if __name__ == "__main__" :
    
    arguments = " ".join(sys.argv[1:]) 
    
    _list_file = False
    _list_dir = False
    _list_mod_info = False
    
    if len(re.findall("-f |-f\s.*-",arguments)) != 0  or len(re.findall("--file |--file\s.*-",arguments)) != 0:
        _list_file = True
        
    if len(re.findall("-d |-d\s.*-",arguments)) != 0  or len(re.findall("--directory |--directory\s.*-",arguments)) != 0:
        _list_dir = True
        
    if len(re.findall("-m |-m\s.*-",arguments)) != 0 :
        _list_mod_info = True
        
    root = Get_Root(arguments)
        
    if _list_file :
        List_file(root,_list_mod_info)
    if _list_dir :
        List_dir(root,_list_mod_info)
    

