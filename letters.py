from collections import Counter
import matplotlib.pyplot as plt

def count_letters(filename):
    letter_counter = Counter()
    with open(filename) as file:
        for line in file:
            line_letters = [
                char for char in line.lower() if char.isalpha()
            ]
            letter_counter.update(Counter(line_letters))
    return letter_counter


if __name__ == '__main__':
    lc = count_letters('the_zen_of_python.txt').most_common()
    x, y = zip(*lc)
    plt.bar(x,y)
    plt.show()
