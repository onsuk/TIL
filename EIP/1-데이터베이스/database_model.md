# 데이터베이스 모델(Database Model)
데이터 베이스 모델은 크게 관계형 데이터 모델, 계층형 데이터 모델, 네트워크형 데이터 모델이 있다. 하지만 중요한 것은 실제 사용하는 대부분의 DBMS는 관계형 데이터베이스 모델을 따르고 있다는 것이다. 계층형, 네트워크형은 어떤 개념인지만 어렴풋이 이해하고 있으면 충분하다.

## 계층형 데이터 모델
- 트리 형태의 수직적인 데이터 모델이다.
- 1:N의 대응 관계만 존재한다.
- 상위 레코드 삭제 시 연쇄 삭제(Triggered Delete)가 일어난다.
- 개체들 간에는 Cycle이 허용되지 않는다.
- 관계형 모델에서의 Entity를 계층형에선 Segment라 부른다.
- 파일 시스템을 생각하면 이해하기 쉽다. 풀더 안에 하위 폴더 안에 파일이 있는 형태이다. 여러 하위 폴더가 한 상위폴더에 있을 수는 있지만 한 하위폴더가 상위폴더에 위치할 순 없다.
- 대표적인 DBMS는 IBM의 IMS가 있다.

## 네트워크형 데이터 모델
- 계층형의 단점을 좀 더 보완한 데이터 모델이다.
- 상하위 레코드 사이에서 N:N 구조를 허용한다.
- CODASYL이란 회사에서 DBTG라는 데이터베이스로 출시하며 제안한 모델로, CODASYL DBRG모델이라고 불리기도 한다.
- 정확한 비유는 아니지만, 바로가기(링크)가 자유롭게 사용되는 파일 시스템을 떠올리면 어떤 계층형에 비해 어떤 보완이 이루어졌는지 이해하기 쉽다. 하위에서 상위로의 이동이 자유로우며 여러 상위 계층으로의 이동도 자유로운 것이다.
- 여기선 상하위 관계를 Owner, Member라고 표현한다.
- 대표적인 DBMS는 DBTG, EDBS, TOTAL 등이 있다.

## 관계형 데이터 모델
- 계층형, 네트워크형의 단점을 보완한 현재 가장 이상적인 모델이다.
- 우리가 흔히 보는 TABLE(표)들로 구성되고 표의 칼럼 간 관계가 정의되는 구조의 DB가 관계형 데이터 모델이다.
- 대표적인 DBMS로 오라클, MySQL, MsSQL, SQLite 등 우리가 아는 거의 모든 데이터베이스들이 여기 속한다.
- DBMS간 변환이 용이하다.
- 많은 연산에 대해 계층형이나 네트워크형보다 퍼포먼스가 떨어지는 경우가 많다.

# Reference
https://raisonde.tistory.com/entry/%EC%8B%9C%ED%97%98%EB%8C%80%EB%B9%84-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4-%EB%AA%A8%EB%8D%B8%EC%9D%98-%EC%A2%85%EB%A5%98%EC%99%80-%ED%8A%B9%EC%A7%95%EC%9D%84-%EC%89%BD%EA%B2%8C-%EC%9D%B4%ED%95%B4%ED%95%98%EC%9E%90