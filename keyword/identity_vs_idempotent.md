# Identity vs Idempotent

**항등**(Identity)와 **멱등**(Idempotent)의 개념이 헷갈려서 나의 쉬운 말로 간단히 정리해보려고 한다.


## 항등(Identity)

연산을 적용했을 때 **자기 자신**이 나오는 성질을 의미한다.

### Example
```
1+0=1       1x1 = 1
2+0=2       2x1 = 2
3+0=3       3x1 = 3
.           .
.           .
.           .

이므로

덧셈에 대한 항등원은 0
곱셈에 대한 항등원은 1
```

## 멱등(Idempotent)

연산을 **여러 번 적용**하더라도 결과가 달라지지 않는 성질을 의미한다.

### Example
```
0+0+0+0+0+...=0

0*0*0*0*0*...=0

1*1*1*1*1*...=1

이므로

덧셈에 대한 멱등원은 0
곱셈에 대한 멱등원은 0, 1
```
