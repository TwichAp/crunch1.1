from itertools import product
import argparse
import os

"""
Проблема 1 - Путь сохранения файла (желательно и на Unix)
Проблема 2 - Организация шаблонов
"""

alp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?/~`'

request = argparse.ArgumentParser()
request.add_argument('minimum', type = int, help = 'Minimum length of combinations')
request.add_argument('maximum', type = int, help = 'Maximum length of combinations')
request.add_argument('-o', '--output', help = 'Save dictionary to the specified directory')
request.add_argument('-c', '--chars', default = alp, help = 'Valid characters (default: all printable chars)')

# G Придумать, как организовать шаблоны 
request.add_argument('-s', '--sample', help = 'Sample for combinations')
# Идея 1: Отдельно стоящая функция

request.add_argument('-f', '--filename', default = 'dict', help = 'Set your file name (default: dict)')
args = request.parse_args()

_copy = 2
while f'{args.filename}.txt' in os.listdir('.'):
    args.filename = f'dict ({_copy})'
    _copy += 1

with open(f'{args.filename}.txt', 'x+') as _file:
    for iteration in range(args.minimum, args.maximum + 1):
        for comb in product(alp, repeat=iteration):
            _file.write(f'{''.join(comb)}\n')


