import Data.List

data Program = Program { name :: String, size :: Int, childNames :: [String] } deriving (Eq, Show) 

parse :: IO [Program]
parse = map (toProgram . words) . lines <$> readFile "07.txt"
  where
    toProgram (name : size : children) =
      Program name (read size)
        (if children == []
            then []
            else map (filter (/=',')) $ drop 1 children)

findRoot :: [Program] -> Program
findRoot ps = root
  where
    notRoots = nub $ concat $ map childNames ps
    Just root = find (not . (`elem` notRoots) . name) ps

data Tree a = Tree { val :: a, children :: [Tree a], weight :: Int, isBalanced :: Bool } deriving (Eq, Show)

makeTree :: [Program] -> Tree Int
makeTree ps = makeTree' root
  where
    root = findRoot ps 
    makeTree' p = Tree (size p) children (size p + sum childWeights) isBalanced
      where
        children = map makeTree' $ filter ((`elem` childNames p) . name) ps
        childWeights = map weight children
        isBalanced = (1>=) . length $ nub childWeights

-- DFS will find the deepest unbalanced node
weightToBalance :: Tree Int -> Int
weightToBalance node =
  case find (not . isBalanced) (children node) of
       Just child -> weightToBalance child
       Nothing -> val childToBalance + targetWeight - weight childToBalance
  where
    cs = children node
    Just childToBalance = find ((1==) . (`count` ws) . weight) cs
      where
        count x = length . filter (==x)
        ws = map weight cs
    Just targetWeight = weight <$> find (/=childToBalance) cs

main :: IO ()
main = mapM_ (=<< parse) [putStrLn . name . findRoot,
                          print . weightToBalance . makeTree]
