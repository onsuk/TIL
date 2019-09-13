# Javascript Promise란?

프로미스는 자바스크립트 비동기 처리에 사용되는 객체이다.
자바스크립트의 비동기 처리란 **특정 코드의 실행이 완료될 때까지 기다리지 않고 다음 코드를 먼저 수행하는 자바스크립트의 특성**을 의미한다.

## promise가 왜 필요한가?

아래 코드는 간단한 ajax 통신 코드이다.

```javascript
function getData(callbackFunc) {
  $.get('url 주소/products/1', function (response) {
    callbackFunc(response); // 서버에서 받은 데이터 response를 callbackFunc() 함수에 넘겨줌
  });
}

getData(function (tableData) {
  console.log(tableData); // $.get()의 response 값이 tableData에 전달됨
});
```

위 코드는 jQuery의 ajax 통신을 이용하여 지정한 url의 데이터를 받아오는 코드이다. 비동기 처리를 위해 콜백 함수를 이용했다.

위 코드에 프로미스를 적용하면 아래와 같다.

```javascript
function getData(callback) {
  // new Promise() 추가
  return new Promise(function (resolve, reject) {
    $.get('url 주소/products/1', function (response) {
      // 데이터를 받으면 resolve() 호출
      resolve(response);
    });
  });
}

// getData()의 실행이 끝나면 호출되는 then()
getData().then(function (tableData) {
  // resolve()의 결과 값이 여기로 전달됨
  console.log(tableData); // $.get()의 reponse 값이 tableData에 전달됨
});
```
콜백 함수로 처리하던 구조에서 new Promise(), resolve(), then()과 같은 프로미스 API를 사용한 구조로 바뀌었다.

## Promise의 3가지 상태(states)

프로미스를 사용할 때 알아야 하는 가장 기본적인 개념이 프로미스의 상태(states)이다. 상태란 프로미스의 처리 과정을 의미한다. new Promise()를 통해 프로미스를 생성한 후 종료될때까지 3가지 상태를 갖는다.

- Pending(대기): 비동기 처리 로직이 아직 완료되지 않은 상태
- Fulfilled(이행): 비동기 처리가 완료되어 프로미스가 결과 값을 반환해준 상태
- Rejected(실패): 비동기 처리가 실패하거나 오류가 발생한 상태

### Pending(대기)
아래 코드와 같이 `new Promise()` 메소드를 호출하면 Pending(대기) 상태가 된다.

```javascript
new Promise();
```

이렇게 `new Promise()` 메소드를 호출할 때 콜백 함수의 인자로 `resolve`, `reject`에 접근할 수 있다.

```javascript
new Promise(function (resolve, reject) {
  // ...
});
```
### Fulfilled(이행)
여기서 콜백 함수의 인자 resolve를 아래와 같이 실행하면 Fulfilled(이행) 상태가 된다.
```javascript
new Promise(function (resolve, reject) {
  resolve();
});
```

그리고 이행 상태가 되면 아래와 같이 `then()`을 이용하여 처리 결과 값을 받을 수 있다.

```javascript
function getData() {
  return new Promise(function (resolve, reject) {
    var data = 100;
    resolve(data);
  });
}

// resolve()의 결과 값 data를 resolvedData로 받음
getData().then(function (resolvedData) {
  console.log(resolvedData); // 100
});
```
### Rejected(실패)
`new Promise()`로 프로미스 객체를 생성하면 콜백 함수 인자로 `resolve`와 `reject`를 사용할 수 있다. 여기서 `reject` 인자로 `reject()` 메소드를 실행하면 Rejected(실패) 상태가 된다.

```javascript
new Promise(function (resolve, reject) {
  reject();
});
```

실패 상태가 되면 실패한 이유(실패 처리의 결과 값)를 `catch()`로 받을 수 있다.

```javascript
function getData() {
  return new Promise(function (resolve, reject) {
    reject(new Error("Request is failed"));
  });
}

// reject()의 결과 값 Error를 err에 받음
getData().then().catch(function (err) {
  console.log(err); // Error: Request is failed
});
```

다음은 프로미스 처리 흐름을 도식화한 그림이다.

![프로미스 처리 흐름](https://joshua1988.github.io/images/posts/web/javascript/promise.svg)

## Promise Code - 쉬운 예제

간단한 프로미스 코드이다. ajax 통신 예제 코드에 프로미스를 적용해보도록 한다.

```javascript
function getData() {
  return new Promise(function (resolve, reject) {
    $.get('url 주소/products/1', function (response) {
      if (response) {
        resolve(response);
      }
      reject(new Error("Request is failed"));
    });
  });
}

// Fulfilled 또는 Rejected의 결과 값 출력
getData().then(function (data) {
  console.log(data); // response 값 출력
}).catch(function (err) {
  console.error(err); // Error 출력
});
```

위 코드는 서버에서 제대로 response를 받아오면 `resolve()` 메소드를 호출하고, response가 없다면 `reject()` 메소드를 호출한다. 호출된 메소드에 따라 `then()`이나 `catch()`로 분기하여 데이터 또는 오류를 출력한다.

## 여러 개의 Promise 연결하기 (Promise Chaining)

프로미스의 또 다른 특징은 여러 개의 프로미스를 연결하여 사용할 수 있다는 점이다. `then()` 메소드를 호출하고 나면 새로운 프로미스 객체가 반환된다. 따라서, 아래와 같은 코드가 가능하다.

```javascript
function getData() {
  return new Promise({
    // ...
  });
}

// then() 으로 여러 개의 프로미스를 연결한 형식
getData()
  .then(function (data) {
    // ...
  })
  .then(function () {
    // ...
  })
  .then(function () {
    // ...
  });
```

위 형식을 참고하여 동작하는 예제를 살펴보자. setTimeout() API를 사용하도록 한다.

```javascript
new Promise(function(resolve, reject){
  setTimeout(function() {
    resolve(1);
  }, 2000);
})
.then(function(result) {
  console.log(result); // 1
  return result + 10;
})
.then(function(result) {
  console.log(result); // 11
  return result + 20;
})
.then(function(result) {
  console.log(result); // 31
});
```

위 코드는 프로미스 객체를 하나 생성하고 `setTimeout()`을 이용해 2초 후에 `resolve()`를 호출하는 예제이다.

`resolve()`가 호출되면 프로미스가 **대기** 상태에서 **이행** 상태로 넘어가기 때문에 첫 번째 `.then()`의 로직으로 넘어간다. 첫 번째 `.then()`에서는 이행된 결과 값 1을 받아서 10을 더한 후 그 다음 `.then()`으로 넘겨준다. 두 번째 `.then()`에서도 마찬가지로 이전 프로미스이 결과 값 11을 받아서 20을 더한 후 그 다음 `.then()`으로 넘겨준다. 마지막 `then()`에서 최종 결과 값 31을 출력한다.

## 실무에서 있을 법한 Promise Code Example

실제 웹 서비스에서 있을 법한 사용자 로그인 인증 로직에 프로미스를 여러 개 연결해보도록 한다.
```javascript
getData(userInfo)
  .then(parseValue)
  .then(auth)
  .then(diaplay);
```

위 코드는 페이지에 입력된 사용자 정보를 받아와 parsing, authentication 등의 작업을 거치는 코드이다. 여기서 `userInfo`는 사용자 정보가 담긴 객체이며, 아래의 코드와 같이 `parseValue`, `auth`, `display`는 각각 프로미스를 반환하는 함수라고 가정한다.

```javascript
var userInfo = {
  id: 'test@abc.com',
  pw: '****'
};

function parseValue() {
  return new Promise({
    // ...
  });
}
function auth() {
  return new Promise({
    // ...
  });
}
function display() {
  return new Promise({
    // ...
  });
}
```

이처럼 여러 개의 Promise를 `.then()`으로 연결하여 처리할 수 있다.

## Promise의 에러 처리 방법

앞에서 살펴본 Promise 예제 코드는 항상 정상적으로 동작하는 가정 하의 코드이다. 실제 서비스를 구현하다 보면 네트워크 연결, 상태 코드 문제 등 여러가지 원인으로 인해 오류가 발생할 수 있다. 따라서, 프로미스의 에러 처리 방법에 대해서 알아보도록 한다.

에러 처리 방법에는 2가지 방법이 있다.

- `then()`의 두 번째 인자로 에러를 처리하는 방법

```javascript
getData().then(
  handleSuccess,
  handleError
);
```
- `catch()`를 이용하는 방법

```javascript
getData().then().catch();
```

위 2가지 방법 모두 프로미스의 `reject()` 메소드가 호출되어 실패 상태가 된 경우에 실행된다. 아래와 같다.

```javascript
function getData() {
  return new Promise(function (resolve, reject) {
    reject('failed');
  });
}

// 1. then()으로 에러를 처리하는 코드
getData().then(function () {
  // ...
}, function (err) {
  console.log(err);
});

// 2. catch()로 에러를 처리하는 코드
getData().then().catch(function (err) {
  console.log(err);
});
```

## Promise 에러 처리는 가급적 catch()로

에러 처리 방법 2가지 중 가급적 `catch()`로 에러를 처리하는 것이 더 효율적이다.

아래의 코드를 통해 이유를 알아보도록 한다.

```javascript
// then()의 두 번째 인자로는 감지하지 못하는 오류
function getData() {
  return new Promise(function (resolve, reject) {
    resolve('hi');
  });
}

getData().then(function (result) {
  console.log(result);
  throw new Error("Error in then()"); // Uncaught (in promise) Error: Error in then()
}, function (err) {
  console.log('then error : ', err);
});
```

`getData()` 함수의 promise에서 `resolve()` 메소드를 호출해 정상적으로 로직을 처리했지만, `then()`의 첫 번째 콜백 함수의 내부에서 오류가 나는 경우 `then()`의 두 번째 인자 함수의 오류를 제대로 잡아내지 못한다.

따라서 코드를 실행하면 아래와 같은 오류가 난다.

![error](https://joshua1988.github.io/images/posts/web/javascript/then-not-handling-error.png)

하지만 동일한 오류를 `catch()`로 처리하면 다른 결과가 나온다.

```javascript
// catch()로 오류를 감지하는 코드
function getData() {
  return new Promise(function (resolve, reject) {
    resolve('hi');
  });
}

getData().then(function (result) {
  console.log(result); // hi
  throw new Error("Error in then()");
}).catch(function (err) {
  console.log('then error : ', err); // then error :  Error: Error in then()
});
```

위 코드의 처리 결과는 다음과 같다.

![right error](https://joshua1988.github.io/images/posts/web/javascript/catch-handling-error.png)

발생한 에러를 성공적으로 콘솔에 출력한다.

## Reference

[자바스크립트 Promise 쉽게 이해하기](https://joshua1988.github.io/web-development/javascript/promise-for-beginners/)