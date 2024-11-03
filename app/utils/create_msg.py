ICONS_STEP = {
    'Шаг 1': '1️⃣',
    'Шаг 2': '2️⃣',
    'Шаг 3': '3️⃣',
    'Шаг 4': '4️⃣',
    'Шаг 5': '5️⃣',
    'Шаг 6': '6️⃣',
    'Шаг 7': '7️⃣',
    'Шаг 8': '8️⃣',
    'Шаг 9': '9️⃣',
    'Шаг 10': '1️⃣0️⃣',
    'Шаг 11': '1️⃣1️⃣',
    'Шаг 12': '1️⃣2️⃣',
    'Шаг 13': '1️⃣3️⃣',
    'Шаг 14': '1️⃣4️⃣',
    'Шаг 15': '1️⃣5️⃣',
    'Шаг 16': '1️⃣6️⃣',
    'Шаг 17': '1️⃣7️⃣',
    'Шаг 18': '1️⃣8️⃣',
    'Шаг 19': '1️⃣9️⃣',
    'Шаг 20': '2️⃣0️⃣',
}

ICONS_CAT = {'deserty': '🧁',
             'vtorye-bliuda': '🍳',
             'pervye-bliuda': '🍲',
             'garniry': '🍚',
             'vipechka': '🥧',
             'salaty': '🥗'}


def create_recept_message(row_recept:dict) -> str:
    """оформление рецепта"""
    msg = f'{ICONS_CAT.get(row_recept.get('category'))}\t<b>{row_recept.get('title')}</b>\n\n'
    if row_recept.get('count'):
        msg = f"{msg}Из расчета {row_recept.get('count').get('count')} {row_recept.get('count').get('title').lower()}\n"
    ingredients:dict = row_recept.get('ingredients')
    for lvl, value in ingredients.items():
        msg = f'{msg}<u>{lvl}</u>\n'
        for name, counts in value.items():
            weight = f'{str(counts.get('value',''))} {counts.get('type', '')}'
            weight = f"{weight} ({counts.get('text', '')})" if not counts.get('text', '') in weight else weight
            msg = f'{msg}✅ {name}\t{weight}\n'
    m = row_recept.get('steps')

    steps = [f'{ICONS_STEP.get(f'Шаг {w.split('\n',1)[0].strip()}', '')}  {w.split('\n',1)[1].strip()}' for w in row_recept.get('steps').split('Шаг ') if w]
    steps_all = steps[:-1]
    steps_all.extend([s for s in steps[-1].split('\n') if s])

    return msg, steps_all

if __name__ == '__main__':
    
    row_recept = {'id': 13849, 'img': 'https://cdn.food.ru/unsigned/fit/640/480/ce/0/czM6Ly9tZWRpYS9waWN0dXJlcy9yZWNpcGVzLzg1NDMzL2NvdmVycy80M1VhUVQuanBlZw.jpg', 
                  'description': 'Солянка — это блюдо, которое покорило сердца многих современных хозяек. Отличает этот суп от других большое количество мясных изделий в бульоне. Но данный рецепт вообще не похож на классическую солянку. В состав блюда входит филе рыбы, каперсы, соленые огурцы, пастернак и оливки. И не смотрю на то, что это далеко не классическая солянка, блюдо понравиться всем без исключения.', 
                  'title': 'Пикантная солянка с рыбой', 
                  'steps': 'Шаг 1\nНакрошите мелко лук, морковь, пастернак. В кастрюлю с толстым дном налейте подсолнечное масло, выложите нарезанный лук, тушите две-три минуты. В след за луком добавьте морковь и пастернак, тушите 10 минут.\nШаг 12\nЗатем залейте 500 мл рыбного бульона и готовьте еще 20 минут. Потом добавьте нарезанный огурец, каперсы, томатную пасту, лавровый лист и перец, готовьте ещ е минут 10.\nШаг 3\nПока готовятся овощи, нарежьте красную рыбу небольшими кубиками, добавьте в кастрюлю и варите до готовности рыбы, так чтобы рыба не разварилась.\n\nПодавайте солянку разлив в порционные тарелки. Украсьте зеленью петрушки, базилика, укропа, оливками и маслинами. Подайте к бульону сухарики.', 
                  'count': {'count': 6, 'title': 'Порций'}, 
                  'ingredients': {'Для блюда': {'Сметана': {'text': '4 ст. л.', 'type': 'г', 'value': 100.0}, 'Свежая зелень': {'text': 'по вкусу', 'type': 'по вкусу'}}}, 
                  'nutrients': {'fat': '7,13 грамм', 'protein': '5,7 грамм', 'calories': '96,42 кКал', 'carbohydrates': '2,32 грамм'}, 
                  'category': 'pervye-bliuda', 
                  'products': 'Свежая зелень,Сметана'}

    print(create_recept_message(row_recept))