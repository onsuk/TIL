# ARQ(Automatic Repeat Request)
데이터 통신 시스템에서 에러 발생 시 이를 송신 측에 알리고 송신 측은 에러가 발생한 프레임을 전송하는 방식이다.

## 종류
1. Stop and Wait ARQ (정지 대기방식))
- 송신측이 1개의 프레임을 송신하면 수신측이 에러 유무를 판단하여 송신측에 ACK 또는 NAK를 보내는 방식
- 구현 방식은 단순하나 ACK를 수신할 때까지 다음 프레임을 전송하지 못하므로 전송 효율이 떨어진다.

2. Go back N ARQ (연속적 ARQ)
- 송신 측이 윈도우 크기만큼의 프레임을 순서번호에 따라 연속 전송하고 에러 검출 시 발생한 프레임의 순서대로 송신측에 전송하면 송신측이 에러가 발생한 프레임 이후의 프레임부터 전송하는 방식.

3. Selective ARQ (선택적 ARQ)
- 송신측이 NAK를 받은 프레임부터 연속 재전송하는 Go back N ARQ와 달리 NAK에 해당하는 프레임만을 전송하는 방식.
- 효율은 좋으나 구조가 복잡하다.

4. Adaptive ARQ (적응형 ARQ)
- 통신 회선이 에러 발생률을 감지하여 가장 적절한 프레임의 길이를 동적으로 변경하여 보내는 방식. (회선 불량 프레임 짧게, 회선 양호 프레임 길게)
- 전송 효율은 좋으나 제어회로가 복잡하고 채널 대기시간 발생.

# Reference
https://m.blog.naver.com/PostView.nhn?blogId=thorong&logNo=70146941807&proxyReferer=https%3A%2F%2Fwww.google.com%2F