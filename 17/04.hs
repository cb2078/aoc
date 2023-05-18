import Data.List

parse :: IO [[String]]
parse = map words . lines <$> readFile "04.txt"

part1, part2 :: [String] -> Bool
part1 css = nub css == css  
part2 = part1 . map sort

main :: IO ()
main = do
  input <- parse
  let solve f = sum . map (fromEnum . f)
  mapM_ print $ solve <$> [part1, part2] <*> pure input
