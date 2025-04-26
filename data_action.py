import json
from typing import List, Dict, Union



def get_db(file: str= "data.json") -> List[Dict[str, Union[str, int]]]:
    with open(file, encoding="utf-8") as file:
        db = json.load(file)
    return db

def save_db(db,file: str = "data.json")-> None:
    with open(file, "w", encoding="utf-8") as file:
        json.dump(db, file, indent=2, ensure_ascii=False)










def get_event_db(file: str= "events.json") -> List[Dict[str, Union[str, int]]]:
    with open(file, encoding="utf-8") as file:
        db = json.load(file)
    return db

def save_event_db(db,file: str = "events.json")-> None:
    with open(file, "w", encoding="utf-8") as file:
        json.dump(db, file, indent=2, ensure_ascii=False)





