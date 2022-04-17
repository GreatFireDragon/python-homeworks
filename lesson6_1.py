# ...
import argparse
import os

ans = "Working...\n--------------------------------------\n"
print(ans)

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--name', default='Anonimous', help="Имя пользователя")
parser.add_argument('-p', '--path', help="Путь к файлу изображения")
parser.add_argument('-noQ', '--noQuest', action='store_true', help="Подавление вопросов пользователю")
args = parser.parse_args()

# print(f'Hi, {args.name}!')
print(f'Текущие параметры: {str(vars(args))[1:-1]}')









ans = "\n--------------------------------------\n...End of work"
print(ans)