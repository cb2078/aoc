import Data.List

parse :: IO [Int]
parse = map read . words <$> readFile "06.txt"

update :: [a] -> Int -> a -> [a]
update xs i x = take i xs ++ [x] ++ drop (i + 1) xs

realloc :: [Int] -> [Int]
realloc xs = realloc' (update xs i 0) i x
  where
    x = maximum xs
    Just i = elemIndex x xs
    realloc' xs i n =
      if n == 0
         then xs
         else let j = ((i + 1) `mod` length xs)
              in realloc' (update xs j (1 + xs !! j)) j (n - 1)
    
cycles :: [Int] -> [[Int]]
cycles xs = xs : cycles (realloc xs)

solve :: [Int] -> (Int, Int)
solve xs = solve' 0
  where
    cs = cycles xs
    solve' i =
      case (cs !! i) `elemIndex` take i cs of
           Just j -> (0, i - j)
           Nothing -> let (p1, p2) = solve' (i + 1) in (1 + p1, p2)

main :: IO ()
main = print =<< solve <$> parse
