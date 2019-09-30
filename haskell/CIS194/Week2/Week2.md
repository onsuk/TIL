# CIS194 - Week 2

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

- `safeDiv` 함수는 위 함수를 이용해 divided by zero를 방지할 수 있다. 나눗셈 연산을 위한 인자 중 2번째 인자가 0인 경우는 `Failure`를 반환하고, 나머지 경우는 `OK`와 함께 연산값을 반환한다.

- `failureToZero` 함수는 위 함수를 이용해 `Failure`인 경우는 0을 반환하고, 나머지 경우는 연산값을 반환한다.

다음과 같이 확인할 수 있다.
```bash
*FailableDouble> safeDiv 2 4
OK 0.5
*FailableDouble> failureToZero (safeDiv 2 4)
0.5
*FailableDouble> safeDiv 3 0
Failure
*FailableDouble> failureToZero (safeDiv 3 0)
0.0
```

Algebraic Data Type의 data constructor은 하나의 인자 뿐만 아니라, **여러 개의 인자**를 받을 수 있다.

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


## Then, Algebraic Data Type is

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

## Pattern Matching

패턴 매칭에 관해 몇가지 유의할 점이다.

1. 언더스코어 `_`는 와일드 카드이다.

2. `x@ pat`이라는 문법은 `pat`이라는 패턴을 `x`라는 이름 안에 모두 매칭시킨다.
```haskell
baz :: Person -> String
baz p@ (Person n _ _) = "The name field of (" ++ show p ++ ") is " ++ n
```
GHC를 통해 확인해본다.
```bash
*Person> baz brent
"The name field of (Person \"Brent\" 31 SealingWax) is Brent"
```

3. 패턴을 중첩시킬 수 있다.
```haskell
checkFav :: Person -> String
checkFav (Person n _ SealingWax) = n ++ ", you're my kind of Person!"
checkFav (Person n _ _) = n ++ ", your favorite thing is lame"
```

`Person`에 대한 패턴 안에 `SealingWax`에 대한 패턴이 중첩되었다.

```bash
*Person> checkFav stan
"Stan, your favorite thing is lame"
*Person> checkFav brent
"Brent, you're my kind of Person!"
```

#### 정리하자면
일반적으로 패턴 문법은 다음과 같다.
```haskell
pat ::= _                      -- 와일드카드 패턴
     |  var                    -- 변수 패턴: 모든 값과 일치하며 var라는 이름을 부여함
     |  var @ ( pat )          -- @패턴: 패턴과 일치하는 경우 그 값에 var라는 이름을 부여함
     |  ( Constr pat1 pat2 ... patn ) -- 생성자 패턴
```
> '일반적'일 뿐, 다른 패턴 문법과 기능이 추가적으로 있다.

## case
`case` 문은 다음과 같이 쓰인다.
```haskell
testForCase = case "Onsuk" of
                    [] -> 3
                    ('O':xs) -> length xs
                    _ -> 7
```
`Onsuk`은 'O'로 시작하기 때문에 'nsuk'의 길이 4를 반환한다.
```bash
*Person> testForCase
4
```

실제로 함수를 정의할 때 쓰이는 패턴 매칭은 `case` 문의 **syntax sugaring**이다.

다음은 위 예시 코드의 `failureToZero` 함수를 `case` 문을 통해 재정의한 코드이다.

```haskell
-- failureToZero :: FailableDouble -> Double
-- failureToZero Failure = 0
-- failureToZero (OK d) = d

failureToZero' :: FailableDouble -> Double
failureToZero' x = case x of
                    Failure -> 0
                    OK d -> d
```

## Recursive Data Type
data type은 재귀적으로 정의될 수 있다. 우리는 익숙한 예시를 계속해서 봐왔다. 바로 `List`이다.

```haskell
data IntList = Empty
             | Cons Int IntList
        deriving Show
```

Haskell의 built-in List는 비슷하게 정의되어 있다. `Empty` -> `[]`, `Cons` -> `:` 로 바뀐다는 점만 다르다. *(물론, Haskell의 List는 `Int` 뿐만 아닌 모든 타입을 받는다는 점에서 조금 다르다.)*

```haskell
listTest1 :: IntList
listTest1 = Empty

listTest2 :: IntList
listTest2 = Cons 1 listTest1

listTest3 :: IntList
listTest3 = Cons 2 listTest2
```
GHC에서 확인해보자.
```bash
*Person> listTest1
Empty
*Person> listTest2
Cons 1 Empty
*Person> listTest3
Cons 2 (Cons 1 Empty)
```

Haskell의 List도 이와 같다.
```bash
*Person> []
[]
*Person> (:) 1 []
[1]
*Person> (:) 2 ((:) 1 [])
[2,1]
```

이진 트리도 이와 같은 재귀적 방식으로 정의할 수 있다.

다음은 간단한 예시이다.

```haskell
data Tree = Leaf Char
          | Node Tree Int Tree
        deriving Show

treeTest :: Tree
treeTest = Node (Leaf 'x') 1 (Node (Leaf 'y') 2 (Leaf 'z'))
```