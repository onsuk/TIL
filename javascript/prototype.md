# Prototype

자바스크립트는 프로토타입 기반 언어이다. 프로토타입에 대해서 정리해보고자 한다.

## Prototype vs Class

- 자바스크립트는 프로토타입 기반의 객체지향 언어이다.
- ES6에서 Class 문법이 추가되었지만, 자바스크립트가 클래스 기반으로 바뀐 것은 아니다.

## 언제 쓰는 것인가?
```javascript
function Person() {
    this.eyes = 2;
    this.nose = 1;
}

var kim = new Person();
var park = new Person();

console.log(kim.eyes);  // 2
console.log(kim.nose);  // 1

console.log(park.eyes);  // 2
console.log(park.nose); // 1 
```

`kim`과 `park`는 `eyes`와 `nose`를 공통적으로 갖고 있는데, 메모리에는 `eyes`와 `nose`가 두 개씩 총 4개가 할당된다. 이러한 문제를 프로토타입으로 해결해보자.

```javascript
function Person() {}

Person.prototype.eyes = 2;
Person.prototype.nose = 1;

var kim = new Person();
var park = new Person();

console.log(kim.eyes);  // 2
```

- `Person.prototype`이라는 빈 Object가 존재하며, `Person` 함수로부터 생성된 객체(예시에서는 `kim`, `park`)들은 해당 Object에 들어 있는 값을 모두 쓸 수 있다.

## Prototype Link와 Prototype Object

**Prototype Link**와 **Prototype Object**라는 것이 있으며, 이 둘을 통틀어 **Prototype**이라고 한다.

### Prototype Objet
객체는 언제나 함수(Function)로 생성된다.
```javascript
function Person() {}

var personObject = new Person();
```

- 여기서 `personObject` 객체는 `Person`이라는 함수로 생성된 객체이다.
- 언제나 객체는 함수에서 시작된다.

```javascript
var obj = {};
```

위 코드는 다음 코드와 같다.

```javascript
var obj = new Object();
```

- 위 코드에서 `Object`가 자바스크립트에서 기본적으로 제공하는 **함수**이다.
- `Object`와 마찬가지로 `Function`, `Array`도 모두 함수로 정의되어 있다.
