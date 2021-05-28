=======================
回退版本/撤销操作/删除操作

1. git reset --hard HEAD^  回退到上个commit,一个^是回退一步

2. git reset --hard <commit id> 回退到指定版本

3. git reflog   查看你的每一步命令

4.  git log   查看commit历史

5. git checkout -- <file>  丢弃工作区的修改, 这是相对于暂存区(stage)而言的

6.  git reset HEAD <file> 把暂存区的修改unstaged, 从新放回工作区

7.  git HEAD -- <file>  查看工作区和版本库内容的区别











========================
分支

1. git cheakout -b <branch name>  创建分支并切换到这个分支
相当于 git branch <branch name>   创建分支
            git checkout <branch name>  切换分支

2. git branch  查看当前所有分支

3. git checkout <branch name> 或   git switch <branch name>
 切换到指定分支

4. git merge <branch name> 用于合并指定分支到当前分支

5. git branch -d <branch name> 删除指定分支

6.git branch -D <branch name> 强行删除一个没有合并过的分支

========================
保存现场

1. 在当前分支的更改commit或者stash之前,是不能切换分支的

2. dev分支更改或者添加的内容stash或者commit之后切换到其他分支之后,
在其他分支看不到dev的更改,只有两个分支合并之后才
能在main看到之前dev上面的更改

3. 合并冲突, 当两个分支的更改是冲突的,执行合并本身就是一次
commit, (执行合并之后就默认了你已经更改冲突)可以忽视冲突,
再add,然后再进行一次commit

$ git stash   可以在任何工作状态保存现场

$ git stash list   查看保存的现场列表

两种恢复现场并删除stash的方法

1. 
$  git stash apply stash@{ 数字 }   恢复现场, 但是stash并没删除
$  git stash drop 删除(接着上一条命令,就会只删除已经恢复现场的stash)

2. 
$ git stash pop  弹出现场的同时删除stash

cat <file>  查看文件内容

============================
推送/抓取分支,@@@把本文件不断补充上传的时候会经常用这个功能

1. git remote -v  查看远程库信息

2. git push origin <branch name>  把该分支上的所有本地提交推送到远程库


========================
分支合并

1. git merge <branch name> 将指定分支的修改归并到当前分支
 这个操作会在该分支产生一个新的commit
例子,   
$ git checkout master
$ git merge test 
test 分支没有变化, test内容合并到master,master向前进一个提交

2. git rebase <branch name> 将当前节点的工作直接移到指定节点
@@@图解4种git合并分支方法（转载）看csdn收藏讲的很详细

3. git cherry-pick <commit id>  可以复制一次特定的提交到当前分支
           



========================
创建标签

1. git tag <tagname>  用于新建一个标签,默认为HEAD,(当前分支的最近一次提交)
也可以在后面追加commit id进行指定

2. git tag -a <tag name> -m'blablabla...' 可以指定标签信息

3. git tag 可以查看所有标签

4. git push origin <tagname> 推送一个本地标签到远程

5. git push origin --tags  可以推送全部未推送过的本地标签

6. git tag -d <tagname>可以删除一个本地标签；

7. git push origin :refs/tags/<tagname>可以删除一个远程标签。



