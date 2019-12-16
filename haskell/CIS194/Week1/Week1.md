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

## Literate Haskell

## Declaratinos and variables

## Basic Types

## GHCi

## Arithmetic

## Boolean logic

## Defining basic functions

## Pairs

## Using functions, and multiple arguments

## Lists

## Constructing lists

## Functions on lists

## Combining functions

## A word about error messages
