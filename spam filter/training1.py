from utils import *
#звездочка позволяет использовать функции из модуля, write_classification_to_file()
import os

class NaiveFilter:
#self - элемент класса, директория - аргумент. делаем констурктор.

    def __init__(self): #инициализировали self, инстанс класса
        pass


    def train(self, dir_name):
        pass

    def test (self, dir_name):
    '''типа протестировать,но в этом фильтре всё не спам '''


'''1. Получить список файлов в диркетории(email_files). 2. Сделать словарь спам-не спам (новый словарь)
Пройти по первому словарю
Для каждого элемента сделать запись в новом словаре '''

    email_files = self._get_emails(dir_name) #   словарь в функции, инстанс класса называется сэлф,
#  вызвать функцию write classification, записать в файл !prediction.txt словарь

 #эту функцию лучше не трогать
 #файл truth начинается с восклицательного знака и он нам не нужен!
 #эта функция смотрит в диркеторию, возвращает файлы в словаре
    def _get_emails(self, dir_name):
        files_dict = {}
        iter1 = os.scandir(dir_name)  #возвращает всё,что есть в директории
        for f in iter1:
            if not f.name.startswith('!') and f.is_file():
               files_dict[f.name] = f.path
        return files_dict

class ParanoidFilter:

    def __init__(self):
        pass


    def train(self, dir_name):
        pass

    def test (self, dir_name):


class RandomFilter:

    def __init__(self):
        pass


    def train(self, dir_name):
        pass

    def test (self, dir_name):
