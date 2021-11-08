import re

def readFile(path, encoding='utf-8'):
    try:
        with(open(path, encoding=encoding)) as file:
            data = file.read()
            print("soubor otevren")
    except FileNotFoundError as error:
        return 'soubor nebyl nalezen'
    except Exception as error:
        return f'doslo k problemu pri otevirani souboru: {error}'
    finally:
        file.close()
    return data


def charFrequency(vety):
    char = re.findall(r".", vety, re.MULTILINE)
    my_dict = {i: char.count(i) for i in char}
    list = [(k, v) for k, v in my_dict.items()]
    list.sort(reverse=True,key=lambda y: y[1])
    return list

print(charFrequency(readFile("veta.txt")))