print('sunqi')
print('newadd')
print('git diff file name')
print('git add filename')
print('git status filename')
print('git commit -m')
print('git log')
print('git log --pretty=oneline')
print('git reflog')
print('git reset --hard HEAD^')
print('git reset --hard commit_id')
print('git checkout -- filename')
print('git rm filename;git commit -m ')
print()
print('github')
print('git remote add origin git@github.com:sq08201329/gitStroe.git')
print('git push -u origin master')
print('git clone git@github.com:sq08201329/gitStroe.git')
print()
print('git checkout -b branchname')
print('git checkout branchname')
print('git branch branchname')
print('git merge branchname')
feature1 and  featrue2
print('git log --graph --pretty=oneline -abbrev-commit')

branch dev added

brach dev add again
print('git merge --no-ff -m "" branchname')

print('git stash')
print('git stash list')
print('git stash apply')
print('git stash drop')
print('git stash pop')

print('git branch -d branchname')
print('git branch -D branchname')

git remote -v

git push remote_git local_branchname
git checkout -b branchname remote_git/remote_branchname
git branch --set-upstream branchname remote_git/branchname
git pull

git tag
git tag v1.0 commit_id
git tag -a v1.0 -m 'describe' commit_id

git show v1.0

git tag -d v0.1
git push origin v0.1
git push origin --tags
git tag -d v0.1
git push origin :refs/tags/v0.1

#����ʱ�
[user]
	email = sq08201329@126.com
	name = sunqi
[gui]
	recentrepo = D:/Python/me/gitStroe
	encoding = utf-8 #代码库统一使用utf-8  
	encoding = utf-8 #�����ͳһʹ��utf-8
[alias]
	st = status
[core]
	quotepath = false
[i18n]  
	commitencoding = GB2312 #log编码，window下默认gb2312,声明后发到服务器才不会乱码  
[svn]  
	pathnameencoding = GB2312 #支持中文路径
