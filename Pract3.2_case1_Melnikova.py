print("Является ли стово палиндромом?")
print("Введите слово")
slovo1 = str(input())
slovo2 = slovo1[::-1]
if slovo2 == slovo1:
    print("YES")
else:
    print("NO")