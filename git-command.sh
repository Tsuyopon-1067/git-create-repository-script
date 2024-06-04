#/bin/bash
repository_name=$(basename "$PWD")
user_name=$(git config --global user.name)
git init
echo "# "$repository_name >> README.md
git add README.md
git commit -m ":tada: first commit"
git branch -M main
git remote add origin git@github.com:$user_name/$repository_name.git
git push -u origin main
