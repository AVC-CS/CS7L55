def printscores1(**scores):
    for k, v in scores.items():
        print(f'Subject {k:>10}: {v:>10}')


def printscores2(scores):
    for k, v in scores.items():
        print(f'Subject {k:>10}: {v:>10}')


def printscores3(Computer, Math, English):
    print(f'{Math:>10} {English:>10} {Computer:>10}')


def main():
    kwargs = {'Math': 90, 'English': 100, 'Computer': 90}
    printscores1(**kwargs)
    printscores2(kwargs)
    printscores3(**kwargs)


if __name__ == '__main__':
    main()
