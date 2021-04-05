cook_book = {}
with open('recipes.txt', encoding='utf-8') as f:
    while True:
        dish_name = f.readline().strip()
        count = int(f.readline())
        ing_list = []
        for el in range(count):
            ingr = f.readline().strip()
            splited = ingr.split('|')
            ing_list.append({'ingredient_name': splited[0], 'quantity': splited[1], 'measure': splited[2]})
        cook_book[dish_name] = ing_list
        line = f.readline()
        if not line:
            break
f.close()


def get_shop_list_by_dishes(dishes, person_count):
    set_1 = set(cook_book.keys()) and set(dishes)
    shop_list = {}
    for el in set_1:
        x = 0
        list_ = cook_book.get(el)
        for elem in list_:
            if list_[x].get('ingredient_name') in shop_list:
                shop_list[list_[x].get('ingredient_name')]['quantity'] += int(list_[x].get('quantity')) * person_count
            else:
                shop_list[list_[x].get('ingredient_name')] = {'measure': list_[x].get('measure'),
                                                              'quantity': int(list_[x].get('quantity')) * person_count}
                x += 1
    print(shop_list)


get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
