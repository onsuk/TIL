# 논블록킹(Non-blocking)과 비동기(Asynchronous)와 동시성(Concurrency)

## 논블록킹(Non-blocking)
Non-blocking은 크게 보았을 때, 다음과 같은 두 가지 의미로 사용한다.
- **Non-blocking algorithm(Non-blocking synchronization)** : Non-blocking이란, 어떤 쓰레드에서 오류가 발생하거나 멈추었을 때 다른 쓰레드에게 영향을 끼치지 않도록 만드는 방법들을 말한다. 공유 자원(메모리, 파일 등)을 사용하는 멀티 쓰레드 프로그래밍을 할 때, 특정 공유 자원을 사용하는 부분에서 뮤텍스나 세마포어 등을 사용하여 여러 쓰레드에서 동시에 접근하지 못하도록 개발자가 보장하는 것이 전통적인 방법이었다. 반면 Non-blocking algorithm(Wait-freedom, Lock-freedom 등)을 사용하면 공유 자원을 안전하게 동시에 사용할 수 있다.

- **Non-blocking I/O(Asynchronous I/O 혹은 Non-sequential I/O)** : Non-blocking I/O란, 입출력 처리는 시작만 해둔 채 완료되지 않은 상태에서 다른 처리 작업을 계속 진행할 수 있도록 멈추지 않고 입출력 처리를 기다리는 방법을 말한다. I/O 처리를 하는 전통적인 방법은 I/O 작업을 시작하면 완료될 때까지 기다리는 방법이다. 기존에는 synchronous I/O 혹은 blocking I/O를 통해 I/O 작업을 진행하는 동안 프로그램의 진행을 멈추고(block) 기다리는 방식이 사용되었으나, 이는 수많은 I/O 작업이 있는 경우 I/O 작업이 진행되는 동안 프로그램이 아무일도 하지 않고 시간을 소비하게 만든다. 반면, Non-blocking I/O 방식을 사용하면 외부에 I/O 작업을 하도록 요청한 후 즉시 다음 작업을 처리함으로써 시스템 자원을 더 효율적으로 사용할 수 있게 된다. 그러나 I/O 작업이 완료된 이후에 처리해야 하는 후속 작업이 있다면, I/O 작업이 완료될 때까지 기다려야 한다. 따라서 이 후속 작업이 프로세스를 멈추지 않도록 만들기 위해, I/O 작업이 완료된 이후 후속 작업을 이어서 진행할 수 있도록 별도의 약속(Polling, Callback function 등)을 한다.


## 동시성(Concurrency)와 병렬성(Parallelism)
- **Concurrency**란 각 프로그램 조각들이 실행 순서와 무관하게 동작할 수 있도록 만들어 한 번에 여러 개의 작업을 처리할 수 있도록 만든 구조이다. 좀 더 쉽게 말해 하나의 작업자가 여러 개의 작업을 번갈아가며 수행할 수 있도록 만드는 것이다. 동시성을 확보하게 되면, 작업 순서와 상관없이 각 작업이 완료되지 않았더라도 필요에 따라 번갈아 가며 작업을 수행함으로써 전체 작업 수행 속도를 향상시킬 수 있다.

## 비동기 프로그래밍(Asynchronous Programming)
- **Parallelism**이란 많은 작업을 물리적으로 동시에 수행하는 것으로써, 작업자를 물리적으로 여럿 둠으로써 같은 작업을 동시에 수행할 수 있도록 만드는 것이다. 병렬성을 확보하게 되면 물리적으로 동일한 시간 내에 동일한 작업을 더 여러 번 수행할 수 있게 된다. Concurrencty와 Parallelism은 혼동하기 쉬운 개념이지만, 서로 의존관계가 없이 분리되어 있는 개념이다. Parallelism은 한 개의 프로세서에서는 확보할 수 없는 개념이다. 한 개의 프로세서가 같은 시간에 두 개의 작업을 수행하는 것은 물리적으로 불가능하기 대문이다. 반면, 한 개의 프로세서만 있다고 하더라도 동시성을 확보할 수 있다. 잘개 쪼갠 작업들이 서로 영향을 끼치지 않는다면, 하나의 작업자가 각 작업이 완료되지 않았더라도 번갈아가며 수행하는 것이 가능하다. Concurrency는 작업을 처리하는 방식을 개선함으로써 효율화를 가져오는 것이 목적이며, Parallelism은 자원 자체를 늘림으로써 작업의 처리량을 늘리는 것이 목적이다. 따라서 Concurrency와 Parallelism을 동시에 확보함으로써 시너지 효과를 가져올 수 있으나, 각각은 서로 의존성이 없다고 볼 수 있다.

## 논블록킹 & 비동기 & 동시성
Non-blocking과 Async를 비교해보자는 질문이 있다면, 질문 자체를 좀 더 명확히 할 필요성이 있다. 우선 Non-blocking은 앞서 짚어본 바와 같이 Non-blocking I/O를 의미할 수도 있고, Non-blocking 알고리즘을 의미할 수도 있다. 또한 Async라는 용어는 Asynchronous I/O를 의미할 수도 있고, Asynchronous Programming을 의미할 수도 있다. Non-blokcing I/O를 구체적으로 분류하면 Synchronous와 Asynchronous로 구분할 수 있기 때문에 이를 비교하는 것은 의미가 있다. 그러나 Non-blocking I/O와 Asynchronous Programming은 비교 대상이 되기 어렵다. 각 개념이 바라보는 관점이 다르기 때문이다. Asynchronous Programming을 위해 Concurrency를 확보하거나  Non-blocking I/O를 활용할 수는 있지만, 이것이 Asynchronous Programming의 필수조건은 아니다. 예를 들어 Event-loop를 사용하여 동시성을 확보했으나, I/O 작업의 성격에 따라 그 처리를 위해 blocking I/O 모델을 사용할 수 있다. Blocking I/O를 사용했어도 이 부분이 별도의 채널을 통한 작업으로 이루어짐으로써 이 프로그램의 주 실행흐름(event-loop)을 막지 않았다면, 이 프로그램은 Asynchronous Programming이라고 부를 수 있다.

# Reference
[논블록킹과 비동기와 동시성](https://tech.peoplefund.co.kr/2017/08/02/non-blocking-asynchronous-concurrency.html)