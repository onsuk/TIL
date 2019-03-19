# 논블록킹(Non-blocking)과 비동기(Asynchronous)와 동시성(Concurrency)

## 논블록킹(Non-blocking)
Non-blocking은 크게 보았을 때, 다음과 같은 두 가지 의미로 사용한다.
- **Non-blocking algorithm(Non-blocking synchronization)** : Non-blocking이란, 어떤 쓰레드에서 오류가 발생하거나 멈추었을 때 다른 쓰레드에게 영향을 끼치지 않도록 만드는 방법들을 말한다. 공유 자원(메모리, 파일 등)을 사용하는 멀티 쓰레드 프로그래밍을 할 때, 특정 공유 자원을 사용하는 부분에서 뮤텍스나 세마포어 등을 사용하여 여러 쓰레드에서 동시에 접근하지 못하도록 개발자가 보장하는 것이 전통적인 방법이었다. 반면 Non-blocking algorithm(Wait-freedom, Lock-freedom 등)을 사용하면 공유 자원을 안전하게 동시에 사용할 수 있다.

- **Non-blocking I/O(Asynchronous I/O 혹은 Non-sequential I/O)** : Non-blocking I/O란, 입출력 처리는 시작만 해둔 채 완료되지 않은 상태에서 다른 처리 작업을 계속 진행할 수 있도록 멈추지 않고 입출력 처리를 기다리는 방법을 말한다. I/O 처리를 하는 전통적인 방법은 I/O 작업을 시작하면 완료될 때까지 기다리는 방법이다. 기존에는 synchronous I/O 혹은 blocking I/O를 통해 I/O 작업을 진행하는 동안 프로그램의 진행을 멈추고(block) 기다리는 방식이 사용되었으나, 이는 수많은 I/O 작업이 있는 경우 I/O 작업이 진행되는 동안 프로그램이 아무일도 하지 않고 시간을 소비하게 만든다. 반면, Non-blocking I/O 방식을 사용하면 외부에 I/O 작업을 하도록 요청한 후 즉시 다음 작업을 처리함으로써 시스템 자원을 더 효율적으로 사용할 수 있게 된다. 그러나 I/O 작업이 완료된 이후에 처리해야 하는 후속 작업이 있다면, I/O 작업이 완료될 때까지 기다려야 한다. 따라서 이 후속 작업이 프로세스를 멈추지 않도록 만들기 위해, I/O 작업이 완료된 이후 후속 작업을 이어서 진행할 수 있도록 별도의 약속(Polling, Callback function 등)을 한다.


## 동시성(Concurrency)와 병렬성(Parallelism)

## 비동기 프로그래밍(Asynchronous Programming)

## 논블록킹 & 비동기 & 동시성

# Reference
[논블록킹과 비동기와 동시성](https://tech.peoplefund.co.kr/2017/08/02/non-blocking-asynchronous-concurrency.html)