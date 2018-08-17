'''
import os
def FindPath():
        mypath = r'/home/allen/myproject_flask/repo'
        files = os.listdir(mypath)
        #files = [f for f in os.walk(path) if os.path.isfile(f)] 
        need_filename = raw_input("FileName:")

        for f in files:
                fullpath = os.path.join(mypath,f)
                if os.path.isdir(fullpath):
                        if need_filename in fullpath:
                         need_fullpath = fullpath
                         print need_fullpath 
         #       if ".txt" or ".py" in f.lower(): 
         #          print f 
                        return need_filename
'''
import os
from git import Repo
#def main():
mypath = r'/home/allen/myproject_flask/repo'
files = []
need_filename = raw_input("FileName:" )
fullpath = os.path.join(mypath,need_filename)
print fullpath 
need_list = os.listdir(fullpath)  

for i in range(0, len(need_list)) :
        need_list[i] = need_filename +'/'+  need_list[i]

#push the file 
repo_dir = '/home/allen/myproject_flask/repo'
repo = Repo(repo_dir)
commit_message = 'Add simple_push sss'
repo.index.add(need_list)
repo.index.commit(commit_message)

origin = repo.remote('origin')
origin.push()

#if __name__ == '__main__':
  #      main()