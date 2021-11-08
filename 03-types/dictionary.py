'''
Slovníky (dictionaries) podobně jako seznamy v sobě obsahují další hodnoty.
Na rozdíl od seznamů, ve kterých jsou všechny prvky uspořádané do jedné sekvence, ve slovnících máme dva druhy prvků:
klíč (angl. key) a hodnotu (angl. value).
Každému klíči je přiřazena jedna hodnota.
'''

# Collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets, and they have keys and values.
car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}

point = {'x': 1, 'y': 10}

# Vytvoření slovníku pomocí konstruktoru dict()
point = dict(x=1, y=10)

# Změna hodnoty jednoho prvku slovníku
point['x'] = 2

# Vložení nového prvku do slovníku
point['z'] = 20

# Přístup k položkám slovníku
print(f'point["x"]: {point["x"]}')
print(f'point.get("x"): {point.get("x")}')

# Zjištění, zda existuje hodnota
if 'z' in point:
    print(f'point.get("z"): {point.get("z")}')

# Když hodnota neexistuje, vrací 0    
print(f'point.get("v", 0): {point.get("v", 0)}')

# Odstranění prvku ze slovníku  
del point['x']
print(f'point: {point}')

print(f'car.pop(): {car.pop("model")}')

# Odstraní poslední prvek ze slovníku
print(f'car.popitem(): {car.popitem()}')

# Procházení slovníkem - vypíše vždy pár klíč - hodnota
for key, value in point.items():
    print(f'{key} - {value}')

# Dictionary comprehension - zkráceně vytvoří slovník, jehož klíče tvoří čísla od 0 do 9 a hodnoty druhé mocniny 
values = {x: x ** 2 for x in range(10)}
print(f'values: {values}')

# Unpacking operator - pro slovníky se používají **
first = {'x': 1, 'y': 2}
second = {'x': 10, 'z': 5}
common = {**first, 'a': 15, **second}
print(f'common: {common}')

# Nested dictionary - vnořené slovníky
myfamily = {
    'child1': {
        'name': 'Emil',
        'year': 2004
    },
    'child2': {
        'name': 'Tobias',
        'year': 2007
    },
    'child3': {
        'name': 'Linus',
        'year': 2011
    }
}
print(f'Nested dictionary myfamily: {myfamily}')

# ??? 4. cvičení ???
# a) Navrhněte vlastní vnořený slovník tvořený 3 reálnými objekty s aspoň 6 klíči tak, abyste kromě jednoduchých
# datových typů (čísla, řetězce, boolean) ve slovníku vhodně využili i všechny v tomto bloku probrané strukturované
# typy - tedy set, tuple a list.
# Volte příklad vycházející z reality - např. slovník aut, slovník filmů, slovník historických postav atd.
# b) Pomocí vhodných metod přidejte do slovníku nový prvek a nějaký starý naopak odstraňte
# c) Proveďte výpis obsahu slovníku tak, aby i v konzoli vytvořil hezky naformátovanou tabulku i s mezerami
# viz níže uvedený vzor.

pecivo = {
    'pecivo1': {
        'jmeno': 'houska',
        'rok_vyhotoveni': 2021,
        'cerstvy': True,
        'pocet_kousnuti': (3, 4, 5),
        'vyrobci': {'Pepa', 'Tomas'},
        'info': ['obyc', {'kod': 1234}, 'mak', {'kod': 1324}]
    },
    'pecivo2': {
        'jmeno': 'chleba',
        'rok_vyhotoveni': 2021,
        'cerstvy': True,
        'pocet_kousnuti': (30, 32, 33),
        'vyrobci': {'Pepa'},
        'info': ['obyc', {'kod': 2311}]
    },
    'pecivo3': {
        'jmeno': 'rohlik',
        'rok_vyhotoveni': 2019,
        'cerstvy': False,
        'pocet_kousnuti': (4, 5, 6),
        'vyrobci': {'Tomas'},
        'info': ['obyc', {'kod': 1323}, 'celozrny', {'kod': 4323}]
    }
}
print(pecivo)
del pecivo['pecivo3']
print(pecivo)
pridejpecivo = {'pecivo4': {
    'jmeno': 'kobliha',
    'rok_vyhotoveni': 2021,
    'cerstvy': True,
    'pocet_kousnuti': (2, 3, 4),
    'vyrobci': {'Ema'},
    'info': ['coko', {'kod': 2216}, 'banan', {'kod': 4356}, 'marmelada', {'kod': 1116}]
}}
pecivo.update(pridejpecivo)
print(pecivo)
import pandas


def table(dict={}):
    print('Dictionary: pecivo')
    pandas.set_option('display.max_colums', None)
    pandas.set_option('display.width', None)
    pandas.set_option('display.max_colwidth', -1)
    dictionary = pandas.DataFrame(dict).T
    print(dictionary)


table(pecivo)
