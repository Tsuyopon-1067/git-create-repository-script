# git-create-repository-script

## What is git-create-repository-script?

_git-create-repository-script_ can print or excute git command to excute in initializing repository.
Here is the command to be executed or printed when repository name is _HOGE_ and user name is _FUGA_.

```
git init
echo "# HOGE" >> README.md
git add README.md
git commit -m ":tada: first commit"
git branch -M main
git remote add origin git@github.com:FUGA/HOGE.git
git push -u origin main
```

## Usage

### shell script
- excute command
```
./git-command.sh
```

When an error `permission denied: ./git-command.sh` occurs, excute bellow.
```
chmod 755 git-command.sh
```

### python
- excute command

```
python3 git-command.py -e
```

- print command

```
python3 git-command.py -p
```

## excute without clone
### shell script
- excute command

```
curl https://raw.githubusercontent.com/Tsuyopon-1067/git-create-repository-script/main/git-command.sh | sh
```

### python
- excute command

```
curl -o git-command.py https://raw.githubusercontent.com/Tsuyopon-1067/git-create-repository-script/main/git-command.py && python3 git-command.py -e && rm git-command.py
```

- print command

```
curl -o git-command.py https://raw.githubusercontent.com/Tsuyopon-1067/git-create-repository-script/main/git-command.py && python3 git-command.py -p && rm git-command.py
```
