import Data.List

divide :: String -> String -> (String, String)
divide pattern = divide'
  where
    divide' "" = ("", "")
    divide' xs
      | isPrefixOf pattern xs = ("", drop (length pattern) xs)
      | otherwise = let (ys, zs) = divide pattern (tail xs) in (head xs : ys, zs)

splitStr :: String -> String -> [String]
splitStr pattern = splitStr'
  where
    splitStr' "" = []
    splitStr' xs = let (ys, zs) = divide pattern xs in ys : splitStr' zs

parse :: String -> [[Int]]
parse = map (map read . splitStr "\n") . splitStr "\n\n"

part1, part2 :: [[Int]] -> Int
part1 = foldr1 max . map sum
part2 = sum . take 3 . reverse . sort . map sum

main :: IO ()
main = do
  input <- parse <$> readFile "01.txt"
  mapM_ print $ [part1, part2] <*> pure input
