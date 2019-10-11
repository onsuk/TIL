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

### Side effects and purity

그래서 우리는 **side effect**의 존재 여부가 정말 중요하다. "side effect"라고 하는 것은 *식의 계산이 식 외부의 무언가와 상호작용하게 하는 모든 것*을 의미한다. (내 생각: 필자는 side effect를 이렇게 표현했지만, 난 필자가 정의한 side effect는 [Kris Jenkins의 글(번역본)](https://medium.com/@jooyunghan/%ED%95%A8%EC%88%98%ED%98%95-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D%EC%9D%B4%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80-fab4e960d263)에서 말하는 **side cause**라고 생각한다. 상호작용을 통해 생긴 **결과**가 side effect일 것이다.)

Anyway,

근본적인 문제는 외부와의 상호작용이 언제 일어났는지에 따라 결과가 달라질 수 있다는 점이다. 예를 들어,
- 전역 객체의 변경 - 전역 객체가 변경되어서 다른 식 계산의 결과값이 달라질 수 있다.
- 화면 출력 - 기존의 것과 다른 것을 화면에 출력하려면 그에 맞는 (외부의) 명령이 필요하기 때문에 화면 출력 함수의 결과값이 달라질 수 있다.
- 파일/네트워크 데이터 읽기 - 파일의 내용에 따라 식의 결과값이 달라질 수 있다.

> 개인적으로는 side effect에 대해 어렵게 설명된 느낌이 드는데, 앞서 언급한 [Kris Jenkins의 글(번역본)](https://medium.com/@jooyunghan/%ED%95%A8%EC%88%98%ED%98%95-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D%EC%9D%B4%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80-fab4e960d263)을 참고하면 조금 더 쉽고 명확하게 insight를 얻을 수 있을 것 같다.

앞서 보았듯이, lazy evaluation은 식이 언제 계산될 것인지에 대한 추론이 어렵다. 그래서 lazy evaluation 언어에 side effect를 포함하는 것은 정말 직관적이지 않다. 이것이 Haskell이 순수 언어인 이유이다. Haskell 설계자들은 lazy functianal language를 만들고 싶었고, 그것의 구현은 side effect를 허용하면 불가능하다는 것을 일찍이 깨달았다.

하지만 side effect가 아예 없는 언어는 유용하지 않다. 그 언어로 할 수 있는 것은 프로그램을 인터프리터에 넣고 식을 계산하는 것이 전부이다. 사용자의 입력을 받을 수도 없고 화면에 어떠한 것도 출력할 수도 없으며, 파일로부터 무언가를 읽어들일 수도 없다. Haskell 설계자들이 맞닥뜨린 과제는 언어의 본질적 순수함을 훼손하지 않는 범위 안에서 원칙에 기반하며 제한적인 방법으로 side effect를 허용하는 것이었다. 마침내 그들은 해결책(`IO monad`)을 찾았으며, 이에 대해서는 나중에 논하도록 한다.

### Lazy evaluation

strict evaluation에 대해서 알아봤으니, lazy evaluation에 대해서 알아보도록 하자. lazy evaluation을 채택하게 되면, 함수 인자의 계산이 가능한만큼 미뤄진다. 인자는 그것이 실제로 필요해지기 직전까지 계산되지 않는다. 어떠한 식이 함수 인자로 전달될 때, 그 식에 대한 계산을 하지 않고 *계산되지 않은 식*(unevaluated expression - called `thunk`)으로 감싸져서 전달된다.

예를 들어 `f 5 (29^35792)`라는 식을 계산할 때, 두번째 인자(`(29^35792)`)는 계산되지 않는 `thunk`로 감싸지고 `f`는 즉시 호출된다. `f`가 해당 인자를 사용하지 않기 때문에 `thunk`는 가비지 콜렉터에 의해 버려진다.


