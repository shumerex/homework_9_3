class EvenNumbers:
    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end
        if self.start % 2 != 0:
            self.start += 1

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        current_number = self.current
        self.current += 2
        return current_number


en = EvenNumbers(10, 25)
for i in en:
    print(i)