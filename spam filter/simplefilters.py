from basefilter import BaseFilter
from utils import write_classification_to_file

import os
import random

class NaiveFilter (BaseFilter):
    
    def train (self, dir_path):
        pass
    
    def get_email_files(self, dir_name):
        email_dict = {}
        it = os.scandir(dir_name)
        for entry in it:
            if not entry.name.startswith('!') and entry.is_file():
                email_dict[entry.name] = entry.path
        return email_dict
    
    def test (self, dir_path):
        emails = self.get_email_files(dir_path)
        pred_dict = {}
        for mail in emails:
            pred_dict[mail] = self.analyse_email(emails[mail])
        write_classification_to_file(pred_dict, os.path.join(dir_path,"!prediction.txt"))
        
    def analyse_email (self, file_path):
        return "OK"
        
        
class ParanoidFilter (BaseFilter):
    
    def train (self, dir_path):
        pass
    
    def get_email_files(self, dir_name):
        email_dict = {}
        it = os.scandir(dir_name)
        for entry in it:
            if not entry.name.startswith('!') and entry.is_file():
                email_dict[entry.name] = entry.path
        return email_dict
    
    def test (self, dir_path):
        emails = self.get_email_files(dir_path)
        pred_dict = {}
        for mail in emails:
            pred_dict[mail] = self.analyse_email(emails[mail])
        write_classification_to_file(pred_dict, os.path.join(dir_path,"!prediction.txt"))
        
    def analyse_email (self, file_path):
        return "SPAM"
        

class RandomFilter (BaseFilter):
    
    def train (self, dir_path):
        pass
    
    def get_email_files(self, dir_name):
        email_dict = {}
        it = os.scandir(dir_name)
        for entry in it:
            if not entry.name.startswith('!') and entry.is_file():
                email_dict[entry.name] = entry.path
        return email_dict
        
    def test (self, dir_path):
        emails = self.get_email_files(dir_path)
        pred_dict = {}
        for mail in emails:
            pred_dict[mail] = self.analyse_email(emails[mail])
        write_classification_to_file(pred_dict, os.path.join(dir_path,"!prediction.txt"))
        
    def analyse_email (self, file_path):
        return random.choice(["SPAM", "OK"])