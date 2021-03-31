cook_book = {}
with open('recipes.txt', encoding='utf-8') as f:
    while True:
        dish_name = f.readline().strip()
        count = int(f.readline())
        for el in range(count):
            ingr = f.readline().strip()
            splited = ingr.split('|')
            ing_dict = {'ingredient_name': splited[0], 'quantity': splited[1], 'measure': splited[2]}
        cook_book[dish_name] = ing_dict
        line = f.readline()
        if not line:
            break
f.close()
# print(cook_book)
# def get_shop_list_by_dishes(dishes, person_count):
#     for el in dishes:
#         for cook_book.keys() in cook_book:
#             if el =


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)