def add_dish_ingredient(ingredient):
    ingredient_list = ingredient.split(' | ')
    ingredients = ('ingredient_name', 'quantity', 'measure')
    dish_ingredient = {}
    for i in zip(ingredients, ingredient_list):
        if i[1].isdigit():
          dish_ingredient[i[0]] = int(i[1])
        else:
          dish_ingredient[i[0]] = i[1]
    return dish_ingredient


def get_shop_list_by_dishes(dishes, person_count):
    ingredients_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                quantity_count = ingredient['quantity']*person_count
                name = ingredient['ingredient_name']
                if name in ingredients_list:
                    quantity_with_mesure = ingredients_list[name]
                    quantity_count += quantity_with_mesure['quantity']
                ingredient_quantity = {}
                ingredient_quantity['measure'] = ingredient['measure']
                ingredient_quantity['quantity'] = quantity_count
                ingredients_list[ingredient['ingredient_name']] = ingredient_quantity
        else:
            print(f'No {dish} in cook book')
    return ingredients_list


with open('Recipes.txt', encoding='utf-8') as f:
    text_from_file = f.readlines()
clear_text = []
for elem in text_from_file:
    el = elem.replace("\n", "")
    if el.isdigit():
      el = int(el)
    clear_text.append(el)
cook_book = {}
for element in clear_text:
    if isinstance(element, str):
        element_index = clear_text.index(element)
        if element == clear_text[0] or clear_text[element_index - 1] == '':
            dish = element
            all_ingridients = []
        if '|' in element:
            all_ingridients.append(add_dish_ingredient(element))
        if element == '' or element == clear_text[-1]:
            cook_book.setdefault(dish, all_ingridients)
    if isinstance(element, int):
        quant = element
print(get_shop_list_by_dishes(['Омлет', 'Утка по-пекински', 'Фахитос'], 2))