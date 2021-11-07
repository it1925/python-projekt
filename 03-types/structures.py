import re
def charFrequency(vety):
    char = re.findall(r".", vety, re.MULTILINE)
    my_dict = {i: char.count(i) for i in char}
    list = [(k, v) for k, v in my_dict.items()]
    list.sort(reverse=True,key=lambda y: y[1])
    return list

veta = "Tři sta třicet tři stříbrných stříkaček přestříkalo přes tři sta třicet tři stříbrných střech."
print(charFrequency(veta))