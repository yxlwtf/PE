t = 0
sum_3 = 0
sum_5 = 0
sum_15 = 0
while t < 1000:
    t = t + 1 
    

    if t % 3 == 0:
        sum_3 += t
    elif t % 5 == 0:
        sum_5 += t
    elif t % 15 == 0:
        sum_15 += t
    else:
        print(f"{t} is not devisable by 3, 5 or 15")

print(sum_3+sum_5-sum_15)

