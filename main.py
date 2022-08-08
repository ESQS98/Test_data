import json, os
from typing import Dict, List
import models
from dataclasses import asdict

FILE_NAME = 'example2.json'
CLEAN_FILE = 'example.json'


def loadEntitysFromFile(file: str) -> List[Dict]:
    """
    Loads a json file and returns a list of dicts.
    """
    with open(file, 'r') as f:
        return json.load(f)
    

def saveEntitys(entitys: List[Dict]) -> None:
    """
    Saves a list of dicts to a json file.
    """
    json_entitys = {
        "Users": {k:asdict(v) for k,v in entitys['Users'].items()},
        "Blogs": {k:asdict(v) for k,v in entitys['Blogs'].items()},
        "Comments": {k:asdict(v) for k,v in entitys['Comments'].items()}
    }
    
    
    with open(CLEAN_FILE, 'w') as f:
        json.dump(json_entitys, f, indent=4)

def flatEntitys(nested: List[Dict]) -> Dict[str, Dict]:
    flat = {
        "Users": {},
        "Blogs": {},
        "Comments": {}
    }
    __walkData(nested, flat['Users'], flat['Blogs'], flat['Comments'])
    
    return flat
    
def __walkData(data: List, Users: Dict, Blogs: Dict, Comments: Dict) -> None:
    
    for entity in data:
        new_object = models.classFactory(entity['_entity'], **entity)
        if type(new_object) == models.User:
            Users[new_object.id] = new_object
        elif type(new_object) == models.Blog:
            Blogs[new_object.id] = new_object
        elif type(new_object) == models.Comment:
            Comments[new_object.id] = new_object
        
        if 'user' in entity:
            new_user = models.classFactory('User', **entity['user'])
            if new_user.id not in Users:
                Users[new_user.id] = new_user
        
        for key in entity:
            if type(entity[key]) == list:
                __walkData(entity[key], Users, Blogs, Comments)
        

if __name__ == '__main__':
    nested = loadEntitysFromFile(FILE_NAME)
    flat = flatEntitys(nested)
    saveEntitys(flat)
    
