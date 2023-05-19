import Data.Array

parse :: IO (Array Int Int)
parse = do
  input <- map read . lines <$> readFile "05.txt"
  return $ listArray (0, pred $ length input) input

type NextJump = (Int -> Int)
part1, part2 :: NextJump
part1 = succ
part2 x = if x >= 3 then x - 1 else x + 1

solve :: NextJump -> Array Int Int -> Int
solve nextJump xs = solve' xs 0
  where
    solve' xs i =
      if i < 0 || i >= length xs
         then 0
         else let e = xs ! i
              in 1 + solve' (xs // [(i, nextJump e)]) (i + e)

main :: IO ()
main = do
  input <- parse
  mapM_ print $ solve <$> [part1, part2] <*> pure input
