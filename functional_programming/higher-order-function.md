# 고차 함수(Higher-Order Functin)

**함수를 인자**로 전달받거나 **함수를 반환**하는 함수이다.

```javascript
// javascript
const twiceFunc = (f, v) => f(f(v));
const square = v => v * v;
console.log(twiceFunc(square, 2)); // 16
```

`twiceFunc`은 `f`라는 함수를 `f(v)`라는 값에다가 apply 한다. 즉 함수를 2회 적용하는 역할을 한다.

다음은 동일한 역할을 하는 함수의 Haskell 코드이다.

```haskell
-- Haskell
twiceFunc :: (a -> a) -> a -> a
twiceFunc f x = f(f x)
```

위 두 예제 코드에서 `twiceFunc`이 **고차 함수**(Higher-Order Function)이다.

[JavaScript Built-in Functions](https://www.tutorialspoint.com/javascript/javascript_builtin_functions.htm) 중 `map`, `filter`, `reduce` 등이 고차 함수이다.

> Higher-Order의 엄밀한 의미는 1) 함수를 인자로 받는 함수, 2) 함수를 반환하는 함수 2가지를 포함한다. 하지만 실제로 **Curried**라는 용어가 2) *함수를 반환하는 함수*를 대표하는 용어로 쓰이기 때문에, Higher-Order은 보통 1) **함수를 인자로 받는 함수**로 쓰이는 경우가 많다.

# Reference
[Higher-Order Function 이란 무엇인가](https://medium.com/@la.place/higher-order-function-%EC%9D%B4%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80-1c61e0bea79)

[하스켈로 배우는 프로그래밍](https://book.naver.com/bookdb/book_detail.nhn?bid=6049202)