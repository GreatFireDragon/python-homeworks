# ...
import argparse
import os
import configparser
import datetime




class Simple_Game:
    def __init__(self, level: int, hp: int, time_played: int):
        self.level = level
        self.hp = hp
        self.time_played = time_played

    def __str__(self):
        return f"Уровень, на котором находится игрок: {self.level} \n" \
               f"Количество здоровья игрока: {self.hp} \n" \
               f"Время в игре: {self.time_played} \n"

def game_builder():
    config = configparser.ConfigParser()
    config.read(config_path, encoding="UTF-8")

    return Simple_Game(
        int(config["SAVE" + str(save_number)]["level"]),
        int(config["SAVE" + str(save_number)]["hp"]),
        int(config["SAVE" + str(save_number)]["time_played"])
    )






parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file_s_name', default='default.ini', nargs='?', help="Файл настроек")
parser.add_argument('-p', '--path', default='Settings\\', help="Путь к файлу настроек")
parser.add_argument('-s', '--save', default=1, help="Номер сохранения")
args = parser.parse_args()

config_path = args.path + args.file_s_name
save_number = args.save






ans = "\nStart of programm...\n--------------------------------------"
print(ans)
print(f'Текущие параметры: {str(vars(args))[1:-1]}')

if os.path.exists(config_path):
    print("Файлы на месте.\n")
    try:
        save1 = game_builder()
    except Exception:
        print("Произошла непредвиденная ошибка")
        exit(1)

    print(save1.__str__())
else:
    print("\nПроверьте наличие папки Settings.\nОна должна находиться в корне и содержать файл default.ini"
          " и settings.ini\n"
          "Если файлы прсиутствуют, а ошибка не исчезла, скорее всего файлы повреждены.")
    exit(0)




ans = "\n--------------------------------------\n...End of programm"
print(ans)