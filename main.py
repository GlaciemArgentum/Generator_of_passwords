from random import *
from string import *
from time import *

symb = punctuation
password = []
positive_answer = 'да'
negative_answer = 'нет'


def correct_answer(input_, must_be='digit', phrase=''):
    if must_be == 'digit':
        while not (input_.isdigit() and int(input_) >= 0):
            input_ = input(f'{phrase} — это целое неотрицательное число. Введите данные в необходимом формате: ')
        return int(input_)
    elif must_be == 'Да/Нет':
        while not (input_ == positive_answer or input_ == negative_answer):
            input_ = input(
                f'Вы должны ответить "{positive_answer}" или "{negative_answer}". Введите данные в необходимом формате: ')
        return input_
    elif must_be == 'choice':
        while not (input_ == '1' or input_ == '2'):
            input_ = input('Вы должны ответить "1" или "2". Введите данные в необходимом формате: ')
        return input_
    elif must_be == 'symb':
        while input_ == '':
            input_ = input('Вы должны ввести символы, которые будут использоваться в пароле: ')
        return input_


def correct_logic(type_, fig, len_, symb=0):
    if type_ == 'fig':
        while not (str(fig).isdigit() and len_ >= int(fig) >= 0):
            fig = correct_answer(fig, phrase='Количество цифр')
            if not (len_ >= int(fig)):
                fig = input(
                    f'Колличество цифр должно быть не больше длины пароля. Введите число, которое не больше {len_}: ')
        return int(fig)
    if type_ == 'symb':
        while not (str(symb).isdigit() and len_ - fig >= int(symb) >= 0):
            symb = correct_answer(symb, phrase='Количество символов')
            if not (len_ - fig >= int(symb)):
                symb = input(
                    f'Колличество символов и цифр должно быть не больше длины пароля. Введите число, которое не больше {len_ - fig}: ')
        return int(symb)


length_of_password = correct_answer(input('Здравствуйте! Давайте придумаем вам пароль. Введите длину пароля: '), phrase='Длина пароля')
if length_of_password == 0:
    for _ in range(5):
        print('.', end='')
        sleep(1)
    print('\nСерьёзно?')
    sleep(1)
    while not (str(length_of_password).isdigit() and int(length_of_password) > 0):
        length_of_password = input('Длина пароля — это целое положительное число. Введите данные в необходимом '
                                   'формате: ')
    length_of_password = int(length_of_password)
options = correct_answer(input(f'Будем настраивать пароль? ({positive_answer}/{negative_answer}): '), 'Да/Нет')
if options == positive_answer:
    quant_of_figures = correct_logic('fig', input('Введите количество цифр: '), length_of_password)
    quant_of_symbols = correct_logic('symb', quant_of_figures, length_of_password, input('Введите количество символов: '))
    if quant_of_symbols > 0:
        opt_symb = correct_answer(input(f'Будем настраивать используемые символы? ({positive_answer}/{negative_answer}): '), 'Да/Нет')
    if quant_of_symbols > 0 and opt_symb == positive_answer:
        print('На данный момент используется стандартный список символов:', symb)
        redact_symb = correct_answer(input(
            'Вы можете изменить стандартный список (введите 1) или использовать только свои символы (введите 2): '), 'choice')
        flag = negative_answer
        if redact_symb == '1':
            while flag == negative_answer:
                must_delete = [i for i in input(
                    f'Без пробелов введите символы, которые хотите удалить из списка: {symb} Чтобы не удалять символы, введите пробел: ')
                               if i in symb]
                if must_delete != [' ']:
                    symb = [i for i in symb if not i in must_delete]
                    symb = ''.join(symb)
                must_add = input(
                    f'Без пробелов введите символы, которые хотите добавить в список (латиница и цифры не добавляются): {symb} Чтобы не добавлять символы, введите пробел: ')
                if must_add != ' ':
                    for i in range(len(must_add)):
                        if must_add[i] not in (ascii_letters + digits + symb):
                            symb = symb + must_add[i]
                flag = correct_answer(input(f'Закончить редактирование списка символов? ({positive_answer}/{negative_answer}): '), 'Да/Нет')
        if redact_symb == '2':
            symb = ''
            must_add = correct_answer(input('Введите свои символы без пробелов (латиница и цифры не добавляются): '), 'symb')
            for i in range(len(must_add)):
                if must_add[i] not in (ascii_letters + digits + symb):
                    symb = symb + must_add[i]
    quant_of_letters = length_of_password - quant_of_figures - quant_of_symbols
    for _ in range(quant_of_letters):
        password.append(choice(ascii_letters))
    for _ in range(quant_of_figures):
        password.append(choice(digits))
    for _ in range(quant_of_symbols):
        password.append(choice(symb))
    shuffle(password)
elif options == negative_answer:
    symb = ascii_letters + digits + punctuation
    for _ in range(length_of_password):
        password.append(choice(symb))
print('Ваш новый пароль:', ''.join(password))