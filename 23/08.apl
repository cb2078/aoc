⎕IO←0 ⋄ ⎕PP←34
i←1+'LR'⍳⊃in←⊃⎕NGET'08.txt'1
t←{(⍳≢⍵),⍵[;0]⍳⍵[;1 2]}e←↑(∊∘(⎕A,⎕D)⊆⊢)¨2↓in
a z←e[;0]⍳('AAA')('ZZZ')
f←{⍺←0 ⋄ ⍵∊z:0 ⋄ 1+((≢i)|⍺+1)∇t[⍵;i[⍺]]}
f a ⍝ p1
as z←↓(⍸⍤1)'AZ'∘.{⍵[2]=⍺}e[;0]
⍝ some interesting observations:
⍝ - there is only one '__Z' in each cycle for every '__A'
⍝ - the cycles lengths are equal to the number of steps needed to reach a '__Z'
⍝ - the answer can by calculated as the gcd of the steps taken to reach the first '__Z' from each '__A'
⍝ so we could simplify g to make it look more like f and still get the correct answer
∧/f¨as ⍝ p2