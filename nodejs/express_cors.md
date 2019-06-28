# Express에서 CORS 허용하기

Express에서 CORS를 허용하는 방법으로는 [express의 CORS 미들웨어](https://github.com/expressjs/cors)를 적용하는 것이다.

```javascript
var express = require('express');
var cors = require('cors');
var app = express();

app.use(cors());

app.get('products/:id', function(req, res, next) {
    res.json({msg: 'This is CORS-enabled for all origins!'})
});

app.listen(80, function () {
    console.log('CORS-enabled web server listening on port 80')
});
```
미들웨어를 사용하면 모든 CORS 요청을 허용할 시 한 줄로 간단하게 추가할 수 있다.

# Reference
[node.js express에서 CORS 허용하기](http://guswnsxodlf.github.io/enable-CORS-on-express)