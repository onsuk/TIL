# Babel - Javascript Transpiler

## Babel이란?
Babel은 ES6+ 코드를 ES5 이하의 버전으로 트랜스파일링한다.

```javascript
// ES6(Arrow Function) + ES7(Exponentiation operator)
[1, 2, 3].map(n => n ** n);
```

위 코드는 ES6에서 도입된 Arrow Function과 ES7에서 도입된 거듭제곱 연산자를 사용하고 있다. 이 두가지 기능은 IE를 포함한 구형 브라우저에서는 지원하지 않는다. 따라서 IE나 구형 브라우저에서도 동작하는 애플리케이션을 구현하기 위해 ES6+ 코드를 ES5 이하의 버전으로 변환(트랜스파일링)할 필요가 있다. Babel을 사용하면 위 코드를 아래와 같이 ES5 이하의 버전으로 트랜스파일링할 수 있다.

```javascript
// ES5
"use strict";

[1, 2, 3].map(function (n) {
    return Math.pow(n, n);
});
```

# Reference
[Babel과 Webpack을 이용한 ES6 환경 구축 ①](https://poiemaweb.com/es6-babel-webpack-1)