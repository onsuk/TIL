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
2. 복잡성을 표면(함수 시그니처) 위로 드러낸다.
3. 그냥 무시하고 잘 되길 바란다. (결국 엄청난 실수를 유발한다.)

## 부작용(Side-Effect)가 나쁜가?
프로그래머가 예상한 그대로 동작한다면 괜찮다. 하지만 숨겨진 예상이 정확하며, 시간이 지나더라도 