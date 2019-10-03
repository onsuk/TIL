# Webpack - Javascript Module Bundler

## Javascript module bundler

### module bundler
여러개의 나누어져 있는 파일들을 하나의 파일로 만들어주는 라이브러리

**웹팩 사용의 이점**

- **브라우저 로딩 속도 증가**
    - 여러 개의 자바스크립트 코드를 압축해서 하나의 파일로 가져올 수 있게 한다.
    - 서버와 여러번 통신하는 비효율성을 해결한다.

- **최신 문법 지원**
    - 여러가지 loader를 통해 브라우저에게 코드를 전달한다.
        - ex) [babel-loader](https://github.com/babel/babel-loader), [css-loader](https://github.com/webpack-contrib/css-loader), [sass-loader](https://github.com/webpack-contrib/sass-loader)
    - 그로 인해, ES6+ 문법을 지원하지 않는 구형 브라우저에도 코드가 작동될 수 있게 한다.


# Reference
[Webpack 이 뭐지?](https://velog.io/@ground4ekd/Webpack)

[웹팩에 대해 알아보자!](https://medium.com/humanscape-tech/webpack-%EC%9B%B9%ED%8C%A9-a3fd1911e5e7)