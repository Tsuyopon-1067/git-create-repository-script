#/bin/bash
function gitnewrepo() {
    flag=$1
    if [[ "$flag" != "--public" && "$flag" != "--private" ]]; then
        echo "Error: The first argument must be either --public or --private."
        return 1
    fi

    repository_name=$(basename "$PWD")
    user_name=$(git config --global user.name)
    gh repo create $repository_name $flag
    git init
    echo "# "$repository_name >> README.md
    git add README.md
    git commit -m ":tada: first commit"
    git branch -M main
    git remote add origin git@github.com:$user_name/$repository_name.git
    git push -u origin main
}

gitnewrepo "$@"
