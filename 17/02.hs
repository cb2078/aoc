import Data.List

parse :: IO [[Int]]
parse =  map (map read . words) . lines <$> readFile "02.txt"

part1, part2 :: [Int] -> Int
part1 xs = foldr1 (-) $ [maximum, minimum] <*> pure xs
part2 = sum . map f . filter ((==2) . length ) . subsequences
  where f [x, y] | x < y = f [y, x]
                 | x `mod` y == 0 = x `div` y
                 | otherwise = 0

solve f = sum . map f
main :: IO ()
main = do
  input <- parse
  mapM_ print $ solve <$> [part1, part2] <*> pure input
