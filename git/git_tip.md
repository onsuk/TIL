# Git Tip
개인적으로 유용했던 git 명령어를 가볍게 정리하는 글이다.

- **add 취소하기** : `$ git reset HEAD [file]`
    - 파일명이 없으면 add한 파일 전체를 unstaged 상태로 변경한다.

- **commit 취소하기** 
    - unstaged 상태로 만들기 : `$ git reset HEAD^`
    - staged 상태로 만들기 : `$ git reset --soft HEAD^`

- **shallow clone** : `$ git clone --depth=1 [repo]`
    - `[repo]`의 복제가 만들어지며 가장 최근의 커밋만 복제된 Repository에 포함된다. 광범위한 커밋 내역이 있는 repository로 작업할 때 유용하다.

# Reference
[[Git] git add 취소하기, git commit 취소하기, git push 취소하기](https://gmlwjd9405.github.io/2018/05/25/git-add-cancle.html)