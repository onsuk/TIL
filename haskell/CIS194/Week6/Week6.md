# CIS194 - Week 6

## Lazy evaluation

하스켈은 **lazy**하다. lazy하다는 것이 무엇인지에 대해 배워보려고 한다.

### Strict evaluation

lazy evaluation에 대해 얘기하기 전에 반대말인 strict evaluation에 대해 알아두면 좋다.

strict evaluation을 채택하게 되면, 함수 인자들이 함수로 전달되기 전에 완전히 계산된다. 예를 들어 아래와 같은 정의를 살펴보자.

```haskell
f x y = x + 2
```

strict language은 `f 5 (29^35792)`를 계산할 때, (이미 계산된)`5`와 (상당히 계산할 것이 많은)`29^35792`를 완전하게 계산한 후에 그 결과를 함수 `f`에게 전달해준다.

`f` 함수가 두번째 인수(`29^35792`)를 무시하기 때문에, 이러한 특정 예제에서의 strict evaluation은 멍청하다. `29^35792`에 대한 모든 연산은 낭비되었다. 그럼에도 불구하고 우리는 왜 strict evaluation이 필요할까?

strict evaluation의 장점은 언제 어떤 순서로 일이 일어나는지 예측하기 쉽다는 것이다. 심지어 일반적으로 strict evaluation 언어는 인수의 평가 순서도 정한다.(ex. 왼쪽에서 오른쪽으로)

예를 들어, Java에서 우리는 

```java
f (release_monkeys(), increment_counter())
```

우리는 `monkeys`가 release되었으며, `counter`이 increment되었다는 것, 그리고 두가지 작업의 결과값이 `f` 함수로 전달되는 것, `f` 함수가 결과값을 사용하는 지는 중요하지 않다는 것을 안다.

만약 `f`가 결과를 사용하는지의 여부에 따라서 `monkeys`의 releasing과 `counter`의 incrementing이 독립적으로 일어난다면 몹시 혼란스러울 것이다. 이러한 **side effect**(부작용)가 있는 경우에는, strict evaluation을 택하는 것이 적합하다.

