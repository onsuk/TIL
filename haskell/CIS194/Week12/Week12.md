# Monads

## Motivation

지난 2주동안 *특별한 콘텍스트*에서 일어나게 되는 계산을 `Applicative` 클래스를 통해 높은 추상화 레벨에서 할 수 있다는 것을 살펴보았다. 예를 들어, 실패 가능성이 있는 `Maybe`, 여러 개의 결과값이 있을 수 있는 `[]`, `((->) e)`를 사용해서 environment를 다룰 때, 혹은 'combinator'을 사용해서 parser을 구성하는 것 등이다.

지금까지 살펴봐왔던 것은 고정된 인자 집합에 data constructor을 적용하는 것처럼 변하지 않는 구조의 계산이었다. 만약 계산의 구조를 미리 알 수 없는 상황이라면 어떻게 하면 될까? 다시 말해, intermediate한 결과값을 기반으로 결정하려면 어떻게 해야 될까?

예를 들어 `Parser`을 다시 생각해보자. 그리고 `Functor`과 `Applicative` 인스턴스로 구현했다고 가정해보자.

```haskell
newtype Parser a = Parser { runParser :: String -> Maybe (a, String) }
instance Functor Parser where
    ...

instance Applicative Parser where
    ...
```

`Parser a` 타입의 값은 `String`을 입력값으로 받아서, 가능한 경우 `a` 타입의 값과 파싱되지 않은 남은 부분 `String`을 함께 생성한다. 예를 들어 integers에 대한 parser인 경우, 다음과 같은 문자열을 입력값으로 받는다고 하자.

```
"143xkkj"
```

이것은 아마 다음과 같은 결과값을 생성할 것이다.

```haskell
Just (143, "xkkj")
```

homework에서 볼 수 있었듯이, 우리는 이제 다음과 같이 쓸 수 있다.

```haskell
data Foo = Bar Int Int Char

parseFoo :: Parser Foo
parseFoo = Bar <$> parseInt <*> parseInt <*> parseChar
```

`parseInt :: Parser Int`와 `parseChar :: Parser Char` 함수를 갖고 있다고 가정해보자. `Applicative` 인스턴스는 자동적으로 실패 가능성에 대해 핸들링할 것이다.(컴포넌트 중 하나라도 fail이라면 `Foo` 전체가 fail일 것이다.) 그리고 소비되지 않는 남은 `String`에 대해 순차적으로 해결할 것이다.

하지만 다음과 같이 연속적인 숫자가 포함된 파일을 파싱하려고 하는 경우를 생각해보자.

```
4 78 19 3 44 3 1 7 5 2 3 2
```

파일의 첫 번째 숫자는 그 후의 '그룹'의 길이에 대해 말해준다. 그룹에 해당하는 숫자 다음에 나오는 숫자는, 다음 그룹의 길이에 대해 말해준다. 그래서 다음과 같은 그룹으로 나눠지게 된다.

```haskell
78 19 3 44  -- first group
1 7 5       -- second group
3 2         -- third group
```

조금 얄궂은 예제이지만, 사실 "real-world" 파일 형식에서도 비슷한 원칙을 따르는 경우가 많다. block의 길이를 말해주는 header이나, 파일의 어디에서 찾아야 할지를 말해주는 것 등을 읽게 된다.

이러한 타입의 파일 형식에 대한 parser을 작성해보자.

```haskell
parseFile :: Parser [[Int]]
```

유감스럽게도 `Applicative` 인터페이스만을 이용해서는 불가능하다. `Applicative`는 이전의 결과값에 기반해서 다음에 무엇을 할 지 결정하는 것이 불가능하기 때문이다. 실행하려고 하는 파싱 연산을, 결과값을 보기 전에 미리 결정해야만 한다.

하지만 `Parser` 타입이 이러한 패턴을 사용할 수 있다는 것이 밝혀졌고, 그것은 `Monad` 타입 클래스로 추상화된다.

## Monad

`Monad` 타입 클래스는 다음과 같이 정의되어 있다.

```haskell
class Monad m where
    return :: a -> m a
    
    (>>=) :: m a -> (a -> m b) -> m b

    (>>) : m a -> m b -> m b
    m1 >> m2 = m1 >>= \_ -> m2
```

상당히 친숙해 보인다! 이러한 메소드를 `IO` 콘텍스트에서 본 적이 있다. 하지만 이것은 단지 `IO`에만 국한되지 않는다. 유용한 것으로 증명된 `IO`에 관한 모나드 인터페이스일 뿐이다.

`return` 또한 친숙해 보이는데, `pure`과 같은 타입을 갖기 때문이다. 사실 모든 `Monad`는 또한 `Applicative`이며 `pure` 역할을 하는 `return`을 갖고 있다. 둘 다 필요한 이유는 `Monad`가 쓰이고 있던 이후에 `Applicative`가 발명되었기 때문이다.

`(>>)`는 `(>>=)`의 특별한 버전일 뿐이다. 이것은 `Monad` 클래스에 포함되어 있는데, 조금 더 효율적인 구현 제공이 필요할 때 쓰는 인스턴스이다. 하지만 보통의 경우 없어도 괜찮다.(?) 그래서 `(>>)`를 이해하기 위해서는 우선 `(>>=)`를 이해해야 한다.

사실 `fail`이라는 네번째 방법이 있다. 하지만 `Monad` 클래스 안에 `fail`을 넣은 것은 실수이기 때문에 그것을 절대 쓰면 안된다. 그래서 `fail`에 대해서는 말하지 않으려고 한다. (관심있다면 [Typeclassopedia - HaskellWiki](http://www.haskell.org/haskellwiki/Typeclassopedia#do_notation)에서 읽어보도록 하자.)

"bind"라고 읽는 `(>=)`는 모든 action이 있는 곳이다.(?) 눈을 크게 뜨고 타입을 살펴보자.

```haskell
(>>=) :: m a -> (a -> m b) -> m b
```

`(>=)`는 두 개의 인자를 받는다. 첫 번째 인자는 `m a` 타입의 값이다.(번외로, 이러한 값들은 가끔 **monadic values**나 **computations**로 불린다. **mobits**라고 부르자고도 제안되었다. 이들을 지칭하는 데에 있어 한가지 하지 말아야 할 것이 있는데, 바로 "**Monads**"이다. type constructor `m`이 monad이며, 그로 인해 그 명칭은 kind error가 있기 때문이다.) 어떠한 경우든, `m a` 타입의 "mobit"이 `a` 타입의 값을 생성하는 계산을 나타낸다. 혹은 다음과 같은 "effect"를 가질 수도 있다.

- `c1 :: Maybe a`는 실패할 수도 있으며 성공했을 때에 `a`를 생성하는 계산이다.
- `c2 :: [a]`는 `as` 계산이다.
- `c3 :: Parser a`는 암묵적으로 `String`을 소비하며 가능한 경우 `a`를 생성하는 계산이다.
- `c4 :: IO a`는 잠재적인 I/O effect를 갖고 `a`를 생성하는 계산이다.

이제 두번째 인자를 살펴보도록 하자. `(a -> m b)` 타입의 함수이다. 즉, 첫번째 계산의 결과값을 기반으로 다음 계산을 결정한다는 것이다. 