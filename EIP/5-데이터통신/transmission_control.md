# 전송제어(Transmission Control)
데이터의 원활한 흐름을 위한 입출력 제어, 회선 제어, 동기 제어, 오류 제어, 흐름 제어, 보완제어
- OSI7 참고모델의 2계층, 데이터 링크 계층에서 수행

## 전송 제어 절차
1. 데이터 통신 회선의 접속
- 통신 회선과 단말기의 물리적 접속
- 포인트 투 포인트(Point to Point)나 멀티 포인트(Multi Point) 방식으로 연결된 경우에 필요

2. 데이터 링크 설정(확립)
- 논리적 경로를 구성

3. 정보 메세지 전송
- 수신측 전송 및 오류제어와 순서제어를 수행

4. 데이터 링크 종결(해제)
- 논리적 경로 해제

5. 데이터 통신 회선 절단
- 물리적 접속 절단

## 전송 제어 문자
- SYN(Synchronous Idle) - 문자 동기
- SOH(Start of Heading) - 헤딩의 시작
- STX(Strat of text) - 본문의 시작
- ETX(End of Text) - 본문의 종료
- ETB(End of transmission Block) - 블록 종료
- EOT(End of Transmission) - 전송 종료
- ENQ(Enquiry) - 상대편에 응답 요구
- DLE(Date Link Escape) - 전송 제어 문자 앞에 삽입하여 전송제어 문자 알림. 문자의 투과성, 투명한 데이터 전달을 위함
- ACK(Acknowledge)/NAK(Negative Acknowledge) - 긍정응답/부정응답

# Reference
https://m.blog.naver.com/PostView.nhn?blogId=c_18&logNo=220687547123&proxyReferer=https%3A%2F%2Fwww.google.com%2F
https://tbbrother.tistory.com/20