# CIS194 - Week 10

## Applicative functors, Part I

다음 `Employee` 타입에 대해 살펴보자.

```haskell
type Name = String

data Employee = Employee { name :: Name
                         , phone :: String }
                deriving Show
```

Data constructor `Employee`는 다음과 같은 타입을 가진다.

```haskell
Employee :: Name -> String -> Employee
```

`Name`과 `String`이 있다면, data constructor `Employee`을 적용해서 `Employee` object를 만들 수 있다.

하지만 우리가 `Name`과 `String`을 갖고 있는게 아니라, `Maybe Name`과 `Maybe String`을 갖고 있다고 가정해보자. 아마도 오류로 가득찬 파일을 파싱하거나 일부 필드를 비워두거나, 비슷한 종류의 파일을 파싱했을 것이다. 한 마디로 `Employee`를 만들 수 없다. 하지만 `Maybe Employee`는 만들 수 있다. 즉 우리는 `(Name -> String -> Employee)` 함수를 `(Maybe Name -> Maybe String -> Maybe Employee)` 함수로 바꿀 수 있다. 이 타입으로 무언가를 쓸 수 있을까?

```haskell
(Name -> String -> Employee) ->
(Maybe Name -> Maybe String -> Maybe Employee)
```

물론이다. 어떻게 동작할 지 상상해보자. 만약 `Name`이나 `String`이 둘 중 하나라도 `Nothing`이라면 결과값으로 `Notihng`을 얻을 것이다. 만약 둘 다 `Just`라면, `Just`로 감싸졌으며 `Employee` data constructor로 만들어진 `Employee`를 얻을 것이다.

계속해서 생각해보자. 이제 `Name`과 `String` 대신 `[Name]`과 `[String]`에 대해 생각해보자. 아마 `[Employee]`를 얻을 수 있을 것 같지 않은가? 아래와 같은 결과를 기대할 것이다.

```haskell
(Name -> String -> Employee) ->
([Name] -> [String] -> [Employee])
```

이렇게 동작하기 위한 두가지 방법을 생각해볼 수 있다. `Employees`를 구성하기 위해 일치하는 `Name`과 `String`을 조합하거나, 가능한 모든 방법으로 `Name`과 `String`을 조합하는 것이다.

혹은 `e` 타입으로 만들어진 `(e -> Name)`와 `(e -> String)`은 어떠한가? 예를 들어, `e`가 방대한 규모의 데이터 구조라고 하자. 그렇다면 `Name`과 `String`을 어떻게 추출해낼 수 있는지 말해주는 함수를 갖고 있게 된 것이다. 그렇다면 똑같은 데이터 구조를 갖는 `Employee`를 추출해낼 수 있는 '레시피' 역할을 하는 `(e -> Employee)`를 만들 수 있을까?

```haskell
(Name -> String -> Employee) ->
((e -> Name) -> (e -> String) -> (e -> Employee))
```

문제 없다. 그리고 이 함수를 쓰기 위해선 이번엔 정말 한가지 방법밖에 없다.

## Generalizing

이제 이러한 패턴의 유용함을 알았으니 조금 일반화해보도록 하자. 우리가 원하는 함수의 타입은 실제로 다음과 같을 것이다.

```haskell
(a -> b -> c) -> (f a -> f b -> f c)
```

음... 어디서 본것 같다. 이것은 `fmap`과 꽤 닮아있다.

```haskell
fmap :: (a -> b) -> (f a -> f b)
```

유일한 차이점은 인자 개수이다. `fmap` 함수는 두 개의 인자밖에 못 받기 때문에, 우리가 원하는 함수인 `fmap2` 함수를 써보자. `fmap`처럼 `fmap2`를 쓸 수 있을 것이다. 그래서 `f` `Functor` 제약이 필요하다.

```haskell
fmap2 :: Functor f => (a -> b -> c) -> (f a -> f b -> f c)
fmap2 h fa fb = undefined
```

할 수 있는만큼 해봤지만, `Functor`은 `fmap2`를 구현하기에 충분하지 않다.

무엇이 잘못되었을까? 우리는 다음과 같은 것들을 갖고 있다.

```haskell
h :: a -> b -> c
fa :: f a
fb :: f b
```

`h`의 타입을 `a -> (b -> c)`와 같이 쓸 수 있다는 점을 기억하자. 그래서 우리는 `a`를 인자로 갖는 함수와, `f a` 타입을 갖는 값 `fa`를 갖고 있다. `f` 함수를 lift over하기 위해, 우리가 할 수 있는 유일한 것은 `fmap`을 쓰는 것이다. 아래와 같은 타입의 결과를 볼 수 있다.

```haskell
h :: a -> (b -> c)
fmap h :: f a -> f (b -> c)
fmap h fa :: f (b -> c)
```

이제 우리는 `f (b -> c)`와 `f (b...` ... 여기서 막히게 된다! `fmap`은 더 이상 도움이 되지 않는다. 함수를 `Functor` 콘텍스트 내의 값에 적용하는 방법은 될 수 있지만, 우리가 지금 필요한 것은 `Functor` 콘텍스트 내의 함수를 `Functor` 콘텍스트의 값에 적용하는 방법이다.


## Applicative

이러한 종류의 'contextual application' `Functor`은 **applicative**라고 부를 수 있다. 그리고 `Applicative` 클래스가 이러한 패턴을 정의한다. 

```haskell
class Functor f => Applicative f where
    pure :: a -> f a
    (<*>) :: f (a -> b) -> f a -> f b
```

`(<*>)` 연산자는 'apply'의 줄임말인 'ap'으로 자주 발음된다. `(<*>)`는 정확히 'contextual application'의 원칙을 고수한다. `Applicative` 클래스의 인스턴스는 `Functor`의 인스턴스이기 때문에, `Applicative` 클래스의 인스턴스에 `fmap`을 항상 쓸 수 있다는 점을 유의하자. `Applicative`는 또 다른 메소드 `pure`을 갖고 있다. `pure`은 컨테이너에 `a` 타입의 값을 넣는다. 여기서 흥미로운 점은 `fmap0`이 `pure`의 또 다른 reasonable한 이름일 수 있다는 점이다.

```haskell
pure :: a              -> f a
fmap :: (a -> b)       -> f a -> f b
fmap2 :: (a -> b -> c) -> f a -> f b -> f c
```

이제 우리는 `(<*>)`를 갖고 있으니 `fmap2`를 구현할 수 있다. 이 함수는 하스켈 표준 라이브러리에는 `liftA2`라는 이름으로 존재한다. (`Control.Applicative` 모듈 안에 있다.)

```haskell
liftA2 :: Applicative f => (a -> b -> c) -> f a -> f b -> f c
liftA2 h fa fb = (h `fmap` fa) <*> fb
```

사실, 이러한 패턴은 `Control.Applicative` 모듈에서 흔하게 정의되어 있다. `(<$>)`은 `fmap`의 또 다른 이름이다.

```haskell
(<$>) :: Functor f => (a -> b) -> f a -> f b
(<$>) = fmap
```

그래서 다음과 같이 쓸 수 있다.

```haskell
liftA2 h fa fb = h <$> fa <*> fb
```

`liftA3`은 어떨까?

```haskell
liftA3 :: Applicative f => (a -> b -> c -> d) -> f a -> f b -> f c -> f d
liftA3 h fa fb fc = ((h <$> fa) <*> fb) <*> fc
```

> 실제로는 `<$>`과 `<*>`에 위의 괄호가 하나도 없어도 우선순위와 연관성에 있어서 잘 동작하도록 정의되어 있다.

`fmap`에서 `liftA2`로 넘어가려면 `Functor`에서 `Applicative`로 바뀌어야 한다. 하지만 `liftA2`에서 `liftA3`으로 넘어가거나 그 다음 `liftA4` 등으로 넘어가는 것은 바뀌는 것이 없다. `Applicative`이면 충분한 것이다.

실제로 이와 같이 여러 인자들을 받을 때 `liftA2`, `liftA3`과 같이 귀찮은 방법을 쓰지 않는다. `f <$> x <*> y <*> z <*> ...`과 같은 방식으로 직접적으로 쓴다. (하지만 partial application할 때는 `liftA2`와 같은 방식을 쓴다.)

그렇다면 `pure`은 무엇일까? `pure`은 functor 타입 `f`의 콘텍스트 안에 있지만 **`f`가 아닌** 어떠한 인자에 함수를 적용하려고 하는 상황을 위한 것이다. 이러한 인자들은 말 그대로 'pure'하기 때문에 그렇게 부른다. apply하기 전에 `pure`을 써서 `f`로 lift 할 수 있다.

```haskell
liftX :: Applicative f => (a -> b -> c -> d) -> f a -> b -> f c -> f d
liftX h fa b fc = h <$> fa <*> pure b <*> fc
```

## Applicative laws

`Applicative`에는 정말 흥미로운 한가지 법칙이 있다.

```haskell
f `fmap` x === pure f <*> x
```

컨테이너 `x`에 함수 `f`를 매핑하면 먼저 컨테이너에 함수를 주입 한 다음 `(<*>)`를 사용하여 `x`에 적용하는 것과 동일한 결과를 줘야 한다.

다른 법칙들이 있지만 그닥 유익하지 않을 수 있다. 정말 필요할 때 읽어보면 좋을 것 같다.

## Applicative examples

#### Maybe

`Maybe`로 시작하는 `Applicative`의 인스턴스를 써보자. `pure`은 `Just`로 감싸는 값을 주입하도록 동작한다. `<*>`은 실패할 가능성이 있는 함수 적용이다. 함수 또는 인자가 하나라도 `Nothing`이라면 결과는 `Nothing`이다.

```haskell
instance Applicative Maybe where
    pure = Just
    Nothing <*> _ = Nothing 
    _ <*> Nothing = Nothing
    Just f <*> Just x = Just (f x)
```

예제를 살펴보자.

```haskell
m_name1, m_name2 :: Maybe Name
m_name1 = Nothing
m_name2 = Just "Brent"

m_phone1, m_phone2 :: Maybe String
m_phone1 = Nothing
m_phone2 = Just "555-1234"

ex01 = Employee <$> m_name1 <*> m_phone1
ex02 = Employee <$> m_name1 <*> m_phone2
ex03 = Employee <$> m_name1 <*> m_phone1
ex04 = Employee <$> m_name2 <*> m_phone2
```

```haskell
*Thing> ex01
Nothing
*Thing> ex02
Nothing
*Thing> ex03
Nothing
*Thing> ex04
Just (Employee {name = "Brent", phone = "555-1234"})
```
