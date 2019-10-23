# CIS194 - Week 1 Homework

## Exercise - 1

We need to first find the digits of a number. Define the functions
```haskell
toDigits :: Integer -> [Integer]
toDigitsRev :: Integer -> [Integer]
```

toDigits should convert positive Integers to a list of digits. (For 0 or
negative inputs, toDigits should return the empty list.) toDigitsRev
should do the same, but with the digits reversed.

```haskell
Example: toDigits 1234 == [1,2,3,4]
Example: toDigitsRev 1234 == [4,3,2,1]
Example: toDigits 0 == []
Example: toDigits (-17) == []
```

## Answer - 1
```haskell
-- Card.hs
module Card where

toDigits :: Integer -> [Integer]
toDigitsRev :: Integer -> [Integer]

strToIntegerList :: String -> [Integer]
strToIntegerList [] = []
strToIntegerList xs = map (\x -> read [x] :: Integer) xs

toDigits x
    | x <= 0 = []
    | otherwise = strToIntegerList (show x)

toDigitsRev x = reverse (toDigits x)
```

## Exercise - 2

Once we have the digits in the proper order, we need to
double every other one. Define a function
```haskell
doubleEveryOther :: [Integer] -> [Integer]
```

Remember that doubleEveryOther should double every other number beginning from the right, that is, the second-to-last, fourth-to-last,
. . . numbers are doubled.

```haskell
Example: doubleEveryOther [8,7,6,5] == [16,7,12,5]
Example: doubleEveryOther [1,2,3] == [1,4,3]
```


## Answer - 2

```haskell
-- Card.hs
module Card where

doubleEveryOther :: [Integer] -> [Integer]
doubleEveryOther xs
    | even (length xs) = doubleWhenEven xs
    | odd (length xs) = doubleWhenOdd xs

doubleWhenEven [] = []
doubleWhenEven (x1:x2:xs) = (x1*2):x2:doubleWhenEven xs

doubleWhenOdd [] = []
doubleWhenOdd [x] = [x]
doubleWhenOdd (x1:x2:xs) = x1:(x2*2):doubleWhenOdd xs
```
