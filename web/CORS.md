# CORS(Cross Origin Resource Sharing)

## CORS란?
**현재 도메인과 다른 도메인으로 리소스를 요청하는 경우**이다. 예를 들어, 도메인 http://A.com 에서 읽어온 HTML 페이지에서 다른 도메인 http://B.com/image.jpg 를 요청하는 경우 등이다. 이런 경우에 해당 리소스는 cross-origin HTTP 요청에 의해 요청된다. **보안 상의 이유로, 브라우저는 CORS를 제한하고 있다.**

하지만 REST API를 기반으로 비동기 네트워크 통신을 하는 경우, SPA(Single Page Application)의 경우 등은 API 서버와 웹 페이지 서버가 다를 수 있다. 이런 경우에 API 서버로 요청을 할 시에 CORS 제한이 걸리게 된다.

# Reference
[node.js express에서 CORS 허용하기](http://guswnsxodlf.github.io/enable-CORS-on-express)