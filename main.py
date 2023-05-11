from pprint import pprint

with open('file1.txt', 'rt', encoding = 'utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ingrs_count = int(file.readline())
        ingrs = []
        for i in range(ingrs_count):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            dish_ingrs = {
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            }
            ingrs.append(dish_ingrs)
        file.readline()
        cook_book[dish_name] = ingrs
    pprint(cook_book, sort_dicts=False)

def get_shop_list_by_dishes(dishes, person_count):
    for dish in dishes:
        if dish not in cook_book.keys():
            return f'Блюдо {dish} отсутствует'
    ingrs_dict = {}
    for dish in dishes:
        for ingrs in cook_book.get(dish):
            ingredient_name, quantity, measure = ingrs.get('ingredient_name'), int(ingrs.get('quantity')) * person_count, ingrs.get('measure')
            if ingredient_name not in ingrs_dict.keys():
                ingrs_dict[ingredient_name] = {
                    'measure': measure,
                    'quantity': quantity
                    }
            else:
                exist_quantity = int(ingrs_dict[ingredient_name]['quantity'])
                ingrs_dict[ingredient_name] = {
                    'measure': measure,
                    'quantity': exist_quantity + quantity
                    }
    return ingrs_dict
pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 4))
