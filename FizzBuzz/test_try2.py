"""the script is based on the game FizzBuzz."""


class Game:  # used the class to improve the program in the future
    def __init__(self, limit: int, sep_1=4, sep_2=7):
        self.limit = limit  # limit - maximum input numbers
        self.sep_1 = sep_1  # sep_1 - the first separator
        self.sep_2 = sep_2  # sep_2 - the second separator
        print(sep_1, sep_2)

    def check_exeption(self):
        count = 0
        _list_results = []  # here writing results
        while self.limit > count:
            try:  # if value doesn't int then will be error
                num = int(input("Напишите число: "))  # player writing number
                _list_results.append(num)
            except ValueError:
                print("Напишите пожалуйста число!")
                continue
            count += 1
        return _list_results

    def function_replace(self):  # the function swaps the numbers
        _list_num = self.check_exeption()
        for i in _list_num:  # if True then loop moves to another iteration
            if i % 5 == 0 and i % 3 == 0:  # right now conditions set for the numbers 3 and 5,
                # you can # change to # sep_1 and sep_2
                print('FizzBuzz')
                continue
            elif self.sep_1 == 4 and i % self.sep_1 == 0 and i % 3 == 0:
                print('Argh')
                continue
            elif self.sep_1 == 7 and i % self.sep_1 == 0 and i % 3 == 0:
                print('Blergh')
                continue
            elif i % 5 == 0:
                print('Buzz')
                continue
            elif i % 3 == 0:
                print('Fizz')
                continue
            elif i % self.sep_2 == 0:
                print('Blergh')
                continue
            elif i % self.sep_1 == 0:
                print('Argh')
                continue
            else:
                print(i)


def main():
    print('Приветствую тебя в игре "FizzBuzz"!')
    print('Напиши цифру, сколько чисел вы будете называть: ')
    lenth_of_game = int(input())
    print('Если ты хочешь менять числа, которые без остатка делятся на 4 и 7,то напиши "change", иначе любое слово: ')
    change = input().lower().strip()
    if change == 'change':
        exemp_1 = Game(lenth_of_game)
        exemp_1.function_replace()
    else:
        exemp_2 = Game(lenth_of_game, 3, 5)
        exemp_2.function_replace()


if __name__ == "__main__":
    main()
