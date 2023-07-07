with open('3EWksN0.txt') as f:
    first = f.read()
with open('t9midEtQ.txt') as f:
    second = f.read()

# first = """? ( u   f 1 e w o s a w y   h i i g 



# 3 M + M   a v n   w t e l n 

# U   n o p e e T E . 


# U   n o p e e T E 


# N a   o a """

# second = """   s m o   n   h i   l a s c a n n ) 
 
#  W 7 2 6 S l a , S i z r a d 
 
#  . i c m l t   H e 

 
#  . i c m l t   H 

 
#  y , p k !"""

for i, v in enumerate(first):
    if i % 2 == 1:
        print(first[i], end="")
    else:
        print(second[i], end="")
