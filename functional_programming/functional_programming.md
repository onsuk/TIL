# 함수형 프로그래밍(Functional Programming)

## 부작용(Side-Effect)이란?
우리가 작성하는 모든 함수는 두 종류의 입력과 출력을 가진다.

1) 일반적인 입출력
```java
public int square(int x) {
    return x * x;
}
```
일반적인 형태의 입출력이다. 입력은 `int x` 이며 출력이 `int`이다.

2) 숨겨진 입출력
```java
public void processNext() {
    Message message = InboxQueue.popMessage();

    if (message != null) {
        process(message);
    }
}
```

이 함수는 겉으로 보기에 입력과 출력이 없다. 하지만 분명히 무언가 **의존성**을 가지며 **뭔가 하는 일**이 있다. 이 함수가 **숨겨진 형태의 입출력**을 가진다는 의미이다. 숨겨진 입력은 `popMessage()`를 호출하기 전의 `InboxQueue` 상태이며 숨겨진 출력은 `process`의 호출을 통해 발생하는 모든 것과 그것들이 끝났을 때의 `InboxQueue`의 상태이다. 그리고 이 숨겨진 입출력을 두고 **부작용**(Side-Effect)이라고 한다.

## 부작용은 복잡성 빙산(iceberg)이다.
```java
public boolean processMessage(Channel channel) {...}
```
이 함수의 내부를 보지 않고는 무엇을 필요로 하는지, 무슨 일을 하는지 알 수 없다. 즉, 이 함수에서 나타날 수 있는 부작용은 복잡성 빙산이다. 우리는 함수 시그니처와 이름이라는 표면 위의 빙산의 일각만 볼 수 있는 셈이다.

상황에 대한 대안 3가지

1. 함수 정의를 파고 든다.
2. 복잡성을 표면 위로 드러낸다.
3. 그냥 무시하고 잘 되길 바란다. (결국 엄청난 실수를 유발한다.)

## 부작용(Side-Effect)이 나쁜가?
프로그래머가 예상한 그대로 동작한다면 괜찮다. 하지만 프로그래머가 의도한 숨겨진 예상이 정확하며, 시간이 지나더라도 여전히 정확할 것이라는 가정을 **의존**해야 한다.

이러한 코드는 완전히 분리해서 테스트할 수 없다. 회로기판처럼 입력을 연결하고 출력만 확인하는 **블랙 박스 테스트**를 할 수 없다. 코드를 열어보고 **숨겨진** 원인과 결과를 파악하고, 환경을 그럴듯하게 시뮬레이션해야 한다. 우리는 블랙 박스 테스트를 해야 한다. 즉, 구현 세부 사항을 무시할 수 있어야 한다. 하지만 부작용을 허용하게 된다면 블랙 박스 테스트를 할 수 없다. 박스를 열고 그 안에 무엇이 들어있는지 확인하지 않고는 입력과 그에 따른 출력을 결정할 수 없기 때문이다.

부작용의 유무는 디버깅 시에 그 차이가 증폭된다. 함수가 부작용을 허용하지 않는다면, 우리는 몇 가지의 입력에 대해 출력을 확인하는 것으로 함수 작동의 올바름 여부를 확인할 수 있다. 하지만 부작용이 있는 함수라면, 시스템의 여타 부분을 어디까지 고려해서 테스트를 해야 하는지 그 끝을 가늠할 수 없다. **함수가 무엇에든 의존할 수 있고 무엇이든 변경할 수 있다면 버그는 어느 곳에든 있을 수 있다.**

## 부작용은 항상 표면 위로 드러낼 수 있다.
```java
public Program  getCurrentProgram(TVGuide guide, int channel) {
    Schedule schedule = guide.getSchedule(channel);

    Program current = schedule.programAt(new Date());

    return current;
}
```

위 함수는 숨겨진 입력을 가진다. 무엇일까?

정답은 현재 시간 `new Date()`이다. 우리는 이 추가 입력을 정직하게 대하는 것을 통해 복잡성을 표면화할 수 있다.

```java
puclic Program getProgramAt(TVGuide guide, int channel, Date when) {
    Schedule schedule = guide.getSchedule(channel);

    Program program = schedule.programAt(when);

    return program;
}
```