# CIS194 - Week 1

## What is Haskell?

하스켈은 1980년도에 만들어진 lazy한 함수형 프로그래밍 언어이다. 많은 lazy한 함수형 언어들이 있었다. 모두들 각자 선호하는 것들이 있었고 소통하기 어려웠다. 그래서 어떤 사람들은 존재하는 언어들에서 장점만을 취한 (또는 아예 새로운 특징을 취한) 새로운 언어를 만들게 되었다. 하스켈이 만들어지게 된 것이다.

그래서 하스켈이 무엇인가? 하스켈은 다음과 같다.

### Functional

![](img/image1.png)

'Functional'이라는 용어에 대해서 정확한 표현할 수 있는 의미는 없다. 하지만 **Haskell은 functional language**이라고 말할 수 있으며, 다음과 같은 두가지를 명심해야 한다.
- 함수는 first-class이며 다른 어떠한 값들과 정확히 같은 방법으로 쓰일 수 있다.
- Haskell 프로그램의 의의는 명령을 실행하는 것이 아닌 **식을 계산하는 것**에 있다.

두 가지의 특징은 프로그래밍에 대해 완전히 다른 방식의 생각을 초래한다.

### Pure

Haskell 표현식은 항상 **referentially transparent**(참조 투명)하다.
- 불변성을 갖는다. 모든 것(변수, 데이터 구조)는 불변하다.
- 표현식은 side effects(부작용)을 갖지 않는다. (전역 변수를 업데이하거나 화면에 무언가를 출력하는 것 등)
- 같은 인자로 같은 함수를 호출하면 항상 같은 값이 나와야 한다.

(함수형 프로그래밍을 모르는) 현 시점에서는 이것이 말도 안되는 소리같을 것이다. mutation(가변성)과 side effects(부작용)가 없이 어떻게 뭔갈 해본다는 말인가? (만약 당신이 명령형 혹은 객체지향 패러다임을 써왔다면) 분명히 사고의 전환이 필요할 것이다. 하지만 한번 사고의 전환을 해본다면 다음과 같은 엄청난 장점들이 있다.
- Equational resoning and refactoring (등식 추론 및 리팩토링): Haskell은 대수학에서 배우듯이 항상 등호가 성립한다.
- Parallelism(병렬성): 병렬식으로 표현식을 계산하는 것은 다른 표현식에 영향을 미치지 않는다는 것이 보장될 때 상당히 쉬워진다.
- Fewer hadaches: 통제되지 않는 작용들로 인해 프로그램은 디버깅과 유지보수, 추론을 하기 힘들어진다.

### Lazy

Haskell에서는 표현식들이 실제로 결과값이 필요하기 전까지는 계산하지 않는다. 이 간단한 결정은 다음과 같은 광범위한 결과를 가져온다.
- 단지 함수를 정의하는 것만으로 control structure을 쉽게 정의할 수 있다.
- Infinite data structures(무한한 데이터 구조)를 다룰 수 있게 된다.
- 더 compositional한 프로그래밍 스타일을 가능하게 한다. (추후 Wholemeal programming이라고 부르게 될 것이다.)
- 한 가지 단점이 있는데, 시간과 메모리 사용량을 추론하기 까다롭게 만든다는 것이다.

### Statically typed

모든 Haskell 표현식은 타입을 가지며, 컴파일 타임에 모두 체킹된다. 타입 에러가 있는 프로그램은 컴파일 되지 않으며 당연히 실행되지도 않는다.

## Themes

다음과 같은 세가지의 themes에 집중해보도록 한다.

### Types

정적 타입 시스템은 성가시며 까다로운 것으로 보인다. 사실 C++나 Java같은 언어는 까다롭다. 하지만 이 언어들은 정적 타입 시스템 때문에 성가시고 까다로운 것은 아니다. C++과 Java의 타입 시스템의 불충분한 표현력 때문이다! 해당 수업에서는 다음과 같은 Haskell 타입 시스템에 대해서 배우게 될 것이다.
- Helps clarifty thinking and express program structure
    - Haskell 프로그램을 작성하는 첫번째 단계는 보통, 모든 타입을 작성하는 것으로 시작한다. Haskell의 타입 시스템은 표현력이 좋기 때문에, 타입을 작성하는 것은 사소한 디자인 단계임과 동시에 프로그램에 대한 생각을 명확하게 만드는 데에 커다란 도움을 준다.
- Serves as form of documentation
    - 타입 시스템으로 인해 단지 함수의 타입을 보는 것만으로 함수가 무엇을 하는지, 어떻게 실행되는 지 등을 문서를 보지 않고 알 수 있다.
- Turns run-time errors into complie-time errors
    - 테스트를 많이 하는 것보다 오류를 미리 고칠 수 있는 것이 좋다. "컴파일된거면 딱 끝난거다."는 주로 농담식으로 하는 말이지만 (타입이 올바른 프로그램 로직에도 아직 에러가 있을 수 있기 때문에), 다른 언어에 비해 Haskell에서는 더욱 가능하다.

### Abstraction

"Don't repeat Yourself"은 프로그래밍의 세계에서 마법처럼 외는 주문이다. "Abstraction Principle"로 알려진 이 개념은 그 무엇도 중복되어선 안된다. 모든 개념, 알고리즘, 데이터조차도 코드 상에 정확히 한번만 등장한다. 비슷한 코드를 취하고 그들의 일반성을 취하는 것은 abstraction(추상화)의 절차이다.

Haskell은 추상화에 탁월하다. Parametric polymorphism, higher-order functions(고차 함수), 타입 클래스와 같은 특징들 모두 **반복되는 것을 지양**한다. Haskell을 통해 세부구현에서 추상화로 생각을 옮겨갈 수 있을 것이다.

### Wholemeal programming

Ralf Hinze의 말을 인용하자면

"함수형 언어는 (Geraint Jones가 만든 단어인) 통밀 프로그래밍(wholemeal programming)에 탁월하다. 통밀 프로그래밍은 크게 크게 생각하는 것이다. 요소를 연속적으로 처리하는 것이 아니라 리스트 전체를 처리하는 것이다. 각각의 솔루션을 찾는 것이 아니라 솔루션의 공간을 개발하는 것이다. 단일 경로를 생각하는 것이 아닌 그래프를 생각하는 것이다. 통밀 방식은 주어진 문제에 대해서 새로운 통찰력과 관점을 갖게 해준다. 투영 프로그래밍(Projective programming)의 개념으로 잘 보완된다. 우선 일반적인 문제를 해결하고, 일반적 프로그램을 특화함으로써 관심있는 부분만 추출해내는 것이다."

C나 Java로 된 다음과 같은 셰도 코드를 살펴보도록 하자.

```java
int acc = 0;
for (int i = 0; i < lst.length; i++ ) {
    acc = acc + 3 * lst[i];
}
```

이 코드는 Richard Bird가 말했던 "indexitis" 문제가 있다. 이 코드는 현재 인덱스에 대해 집중하며 배열을 순회하는 낮은 레벨의 구현부에 대해 관심을 갖고 있다. 또한 각 아이템에 3을 곱하고 결과값을 더하는 각각의 유용한 연산이 섞여 있다.

Haskell에서는 다음과 같이 작성할 수 있다.

```haskell
sum (map (3*) lst)
```

이번 수업에서 이러한 방식을 대표하는 생각들에 대해 배워볼 것이다. 그리고 Haskell이 왜 / 어떻게 그것을 가능케 하는지를 볼 것이다.

## Declaratinos and variables

다음은 Haskell 코드이다.

```haskell
x :: Int
x = 3
```

`x`라는 변수를 `Int` 타입으로 선언했다. (`::`는 '타입을 갖는다'로 읽으면 된다.) 그리고 `x`는 `3`으로 선언했다. `x`의 값이 영원하다는 것에 주목하자. (적어도 이 프로그램에서 말이다.) `x`의 값은 추후에 변경될 수 없다.

만약 `x = 4`라는 코드가 밑에 추가되었다면 `x`에 대해 Multiple declarations 에러를 일으킬 것이다.

Haskell에서 변수는 가변적인 공간이 아니다. 그것은 어떠한 값의 이름일 뿐이다.

다시 말해, 다른 언어와는 달리 Haskell의 `=`는 '할당'을 나타내지 않는다. 대신 `=`는 '정의'를 나타낸다. 수학에서의 `=`와 같다. 즉 `x = 4`는 '`x`가 `4`를 취한다.' 혹은 '`4`를 `x`에 할당한다.' 등으로 읽으면 안된다. '`x`를 `4`로 정의한다.'로 읽혀야 한다.

다음과 같은 코드가 어떤 의미인지 생각해보자.

```haskell
y :: Int
y = y + 1
```
> 무한 루프가 발생하는 것으로 생각된다.

## Basic Types

```haskell
-- 머신에 따라 범위가 정해지는 정수
i :: Int
i = -78
```

`Int`는 Haskell에 의해 최소 (-2^29)부터 (+2^29)의 범위를 보장하는 정수타입이다. 아키텍쳐(컴퓨터)에 따라 달라질 수 있다. 다음을 계산하면 각 머신의 범위를 알 수 있다.

```haskell
biggestInt, smallestInt :: Int
biggestInt = maxBound
smallestInt = minBound
```

> 일반적으로 Haskell은 카멜케이스를 사용한다.

반면 `Integer` 타입은 시스템의 메모리 양에 의해서만 제한받는다.

```haskell
-- 임의 크기의 정수
n :: Integer
n = 17403932978410329847102398472039847109834790

reallyBig :: Integer
reallyBig = 2^(2^(2^(2^2)))

numDigits :: Int
numDigits = length (show reallyBig)
```

부동 소수점 숫자에 대해서는 `Double`이 있다.

```haskell
d1, d2 :: Double
d1 = 4.5387
d2 = 6.2831e-4
```

Single-precision 소수점 숫자에 대해서는 `Float`이 있다.

그리고 불리언, 문자, 문자열이 있다.

```haskell
-- 불리언
b1, b2 :: Bool
b1 = True
b2 = False

-- 문자
c1, c2, c3 :: Char
c1 = 'x'
c2 = 'Ø'
c3 = 'ダ'

-- 문자열은 문자로 이루어진 리스트의 특별한 문법이다.
s :: String
s = "Hello, Haskell!"
```

## GHCi

GHCi는 CHC를 통한 Haskell REPL(Read-Eval-Print-Loop)이다. GHCi에서 식을 계산할 수 있고 `:load` or `:l` 명령어를 통해서 파일을 로드할 수 있으며, `:reload` or `:r`을 통해 리로드, `:type` or `:t`을 통해 타입 질의 등의 많을 것들을 할 수 있다. `:?` 명령어를 통해 어떠한 것들을 할 수 있는지 알 수 있다.

## Arithmetic

다음 표현식을을 GHCi에서 계산해보도록 하자.

```haskell
ex01 = 3 + 2
ex02 = 19 - 27
ex03 = 2.35 * 8.6
ex04 = 8.7 / 3.1
ex05 = mod 19 3
ex06 = 19 `mod` 3
ex07 = 7 ^ 222
ex08 = (-3) * (-7)
```

`(backticks)가 중위 함수로 만들어 주는 것을 유의하도록 하자. 그리고 음수는 괄호에 의해 감싸져야 한다는 점, 그렇게 해야 뻴셈 연산과의 착오를 피할 수 있다는 점 또한 유의하자.

다음과 같은 식은 에러를 반환할 것이다.

```haskell
-- i는 Int 타입, n은 Integer 타입이다.
badArith1 = i + n
```

같은 타입의 값만 덧셈 연산을 할 수 있으며, Haskell에서는 이를 암묵적으로 변환해주지 않는다. 다음과 같은 방법으로 명시적으로 변환해줘야 한다.
- `fromIntegral`
- `round`, `floor`, `ceiling`: 소수점 숫자를 `Int`나 `Integer`으로 바꿔준다.

다음과 같은 식을 계산해보자.

```haskell
badArith2 = i / i
```

`/`는 소수점 숫자만 쓸 수 있기 때문에 에러를 반환할 것이다. 정수의 나눗셈은 `div`를 쓸 수 있다.

```haskell
ex09 = i `div` i
ex10 = 12 `div` 5
```

정수에 대해 암묵적 변환이 일어나는 언어를 썼었다면, 이러한 부분이 처음에는 상당히 까다롭고 성가셔 보일 것이다. 하지만 익숙해질 것이라 장담한다. 그리고 곧 감사해 할 것이다. 암묵적 숫자 변환은 숫자 코드에 대한 조잡한 사고를 조장한다.

## Boolean logic

불리언 값은 `(&&)`(and), `(||)`(or), `not` 등을 통해 결합 될 수 있다.

```haskell
ex11 = True && False
ex12 = not (False || True)
```

값들은 `(==)`와 `(/=)`를 통해 동등성을 비교할 수 있다. 그리고 `(<)`, `(>)`, `(<=)`, `(>=)` 등을 통해 대소를 비교할 수 있다.

```haskell
ex13 = ('a' == 'a')
ex14 = (16 /= 3)
ex15 = (5 > 3) && ('p' <= 'q')
ex16 = "Haskell" > "C++"
```

Haskell은 `if` 표현식 또한 갖고 있다. `if b then t else f`은 `b`가 `True`라면 `t`를 계산하고 `False`라면 `f`를 계산한다는 뜻이다. `if` 표현식은 `if` 문과 다르다는 점을 주의하도록 하자. 예를 들어, `if` 문은 `else` 부분은 있어도 되고 없어도 된다. `else` 문을 생략한다면 그 뜻은 '`False`가 되었을 때는 아무것도 하지 않는다.'가 된다. 하지만 `if` 표현식에서는 `else` 부분은 필요하다. `if` 표현식은 **반드시 어떠한 값**을 가져야 하기 때문이다.

Haskell은 `if` 표현식을 잘 쓰지 않는다. Pattern matching이나 guards를 주로 쓴다.

## Defining basic functions

## Pairs

## Using functions, and multiple arguments

## Lists

## Constructing lists

## Functions on lists

## Combining functions

## A word about error messages
