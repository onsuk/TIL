# 명령어 수행 사이클(Instruction Cycle)

- **명령어 인출**(Instruction Fetch) - 기억장치로부터 명령어를 읽어 온다.
- **명령어 해독**(Instruction Decode) - 명령어가 수행해야 할 동작을 결정하기 위하여 명령어를 해석한다.
- **데이터 인출**(Data Fetch) - 명령어 실행을 위해 데이터가 필요한 경우 기억장치에서 데이터를 읽어온다.
- **실행 사이클**(Execution Cycle) - 명령어 실행 시 기억장치에서 읽어온 데이터에 대한 산술연산 또는 논리 연산을 수행한다.
- **결과 저장** - 실행결과를 기억장치에 저장한다.

### 번외(?)
- **간접 단계**(Indirect Cycle) - 인출 단계에서 해석된 명령의 Operand 부가 간접 주소일 경우 유효 주소를 구하는 단계이다.
- **인터럽트 단계**(Interrupt Cycle) - 인터럽트 발생 시 복귀 주소를 저장시키고, 제어 순서를 인터럽트 처리 프로그램의 첫번째 명령으로 옮기는 단계이다.

# Reference
http://blog.naver.com/PostView.nhn?blogId=k97b1114&logNo=140157984279&beginTime=0&jumpingVid=&from=search&redirect=Log&widgetTypeCall=true