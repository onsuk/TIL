# Buffer & Stream

Buffer 클래스는 버퍼를 직접 다룰 수 있다.
```javascript
// buffer_practice.js
const buffer = Buffer.from('날 버퍼로 보내라');
console.log('from():', buffer);
console.log('length:', buffer.length);
console.log('toString():', buffer.toString());

const array = [Buffer.from('띄엄 '), Buffer.from('띄엄 '), Buffer.from('띄어쓰기')];
const buffer2 = Buffer.concat(array);
console.log('concat():', buffer2.toString());

const buffer3 = Buffer.alloc(5);
console.log('alloc():', buffer3);
```

```bash
$ node buffer_prcatice
from(): <Buffer eb 82 a0 20 eb b2 84 ed 8d bc eb a1 9c 20 eb b3 b4 eb 82 b4 eb 9d bc>
length: 23
toString(): 날 버퍼로 보내라
concat(): 띄엄 띄엄 띄어쓰기
alloc(): <Buffer 00 00 00 00 00>
```

Buffer 객체는 여러가지 메서드를 제공한다.
- from(문자열) : 문자열을 버퍼로 바꿀 수 있다. length 속성은 버퍼의 크기를 알려준다.
- toString(버퍼) : 버퍼를 다시 문자열로 바꿀 수 있다. 이 때 base64나 hex를 인자로 넣으면 해당 인코딩으로도 변환할 수 있다.
- concat(배열) : 배열 안에 든 버퍼들을 하나로 합친다.
- alloc(바이트) : 빈 버퍼를 생성한다. 바이트를 인자로 지정해주면 해당 크기의 버퍼가 생성된다.

readFile() 방식의 버퍼가 편리하긴 하지만 **문제점** 또한 존재한다. 가령 용량이 100MB인 파일이 있다면 그것을 읽을 때에는 100MB의 버퍼를 만들어야 한다. 해당 작업을 동시에 10개만 해도 1GB에 달하는 메모리가 사용될 것이다. 특히 서버같이 몇 명이 이용할지 모르는 환경에서는 메모리 문제가 발생할 수 있다.

그래서 버퍼의 크기를 작게 만들어서 여러 번에 나눠서 보내는 방식이 등장했다. 예를 들면 버퍼 1MB를 만든 후 100MB 파일을 백 번에걸쳐 보내는 것이다.

이를 편리하게 만든 것이 스트림(Stream)이다.

파일을 읽는 스트림 메소드로는 createStream이 있다. 다음과 같이 사용한다.

```
// readme3.txt
저는 조금씩 조금씩 나눠서 전달됩니다. 나눠진 조각을 chunk라고 부릅니다.
```
```javascript
// createReadStream_practice.js
const fs = require('fs');

const readStream = fs.createReadStream('./readme3.txt', { highWaterMark: 16});
const data = [];

readStream.on('data', (chunk) => {
    data.push(chunk);
    console.log('data :', chunk, chunk.length);
});

readStream.on('end', () => {
    console.log('end :', Buffer.concat(data).toString());
});

readStream.on('error', (err) => {
    console.log('error :', err);
});
```
```bash
$ node createReadStream_practice
data : <Buffer ec a0 80 eb 8a 94 20 ec a1 b0 ea b8 88 ec 94 a9> 16
data : <Buffer 20 ec a1 b0 ea b8 88 ec 94 a9 20 eb 82 98 eb 88> 16
data : <Buffer a0 ec 84 9c 20 ec a0 84 eb 8b ac eb 90 a9 eb 8b> 16
data : <Buffer 88 eb 8b a4 2e 20 eb 82 98 eb 88 a0 ec a7 84 20> 16
data : <Buffer ec a1 b0 ea b0 81 ec 9d 84 20 63 68 75 6e 6b eb> 16
data : <Buffer 9d bc ea b3 a0 20 eb b6 80 eb a6 85 eb 8b 88 eb> 16
data : <Buffer 8b a4 2e> 3
end : 저는 조금씩 조금씩 나눠서 전달됩니다. 나눠진 조각을 chunk라고 부릅니다.
```

먼저 createReadStrea()으로 읽기 스트림을 만든다. 첫 번째 인자는 읽을 파일 경로이며, 두번째 인자는 옵션 객체이다. `highWaterMark`라는 옵션이 버퍼의 크기(바이트 단위)를 정할 수 있는 옵션이다.
> `highWaterMark` 옵션의 default는 64KB지만, 여러 번에 걸쳐 나눠 보내는 것을 나타내기 위해 16B로 낮춘 모습이다.

readStream은 이벤트 리스너를 붙여서 사용한다. 보통 data, end, error 이벤트를 사용한다. 읽는 도중 에러 발생시 error 이벤트 호출, 읽기가 시작되면 data 이벤트 발생, 다 읽으면 end 이벤트가 발생한다.

이번에는 파일을 써보도록 한다.
```javascript
// createWriteStream_practice.js
const fs = require('fs');

const writeStream = fs.createWriteStream('./writeme2.txt');
writeStream.on('finish', () => {
    console.log('파일 쓰기 완료');
});

writeStream.write('이 글을 씁니다. \n');
writeStream.write('한 번 더 씁니다.');
writeStream.end();
```

writeme2.txt를 열어 보면 글이 써져 있는 것을 확인할 수 있다.

```bash
$ node createWriteStream_practice
파일 쓰기 완료
```
먼저 createWriteStrea()으로 쓰기 스트림을 만들어준다. 첫 번째 인자는 출력 파일명이고 두 번째 인자는 옵션이며 여기서는 사용하지 않았다.

writeStream에서 제공하는 write() 메소드로 넣을 데이터를 쓴다. 데이터를 다 썼다면 end() 메서드로 종료를 알려준다. 이 때 finish 이벤트가 발생한다.

createReadStream으로 파일을 읽고 그 스트림을 전알받아 createWriteStream으로 파일을 쓸 수도 있다. 파일 복사와 비슷하다. 스트림끼리 연결하는 것을 '파이핑'이라고 표현한다.

pipe 메서드를 사용해보자.
```
// readme4.txt
저를 writeme3.txt로 보내주세요.
```
```javascript
// pipe_practice.js
const fs = require('fs');

const readStream = fs.createReadStream('readme4.txt');
const writeStream = fs.createWriteStream('writeme3.txt');
readStream.pipe(writeStream);
```
readme4.txt와 똑같은 내용의 writeme3.txt가 생성된다. 미리 읽기 스트림과 쓰기 스트림을 만들어둔 후 두 개의 스트림 사이를 pipe 메소드로 연결해주면 저절로 데이터가 writeStream으로 넘어간다. 

## Reference
[Node.js 교과서 3.6.2 버퍼와 스트림 이해하기](https://www.inflearn.com/course/node-js-%EA%B5%90%EA%B3%BC%EC%84%9C/) 서적 참고