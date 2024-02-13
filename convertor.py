import os


def start_translation(file, translation_pattern):
    if (os.path.isfile(file)):
        print("file exists")
        appartment_data = read_text_file(file)
    else:
        print("file not found")
        quit()
        
        
def iterate_through_all_data(file):
    results = []
    
    for row in file:
        pass
        
        
def read_text_file(file):
    with open("file", mode = "r", encoding= "UTF-8") as txt:
        return txt.readlines()


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

