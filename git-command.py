import subprocess
import sys
import os


def main():
    args = sys.argv
    if len(args) <= 1:
        print('-e: excute command')
        print('-p: print command')
        exit()

    git_config_command_result = subprocess.run(
        ['git', 'config', '--global', 'user.name'],
        stdout=subprocess.PIPE, text=True)
    user_name = git_config_command_result.stdout.strip()
    current_dir = os.getcwd()
    repository_name = os.path.basename(current_dir)

    commands = ['git init']
    commands.append('echo "# {}" >> README.md'.format(repository_name))
    commands.append('git add README.md')
    commands.append('git commit -m ":tada: first commit"')
    commands.append('git branch -M main')
    commands.append(
        'git remote add origin git@github.com:{}/{}.git'.format(
            user_name, repository_name))
    commands.append('git push -u origin main')

    full_command = ' && '.join(commands)

    if args[1] == '-e':
        subprocess.run(full_command, shell=True)
    elif args[1] == '-p':
        print(full_command)


main()
