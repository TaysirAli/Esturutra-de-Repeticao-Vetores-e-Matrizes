n = int(input("da um numero ai"))
i = 1
total = 0
count = 0
while i <= n:
    resto = i % 2
    if resto != 0:
        total = total + i
    i = i + 1
for numero in range(1, n+1):
    resto2 = numero % 2
    if resto2 == 0:
        resto3 = numero % 3
        if resto3 == 0:
            count = count + 1


print(total)
print(count)

