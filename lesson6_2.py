# ...
import argparse
import os
import configparser


ans = "Start of programm...\n--------------------------------------"
print(ans)



class Cartoon:
    def __init__(self, name, genre, origin, main_character):
        self.name = name
        self.genre = genre
        self.origin = origin
        self.main_character = main_character

    def __str__(self):
        return f"Cartoon's name: {self.name} \nGenre: {self.genre} \nOrigin: {self.origin} \nMain character_s: {self.main_character}"

    def __getstate__(self) -> dict:
        state = {}
        state["name"] = self.name
        state["genre"] = self.genre
        state["origin"] = self.origin
        state["main_character"] = self.main_character
        return state

    def __setstate__(self, state: dict):
        self.name = state["name"]
        self.genre = state["genre"]
        self.origin = state["origin"]
        self.main_character = state["main_character"]


parser = argparse.ArgumentParser(description='Parser. Just a parser.')
parser.add_argument('-f', '--file_s_name', default='default.ini', nargs='?')
parser.add_argument('-p', '--path', default='Settings\\', help="Here's the path to your file")
args = parser.parse_args()
print(f'Текущие параметры: {str(vars(args))[1:-1]}', end='\n\n')

config_path = args.path + args.file_s_name
config = configparser.ConfigParser()
config.read(config_path, encoding="UTF-8")

print(config["GIT"]["TOKEN"])


print(config_path)
if os.path.exists(config_path):
    print("\nФайлы на месте.\n")
    pass
else:
    print("\nПроверьте наличие папки Settings.\nОна должна находиться в корне и содержать файл default.ini\n"
          "Если файлы прсиутствуют, а ошибка не исчезла, скорее всего файлы повреждены.")

























ans = "\n--------------------------------------\n...End of programm"
print(ans)