x = 0
y = 1

sum = 0

while sum < 4_000_000:
    z = x + y
    x = y
    y = z
    
    if z % 2 == 0:
        sum = sum + z
    

print(sum)