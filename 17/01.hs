import Data.List

parse :: IO [Int]
parse = map (read . pure) . init <$> readFile "01.txt"

rotate :: Int -> [a] -> [a]
rotate = drop <> take

solve :: Int -> [Int] -> Int
solve n xs = sum $ zipWith (\ x y -> if x == y then x else 0) xs (rotate n xs) 

part1, part2 :: [Int] -> Int
part1 = solve 1
part2 xs = solve (length xs `div` 2) xs

main :: IO ()
main = do
  input <- parse
  mapM_ print $ [part1, part2] <*> pure input
