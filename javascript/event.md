# Event 이해하기

이벤트를 만들고 호출하고 삭제해보도록 한다.
```javascript
// event_practice.js
const EventEmitter = require('events');

const myEvent = new EventEmitter();
myEvent.addListener('event1', () => {
    console.log('이벤트 1');
});
myEvent.on('event2', () => {
    console.log('이벤트 2');
});
myEvent.on('event2', () => {
    console.log('이벤트 2 추가');
});

myEvent.emit('event1');
myEvent.emit('event2');

myEvent.once('event3', () => {
    console.log('이벤트 3');
});
myEvent.emit('event3');
myEvent.emit('event3');

myEvent.on('event4', () => {
    console.log('이벤트 4');
});
myEvent.removeAllListeners('event4');
myEvent.emit('event4');

const listener = () => {
    console.log('이벤트 5');
};
myEvent.on('event5', listener);
myEvent.removeListener('event5', listener);
myEvent.emit('event5');

console.log(myEvent.listenerCount('event2'));
```
```bash
$ node event_practice
이벤트 1
이벤트 2
이벤트 2 추가
이벤트 3
2
```

events 모듈을 사용하면 된다. myEvent라는 객체를 먼저 만든다. 객체는 이벤트 관리를 위한 메소드를 가지고 있다.

- on(이벤트명, 콜백) : 이벤트 이름과 이벤트 발생 시의 콜백을 연결해준다. 이렇게 연결하는 동작을 이벤트 리스닝이라고 한다. `event2`처럼 이벤트 하나에 이벤트 여러 개를 달아줄 수도 있다.
- addListner(이벤트명, 콜백) : on과 기능이 같다.
- emit(이벤트명) : 이벤트를 호출하는 메서드이다. 이벤트 이름을 인자로 넣어주면 미리 등록해뒀던 이벤트 콜백이 실행된다.
- once(이벤트명, 콜백) : 한 번만 실행되는 이벤트이다. myEvent.emit('event3')을 두 번 연속 호출했지만 콜백이 한 번만 실행된다.
- removeAllListeners(이벤트명) : 이벤트에 연결된 모든 이벤트 리스너를 제거한다. event4가 호출되기 전에 리스너를 제거했으므로 event4의 콜백은 호출되지 않는다.
- removeListener(이벤트명, 리스너) : 이벤트에 연결된 리스너를 하나씩 제거한다. 역시 event5의 콜백도 호출되지 않는다.
- off(이벤트명, 콜백) : 노드 10 버전에서 추가된 메소드며, removeListener과 기능이 같다.
- listenerCount(이벤트명) : 현재 리스너가 몇 개 연결되어 있는지 확인한다.

직접 이벤트를 만드는 것을 통해 다양한 동작을 직접 구현할 수 있다. 웹 서버를 구축할 때 많이 사용된다.