class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        calc = self.size + n

        if calc > self.capacity:
            raise ValueError("Too much cookie in the jar!")

        self.size = calc

    def withdraw(self, n):
        calc = self.size - n

        if calc < 0:
            raise ValueError(
                f"That's too much! You only have {self.size} cookies left!"
            )

        self.size = calc

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, n):
        if n < 0:
            raise ValueError("Capacity can't be negative!")

        self._capacity = n

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n):
        self._size = n


def main():
    jar = Jar(15)

    print(jar.size)
    print(jar)

    jar.deposit(15)

    print(jar.size)
    print(jar)

    jar.withdraw(10)

    print(jar.size)
    print(jar)


if __name__ == "__main__":
    main()
