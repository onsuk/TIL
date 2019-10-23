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

