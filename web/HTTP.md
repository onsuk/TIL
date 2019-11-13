# HTTP
**HTTP**(HyperText Transfer Protocol)
- 웹 브라우징에 사용되는 통신 프로토콜이다.
- **클라이언트 / 서버 모델**에 기반한 메세지를 사용한다.
    - 클라이언트가 웹 서버에게 요청(request)을 보내면 웹 서버가 브라우저에 표시될 응답(response)를 보내는 방식의 모델
- 그렇기 때문에 모든 HTTP 통신은 요청과 응답을 포함한다.
- **Stateless**하게 작동한다.
    - 모든 요청은 다른 요청과 분리된다.
    - 그렇기 때문에 각 요청은 요청을 수행하기에 충분한 정보를 담고 있다.

## URL
**URL**(Uniform Resource Locator)
- 웹에 있는 자원을 나타내는 고유한 주소이다.
    - 웹은 text, HTML, 문서, 이미지 등의 자원을 공유하기 위한 플랫폼으로 시작되었다.
    - 그렇기 때문에 웹은 자원을 중심으로 구성되었다.

![](img/image4.png)

위와 같은 방식으로 구성되어 있다.

- **Protocol**
    - 많은 경우 HTTP, HTTPS이다.
    - 다른 프로토콜의 경우
        - **FTP**(File Transfer Protocol) - 클라이언트와 서버의 파일 전송에 쓰이는 대표적인 프로토콜이다.
        - **SMTP**(Simple Mail Transfer Protocol) - 이메일 전송 표준 프로토콜이다.
- **Domain**
    - 인터넷 자원이 위치하고 있는 곳을 나타내는 하나 혹은 여러 개의 IP주소이다.
- **Path**
    - 서버 내의 자원의 위치를 나타낸다.
- **Parameters**
    - 자원을 나타내거나 필터링하는 등의 추가적인 데이터이다.

## HTTP Requests
모든 HTTP 요청은 URL 주소를 갖고 있다. 

그리고 메소드 또한 필요하다.
- `GET` - read
- `POST` - create
- `PUT` - update
- `DELETE` - delete

위와 같이 대표적인 4가지의 메소드가 있다.

모든 HTTP 메세지는 하나 이상의 헤더와 바디를 갖고 있다.

# Reference
[HTTP and everything you need to know about it](https://medium.com/faun/http-and-everything-you-need-to-know-about-it-8273bc224491)