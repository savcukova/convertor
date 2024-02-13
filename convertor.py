def start_translation(abs_path, translation_pattern):
    print("zaciname")


def apartment_translation():
    abs_path = ""
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
    apartment_translation()