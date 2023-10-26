import json
from pathlib import Path
import os.path as osp


def check_word_list(word_list) -> list:
    for w in word_list:
        if " " in w:
            return False
        elif any([c.isupper() for c in w]):
            return False
        
        return True

def simplify_words(words_list: list) -> list:
    return [w.replace(" ", "").lower() for w in words_list]

def load_companies():
    #file_path = osp.join("data","companies.json")
    file_path = Path(__file__).parent/ "data" / "companies.json"
    print(file_path)

    return json.load(open(file_path, "r"))