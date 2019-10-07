# CIS194 - Week 5

하스켈의 다형성은 **parametric polymorphism**으로 알려져있다. 풀어 말하자면, polymorphic function이 어떠한 입력 타입에 대해서든 동일하게 작동한다는 뜻이다. 이것은 polymorphic function 사용자에게 흥미로운 영향을 준다.

## Parametricity

다음과 같은 타입을 가정한다.
```haskell
a -> a -> a
```

`a`라는 타입은 어떠한 타입으로도 사용될 수 있다. 어떠한 함수가 이러한 유형의 타입을 가질까?

아래 코드를 살펴보자.
```haskell
f :: a -> a -> a
f x y = x && y
```

위 코드는 작동하지 않는다. 문법은 유효하지만 타입 체크를 통과하지 못한다. 이러한 에러 메시지를 확인할 수 있다.

```
• Couldn't match expected type ‘Bool’ with actual type ‘a’
    ‘a’ is a rigid type variable bound by
    the type signature for:
        f :: forall a. a -> a -> a
    at /Users/onz/haskell-practice/src/Golf.hs:27:1-16
• In the first argument of ‘(&&)’, namely ‘x’
    In the expression: x && y
    In an equation for ‘f’: f x y = x && y
```

위 코드가 작동하지 않는 이유는 polymorphic function의 **호출자**가 타입을 선택해야 하기 때문이다. 여기서는 함수 **구현자**가 특정한 타입(`Bool`)을 선택하려고 했지만, `String`, `Int` 등 미리 알 수 없는 여러 타입들 또한 받을 수 있게 되어 있다.

다시 말해, `a -> a -> a`라는 타입이란 함수 호출자가 어떠한 타입을 지정하더라도 모두 만족시킨다는 약속이다.


#### 다른 함수 구현 방법을 모색해보자.

```haskell
pf a1 a2 = case (typeOf a1) of
            Int  -> a1 + a2
            Bool -> a1 && a2
            _    -> a1
```

위 코드는 특정한 타입에 대해서만 특정한 방식으로 작동하는 `pf`라는 함수를 표현하려고 한다. 우리는 이것을 Java로 아래와 같이 구현할 수 있다.

```java
class AdHoc {
    public static Object pf(Object a1, Object a2) {
        if (a1 instanceof Integer && a2 instanceof Integer) {
            return (Integer)a1 + (Integer)a2;
        } else if (a1 instanceof Boolean && a2 instanceof Boolean) {
            return (Boolean)a1 && (Boolean)a2;
        } else {
            return a1;
        }
    }
}
```

하지만 Haskell에서 이와 같이 코드를 작성할 수 없다. Haskell은 Java와 같이 `instanceof` 연산자가 없기 때문이다. 값의 유형에 대해 묻고 그에 대한 답을 통해 연산을 결정하는 것이 불가능하다. 한 가지 이유를 들자면, Haskell의 타입은 체크된 후 **컴파일러에 의해 지워진다**. 그렇기 때문에 런타임 시에 질의할 수 있는 타입 정보가 없다! (*값의 유형에 대해 묻고 답을 들어야 하는데 말이다!*) 하지만, 곧 보게 될 다른 긍정적인 이유도 있다.

이러한 방식의 polymorphism을 **parametric polymorphism**이라고 한다. `f :: a -> a -> a`이라는 함수는 `a` 타입에서 parametric하다고 말한다. 여기서 parametric이라는 단어는 '**호출자가 선택한 어떠한 타입에도 동작한다**'라는 뜻이다. Java에서는 이러한 polymorphism 스타일이 **generics**를 통해 제공된다(짐작할 수 있듯이, generics는 하스켈에서 영감을 받았다. Haskell을 설계한 개발자가 generics의 메인 개발자).

그래서 사실 `a -> a -> a`라는 타입을 만족하는 함수는 2개밖에 없다.

```haskell
f1 :: a -> a -> a
f1 x y = x

f2 :: a -> a -> a
f2 x y = y
```

`a -> a -> a`라는 타입이 사실상 꽤 많은 정보를 담고 있다는 것을 알 수 있다.

다음 타입들을 만족하는 함수의 동작에 대해 생각해보자.

```haskell
a -> a
a -> b
a -> b -> b
[a] -> [a]
(b -> c) -> (a -> b) -> (a -> c)
(a -> a) -> a -> a
```

```haskell
hmm....
```

## Two view on parametricity

특히 Java와 같이 `instanceof` 구문을 가진 언어를 이용해 polymorphic function의 구현하는 사람이라면 이러한 제약들이 성가시게 느껴질 것이다. "이게 안된다고?"

#### 하지만 관점을 조금 바꿔서 생각해보자.

polymorphic function의 유저로써, parametricity는 **제한**이 아닌 **보증**이라고 볼 수 있다. 일반적으로 어떻게 동작할지 확실하게 보증된 제품이 사용하기 편리하다. Haskell 함수의 타입만을 통해 함수의 많은 것을 알 수 있는 이유가 바로 parametricity이다.

가끔은 타입에 기반해서 결정하는 것이 유용할 경우가 있다. 예를 들어, 덧셈 연산이다. 덧셈 연산이 polymorphic이라는 것을 안다.(`Int`, `Integer`, `Double` 타입 등에 대해서 동작하기 때문이다.) 하지만 어떤 타입에 대한 덧셈인지 알아야 실제 덧셈을 수행할 수 있다. `Integer`와 `Doubles` 타입의 덧셈은 완전히 다른 방식으로 동작하기 때문이다. 어떻게 동작하는 걸까? 그냥 적어놓으면 알아서 돌아가는 걸까?

#### 그렇지 않다!

사실 우리는 Haskell에서 타입에 기반해서 어떠한 동작을 할 수 있을지 결정할 수 있다.(전에 모색했던 방법 말고!) `(+)`의 타입을 통해 살펴보자.

```bash
Prelude> :t (+)
(+) :: Num a => a -> a -> a
```

대체 `Num a =>`란 뭘까? 사실 `(+)` 뿐만 아니라 많은 standard 함수들이 `=>`를 포함하고 있다. 다른 몇가지 예를 살펴보자.

```bash
Prelude> :t (==)
(==) :: Eq a => a -> a -> Bool
Prelude> :t (<)
(<) :: Ord a => a -> a -> Bool
Prelude> :t (show)
(show) :: Show a => a -> String
```

대체 이게 무엇일까?

## Type classes

`Num`, `Eq`, `Ord`, `Show` 등은 타입 클래스이다. 그리고 우리는 `(==)`, `(<)`, `(+)`와 같은 함수를 **타입 클래스 polymorphic**이라고 한다. 직관적으로 얘기하자면, 타입 클래스는 특정 연산이 정의된 타입 집합에 해당한다. 타입 클래스 polymorphic 함수는 해당 타입 클래스의 인스턴스인 타입에 대해서만 작동한다. `Eq` 타입 클래스 예시를 통해서 살펴보자.

```haskell
class Eq a where
    (==) :: a -> a -> Bool
    (/=) :: a -> a -> Bool
```

위 코드의 뜻을 살펴보자면 이러하다.
- `Eq`는 `a` 타입 파라미터와 함께 선언된 타입 클래스이다.
- 타입 `a`가 `Eq`의 인스턴스가 되려고 한다면 두 함수(`(==)`와 `(/=)`)를 타입 시그니처에 맞도록 정의해야 한다.
- 예를 들어, `Int`를 `Eq`의 인스턴스가 되게 하려면 `(==) :: Int -> Int -> Bool`과 `(/=) :: Int -> Int -> Bool`을 정의해야 한다.
    - Standard prelude에서 정의하고 있기 때문에 당연히 프로그래머가 따로 정의할 필요는 없다.


다시 `(==)`를 살펴보자.

```haskell
(==) :: Eq a => a -> a -> Bool
```

`=>` 앞에 있는 `Eq`는 **타입 클래스 제약**이다. "`Eq` 클래스에 속한 모든 타입 `a`에 대해서, `(==)`는 2개의 `a`타입 값을 입력받을 수 있으며 `Bool`타입 값을 출력한다. `Eq` 클래스의 인스턴스가 아닌 값으로 `(==)` 함수를 호출한다면 타입 에러가 발생한다. 만약 일반적인 polymorphic type이 "함수 호출자가 어떤 타입을 선택하던 작동할 것이다"라는 약속이라면, **타입 클래스 polymorphic** 함수는 "함수 호출자가 **타입 클래스의 인스턴스 중**에 어떤 타입을 선택하던 작동할 것이다"라는 한층 **제약된 약속**이다.

중요한 점은 `(==)`이 사용될 때, 컴파일러는 `(==)`의 구현부 중 어떤것을 선택할 지 알아내기 위해 타입 추론을 사용한다. 즉, Java의 overloaded method와 비슷하다.

타입을 만들어보고 `Eq`의 인스턴스를 선언해보는 것을 통해 실제로 어떻게 작동하는지 알아보자.
```haskell
data Foo = F Int
        |  G Char

instance Eq Foo where
    (F i1) == (F i2) = i1 == i2
    (G c1) == (G c2) = c1 == c2
    _ == _ = False

    foo1 /= foo2 = not (foo1 == foo2)
```

`(==)`와 `(/=)`를 이러한 방식으로 정의해야만 하는 것은 다소 성가신 일이다. 사실 타입 클래스는 (해당 타입 클래스의 인스턴스가 기본 정의를 자체적으로 오버라이드하지 않는) 다른 메소드를 통해 메소드의 디폴트 구현부를 제공할 수 있다.

그래서 이러한 방식으로 `Eq` 클래스의 선언 방법을 생각해볼 수 있다.

```haskell
class Eq a where
    (==) :: a -> a -> Bool
    (/=) :: a -> a -> Bool
    x /= y = not (x == y)
```

이제 `Eq` 클래스의 인스턴스를 선언하는 모두가 `(==)`를 구현하면 `(/=)`를 거저 얻을 수 있다. 하지만 반대로 `(/=)`를 구현하고 싶다면 그렇게 해도 된다.

실제로 `Eq` 클래스가 정의되어 있는 방법은 다음과 같다.

```haskell
class Eq a where
    (==), (/=) :: a -> a -> Bool
    x == y = not (x /= y)
    x /= y = not (x == y)
```

즉 `Eq` 클래스의 인스턴스를 만들 때, `(==)`와 `(/=)` 중 편한 것을 골라서 정의하면 된다. 다른 하나는 자동으로 정의될 것이다. (하지만 아무것도 정의하지 않을 시, 무한 재귀가 발생하기 때문에 주의해야 한다!)

GHC에서 자동으로 standard 타입 클래스(`Eq`와 같은)의 인스턴스를 만들어주기도 한다. 다음과 같은 방식으로 쓴다.

```haskell
data Foo' = F' Int
        |   G' Char
    deriving (Eq, Ord, Show)
```

`deriving` 키워드를 통해서 GHC에게 `Foo'` 타입을 `Eq`, `Ord`, `Show` 타입 클래스의 인스턴스로 만든다. 그에 속하는 구현부를 자동으로 생성해주는 것이다.


