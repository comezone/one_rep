"""the script is based on the game FizzBuzz."""


class Game:  # used the class to improve the program in the future
    def __init__(self, limit: int, sep_1=4, sep_2=7):
        self.limit = limit  # limit - maximum input numbers
        self.sep_1 = sep_1  # sep_1 - the first separator
        self.sep_2 = sep_2  # sep_2 - the second separator
        print(sep_1, sep_2)

    def function_replace(self):  # the function swaps the numbers
        _list_results = []  # here writing results
        count = 0
        while self.limit > count:
            try:  # if value doesn't int then will be error
                num = int(input("Напишите число: "))  # player writing number
            except ValueError:
                print("Напишите пожалуйста число!")
                continue
            if num % 5 == 0 and num % 3 == 0:  # right now conditions set for the numbers 3 and 5,
                # you can # change to # sep_1 and sep_2
                num = 'FizzBuzz'
            elif self.sep_1 == 4 and num % self.sep_1 == 0 and num % 3 == 0:
                num = 'Argh'
            elif self.sep_1 == 7 and num % self.sep_1 == 0 and num % 3 == 0:
                num = 'Blergh'
            elif num % 5 == 0:
                num = 'Buzz'
            elif num % 3 == 0:
                num = 'Fizz'
            elif num % self.sep_2 == 0:
                num = 'Blergh'
            elif num % self.sep_1 == 0:
                num = 'Argh'

            _list_results.append(num)  # append result in _list_results
            count += 1
        print("Ваш результат: ", *_list_results, "Сыграем еще раз? :)", sep='\n')  # output _list_results


def main():
    print('Приветствую тебя в игре "FizzBuzz"!')
    print('Напиши цифру, сколько чисел вы будете называть: ')
    lenth_of_game = int(input())
    print('Если ты хочешь менять числа, которые без остатка делятся на 4 и 7,то напиши "change", иначе любое слово : ')
    change = input().lower().strip()
    if change == 'change':
        exemp_1 = Game(lenth_of_game)
        exemp_1.function_replace()
    else:
        exemp_2 = Game(lenth_of_game, 3, 5)
        exemp_2.function_replace()


if __name__ == "__main__":
    main()
