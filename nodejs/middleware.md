# Express Middleware

## Express란?
Express는 자체적인 최소한의 기능을 갖춘 라우팅 및 미들웨어 웹 프레임워크이며, Express 애플리케이션은 기본적으로 일련의 미들웨어 함수 호출이다.

## Middleware란?
미들웨어 함수는 **요청 오브젝트**(`req`), **응답 오브젝트**(`res`), 그리고 애플리케이션의 요청-응답 주기 중 그 다음의 미들웨어 함수에 대한 액세스 권한을 갖는 함수이다. 그 다음의 미들웨어 함수는 일반적으로 `next`라는 이름의 변수로 표시된다.

미들웨어 함수는 다음과 같은 태스크를 수행한다.
- 모든 코드를 실행
- 요청 및 응답 오브젝트에 대한 변경을 실행
- 요청 - 응답 주기를 종료
- 스택 내의 그 다음 미들웨어 함수를 호출

현재의 미들웨어 함수가 요청 - 응답 주기를 종료하지 않는 경우에는 `next()`를 호출하여 그 다음 미들웨어 함수에 제어를 전달해야 한다. 그렇지 않으면 해당 요청은 정지된 채로 방치된다.

## 미들웨어의 유형
Express 애플리케이션은 다음과 같은 유형의 미들웨어를 사용할 수 있다.

1. 애플리케이션 레벨 미들웨어
2. 라우터 레벨 미들웨어
3. 오류 처리 미들웨어
4. 기본 제공 미들웨어
5. 써드파티 미들웨어

애플리케이션 레벨 및 라우터 레벨 미들웨어는 선택적인 마운트 경로를 통해 로드할 수 있다. 일련의 미들웨어 함수를 함께 로드할 수 있으며, 이를 통해 하나의 마운트 위치에 미들웨어 시스템의 하위 스택을 작성할 수 있다.

### 1. 애플리케이션 레벨 미들웨어
`app.use()`및 `app.METHOD()` 함수를 이용해 애플리케이션 미들웨어를 앱 오브젝트의 인스턴스에 바인드한다. 이 때 `METHOD`는 미들웨어 함수가 처리하는 요청(`GET`, `PUT`, `POST` 등)의 소문자로 된 HTTP 메소드이다.

다음은 마운트 경로가 없는 미들웨어 함수이다. 이 함수는 앱이 요청을 수신할 때마다 실행된다.

```javascript
var app = express();

app.use(function (req, res, next) {
    console.log('Time:', Date.now());
    next();
});
```

다음은 `/user/:id` 경로에 마운트되는 미들웨어 함수이다. 이 함수는 `/user/:id` 경로에 대한 모든 유형의 HTTP 요청에 대해 실행된다.

```javascript
app.use('/use/:id', function (req, res, next) {
    console.log('Request Type:', req.method);
    next();
});
```

다음은 라우트 및 해당 라우트의 핸들러 함수(미들웨어)이다. 이 함수는 `/user/:id` 경로에 대한 `GET` 요청을 처리한다.

```javascript
app.get('/user/:id', function (req, res, next) {
    res.send('USER');
});
```

다음은 하나의 마운트 경로를 통해 일련의 미들웨어 함수를 하나의 마운트 위치에 로드하는 예이다. `/user/:id` 경로에 대한 모든 유형의 HTTP 요청에 대한 요청 정보를 출력하는 미들웨어 하위 스택이다.

```javascript
app.use('/user/:id', function (req, res, next) {
    console.log('Request URL:', req.originalUrl);
    next();
}, function (req, res, next) {
    console.log('Request Type:', req.method);
    next();
});
```

라우터 핸들러를 이용하면 하나의 경로에 대해 여러 라우트를 정의할 수 있다. 다음은 `/user/:id` 경로에 대한 `GET` 요청에 대해 2개의 라우터를 정의한다. 두 번째 라우터는 어떠한 문제도 없지만, 첫 번째 라우터가 **요청 - 응답 주기를 종료**시키므로 두 번째 라우터는 절대 호출되지 않는다.

```javascript
app.get('/user/:id', function (req, res, next) {
    console.log('ID:', req.params.id);
    next();
}, function (req, res, next) {
    res.send('User Info');
    // there is NO next()
});

// handler for the /user/:id path, which prints the user ID
app.get('/user/:id', function (req, res, next) {
    res.end(req.params.id);
});
```

라우터 미들웨어 스택의 나머지 미들웨어 함수들을 건너뛰려면 `next('route')`를 호출하여 제어를 그 다음 라우터로 전달한다.

> `next('route')`는 `app.METHOD()` 또는 `router.METHOD()` 함수를 이용해 로드된 미들웨어 함수에서만 작동한다.

다음은 `/user/:id` 경로에 대한 `GET` 요청을 처리하는 미들웨어 하위 스택이다.

```javascript
app.get('/user/:id', function(req, res, next) {
    // if the user ID is 0, skip to the next route
    if (req.params.id == 0) next('route');
    // otherwise pass the control to the next middleware function in this stack
    else next();
}, function (req, res, next) {
    // redner a regular page
    res.render('regular');
});

// handler for the /user/:id path, which renders a special page
app.get('/user/:id', function (req, res, next) {
    res.render('special');
});
```

### 2. 라우터 레벨 미들웨어

라우터 레벨 미들웨어는 `express.Router()` 인스턴스에 바인드된다는 점을 제외하면 애플리케이션 레벨 미들웨어와 동일한 방식으로 작동한다.

```javascript
var router = express.Router();
```

마찬가지로 `router.use()` 및 `router.METHOD()` 함수를 사용하여 라우터 레벨 미들웨어를 로드한다.

다음은 위의 에플리케이션 레벨 미들웨어의 시스템을 라우터 레벨 미들웨어를 사용하여 복제하는 코드이다.

```javascript
var app = express();
var router = express.Router();


// a middleware function with no mount path. This code is executed for every request to the router
router.use(function (req, res, next) {
    console.log('Time:', Date.now());
    next();
});

// a middleware sub-stack shows request info for any type of HTTP request to the /user/:id path
router.use('/user/:id', function(req, res, next) {
    console.log('Request URL:', req.originalUrl);
    next();
}, function (req, res, next) {
    console.log('Request Type:', req.method);
    next();
});

// a middleware sub-stack the handles GET requests to the /user/:id path
router.get('/user/:id', function (req, res, next) {
    // if the user ID is 0, skip to the next router
    if (req.params.id == 0) next('route');
    // otherwise pass control to the next middleware function in this stack
    else next();
}, function (req, res, next) {
    // render a regular page
    res.render('regular');
});

// handler for the /user/:id path, which renders a special page
router.get('/user/:id', function (req, res, next) {
    console.log(req.params.id);
    res.render('special');
});

// mount the router on the app
app.use('/', router);
```

### 3. 오류 처리 미들웨어

> 오류 처리 미들웨어에는 항상 **4개의 인수**가 필요하다. `next` 오브젝트를 사용할 필요는 없지만, 시그니처를 유지하기 위해 해당 오브젝트를 지정해야 한다. 그렇지 않으면 `next` 오브젝트는 일반적인 미들웨어로 해석되어 오류 처리를 할 수 없다.

**4개의 인수**를 갖는다는 점을 제외하면, 다른 미들웨어 함수와 동일한 방법으로 오류 처리 미들웨어 함수를 정의할 수 있다.

```javascript
app.use(function (err, req, res, next) {
    console.error(err.stack);
    res.status(500).send('Something broke!');
});
```

### 4. 기본 제공 미들웨어

### 5. 써드파티 미들웨어


# Reference
[Express 미들웨어 사용 - Express.js](https://expressjs.com/ko/guide/using-middleware.html)