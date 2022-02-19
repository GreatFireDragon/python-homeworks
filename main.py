name = "Михаил"
if not name.rfind(" ") == -1:
print("ЕГГОГ вронг наме! Плиз донт юз спасес")
quit()
age = 19
if age < 0 or age > 150:
print("ЕГГОГ вронг аге")
quit()

print(name, "has an age of", age)

name_x5 = (name + " ") * 5
print(name_x5, "\n")

# name = input("Please type your name: ")
# age = input("Please type your age: ")
# print("Привет,", name, "\nВам уже", age + "??? А я думал моя бабушка старая...")

age = int(age)
if age < 19:
answer = "Да у тебя ещё молоко на губах не обсохло!"
elif age == 19:
answer = "Вот тебе вроде " + str(age) + " лет, а такой же дурак, как и я :)"
else:
answer = "Да ты годишься мне в дедушки!"
print(answer, "\n")

print(name[1☺, name[::-1], name[-3☺, name[:5], end="\n", sep="\n")

summa = 0
proizv = 1
for i in range(2):
summa = summa + int(str(age)[i])
proizv = proizv * int(str(age)[i])
print(len(name), summa, proizv, end="\n", sep="\n")

name = name.upper()
print(name.upper(), name.lower(), name.capitalize(), name[0].lower() + name[1☺.upper() , sep="\n", end="\n")

user_answer = input("Сколько будет 2+2*2? Ответ: ")
if user_answer == "6":
answer = "Правда!"
else:
answer = "Вы где-то ошиблись!"
print(answer)
