# CIS194 - Week 6

## Lazy evaluation

하스켈은 **lazy**하다. Lazy하다는 것이 무엇인지에 대해 배워보려고 한다.

### Strict evaluation

Lazy evaluation에 대해 얘기하기 전에 반대말인 strict evaluation에 대해 알아두면 좋다.

Strict evaluation을 채택하게 되면, 함수 인자들이 함수로 전달되기 전에 완전히 계산된다. 예를 들어 아래와 같은 정의를 살펴보자.

```haskell
f x y = x + 2
```

Strict language은 `f 5 (29^35792)`를 계산할 때, (이미 계산된)`5`와 (상당히 계산할 것이 많은)`29^35792`를 완전히 계산한 후에 그 결과를 함수 `f`에게 전달해준다.

`f` 함수가 두번째 인수(`29^35792`)를 무시하기 때문에, 이러한 특정 예제에서의 strict evaluation은 멍청한 짓이다. `29^35792`에 대한 모든 연산은 낭비되기 때문이다. 그럼에도 불구하고 우리는 왜 strict evaluation이 필요할까?

Strict evaluation의 장점은 언제 어떤 순서로 일이 일어나는지 예측하기 쉽다는 것이다. 심지어 일반적으로 strict evaluation 언어는 인수의 평가 순서도 정한다(ex. 왼쪽에서 오른쪽으로).

예를 들어, Java에서 우리는 

```java
f (release_monkeys(), increment_counter())
```

`monkeys`가 release되었으며, `counter`이 increment되고 두가지 작업의 결과값이 `f` 함수로 전달된다. 그리고 `f` 함수가 결과값을 사용하는 지는 중요하지 않다.

만약 `f`가 결과를 사용하는지의 여부에 따라서 `monkeys`의 releasing과 `counter`의 incrementing이 독립적으로 일어난다면 몹시 혼란스러울 것이다. 이러한 **side effect**(부작용)가 있는 경우에는, strict evaluation을 택하는 것이 적합하다.

### Side effects and purity

그래서 우리는 **side effect**의 존재 여부가 정말 중요하다. "side effect"라고 하는 것은 *식의 계산이 식 외부의 무언가와 상호작용하게 하는 모든 것*을 의미한다.

> 내 생각: 필자는 side effect를 이렇게 표현했지만, 난 필자가 정의한 side effect는 [Kris Jenkins의 글(번역본)](https://medium.com/@jooyunghan/%ED%95%A8%EC%88%98%ED%98%95-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D%EC%9D%B4%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80-fab4e960d263)에서 말하는 **side cause**라고 생각한다. 상호작용을 통해 생긴 **결과**가 side effect일 것이다.

Anyway,

근본적인 문제는 외부와의 상호작용이 언제 일어났는지에 따라 결과가 달라질 수 있다는 점이다. 예를 들어,
- 전역 객체의 변경 - 전역 객체가 변경되어서 다른 식 계산의 결과값이 달라질 수 있다.
- 화면 출력 - 기존의 것과 다른 것을 화면에 출력하려면 그에 맞는 (외부의) 명령이 필요하기 때문에 화면 출력 함수의 결과값이 달라질 수 있다.
- 파일/네트워크 데이터 읽기 - 파일의 내용에 따라 식의 결과값이 달라질 수 있다.

> 개인적으로는 side effect에 대해 어렵게 설명된 느낌이 드는데, 앞서 언급한 [Kris Jenkins의 글(번역본)](https://medium.com/@jooyunghan/%ED%95%A8%EC%88%98%ED%98%95-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D%EC%9D%B4%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80-fab4e960d263)을 참고하면 조금 더 쉽고 명확하게 insight를 얻을 수 있을 것 같다.

앞서 보았듯이, lazy evaluation은 식이 언제 계산될 것인지에 대한 추론이 어렵다. 그래서 lazy evaluation 언어에 side effect를 포함하는 것은 정말 직관적이지 않다. 이것이 Haskell이 순수 언어인 이유이다. Haskell 설계자들은 lazy functianal language를 만들고 싶었고, 그것의 구현은 side effect를 허용하면 불가능하다는 것을 일찍이 깨달았다.

하지만 side effect가 아예 없는 언어는 유용하지 않다. 그 언어로 할 수 있는 것은 프로그램을 인터프리터에 넣고 식을 계산하는 것이 전부이다. 사용자의 입력을 받을 수도 없고 화면에 어떠한 것도 출력할 수도 없으며, 파일로부터 무언가를 읽어들일 수도 없다. Haskell 설계자들이 맞닥뜨린 과제는 언어의 본질적 순수함을 훼손하지 않는 범위 안에서 원칙에 기반하며 제한적인 방법으로 side effect를 허용하는 것이었다. 마침내 그들은 해결책(`IO monad`)을 찾았으며, 이에 대해서는 나중에 논하도록 한다.

### Lazy evaluation

Strict evaluation에 대해서 알아봤으니, lazy evaluation에 대해서 알아보도록 하자. Lazy evaluation을 채택하게 되면, 함수 인자의 계산이 가능한만큼 미뤄진다. 인자는 그것이 실제로 필요해지기 직전까지 계산되지 않는다. 어떠한 식이 함수 인자로 전달될 때, 그 식에 대한 계산을 하지 않고 *계산되지 않은 식*(unevaluated expression - called **thunk**)으로 감싸져서 전달된다.

예를 들어 `f 5 (29^35792)`라는 식을 계산할 때, 두번째 인자(`(29^35792)`)는 계산되지 않는 thunk로 감싸지고 `f`는 즉시 호출된다. `f`가 해당 인자를 사용하지 않기 때문에 thunk는 가비지 콜렉터에 의해 버려진다.


### Pattern matching drives evaluation

#### 그렇다면 언제 식의 계산이 필요한가?

위의 예제는 *함수가 실제로 인자를 사용하는가*에 초점이 맞춰져 있지만 실제로 그것이 그렇게 중요한 차이점은 아니다. 다음 예제를 살펴보도록 하자.

```haskell
f1 :: Maybe a -> [Maybe a]
f1 m = [m, m]

f2 :: Maybe a -> [a]
f2 Nothing = []
f2 (Just x) = [x]
```

`f1`과 `f2` 모두 자신의 인자를 쓰고 있다. 하지만 둘 사이에 큰 차이점이 있다. `f1`은 자신의 인자 `m`을 쓰고 있지만 해당 값에 대해 전혀 알 필요가 없다. `m`은 전혀 계산되지 않은 상태로 남아있어도 되며, *계산되지 않은 식*이 단지 리스트에 추가될 뿐이다. 다시 말해, `f1 e`의 결과값은 `e`의 모양에 의존하지 않는다.

반면 `f2`는 함수의 실행이 진행되려면 인자에 대해 알아야 한다. 즉, 인자의 **data constructor**이  `Nothing`인지 `Just`인지 알야아 한다. 그말은 `f2 e`를 계산하기 위해서는 `e`를 계산해야 한다. `f2 e`의 결과값은 `e`의 모양에 의존적이기 때문이다.

또 다른 중요한 점은 **thunk**(*계산되지 않은 식*)는 정확히 딱 패턴 매칭이 진행될 정도로만 계산된다는 것이다. 예를 들어 다음과 같은 식을 계산하는 것을 가정해보자. 
```
f2 (safeHead [3^500, 49])
```
`f2`는 `safeHead [3^500, 49]`의 호출에 대한 계산을 강제한다. 계산의 결과값은 `Just (3^500)`이다. 여전히 `3^500`은 계산되지 않았다. `f2`와 `safeHead` 둘다 마찬가지로 `3^500`에 대해서 알 필요가 없기 때문이다. `3^500`이 계산되는지의 여부는 `f2`가 어떻게 사용되는지에 따라 달려있다. 즉, `f2`의 결과값(`Just (3^500)`)을 가져다가 `Just` 안에 들어있는 값을 사용하려고 할 때 `3^500`에 대한 계산이 이루어진다.

#### 패턴 매칭이 계산 방법을 이끈다.

우리가 도출해낼 수 있는 문장이다. 중요한 점에 대해 되풀이해보자.
- 계산식은 패턴매칭이 일어날 때에만 계산이 이루어진다.
- 딱 매칭이 진행될 수 있는 선에서 필요한 곳까지만. 더 이상은 naver..!

조금 더 흥미로운 예제를 살펴보자. `take 3 (repeat 7)`을 계산하려고 한다. 참고로 `repeat`과 `take`에 대한 정의는 다음과 같다.

```haskell
repeat :: a -> [a]
repeat x = x : repeat x

take :: Int -> [a] -> [a]
take n _ | n <= 0 = []
take _ [] = []
take n (x:xs) = x : take (n - 1) xs
```

단계별로 계산을 수행하는 과정은 다음과 같다.

```
take 3 (repeat 7)
    { 3 <= 0 이 False이기 때문에, 두번째 인자를 매칭시켜야 하는 두번째 패턴으로 진행한다. 그렇기 때문에 repeat 7을 한단계 진행시켜야 한다. }
= take 3 (7 : repeat 7)
    { 두번째 패턴 또한 매칭되지 않았지만 세번째 패턴이 매칭된다. 여전히 (3-1)이 계산되지 않았음을 유의해야 한다. }
= 7 : take (3-1) (repeat 7)
    { 첫번째 패턴을 결정하기 위해서 (3-1) <= 0 을 계산해봐야 하며, 이는 (3-1)이 필요하다. }
= 7 : take 2 (repeat 7)
    { 2 <= 0 이 False이기 때문에, repeat 7을 다시 진행시킨다. }
= 7 : 7 : take (2-1) (repeat 7)
= 7 : 7 : take 1 (repeat 7)
= 7 : 7 : 7 : take (1-1) (repeat 7)
= 7 : 7 : 7 : take 0 (repeat 7)
- 7 : 7 : 7 : []
```

함수에 대한 계산이 정확히 위와 같이 구현되어 있더라도, 대부분의 Haskell 컴파일러들은 조금 더 세련된 방법을 사용한다. 특히 GHC는 **graph reduction**이라는 기술을 사용한다. 계산되어야 할 식을 그래프로 표현하고, 식에서 다른 부분이 동일한 하위식에 대한 포인터를 공유할 수 있는 방식이다. 이 방식은 불필요하게 중복되는 계산을 방지해준다. 예를 들어 
```
f x = [x, x] 
```
라는 식이 있다고 가정하자. `f (1 + 1)`을 계산할 때 덧셈(`+`)은 단 **한번**만 수행된다. 하위식 `1 + 1`이 `x`가 두번 나타나는 동안 공유되기 때문이다.

### 그 결과...

Laziness는 몹시 흥미롭고 광범위하며 뻔하지만은 않은 몇 가지 결과를 초래한다. 조금 살펴보도록 하자.

#### Purity

우리가 이미 볼 수 있었듯이, lazy evaluation을 채택하는 것은 purity를 채택하는 것을 강제한다.

#### Understanding space usage

Laziness이 무조건 좋은 것만은 아니다. 단점 중 하나는 가끔 프로그램의 메모리 사용량을 추론하기 까다롭다는 점이다. 다음 (아무런 문제가 없어 보이는) 예제를 살펴보자.

```haskell
-- 참고) prelude의 표준 foldl 함수
foldl :: (b -> a -> b) -> b -> [a] -> b
foldl _ z [] = z
foldl f z (x:xs) = foldl f (f z x) xs
```

`foldl (+) 0 [1, 2, 3]`를 계산하려고 할때 어떻게 진행되는지 살펴보자. (리스트 안의 모든 숫자의 합을 구하는 식)

```
foldl (+) 0 [1, 2, 3]
= foldl (+) (0+1) [2, 3]
= foldl (+) ((0+1)+2) [3]
= foldl (+) (((0+1)+2)+3) []
= (((0+1)+2)+3)
= ((1+2)+3)
= (3+3)
= 6
```

전체 리스트의 재귀가 끝나기 전까지는, 누적 함수의 총 덧셈 값이 요구되지 않는다. 누적 함수는 그저 `(((0+1)+2)+3)`라는 거대한 thunk를 쌓아간다. 마지막에 이 값은 `6`으로 줄어들게 된다. 여기에는 두가지 정도의 문제점이 있다.

1. 간단히 말해 효율적이지 않다. 리스트에 있는 모든 숫자들이 실제로 더해지기 전에 thunk의 형태로 변환되어 있는 것이 불필요하다.
2. 두번째 문제가 더욱 미묘하고 교활한 문제이다. `(((0+1)+2)+3)`를 계산하는 것은 사실 `0+1`을 계산하기 전에 `3`과 `2`를 스택에 넣어야 한다. 그러한 방식으로 스택을 줄여가면서 덧셈을 수행하게 된다. 이러한 작은 예제에서는 문제되지 않지만, 정말 긴 리스트의 경우는 큰 문제가 될 수 있다. 주로 스택 메모리의 크기가 그 정도로 크지 않기 때문에 **stack overflow**가 발생할 수 있다.

해결책은 `foldl` 대신 `foldl'` 함수를 쓰는 것이다. `foldl'`은 약간의 strictness가 추가된다. `foldl'`의 두번째 인자(누적 함수)는 계속해서 진행되기 전에 계산되어야 한다. 그로 인해, 커다란 thunk가 쌓이지 않게 된다.

```
foldl' (+) 0 [1, 2, 3]
= foldl' (+) (0+1) [2, 3]
= foldl' (+) 1 [2, 3]
= foldl' (+) (1+2) [3]
= foldl' (+) 3 [3]
= foldl' (+) (3+3) []
= foldl' (+) 6 []
= 6
```

`foldl'`은 위와 같은 방법으로 덧셈을 수행하게 된다. 하지만 이러한 경우에는 프로그램이 **조금 덜** lazy해진다는 사실을 알아야 한다.

(`foldl'`이 어떻게 구현되었는지 궁금하다면, [Haskell wiki - seq](http://www.haskell.org/haskellwiki/Seq)를 읽어보도록 하자.)

#### Short-circuiting operators

Java와 C++같은 언어에서는 `boolean` 연산자 `&&`(AND)와 `||`(OR)이 short-circuiting을 지원한다. 예를 들어, `&&`의 첫번째 인자가 `false`라면 식은 즉시 두번째 인자와 상관없이 `false`를 반환한다. 하지만 Java와 C++와 같은 언어에서는 이러한 short-circuiting이 특별한 경우로 정해져 있다. 일반적으로 strict 언어에서는 두개의 인자를 갖는 함수의 인자는 함수가 호출되기 전에 계산된다. 그렇기 때문에 `&&`와 `||`에 대한 short-circuiting은 언어의 문법에서 정한 특별한 예외이다.

하지만 Haskell에서는 어떠한 예외 없이 short-circuiting을 정의할 수 있다. 사실 `&&`와 `||`은 standard 함수일 뿐이다! 예를 들어 `&&`가 어떻게 정의되었는지 살펴보도록 하자.

```haskell
(&&) :: Bool -> Bool -> Bool
True && x = x
False && _ = False
```

`(&&)`의 정의에서 두번째 인자는 패턴매칭을 하지 않는 것을 볼 수 있다. 게다가 첫번재 인자가 `False`라면 두번째 인자를 아예 통째로 무시하는 것을 확인할 수 있다. `(&&)`가 두번째 인자에 대한 매칭을 전혀 하지 않기 때문에, Java나 C++에 있는 `&&` 연산과 동일하게 short-circuiting을 지원한다.

`(&&)` 함수가 이렇게 정의될 수도 있음을 유의해야 한다.
```haskell
(&&!) :: Bool -> Bool -> Bool
True  &&! True  = True
True  &&! False = False
False &&! True  = False
False &&! False = False
```

이 버전의 `(&&)`는 같은 값을 인자로 받더라도 다른 결과를 초래한다. 예를 들어 다음과 같은 식을 계산한다고 해보자.

```
False && (34^9784346 > 34987345)
False &&! (34^9784346 > 34987345)
```

둘다 `False`를 반환하지만, 두번째 식이 훨씬 더 시간이 오래 걸릴 것이다. 다음 예제도 살펴보자.

```
False && (head [] == 'x')
False &&! (head [] == 'x')
```

첫번째 식은 `False`를 반환하지만, 두번째 식은 계산이 뻑 날(?!) 것이다.

이것들을 통해, 함수를 정의하는 데에 있어서 laziness를 둘러싼 흥미로운 문제들이 많음을 알 수 있다.

#### User-defined control structures

Short-circuiting에 착안해 한단계 더 나아가면, Haskell에서 자신만의 control sturctures를 정의할 수 있다.

대부분의 언어는 내장된 `if` 구문을 갖고 있다. 어떤 사람들은 그 이유에 대해 말하기를, `if`가 앞서 살펴본 short circuiting과 같이 동작하기 때문이라고 한다. 테스트 값에 기반해서 두가지 중 한가지만을 실행/계산한다. 두가지 모두를 계산한다면 전체 목적과 부합하지 않을 것이다.

그런데 Haskell에서는 `if`를 내장 함수처럼 정의할 수 있다.

```haskell
if' :: Bool -> a -> a -> a
if' True x _ = x
if' False _ y = y
```

물론 Haskell에는 `if` 내장 함수가 있다. 하지만 사실 있는 이유를 모르겠다. (없어도 된다고 생각한다.) 아마도 언어 설계자들이 사용자가 그것을 원했다고 생각했을 것이다. 아무튼, `if`는 Haskell에서 그닥 많이 쓰이지 않는다. 패턴 매칭이나 가드(`|`)를 더 많이 쓴다.

우리는 다른 control structures 또한 정의할 수 있는데, 추후 monads에 대해서 논의할 때 더욱 많은 예제를 살펴보도록 하자.

#### Infinite data structrues

Lazy evaluation을 채택했다는 것은 우리가 무한한 데이터 구조를 다룰 수 있다는 말이기도 하다. 사실 우리는 이미 예제를 통해 살펴보았는데, 리스트 안에 7밖에 없는 `repeat 7`이 그러하다. 무한한 데이터 구조는 사실 thunk만 생성하며, 완성될 총 데이터의 잠재적 성장을 위한 씨앗(seed) 정도로 생각할 수 있다.

다른 실용적 적용범위는 "사실상 무한한" 데이터 구조이다. 게임의 공간 상태로 발생하는 tree와 같은 데이터 구조(ex. 체스)를 말한다. 그 tree는 비록 이론 상으로 유한하더라도, 크기가 너무 커서 사실상 무한한 것과 다름없다. Haskell을 쓰게 되면 이동 가능한 모든 tree를 정의한 다음, 원하는 방식으로 별도의 알고리즘을 각각 작성할 수 있다. **실제로 이동한 만큼의 tree만 계산될 것이다.**

#### Pipelining / wholemeal programming

앞서 언급했던 것처럼, 큰 데이터 구조를 "파이프라인"을 통해 점진적으로 변환하는 방식을 사용하면 메모리를 상당히 효율적으로 사용할 수 있다. 이제 우리는 그 이유에 대해 알 수 있다. laziness 덕분에 파이프라인의 각 단계는 부작용이 없이(in lockstep) 동작하며, 다음 단계에서 딱 요구하는 만큼만 생성할 수 있게 된다.

> 내 생각: 'due to laziness, each stage of the pipeline can operate in lockstep'이라고 원문에서 표현하고 있다. 여기서 'in lockstep'은 '정확하게', '예측할 수 있게'의 뜻을 갖고 있다고 생각한다. 그렇기 때문에 '부작용이 없이 동작하는 것'에 대해 말하는 것이라 생각한다.

#### Dynamic programming

Lazy evaluation가 사용자를 사로잡는 멋진 점들에 대한 더욱 구체적인 예시로, 동적 프로그래밍에 대해 논할 수 있다. 보통 동적 프로그래밍은 테이블의 항목을 적절한 순서로 채워넣어가며 해결하는 방식이다. 테이블의 항목을 채워넣을 때는 이미 계산된 항목의 결과값을 기반으로 처리하게 되는데, 올바른 순서대로 값을 채워넣음을 통해서 이미 계산된 항목의 올바른 결과값을 사용할 수 있어야 한다. 올바른 순서를 정의하지 않는다면 잘못된 결과값을 얻게 된다.

하지만 lazy evaluation을 사용하게 되면 Haskell 런타임이 알아서 올바른 계산 순서대로 작동하게 할 수 있다. 예를 들어, **0-1 배낭문제**를 해결하는 Haskell 코드를 살펴보자. 재귀를 통해 간단히 array `m`을 정의하는 것과 lazy evaluation을 통해 정확한 순서로 각 항목을 계산하는 것에 유의해야 한다.

> 참고로 배낭문제(knapsack problem)는 (무게와 가치가) 정해진 물건들을 (최대로 집어넣을 수 있는 무게가 정해진) 가방에 넣되, 물건 전체 가치의 합이 최대가 되게 하는 물건들의 조합을 찾는 문제이다.

```haskell
knapsack01 :: [Double]   -- values 
           -> [Integer]  -- nonnegative weights
           -> Integer    -- knapsack size
           -> Double     -- max possible value
knapsack01 vs ws maxW = m!(numItems-1, maxW)
  where numItems = length vs
        m = array ((-1,0), (numItems-1, maxW)) $
              [((-1,w), 0) | w <- [0 .. maxW]] ++
              [((i,0), 0) | i <- [0 .. numItems-1]] ++
              [((i,w), best) 
                  | i <- [0 .. numItems-1]
                  , w <- [1 .. maxW]
                  , let best
                          | ws!!i > w  = m!(i-1, w)
                          | otherwise = max (m!(i-1, w)) 
                                            (m!(i-1, w - ws!!i) + vs!!i)
              ]

example = knapsack01 [3,4,5,8,10] [2,3,4,5,9] 20
```

(글을 쓰여질 당시에는 무방했던 것 같으나) 현재는 다음과 같은 에러를 출력하게 된다.

```
/Users/onz/haskell-practice/src/Knapsack.hs:2:1: error:
    Could not load module ‘Data.Array’
    It is a member of the hidden package ‘array-0.5.3.0’.
    You can run ‘:set -package array’ to expose it.
    (Note: this unloads all the modules in the current scope.)
    Use -v to see a list of the files searched for.
```

다음과 같이 GHC에 command 하나를 입력하면 해결된다.

```
Prelude> :set -package array
package flags have changed, resetting and loading new packages...
```
