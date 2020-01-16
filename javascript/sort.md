# Javascript sort

Javascript 내장 함수에 `sort()`가 있는데, 타 언어의 정렬 함수에 비해 다른 점이 있어 정리해보려고 한다.

### arrayobj.sort(sortFunction)

`sortFunction`을 생략하면 오름차순, ASCII 코드 순서로 정렬된다.

`sortFunction`이 제공된다면 함수의 반환값에 따라 다음과 같이 결정된다.
- `sortFunction(a, b) < 0`: `a`가 `b`보다 먼저 오도록 정렬한다.
- `sortFunction(a, b) = 0`: `a`와 `b`를 변경하지 않는다.
- `sortFunction(a, b) > 0`: `b`가 `a`보다 먼저 오도록 정렬한다.

### 문자 정렬
```javascript
const os = ['macos', 'ios', 'windows'];
os.sort(); // ['ios', 'macos', 'windows']
```
`sortFunction`을 생략한 문자 정렬의 경우, 일반적으로 예상하는 것과 같이 정렬된다.

### 숫자 정렬

Javascript의 숫자 정렬의 경우 타 언어와 조금 다르다.
다음과 같은 경우는 일반적으로 예상하는 것과 다르게 정렬된다.

```javascript
const nums = [1, 4, 2, 3, 11, 16, 12];
nums.sort(); // [1, 11, 12, 16, 2, 3, 4]
```

`sortFunction`을 생략했기 때문에 ASCII 코드 값을 기준으로 정렬되기 때문이다. 다음과 같이 작성하면 제대로 된 숫자 정렬을 할 수 있다.

```javascript
// 오름 차순
let nums = [1, 4, 2, 3, 11, 16, 12];
nums.sort((a, b) => a - b); // [1, 2, 3, 4, 11, 12, 16]

// 내림 차순
let nums = [1, 4, 2, 3, 11, 16, 12];
nums.sort((a, b) => b - a); // [16, 12, 11, 4, 3, 2, 1]
```

# Reference
[자바스크립트 정렬 함수, sort()](http://dudmy.net/javascript/2015/11/16/javascript-sort/)

[Array.prototype.sort() - JavaScript | MDN - Mozilla](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)