import os
from pprint import pprint


def start_translation(file, translation_pattern):
    if os.path.isfile(file):
        print("soubor existuje")
        appartment_data = read_text_file(file)
        new_data = iterate_through_all_data(appartment_data, translation_pattern)
        pprint(new_data)
    else:
        print("fiel not found.")
        quit()
        

def read_text_file(file):
    with open(file, mode="r", encoding="UTF-8") as txt:
        return txt.readlines()


def iterate_through_all_data(data, translation_pattern):
    results = []
    
    for row in data:
        results.append(rewrite_new_appartment_type(row, translation_pattern))
        
    return results


def rewrite_new_appartment_type(data, translation_pattern):
    disposition, *rest = data.split(",", maxsplit=1)
    new_entry = translation_pattern.get(disposition, "unknown disposition")
    return ", ".join([new_entry] + rest)



def appartment_translation():
    abs_path = f"{os.getcwd()}{os.sep}solution{os.sep}vstupni_data.txt"
    translation_pattern = {
        "byt0001": "1+1",
        "byt0002": "2+1",
        "byt0003": "2+kk",
        "byt0004": "3+1",
        "byt0005": "3+kk",
        "byt0006": "4+1",
        "byt0007": "4+kk",
    }
    
    start_translation(abs_path, translation_pattern)


if __name__ == "__main__":
    appartment_translation()