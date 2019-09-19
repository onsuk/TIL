## Enumeration Type
많은 언어와 같이 하스켈 또한 **emnumeration type**이 있다.

```haskell
module Thing where

data Thing = Shoe
            | Ship
            | SealingWax
            | Cabbage
            | King
        deriving Show
```

위 코드는 5개의 data constructor(ex. `Shoe`, `Ship`, etc.)을 갖고 있는 `Thing`이라는 새로운 타입을 정의했다. data constructor은 `Thing` 타입 내에서 각각 유일한 값들이다.

`deriving` 키워드를 사용하면 built-in 클래스(ex.`Show`, `Eq`, `Ord`,etc.)의 인스턴스로 만들 수 있다. 즉 `deriving Show`를 통해서 GHC는 `Thing` 타입의 모든 값을 `String` 타입으로 자동으로 바꿔준다.

GHC에서 이와 같이 확인할 수 있다.

```bash
*Thing> thisIsShoe = Shoe
*Thing> :t thisIsShoe
thisIsShoe :: Thing
*Thing> thisIsShoe
Shoe
```

하지만 `deriving Show` 키워드가 없다면

```bash
*Thing> thisIsShoe

<interactive>:8:1: error:
    • No instance for (Show Thing) arising from a use of ‘print’
    • In a stmt of an interactive GHCi command: print it
```
와 같이 에러 메시지를 출력한다. print할 수 있는 함수가 없기 때문이다.

Pattern Matching을 통해서도 `Thing` 타입을 사용하는 `isSmall`이라는 함수를 정의할 수 있다.

```haskell
isSmall :: Thing -> Bool
isSmall Ship = False
isSmall King = False 
isSmall _ = True
```


## In fact, Enumeration Type is...

### A kind of Algebraic Data Type!
`Thing`이라는 enumeration type은 여타 언어(ex. Java, C++, etc.)에서 제공하는 것과 비슷하다. 하지만 enumeration type은 사실 Haskell의 **algebraic data type**의 특정한 경우일 뿐이다.

```haskell
module FailableDouble where

data FailableDouble = Failure
                    | OK Double
                deriving Show

safeDiv :: Double -> Double -> FailableDouble
safeDiv _ 0 = Failure
safeDiv x y = OK (x / y)

failureToZero :: FailableDouble -> Double
failureToZero Failure = 0
failureToZero (OK d) = d
```

- `FailableDouble` type은 다음과 같은 2개의 data constructor을 가진다.
    - `Failure`
    - `Double` 타입을 인자로 받아 `FailableDouble` 타입을 반환하는 `OK` 함수

- `safeDiv` 함수는 위 함수를 이용해 divided by zero를 방지할 수 있다. 2번째 인자가 0인 경우는 `Failure`를 반환하고, 나머지 경우는 `OK`와 함께 연산값을 반환한다.

- `failureToZero` 함수는 위 함수를 이용해 failure인 경우는 0을 반환하고, 나머지 경우는 연산값을 반환한다.

다음과 같이 확인할 수 있다.
```bash
*FailableDouble> failureToZero (safeDiv 2 4)
0.5
*FailableDouble> failureToZero (safeDiv 3 0)
0.0
```

data constructor은 하나의 인자 뿐만 아니라, **여러 개의 인자**를 받을 수 있다.

```haskell
module Person where
import Thing

data Person = Person String Int Thing
    deriving Show

brent :: Person
brent = Person "Brent" 31 SealingWax

stan :: Person
stan = Person "Stan" 94 Cabbage

getAge :: Person -> Int
getAge (Person _ a _) = a
```

> **type constructor**과 **data constructor**은 다른 네임 스페이스를 사용하기 때문에 `Person`이라는 같은 이름을 사용해도 무방하다.


## Then, Algebraic Data Type

#### 정리하자면

```haskell
data AlgDataType = Constr1 Type11 Type12
                 | Constr2 Type21
                 | Constr3 Type31 Type32 Type33
                 | Constr4
```
`AlgDataType`은 4가지 data constructor로 구성될 수 있다.

- `Constr1`에 `Type11`, `Type12` 값을 인자로 받는다.
- `Constr2`에 `Type21` 값을 인자로 받는다.
- `Constr3`에 `Type31`, `Type32`, `Type33` 값을 인자로 받는다.
- `Constr4`를 단독 사용한다.

