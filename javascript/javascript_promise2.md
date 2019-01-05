# Javascript Promise

자바스크립트와 노드에서는 주로 비동기 프로그래밍을 한다. 특히 이벤트 주도 방식 때문에 콜백 함수를 자주 사용한다. 하지만 ES2015부터는 자바스크립트와 노드의 API들이 콜백 대신 프로미스(promise) 기반으로 재구성되었다.

![콜백 지옥](https://t1.daumcdn.net/cfile/tistory/2362E03357889CBE1D)

이를 통해 이같은 콜백 지옥(callback hell)을 극복할 수 있다. (해당 경우는 병적으로 극심한 경우이다.)

Promise는 다음과 같은 방식으로 사용한다.

```javascript
const condition = true; // true면 resolve, false면 reject
const promise = new Promise((resolve, reject) => {
    if (condition) {
        resolve('성공');
    } else {
        reject('실패');
    }
});

promise
    .then((message) => {
        console.log(message); // 성공(resolve)한 경우 실행
    })
    .catch((error) => {
        console.error(error); // 실패(reject)한 경우 실행
    });
```

`new Promise`로 프로미스를 생성할 수 있으며, 안에 `resolve`와 `reject`를 매개변수로 갖는 콜백 함수를 넣어준다. 이렇게 만든 `promise` 변수에 `then`과 `catch` 메서드를 붙일 수 있다. 프로미스 내부에서  `resolve`가 호출되면 `then`이 실행되고, `reject`가 호출되면 `catch`가 실행된다.

`resolve`와 `reject`에 넣어준 인자는 각각 `then`과 `catch`의 매개변수에서 받을 수 있다. 즉, `resolve('성공')`이 호출되면 `then`의 `message`가 '성공'이 된다. 만약 `reject('실패')`가 호출되면 `catch`의 `error`가 '실패'가 된다. `condition`변수를 false로 바꿔보면 `catch`에서 에러가 로깅된다.

## Promise Chaining

`then`이나 `catch`에서 다시 다른 `then`이나 `catch`를 붙일 수 있다. 이전 `then`의 return 값을 다음 `then`의 매개변수로 넘긴다. 프로미스를 return한 경우 프로미스가 수행된 후 다음 `then`이나 `catch`가 호출된다. 

```javascriptconst condition = true; // true면 resolve, false면 reject
const promise = new Promise((resolve, reject) => {
    if (condition) {
        resolve('성공');
    } else {
        reject('실패');
    }
});

promise
    .then((message) => {
        return new Promise((resolve, reject) => {
            resolve(message);
        });
    })
    .then((message2) => {
        console.log(message2);
        return new Promise((resolve, reject) => {
            resolve(message2);
        });
    })
    .then((message3) => {
        console.log(message3);
    })
    .catch((error) => {
        console.error(error);
    });
```

처음 `then`에서 `message`를 `resolve`하면 다음 `then`에서 받을 수 있다.여기서 다시 `message2`를 `resolve` 했으므로 다음 `then`에서 `message3`를 받았다.

이것을 활용해서 callback을 promise로 바꿀 수 있다. 코드를 통해 알아보도록 하자.

```javascript
function findeAndSaveUser(Users) {
    Users.findOne({}, (err, user) => { // 첫 번째 콜백
        if (err) {
            return console.error(err);
        }
        user.name = 'zero';
        user.save((err) => { // 두 번째 콜백
            if (err) {
                return console.err(err);
            }
            User.findOne({ gender: 'm' }, (err, user) => { // 세 번째 콜백
                // 생략
            });
        });
    });
}
```

콜백 함수가 세 번 중첩되어 있다. 콜백 함수가 나올 때마다 코드의 depth가 깊어진다. 또 각 콜백 함수마다 error도 따로 처리해줘야 한다. 그래서 이 코드를 다음과 같이 바꿀 수 있다.

```javascript
function findAndSaveUser(Users) {
    Users.findOne({})
        .then((user) => {
            user.name = 'zero';
            return user.save();
        })
        .then((user) => {
            return Users.findOne({gender: 'm'});
        })
        .then((user) => {
            // 생략
        })
        .catch(err => {
            console.error(err);
        });
}
```

코드의 depth가 더 이상 깊어지지 않는다. `then` 메소드는 순차적으로 실행된다. 콜백에서 매번 따로 처리해야 했던 에러도 마지막 `catch`에서 한번에 처리할 수 있다.

>예제의 코드는 `findOne`과 `save` 메소드가 내부적으로 promise 객체를 가지고 있어서 가능한 것이다.

## 여러 Promise가 모두 완료될 때 실행하려면? - Promise.all

Promise 여러 개를 한번에 실행할 수 있는 방법이 있다. 기존의 콜백 패턴이었다면 콜백을 여러 번 중첩해서 사용해야 했을 것이다. 하지만 `Promise.all`을 활용하면 간단히 할 수 있다.

```javascript
const promise1 = Promise.resolve('성공1');
const promise2 = Promise.resolve('성공2');
Promise.all([promise1, promise2])
    .then((result) => {
        console.log(result); // ['성공1', '성공2']
    })
    .catch((error) => {
        console.error(error);
    });
```

`Promise.resolve`는 즉시 `resolve`하는 promise를 만드는 방법이다. 비슷한 것으로 즉시 `reject`하는 `Promise.reject`도 있다.

promise가 여러 개 있을 때 `Promise.all`에 넣으면 모두 `resolve`될 때까지 기다렸다가 `then`으로 넘어간다. 

`result` 매개변수에 각각의 promise 결과값이 **배열**로 들어있다. `Promise` 중 하나라도 `reject`가 되면 `catch`로 넘어간다.

## Reference
[Node.js 교과서 2.1.6 프로미스](https://www.inflearn.com/course/node-js-%EA%B5%90%EA%B3%BC%EC%84%9C/) 서적 참고