# Jest - JavaScript Testing Tool

## Jest란?
페이스북에서 만든 테스팅 프레임워크이다. 페이스북에서 사용되는 리액트 애플리케이션을 포함한 모든 자바스크립트 테스트 도구이다. Jest의 철학 중 하나는 "Zero-Configuration", 설정 없는 테스트 환경을 제공하는 것이다.

## 설치 방법
"Zero-Configuration" 철학에서 볼 수 있듯이, `yarn`이나 `npm`으로 설치만 하면 된다.
- `yarn`으로 설치
```bash
$ yarn add --dev jest
```
- `npm`으로 설치
```bash
$ npm install --save--dev jest
```

## 사용 방법
여러가지 타입의 테스트 기능을 제공한다.
- Common Matchers
```javascript
const sum = function(a, b) {
    return a + b;
}

test('adds 1 + 2 to equal 3', () => {
    expect(sum(1, 2)).toBe(3);
});

test('object assignment', () => {
    const data = { one: 1};
    data['two'] = 2;
    expect(data).toEqual({ one: 1, two: 2});
});

test('adding positive numbers is not zero', () => {
    for (let a = 1; a < 10; a++) {
        for (let b = 1; b < 10; b++) {
            expect(a + b).not.toBe(0);
        }
    }
});
```

- Truthiness
    - 참/거짓 테스트에서는 때때로 `undefined`, `null`, `false`를 구별해줘야 할 때가 있으며, 그것에 대한 테스트를 지원한다.
    - 하지만 사용자가 이것의 구별을 원하지 않는다면 그에 따른 기능도 지원한다.

```javascript
test('null', () => {
    let m;
    const n = null;
    expect(m).toBeUndefined();
    expect(n).toBeNull();
    expect(n).not.toBeUndefined();
    expect(n).not.toBeTruthy();
    expect(n).toBeFalsy();
});

test('zero', () => {
    const z = 0;
    expect(z).not.toBeNull();
    expect(z).toBeDefined();
    expect(z).not.toBeUndefined();
    expect(z).not.toBeTruthy();
    expect(z).toBeFalsy();
});
```

- Number
```javascript
test('two plus two', () => {
    const value = 2 + 2;
    expect(value).toBeGreaterThan(3);
    expect(value).toBeGreaterThanOrEqual(3.5);
    expect(value).toBeLessThan(5);
    expect(value).toBeLessThanOrEqual(4.5);

    expect(value).toBe(4);
    expect(value).toEqual(4);
});

test('adding floating point numbers', () => {
    const value = 0.1 + 0.2;
    expect(value).toBeCloseTo(0.3);
});
```
> `float`값 테스트 시, `toEqual` 대신 `toBeCloseTo`를 사용해야 한다.
> `toEqual`를 사용할 때, 미세하게 값이 다르게 나올 수 있어 테스트가 틀릴 가능성이 있기 때문이다.

- String
```javascript
test('there is no I in team', () => {
    expect('team').not.toMatch(/I/);
});

test('but there is a "stop" in Christoph', () => {
    expect('Christoph').toMatch(/stop/);
});
```

- Array
```javascript
const shoppingList = [
    'diapers',
    'kleenex',
    'trash bags',
    'paper towels',
    'beer'
];

test('the shopping list has beer on it', () => {
    expect(shoppingList).toContain('beer');
});
```

# Reference
[JavaScript Testing Tool - Jest](https://velog.io/@yesdoing/JavaScript-Testing-Tool-Jest-opjocpva77)