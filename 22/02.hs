parse :: IO [(Int, Int)]
parse = map toGame . lines <$> readFile  "02.txt"
  where
    toGame [p1, _, p2] = (fromEnum p1 - fromEnum 'A', fromEnum p2 - fromEnum 'X')

score, score' :: Int -> Int -> Int
score x y = y + 1 + (mod (y - x + 1) 3) * 3 
score' x r = score x (mod (x + r - 1) 3)

main :: IO ()
main = do
  input <- parse
  let solve score = sum . map (uncurry score)
  mapM_ print $ solve <$> [score, score'] <*> pure input
