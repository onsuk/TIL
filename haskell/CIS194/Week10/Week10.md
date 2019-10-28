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

하지만 우리가 `Name`과 `String`을 갖고 있는게 아니라, `Maybe Name`과 `Maybe String`을 갖고 있다고 가정해보자. 아마도 일부 파일을 오류로 파싱하거나 일부 필드를 비워두거나, 비슷한 종류의 파일을 파싱했을 것이다. 한 마디로 `Employee`를 만들 수 없다. 하지만 `Maybe Employee`는 만들 수 있다. 즉 우리는 `(Name -> String -> Emploee)` 함수를 `(Maybe Name -> Maybe String -> Maybe Employee)` 함수로 바꿀 수 있다. 이 타입으로 무언가를 쓸 수 있을까?

```haskell
(Name -> String -> Employee) ->
(Maybe Name -> Maybe String -> Maybe Employee)
```

물론이다. 어떻게 동작할 지 상상해보자. 만약 `Name`이나 `String`이 `Nothing`이라면 `Notihng`을 얻을 것이다. 만약 둘 다 `Just`라면 `Employee` data constructor로 만들어졌으며, `Just`로 감싸진 `Employee`를 얻을 것이다.

고려할 사항이 있다. 이제 `Name`과 `String` 대신 `[Name]`과 `[String]`에 대해 생각해보자. 아마 `[Employee]`를 얻을 수 있겠지? 아래와 같이 원할 것이다.

```haskell
(Name -> String -> Employee) ->
([Name] -> [String] -> [Employee])
```

이렇게 동작하기 위한 두가지 방법을 상상할 수 있다. `Employees`를 구성하기 위해 일치하는 `Name`과 `String`을 조합하거나, 가능한 모든 방법으로 `Name`과 `String`을 조합하는 것이다.

혹은 `e` 타입으로 만들어진 `(e -> Name)`와 `(e -> String)`은 어떠한가? 예를 들어, `e`이 거대한 데이터 구조라고 하자. 그렇다면 `Name`과 `String`을 어떻게 추출해낼 수 있는지 말해주는 함수를 갖고 있게 된 것이다. 그렇다면 똑같은 데이터 구조를 갖는 `Employee`를 추출해낼 수 있는 '레시피' 역할을 하는 `(e -> Employee)`를 만들 수 있을까?

```haskell
(Name -> String -> Employee) ->
((e -> Name) -> (e -> String) -> (e -> Employee))
```

문제 없다. 그리고 이번엔 함수를 쓰기 위해서 정말 한가지 방법밖에 없다.

## Generalizing

이제 이러한 패턴의 유용함을 알았으니 조금 일반화해보도록 하자. 우리가 원하는 함수의 타입은 실제로 다음과 같을 것이다.

```haskell
(a -> b -> c) -> (f a -> f b -> f c)
```

음... 어디서 본것 같다. 이것은 `fmap`과 꽤 닮아있다.

```haskell
fmap :: (a -> b) -> (f a -> f b)
```

유일한 차이점은 인자 개수이다. 두 개의 인자밖에 못 받기 때문에, `fmap2` 함수를 호출해보자. `fmap`처럼 `fmap2`를 쓸 수 있을 것이다. 그래서 `f` Functor 제약이 필요하다.

```haskell
fmap2 :: Functor f => (a -> b -> c) -> (f a -> f b -> f c)
fmap2 h fa fb = undefined
```

할 수 있는만큼 해봤지만, Functor은 `fmap2`를 구현하기에 충분하지 않다. 무엇이 잘못되었을까? 우리는 다음과 같은 것들을 갖고 있다.

```haskell
h :: a -> b -> c
fa :: f a
fb :: f b
```

`h`의 타입을 `a -> (b -> c)`와 같이 쓸 수 있다는 점을 유의하라. 그래서 우리는 `a`를 갖는 함수와, `f a` 타입을 갖는 값을 갖고 있다. `f` 함수를 lift over(?)하기 위해, 우리가 할 수 있는 유일한 것은 `fmap`을 쓰는 것이다. 아래와 같은 타입의 결과를 볼 수 있다.

```haskell
h :: a -> (b -> c)
fmap h :: f a -> f (b -> c)
fmap h fa :: f (b -> c)
```
