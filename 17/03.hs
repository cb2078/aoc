import Data.List
import Control.Monad

data Dir = R | U | L | D deriving (Enum, Show)

next :: Dir -> Dir
next = toEnum . (`mod` 4) . succ . fromEnum

isSquare :: Int -> Bool
isSquare x = f 1
  where
    f n
      | n <= 0 = False
      | n * n > x = False
      | n * n == x = True
      | otherwise = f (n + 1)

layer :: Int -> Int
layer i = let f n = if n * n >= i then n else f (n + 1) in f 1

spiral :: [Dir]
spiral = genSpiral 1 R
  where
    genSpiral i d = d : genSpiral (i + 1) d'
      where d' = if any isSquare [i, 1 + i - layer i] then next d else d

pos :: [(Int, Int)]
pos = scanl add (0, 0) spiral
  where add (x, y) d = case d of
                            R -> (x + 1, y)
                            U -> (x, y + 1)
                            L -> (x - 1, y)
                            D -> (x, y - 1)

neighbors :: Int -> [Int]
neighbors i = do
  let (x, y) = pos !! i
  dx <- [-1, 0, 1]
  dy <- [-1, 0, 1]
  let Just neighbor = elemIndex (x + dx, y + dy) pos
  guard (neighbor < i)
  return neighbor 

spiral' :: [Int]
spiral' = let f i = (sum $ (spiral'!!) <$> neighbors i) : f (i + 1) in 1 : f 1 

part1, part2 :: Int -> Int
part1 i = let (x, y) = pos !! i in abs x + abs y
part2 i = let x = length $ takeWhile (<=i) spiral' in spiral' !! x

parse :: IO Int
parse = read . init <$> readFile "03.txt"

main :: IO ()
main = do
  input <- parse
  mapM_ print $ ($ input) <$> [part1, part2]
