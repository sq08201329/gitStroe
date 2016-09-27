git pull
git add *
git status
git commit -m "auto commit at $(date) $1"
git diff HEAD~1  HEAD
git push origin master
