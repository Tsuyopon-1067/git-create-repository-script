# git-create-repository-script

## what is git-create-repository-script

git-create-repository-script can print or excute git command to excute in initializing repository.
Here is the command to be executed or printed when repository name is _HOGE_.

- **You have to change use name.**

```
git init
echo "# HOGE" >> README.md
git add README.md
git commit -m ":tada: first commit"
git branch -M main
git remote add origin git@github.com:Tsuyopon-1067/HOGE.git
git push -u origin main
```

## usage

- excute command

```
python3 git-command.py -e
```

- print command

```
python3 git-command.py -e
```

## excute without clone

- excute command

```
curl -o git-command.py https://raw.githubusercontent.com/Tsuyopon-1067/git-create-repository-script/main/git-command.py && python3 git-command.py -e && rm git-command.py
```

- print command

```
curl -o git-command.py https://raw.githubusercontent.com/Tsuyopon-1067/git-create-repository-script/main/git-command.py && python3 git-command.py -p && rm git-command.py
```
