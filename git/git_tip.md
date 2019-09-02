# Git Tip
개인적으로 유용했던 git 명령어를 가볍게 정리하는 글이다.

- **add 취소하기** : `$ git reset HEAD [file]`
    - 파일명이 없으면 add한 파일 전체를 unstaged 상태로 변경한다.

- **commit 취소하기** 
    - unstaged 상태로 만들기 : `$ git reset HEAD^`
    - staged 상태로 만들기 : `$ git reset --soft HEAD^`

# Reference
[[Git] git add 취소하기, git commit 취소하기, git push 취소하기](https://gmlwjd9405.github.io/2018/05/25/git-add-cancle.html)