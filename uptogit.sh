find . -name .DS_Store | xargs rm -rf
git add --all
git branch -M main
git commit -m "Initial Commit"
git push -u origin main