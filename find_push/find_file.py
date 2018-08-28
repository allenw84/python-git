import os
mypath = r'/home/allen/myproject_flask/repo'
files = []
#os.listdir(mypath)
#files = [f for f in os.walk(path) if os.path.isfile(f)] 
need_filename = raw_input("FileName:" )

'''
for f in files:
        fullpath = os.path.join(mypath,f)
        if os.path.isdir(fullpath):
                if need_filename in fullpath:
                        need_fullpath = fullpath
                        print fullpath 
                        if os.path.isfile(fullpath):                             
                                if ".txt" or ".py" in f.lower(): 
                                         print f 
'''
fullpath = os.path.join(mypath,need_filename)
print fullpath 
need_list = os.listdir(fullpath)  
#print os.listdir(fullpath)
for i in range(0, len(need_list)) :
        need_list[i] = need_filename +'/'+  need_list[i]
#print need_list

'''for need_file in os.listdir(fullpath):
        #if os.path.isfile(file): #why
        if ".txt" or ".sh" in need_file.lower():
                        files.append(need_file)
                        print (files)
     '''

'''      
for f in os.listdir(fullpath):
        if os.path.isfile(f):
                print f 
                files.append(f)
 '''    