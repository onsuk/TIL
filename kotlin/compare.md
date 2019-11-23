# with Haskell

Haskell 코드와의 비교를 통해 Kotlin에 대해 간략히 알아보았다.

```haskell
module Fp where

factors :: Int -> [Int]
factors n = [x | x <- [1..n], n `mod` x == 0]

isPrime :: Int -> Bool
isPrime n = factors n == [1, n]

primes :: Int -> [Int]
primes n = [x | x <- [2..n], isPrime x]

pairs :: [a] -> [(a, a)]
pairs xs = zip xs (tail xs)

sorted :: [Int] -> Bool
sorted xs = and [x <= y | (x, y) <- pairs xs]

count :: Char -> String -> Int
count x xs = length [x' | x' <- xs, x == x']

countRec :: Char -> String -> Int -> Int
countRec x [] n = n
countRec x (a:xs) n
    | x == a = countRec x xs (n + 1)
    | otherwise = countRec x xs n
```

다음은 같은 함수를 구현한 Kotlin 코드이다.

```kotlin
fun factors(num: Int) = (1..num).toList().filter { num % it == 0 }

fun isPrime(num: Int) = factors(num) == listOf(1, num)

fun primes(num: Int) = (2..num).toList().filter { isPrime(it) }

fun pairs(lis: List<Int>) = lis.zip(lis.drop(1))

// 이렇게도 가능
fun pairs(lis: List<Int>) = lis.zipWithNext()

fun sorted(lis: List<Int>) = pairs(lis).all { it.first <= it.second }

fun count(chr: Char, str: String) = str.filter { it == chr }.length

fun countRec(chr: Char, str:String, cnt: Int): Int = when {
    str.isEmpty() -> cnt
    str.first() == chr -> countRec(chr, str.drop(1), cnt + 1)
    else -> countRec(chr, str.drop(1), cnt)
}
```