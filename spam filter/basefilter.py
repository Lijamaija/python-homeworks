import os


class BaseFilter:
    
    def __init__(self):
        pass

    def _get_emails(self, dir_name):
        files_dict = {}
        iter1 = os.scandir(dir_name)  #возвращает всё,что есть в директории
        for f in iter1:
            if not f.name.startswith('!') and f.is_file():
                files_dict[f.name] = f.path
        return files_dict
