from git import Repo

repo_dir = r'/home/allen/myproject_flask/repo'
repo = Repo(repo_dir)
file_list = [
    'sss/sss.md',
    'sss/sss.txt',
    'sss/sss.sh'
]
commit_message = 'Add simple_push sss'
repo.index.add(file_list)
repo.index.commit(commit_message)

origin = repo.remote('origin')
origin.push()