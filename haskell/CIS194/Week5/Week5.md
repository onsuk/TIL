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

하지만 Haskell에서 이와 같이 코드를 작성할 수 없다. Haskell은 Java와 같이 `instanceof` 연산자가 없기 때문이다. 값의 유형에 대해 묻고 그에 대한 답을 통해 연산을 결정하는 것이 불가능하다. 한 가지 이유를 들자면, Haskell의 타입은 체크된 후 **컴파일러에 의해 지워진다**. 그렇기 때문에 런타임 시에 질의할 수 있는 타입 정보가 없다! (*값의 유형에 대해 묻고 답을 들어야 하는데 말이다!*) 하지만, 곧 보게 될 다른 좋은 이유도 있다.

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
