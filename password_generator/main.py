import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

ans=[]
for num in range(nr_numbers):
    r=random.randint(0,10)
    ans.append(numbers[r])
for num in range(nr_symbols):
    v = random.randint(0, 9)
    ans.append(symbols[v])

nr=nr_letters-nr_symbols-nr_numbers
for num in range (nr):
    v = random.randint(0, len(letters))
    ans.append(letters[v])
z=nr_letters
second_ans=ans.copy()
print("Option 1:")
for value in range(nr_letters):
    y=random.randint(0,z-1)
    print(ans[y],end="")
    ans.remove(ans[y])
    z-=1
print("\nOption 2:")
# instead of random.randint we can use random.shuffle(ans)
random.shuffle(second_ans)
for value in second_ans:
 print(value,end="") 