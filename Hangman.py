from random import choice

clothes_list = ["блузка",
"брюки",
"ветровка",
"галстук",
"джинсы",
"жакет",
"жилет",
"капри",
"кардиган",
"кеды",
"кепка",
"кимоно",
"колготки",
"комбинезон",
"костюм",
"кроссовки",
"куртка",
"леггинсы",
"майка",
"носки",
"пальто",
"перчатки",
"пиджак",
"пижама",
"платье",
"плащ",
"пончо",
"рукавицы",
"сандалии",
"сапоги",
"сарафан",
"свитер",
"свитшот",
"сорочка",
"шарф",
"шорты",
"шуба",
"шапка",
"юбка",
"топ",
"туника",
"трикотаж",
"толстовка",
"футболка",
"украшения",
"белье",
"ходунки",
"чулки"]
food_list = ["яблоко",
"банан",
"груша",
"апельсин",
"помидор",
"огурец",
"морковь",
"картофель",
"лук",
"чеснок",
"брокколи",
"капуста",
"шпинат",
"салат",
"кабачок",
"баклажан",
"перец",
"рыба",
"курица",
"говядина",
"свинина",
"индейка",
"яйцо",
"сыр",
"творог",
"йогурт",
"мёд",
"хлеб",
"рис",
"макароны",
"гречка",
"овсянка",
"торт",
"пирожное",
"мороженое",
"шоколад",
"конфеты",
"овощи",
"фрукты",
"орехи",
"изюм",
"сухофрукты",
"грибы",
"фасоль",
"чечевица",
"горох",
"масло",
"желе",
"запеканка",
"суп"]
animals_list = ["собака",
"кошка",
"лошадь",
"корова",
"овца",
"свинья",
"коза",
"курица",
"утка",
"гусь",
"индейка",
"павлин",
"кролик",
"мышь",
"крыса",
"хомяк",
"черепаха",
"змея",
"ящерица",
"крокодил",
"аллигатор",
"обезьяна",
"горилла",
"шимпанзе",
"орангутан",
"тигр",
"лев",
"леопард",
"пантера",
"слон",
"носорог",
"бегемот",
"жираф",
"буйвол",
"зебра",
"верблюд",
"лама",
"алпака",
"енот",
"волк",
"лиса",
"олень",
"лось",
"медведь",
"пингвин",
"акула"]
music_list = ["мелодия",
"гармония",
"аккорд",
"нота",
"ключ",
"ритм",
"темп",
"партитура",
"симфония",
"концерт",
"опера",
"балет",
"мюзикл",
"композитор",
"музыкант",
"оркестр",
"дирижер",
"альбом",
"песня",
"ария",
"жанр",
"блюз",
"джаз",
"рок",
"фольклор",
"скрипка",
"фортепиано",
"гитара",
"барабаны",
"саксофон",
"труба",
"флейта",
"гобой",
"тромбон",
"арфа",
"балалайка",
"аккордеон",
"синтезатор",
"винил",
"граммофон"]
category_list = ['одежда', clothes_list, 'eда', food_list, 'животные', animals_list, 'музыка', music_list]

def restart(ext = 'да'):
    while ext != 'да' and ext != 'нет':
        ext = input('Хотете сыграть ещё раз? (да/нет) ').strip().lower()
    return ext == 'да'

def get_word(category_list):
    category = 'a'
    while type(category) == str:
        category = choice(category_list)
    word = choice(category).upper()
    return category_list[category_list.index(category) - 1].upper(), word.upper()

def display_hangman(tries):
    stages = [ 
                '''
                _______
                |     |
                |     O
                |    \|/
                |     |
                |   _/ \\_
                |
                |
                
                ''',
                '''
                _______
                |     |
                |     O
                |    \|/
                |     |
                |   _/ \\
                |
                |
                
                ''',
                '''
                _______
                |     |
                |     O
                |    \|/
                |     |
                |    / \\
                |
                |
                
                ''',
                '''
                _______
                |     |
                |     O
                |    \|/
                |     |
                |    / 
                |  
                ''',
                '''
                _______
                |     |
                |     O
                |    \|/
                |     |
                |    
                |  
                ''',
                '''
                _______
                |     |
                |     O
                |    \|
                |     |
                |    
                |  
                ''',
                '''
                _______
                |     |
                |     O
                |     |
                |     |
                |     
                |  
                ''',
                '''
                _______
                |     |
                |     O
                |    
                |     
                |    
                |  
                ''',
                '''
                _______
                |     |
                |     
                |    
                |       
                |  
                ''',
                '''
                       
                       
                      
                     
                        
                   
                ''',
    ]
    return stages[tries]

def play(category, word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 9                          # количество попыток

    print('Давайте играть в Виселицу!')
    print(display_hangman(tries))
    print(f'Тема: {category}')
    print(f'Отгадайте слово: {word_completion}')

    while not guessed and tries > 0:
        text = input('Введите букву или слово целиком: ').upper().strip()
        if text.isalpha() and len(text) == 1:
            if text in guessed_letters:
                print(f'Вы уже называли букву {text}')
            elif text not in word:
                print(f'Буквы {text} нет в загаданном слове')
                tries -= 1
                guessed_letters.append(text)
            else:
                print(f'Буква {text} есть в загаданном слове')
                guessed_letters.append(text)
                word_as_list = list(word_completion)
                indices = [i for i in range(len(word)) if word[i] == text]
                for index in indices:
                    word_as_list[index] = text
                word_completion = ''.join(word_as_list)
                if '_' not in word_completion:
                    guessed = True
        elif text.isalpha() and len(text) == len(word):
            if text in guessed_words:
                print(f'Вы уже называли слово {text}')
            elif text != word:
                print(f'Слово {text} не является загаданным')
                tries -= 1
                guessed_letters.append(text)
            else:
                guessed = True
                word_completion = word
        print(display_hangman(tries))
        print(f'Тема: {category}')
        print(f'Слово: {word_completion}')
        print()
    if guessed:
        print('Поздравляем, вы угадали слово!')
    else:
        print(f'Вы не угадали слово. Загаданным словом было {word}')

while restart():
    category, word = get_word(category_list)
    play(category, word)
    if not restart(''):
        break
print('Спасибо за игру! До встречи!')
input('Нажмите ENTER чтобы выйти')
