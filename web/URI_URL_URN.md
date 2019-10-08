# URI, URL, URN

- **URI**(Uniform Resource Identifier)
    - 인터넷에 있는 자원을 나타내는 유일한 주소
    - 고유하게 지정된 정보 리소스의 위치에 대해 식별
    - 두가지 형태 **URL**, **URN**이 있다.

- **URL**(Uniform Resorce Locator)
    - URI의 가장 흔한 형태
    - 특정 서버의 한 리소스에 대한 위치를 서술한다.
    - ex) `https://www.naver.com`
        - 네이버 사이트의 **URL**
    
- **URN**(Uniform Resouce Name)
    - URL의 한계로 인해 만들어짐
        - 한계: 리소스의 위치가 옮겨지면 더이상 쓸 수 없음.
    - 리소스의 위치에 영향받지 않는 절대적인 이름 역할을 한다.
    - ex) `urn:ietf:rfc:2141`
        - 인터넷 표준 문서 'RFC 2141'의 **URN**

> URL 또한 PURL(Persistant URL)을 사용하면 URN 기능 제공 가능하다.


결론: **URL**, **URN**은 **URI**의 부분집합이다.


# Reference
[URL vs URI](https://velog.io/@honeysuckle/URL-vs-URI)

[URI vs URL vs URN :: 마이구미](https://mygumi.tistory.com/139)

[통합 자원 식별자](https://ko.wikipedia.org/wiki/%ED%86%B5%ED%95%A9_%EC%9E%90%EC%9B%90_%EC%8B%9D%EB%B3%84%EC%9E%90)

[문헌정보학용어사전](http://203.241.185.12/asd/read.cgi?board=Dic&y_number=10257)