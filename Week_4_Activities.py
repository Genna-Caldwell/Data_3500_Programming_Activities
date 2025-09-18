year_born = int(input("Enter the year you were born: "))
if year_born >= 1997:
    print("You are a zoomer!\n")
elif year_born >= 1981:
    print("You are a millenial!\n")
elif year_born >= 1965:
    print("You are a gen x!\n")
elif year_born >= 1946:
    print("You are a baby boomer!\n")
else:
    print("I'm not sure which generation you belong to.\n")


age = int(input("Enter your age: "))
current_year = 2025
while age > 1:
    print("You were alive in", current_year)
    current_year -=1
    age -= 1
else:
    current_year -=1
    print("You were born in", current_year, "\n")


for i in range(1, 96):
    if i % 5 == 0:
        print(i)


num = 1

while num < 96:
    if num % 5 == 0:
        print(num)
    num += 1

