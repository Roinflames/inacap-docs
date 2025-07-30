# 1.3. Las tablas de verdad

# conjuncion
p = True
q = True
print(p and q) # True
p = True
q = False
print(p and q) # False
p = False
q = True
print(p and q) # False
p = False
q = False
print(p and q) # False

# disyuncion
p = True
q = True    
print(p or q) # True
p = True
q = False
print(p or q) # True
p = False
q = True
print(p or q) # True
p = False
q = False
print(p or q) # False

# negacion
p = True
print(not p) # False
p = False
print(not p) # True