import gitlab
import subprocess

# private token or personal token authentication
gl = gitlab.Gitlab('https://motorcode.concirrusquest.com', private_token='CzwME9zCCw2WiCmq-C8x')

# projects = gl.projects.list(all=True)
# for project in projects:
#     print(project.id)
#     print(project.name)
#     print(project.ssh_url_to_repo)
#     print("\n")



project = gl.projects.get(127, 126)
#print(project.attributes)  # displays all the attributes
git_url = project.ssh_url_to_repo
print(git_url)
#Not Working
#subprocess.call(['cd', '/Users/vipinkumar/Documents/Modules/quest/motor'])
subprocess.call(['git', 'clone', git_url])
#branch = project.branches.get('master')
print(branch)