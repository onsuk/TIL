# HDLC(High-level Data Link Control)

## HDLC란?
- 데이터 통신이 발달하여 컴퓨터 사이에 고속의 효율 높은 전송이 필요하게 되어 ISO에서 HDLC를 제정했다.
- HDLC 절차는 임의의 비트 길이의 정보를 프레임이라는 전송 제어 단위로 분할하여 프레임 내의 제어 정보에 포함한 명령과 응답을 이용하여 연속적인 정보를 전달하게 하는 전송 제어 절차이다.
- 포인트 투 포인트어ㅘ 멀티포인트 링크 상에 반이중이나 전이중 통신을 지원하기 위하여 설계된 비트 중심의 데이터링크 프로토콜이다.
- LLC(Logical Link Control, Lan에서 사용), PPP(Point-to-Point Protocol, 인터넷에서 사용), LAP-D(Link Access P:rocedure, D Channel, ISDN에서 사용)과 같은 많은 데이터 링크 제어 프로토콜들의 전신이다.

## HDCL 동작 모드
1. 정규 응답 모드(NRM - Normal Response Mode)
- 불균형적 링크 구성
- 주국이 세션을 열고, 종국들은 단지 응답만 한다.
![](http://cfile239.uf.daum.net/image/2312CE345566A94A316B58)

2. 비동기 평형모드(AMB - Asynchronous Balanced Mode)
- 균형적 링크 구성
- 각 국이 주국이자 종국으로 서로 대등하게 균형적으로 명령과 응답하며 동작
- 가장 널리 사용(전이중 점대점 링크에서 가장 효과적으로 사용 가능)
![](http://cfile233.uf.daum.net/image/2472353A5566A96624E098)
3. 비동기 응답모드(ARM, Asynchronous Response Mode)
- 종국도 전송할 필요가 있는 특수한 경우에만 사용
- 종국은 주국의 허가없이 응답 가능하다.
![](http://cfile221.uf.daum.net/image/2445C8365566A9850B25CC)