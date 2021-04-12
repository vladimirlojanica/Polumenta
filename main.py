import random

slova1 = ('Б', 'В', 'Г', 'Д', 'Ђ', 'Ж', 'З', 'Ј', 'К', 'Л', 'Љ', 'М', 'Н', 'Њ', 'П', 'Р', 
            'С', 'Т', 'Ћ', 'Ф', 'Х', 'Ц', 'Ч', 'Џ', 'Ш', 'Б', 'В', 'Г', 'Д', 'Ђ', 'Ж', 'З',
            'Ј', 'К', 'Л', 'Љ', 'М', 'Н', 'Њ', 'П', 'Р', 'С', 'Т', 'Ћ', 'Ф', 'Х', 'Ц', 'Ч',
            'Џ', 'Ш', 'Бл', 'Бр', 'Вл', 'Вр', 'Гл', 'Гр', 'Дл', 'Др', 'Жл', 'Зл', 'Зр',
            'Кр', 'Кл', 'Мр', 'Мл', 'Пј', 'Пл', 'Пљ', 'Пњ', 'Пр', 'Св', 'Сл', 'См', 'Сп',
            'Ст', 'Тл', 'Тр', 'Фл', 'Фљ', 'Фњ', 'Фр', 'Хл', 'Хр')

slova2 = ('а', 'е', 'и', 'о', 'у', 'р')

slova3 = ('б', 'в', 'г', 'д', 'ђ', 'ж', 'з', 'ј', 'к', 'л', 'љ', 'м', 'н', 'њ', 'п', 'р', 'с', 'т', 'ћ', 'ф', 'х', 'ц', 'ч', 'џ', 'ш')

def jedanPolumenta():
    poc = random.choice(slova1)
    srd = random.choice(slova2)
    kr = random.choice(slova3)
    while (list(poc[-1]) in ['л', 'р', 'ј', 'љ', 'њ', 'Ђ','Ж', 'Ј', 'Л', 'Љ', 'Н', 'Њ','Р', 'Ћ', 'Ч', 'Џ', 'Ш']) and (kr == 'р'):
        kr = random.choice(slova3)
    return f'{poc}{srd}{kr}o'

def Polumente(broj=1):
    if broj < 1:
        broj = 1
    if broj > 100:
        raise ValueError('Највећи број Полумента је 100!')
    poliske = []
    while broj >= 1:
        pol = f'{jedanPolumenta()} Полумента'
        if pol in poliske:
            continue
        else:
            poliske.append(pol)
            broj -= 1
    return poliske


if __name__ == '__main__':
	print(Polumente(3))
