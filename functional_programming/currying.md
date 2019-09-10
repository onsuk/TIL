# Currying

**Currying**이란 여러개의 파라미터를 갖는 함수를 하나의 파라미터를 갖는 함수들로 바꾸는 것이다.

```javascript
// javascript
const sum = (a, b) => a + b
const curriedSum = a => b => a + b
curriedSum(40)(2) // 42
const add2 = curriedSum(2) // (b) => 2 + b
add2(10) // 12
```

위 코드에서 `sum`이라는 함수를 `curriedSum`으로 바꾸는 것을 **Currying**이라고 한다.

다음은 Haskell 코드 예제이다.

```haskell
-- Haskell
mult :: Int -> Int -> Int -> Int
mult x y z = x * y * z
```

두 예제 코드의 `curriedSum`, `mult`와 같이 파라미터를 한 번에 하나씩 받는 함수를 **Curried Function**이라고 한다.

> Curry라는 단어는 [Haskell Brooks Curry](https://en.wikipedia.org/wiki/Haskell_Curry)의 이름에서 유래했다.


#### Reference
[Functional Programming Jargon](https://github.com/sphilee/functional-programming-jargon#currying)

[하스켈로 배우는 프로그래밍](https://book.naver.com/bookdb/book_detail.nhn?bid=6049202)