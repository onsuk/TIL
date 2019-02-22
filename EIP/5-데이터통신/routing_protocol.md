# 라우팅 프로토콜(Routing Protocol)

## 라우팅(Routing)이란?
패킷(packet)을 전송하기 위한 수많은 경로 중에서 한 가지 경로를 결정하는 것이다. 라우팅에는 동적 라우팅(Dynamic Routing)과 정적 라우팅(Static Routing)이 있는데, 동적 라우팅은 변화하는 상황에 맞추어 라우터가 경로를 재설정하고 정적 라우팅은 주로 사람이 수동으로 미리 경로를 지정하는 방식이다.

## 라우팅 프로토콜(Routing Protocol)이란?
라우팅을 위해서 네트워크 상의 모든 라우터(Router)들은 목적지에 따라서 패킷을 보낼 Interface를 선 계산 해놓아야 하는데 이 계산을 해놓은 것을 **라우팅 테이블**이라고 한다.
그리고 **라우팅 테이블을 생성, 유지 업데이트, 전달**하는 프로토콜을 라우팅 프로토콜이라고 한다.

## 라우팅 프로토콜 구성
1) Routing Table
- 패킷을 목적지로 라우팅할 때 참조하는 테이블
- 목적지 주소, Output I/F, Metric 값

2) Message
- 라우터 간 라우팅을 위해 교환하는 메세지
- 이웃 도달 메세지, 라우팅 정보

3) Metric
- 라우팅 테이블 생성 및 업데이트 시 최적의 경로를 결정하는 기술
- 경로 길이, 홉(Hop) 수, 대역폭, 비용, 신뢰성

## 라우팅 프로토콜의 종류
![](https://t1.daumcdn.net/cfile/tistory/242FEE3D58161E7923)

1) 라우팅 경로 고정 여부
- Static Routing Protocol
  - 수동식, 사람이 일일이 경로를 입력, 라우터 부하경감, 고속 라우팅 가능
  - 관리자의 관리부담 증가 및 정해진 경로 문제 발생시 라우팅 불가능
- Dynamic Routing Protocol
  - 라우터가 스스로 라우팅 경로를 동적으로 결정
  - RIP, IGRP, OSPF, EIGRP

2) 내/외부 라우팅
- Interior Gateway Protocol
  - AS 내에서의 라우팅을 담당하는 라우팅 프로토콜
  - RIP, IGRP, OSPF, EIGRP
- Exterior Gateway Protocol
  - 서로 다른 AS 사이에서 사용되는 라우팅 프로토콜
  - BGP, EGP

3) 라우팅 테이블 관리
- Distance Vector Algorithm
  - 라우팅 Table에 목적지까지 가는데 필요한 거리와 방향만을 기록 (인접 라우터)