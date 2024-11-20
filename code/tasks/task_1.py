from sys import exit

class Pair():
    def __init__(self, first: float, second: float):
        if not (isinstance(first, float) and isinstance(second, float)):
            raise ValueError("Значения должны быть дробными числами.")
        self.first = first
        self.second = second

    def read(self):
        while True:
            try:
                self.first = float(input("Введите первое число: "))
                self.second = float(input("Введите второе число: "))
                break
            except ValueError:
                print("Ошибка: Значения должны быть дробными числами. Попробуйте снова.")

    def display(self):
        print(f"Первое число: {self.first}\nВторое число: {self.second}")

    def function(self, x: float):
        return self.first * x + self.second


def make_pair(first, second):
    if not (isinstance(first, float) and isinstance(second, float)):
        raise ValueError("Значения должны быть дробными числами.")
    return Pair(first, second)

def main():
    my_pair = make_pair(3.0, 5.0)
    my_pair.display()
    my_pair.read()
    my_pair.display()
    print(f"Значение функции при x = 9: {my_pair.function(9.0)}")

if __name__ == "__main__":
    main()
