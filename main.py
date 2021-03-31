cook_book = dict()
with open('recipes.txt', encoding='utf-8') as f:
    while True:
        dish_name = f.readline().strip()
        count = int(f.readline())
        ing_list = list()
        for el in range(count):
            ingr = f.readline().strip()
            splited = ingr.split('|')
            ing_list.append(splited)
        cook_book[dish_name] = ing_list
        line = f.readline()
        if not line:
            break
f.close()
print(cook_book)