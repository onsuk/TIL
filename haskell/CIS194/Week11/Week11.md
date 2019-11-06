# Applicative functors, Part II

`Functor`와 `Applicative` 타입 클래스에 대해 복습해보자.

```haskell
class Functor f where
    fmap :: (a -> b) -> f a -> f b

class Functor f => Applicative f where
    pure :: a -> f a
    (<*>) :: f (a -> b) -> f a -> f b
```

모든 `Applicative`는 `Functor`이기도 하다. `fmap`을 `pure`과 `(<*>)`를 통해 구현할 수 있을까? 시도해보도록 하자.

```haskell
fmap g x = pure g <*> x
```

어찌되었든 옳은 타입이긴 하다. 하지만 `=`가 성립하지 않게 하는 타입을 갖는 `Functor`과 `Applicative` 인스턴스를 만드는 것은 그닥 어렵지 않게 느껴진다. 이것은 상당히 모호한 상황이기 때문에, 우리는 `=`가 유지되어야만 한다는 law를 규정한다. 이것은 `Functor`과 `Applicative` 인스턴스가 함께 잘 쓰이게 하기 위한 일반적인 표현 방법이다.

이제 `Applicative` 인스턴스에 대한 몇가지 예제를 살펴보도록 하자.

## More Applicative Examples

#### Lists

List에 대한 `Applicative` 인스턴스는 어떨까? 두 가지 종류의 인스턴스가 가능할 것이다. 하나는 `zip`과 같이 함수의 리스트와 인자의 리스트를 요소별로 매치시키는 것이다. 그리고 다른 하나는 가능한 모든 방법으로 함수와 인자를 결합하는 방법이다.

첫번째로, 가능한 모든 방법으로 결합한 인스턴스를 만들어 보도록 하자. (이것이 디폴트 인스턴스이다. 다음 강의에서 조금 더 명확하게 설명할 것이다.) 이러한 관점에서, 리스트는 비결정적이라고 볼 수 있다. 즉 `[a]` 타입의 값은 여러 가능성이 있는 하나의 값으로 생각할 수 있다. 그리고 `(<*>)`는 비결정적 함수 적용이라고 볼 수 있다. 즉, 비결정적 인자에 비결정적 함수 적용을 하는 것이다.

```haskell
instance Applicative [] where
    pure a        = [a]         -- 단일 값에 그저 리스트를 래핑한 결정적인 값
    [] <*> _      = []
    (f:fs) <*> as = (map f as) ++ (fs <*> as)
```

다음 예제를 살펴보자.

```haskell
names = ["Joe", "Sara", "Mae"]
phones = ["555-5555", "123-456-7890", "555-4321"]

employess1 = Employee <$> names <*> phones
```

이러한 단편적인 예제를 보고는 조금 감흥이 없을 수도 있지만, 그래도 가능한 모든 방법으로 결합하는 것은 그닥 어렵지 않아 보인다. 예를 들어, 다음과 같이 비결정적인 산술을 할 수 있다.

```haskell
(.+) = liftA2 (+)       -- 덧셈이 Applicative context로 lift되었다.
(.*) = liftA3 (*)       -- 곱셈도 마찬가지이다.

-- 비결정적인 산술
n = ([4, 5] .* pure 2) .+ [6, 1]        -- 4와 5를 2와 곱하고, 6과 1을 더한다.

-- 실패 가능성이 있는 산술
m1 = (Just 3 .+ Just 5) .* Just 8
m2 = (Just 3 .+ Nothing) .* Just 8
```

> 현재 컴파일러 기준으로는 예제의 `(.+)`과 `(.*)`를 정의하려고 하면 다음과 같은 에러를 뿜어낸다. 타입과 관련된 에러인것 같지만 잘 모르겠다.

```
/Users/onz/haskell-practice/src/Thing.hs:88:8: error:
    • Ambiguous type variable ‘f0’ arising from a use of ‘liftA2’
      prevents the constraint ‘(Applicative f0)’ from being solved.
      Relevant bindings include
        (.*) :: f0 Integer -> f0 Integer -> f0 Integer
          (bound at /Users/onz/haskell-practice/src/Thing.hs:88:1)
      Probable fix: use a type annotation to specify what ‘f0’ should be.
      These potential instances exist:
        instance Control.Arrow.Arrow a => Applicative (WrappedArrow a b)
          -- Defined in ‘Control.Applicative’
        instance Monad m => Applicative (WrappedMonad m)
          -- Defined in ‘Control.Applicative’
        instance Applicative ZipList -- Defined in ‘Control.Applicative’
        ...plus five others
        ...plus 23 instances involving out-of-scope types
        (use -fprint-potential-instances to see them all)
    • In the expression: liftA2 (*)
      In an equation for ‘.*’: (.*) = liftA2 (*)
```

> 그래서 아래와 같은 코드로 실습해봤고 다음과 같은 결과를 확인했다.

```haskell
n' = liftA2 (+) [6, 1] (liftA2 (*) [4, 5] (pure 2))

m1' = liftA2 (*) (Just 8) (liftA2 (+) (Just 3) (Just 5))
m2' = liftA2 (*) (Just 8) (liftA2 (+) (Just 3) Nothing)
```

충분히 예상할 수 있는 결과값이다.
```
*Thing> n'
[14,16,9,11]
*Thing> m1'
Just 64
*Thing> m2'
Nothing
```

그 다음은 요소별 결합을 하는 인스턴스를 만들어 보자. 우선, 한가지 중요한 질문에 답해야 한다. 각자 길이가 다른 리스트는 어떻게 다룰 것인가? 어떤 사람은 더 긴 리스트의 끄트머리를 더 짧은 리스트의 길이에 맞춰서 잘라내어 없애는 것이 현명한 생각이라고 한다. 물론 다른 방법도 가능하다. 더 짧은 리스트의 마지막 요소를 복사해서 늘리는 방법 등이다. 하지만 이 방법에서의 빈 리스트는 어떻게 하면 좋을까? 혹은 더 짧은 리스트에 '중립적인' 요소를 추가해서 늘려주는 방법도 있을 것이다. 하지만 그렇게 된다면 적용을 위한 `Monoid` 인스턴스 혹은 'default' 역할을 해줄 인자가 필요할 것이다.

이러한 결정은 어떻게 `pure`을 구현하는 지에 영향을 준다. 우리는 법칙을 지켜야 하기 때문이다.

```haskell
pure f <*> xs === f <$> xs
```

오른쪽 식은 `f`를 `xs`의 모든 요소에 적용하여 만들어진, `xs`와 같은 길이의 리스트이다. 왼쪽 식이 똑같은 결과값을 같게 하는 유일한 방법은 `pure`을 통해 `f`의 복사본으로 이루어진 무한 리스트를 만드는 것이다. `xs`의 길이가 얼만큼 길 지 미리 알지 못하기 때문이다.

다른 리스트 인스턴스와 구분하기 위해 `newtype` 래퍼를 사용해서 인스턴스를 만들도록 해보자. 표준 함수에 있는 `zipWith` 또한 유용하다.

```haskell
newtype ZipList a = ZipList { getZipList :: [a] }
    deriving (Eq, Show, Functor)

instance Applicative ZipList where
    pure = ZipList . repeat
    ZipList fs <*> ZipList xs = ZipList (zipWith ($) fs xs)

employees2 = getZipList $ Employee <$> ZipList names <*> ZipList phones
```

#### Reader/environment

마지막 예제인 `(->) e`를 살펴보자. 이것은 `reader` 혹은 `environment` applicative로 알려져있다. 이것은 말 그대로 `e`라는 'environment'에서 'reading'을 가능하게 하기 때문이다. 인스턴스를 구현하는 것 자체는 그닥 어렵지 않지만, 정신을 바짝 차리고 타입을 살펴보도록 하자.

```haskell
instance Functor ((->) e) where
    fmap = (.)

instance Applicative ((->) e) where
    pure = const
    f <*> x = \e -> (f e) (x e)
```

`Employee` 예제이다.

```haskell
data BigRecord = BR { getName :: Name
                    , getSSN :: String
                    , getSalary :: Integer
                    , getPhone :: String
                    , getLicensePlate :: String
                    , getNumSickDays :: Int
                    }

record = BR "Onsuk" "xxx-xx-xxxx" 60000000 "555-1234" "ASD-1234" 2

getEmp :: BigRecord -> Employee
getEmp = Employee <$> getName <*> getPhone

exam01 = getEmp record
```

다음과 같은 결과를 확인할 수 있다.

```
*Thing> exam01
Employee {name = "Onsuk", phone = "555-1234"}
```

## Aside: Levels of Abstraction

`Functor`은 멋진 도구임에 반해 비교적 쉽다. 그리고 언뜻 봤을때 '어? `Functor`이 제공하는 것에 더해서 `Applicative`는 대체 뭐가 더 추가된 거지? 별반 차이 없는데?' 라고 할 수 있다. 하지만 소정의 추가기능으로 인해 엄청난 효과를 가져온다. `Applicative`(그리고 다음 강의에서 보게 될 `Monad`)는 '계산 모델'이라고 불릴 만하다. 하지만 `Functor`은 그렇지 않다.

`Applicative`와 `Monad`를 통해 프로그래밍할 때에는, 여러 레벨의 추상화가 포함되어 있다는 것을 항상 명심해야 한다. 간략히 말해 추상화란, 낮은 레벨의 디테일한 부분은 숨기고 높은 레벨의 유용한 인터페이스를 제공하는 것이다. 높은 레벨에 해당하는 인터페이스는 낮은 레벨의 구현에 대해서 신경 쓸 필요가 없다. 비록 낮은 레벨의 디테일한 부분이 어떠한 '누수'가 있더라도 말이다. 계층의 추상화에 대한 아이디어는 편만하게 쓰인다. User Program, OS, kernel, integrated circuits(집적 회로), gates(논리 회로), silicon 또는 HTTP, TCP, IP, Ethernet, 프로그래밍 언어, 바이트 코드, 어셈블리, 머신 코드 등에 대해 생각해보라. 우리가 봐왔듯이 Haskell은 Haskell 내의 프로그램을 통해 여러 층의 추상화를 구성하는 많은 도구를 제공한다. 즉 '프로그래밍 언어' 계층을 높은 레벨의 추상화로 끌어올리고 있다. 이것은 강력한 도구이지만 혼란을 조장할 수 있다. 여러 레벨의 추상화에 대해 생각할 수 있어야 하며, 또한 여러 레벨을 오가며 생각할 수 있어야 한다.

특히 `Applicative`와 `Monad`에 관하여 고려해야 할 두가지 레벨이 있다. 첫번째 레벨은 다양한 `Applicative`와 `Monad` 인스턴스의 구현 레벨이다. 'raw Haskell' 레벨 말이다. homework에서 `Parser`을 위한 `Applicative` 인스턴스를 구현해보며 이러한 단계에 대한 경험을 해봤을 것이다.

`Parser`와 같은 타입을 위한 `Applicative` 인스턴스가 있는 상황이라면, `Applicative` 인터페이스 사용을 통해 `Parser`로 프로그래밍을 하는 것과 같이 **높은 레벨의 추상화 계층으로 끌어올리는 것**이 요점이다. 여기서 `Parser`과 `Applicative` 인스턴스가 어떻게 구현되었는지에 대해서는 신경쓰지 않아도 된다. 이러한 단계에서 프로그래밍하는 것(높은 레벨)은 인스턴스를 실제로 구현하는 것(낮은 레벨)에 비해 몹시 다른 경험을 할 수 있다. 몇 가지 예제를 더 살펴보자.

## The Applicative API

`Applicative`와 같이 통합된 인터페이스를 갖고 있다는 것의 장점은 generic한 도구와 (`Applicative` 인스턴스로 이루어진 어떠한 타입이든 동작하는) control structure을 쓸 수 있다는 점이다. 첫 번째 예제를 살펴보도록 하자.

```haskell
pair :: Applicative f => f a -> f b -> f (a, b)
```

`pair`은 두 개의 `Applicative f` 콘텍스트 값을 받고 pair한다. paring할 함수를 받고 `(<$>)`와 `(<*>)`를 사용해서 인자를 **lift**해보도록 하자.

```haskell
pair fa fb = (\x y -> (x, y)) <$> fa <*> fb
```

작동하긴 하지만 조금 더 단순화할 수 있다. Haskell이 pair constructor을 뜻하는 `(,)`라는 특별 문법을 제공한다. 그래서 우리는 다음과 같이 쓸 수 있다.

```haskell
pair fa fb = (,) <$> fa <*> fb
```

그런데 사실 이러한 패턴을 이전에 보았다. 바로 `liftA2` 패턴이다. (이것이 바로 진정한 `Applicative`의 길...) 더욱 단순화해보자.

```haskell
pair fa fb = liftA2 (,) fa fb
```

하지만 인자를 명시할 이유가 없기 때문에, 우리는 마지막 버전에 도달하게 된다.

```haskell
pair = liftA2 (,)
```

이제 이 함수는 어떤 행위를 하는가? 물론 `f`의 선택에 영향을 받는다. `f`에 따라 달라지는 몇가지 예를 살펴보도록 하자.

- `f = Maybe`
    - 인자 중 하나라도 `Nothing`이라면 결과값은 `Nothing`이다.
    - 둘다 `Just`라면 결과값은 paring된 `Just`이다.
- `f = []`
    - 두 리스트의 곱집합이 결과값이다.
- `f = ZipList`
    - 표준 함수의 `zip` 함수와 같다.
- `f = IO`
    - 두 개의 `IO`를 순차적으로 실행하고, 결과값을 페어링해서 반환한다.
- `f = Parser`
    - 두개의 parser을 순차적으로 실행한다. parser은 연속적인 입력값을 소비하고 pair로써 결과값을 반환한다. parser 중 하나라도 fail이 난다면, 전체가 fail이 된다.

다음 함수의 구현부를 작성할 수 있겠는가? `f`가 위의 타입과 같이 대체되었을 때 어떻게 함수가 작동할 지 고려해보라.

```haskell
(*>) :: Applicative f => f a -> f b -> f b
mapA :: Applicative f => (a -> f b) -> ([a] -> f [b])
sequenceA :: Applicative f => [f a] -> f [a]
replicateA :: Applicative f => Int -> f a -> f [a]
```
