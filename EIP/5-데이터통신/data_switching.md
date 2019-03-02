# 데이터 교환(Data Switching)
떨어져 있는 두 장치가 서로 데이터를 송수신할 수 있도로 경로를 제공하며, 중간에 하나 이상의 교환기를 통하는 것이 원칙이다.

![](https://t1.daumcdn.net/cfile/tistory/2659F84A59037EDE03)

## 회선 교환 방식(Circuit Switching)
- 전체 네트워크에서 쌍으로만 연결
- 전화와 비슷하며, 1:1 연결이다. -> 통신 보장 x
- 점유되고 있으면 점유할 수 없다. -> 회선 고정할당
- 회선이 설정되어 있어야 사용 가능하다.

## **패킷 교환 방식**(Packet Switching)
- 현재 가장 많이 사용하고 있는 통신방식
- 축적과 전송이 이뤄진다,.
- 데이터를 전송하는 동안 네트워크 자원 사용
- 짤막한 데이터 트래픽에 적합하다.
- 회선의 사용률이 높고 높은 품질의 전송이 가능하다.
- 전송방식에 따라 2개로 나눠진다.
  - 가상 회선 방식(Virtual Circuit)
    - 이름과 달리 연결 지향성이다.
    - Frame relay, X.25, ATM이 사용
  > Frame relay : 사용자가 요구하는 만큼의 대역폭을 필요한 순간에만 쓰는 연결 서비스
  > ATM : Asynchronous Transfer Mode. 비동기 전달 모드이다.
  - 데이터 그램 방식(Datagram)
    - 비연결형이다.
    - IP가 사용한다.
    - 오버헤드가 적다.
    - 각 패킷마다 라우팅을 하므로 융통성이 있다.

# Reference
https://maktooob.tistory.com/64
https://m.blog.naver.com/PostView.nhn?blogId=zoph&logNo=220605517575&proxyReferer=https%3A%2F%2Fwww.google.com%2F