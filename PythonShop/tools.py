import time

class Tools:
    SLEEP_SECONDS = 1
    GRAMS_PER_KILOGRAM = 1000
    KILOGRAM_TO_POUND = 2.2046
    OUNCES_PER_POUND = 16
    POUNDS_PER_STONE = 14
    #Space wasting constants (if you need sources)

    def findounces(self, a, b):
        total_kg = (b + self.GRAMS_PER_KILOGRAM * a) / self.GRAMS_PER_KILOGRAM
        total_ounces = total_kg * self.KILOGRAM_TO_POUND * self.OUNCES_PER_POUND

        stone = total_ounces // (self.POUNDS_PER_STONE * self.OUNCES_PER_POUND)
        total_ounces = total_ounces % (self.POUNDS_PER_STONE * self.OUNCES_PER_POUND)
        pounds = total_ounces // self.OUNCES_PER_POUND
        total_ounces = total_ounces % self.OUNCES_PER_POUND

        time.sleep(self.SLEEP_SECONDS)
        return (
            f"{a} kilograms and {b} grams is equivalent to {stone} stones, "
            f"{pounds} pounds, and about {round(total_ounces, 5)} ounces."
        )

    def sums(self):
        active = True
        int_total = 0
        float_total = 0.0

        while active:
            value = input('Enter an integer or a float. 0 to stop.\n')
            if value == '0':
                active = False
            else:
                if '.' in value:
                    float_total += float(value)
                else:
                    int_total += int(value)

        print('Done!')
        print('Integer sum:', int_total, '\n Float sum:', float_total)

    def get_grades(self, first_subject, second_subject):
        first_grade = input(first_subject + ' grade: ')
        second_grade = input(second_subject + ' grade: ')

        if first_grade == 'd' and second_grade == 'd':
            outcome = 'Not promoted'
        elif first_grade == 'f' or second_grade == 'f':
            if first_grade in ('a', 'b') or second_grade in ('a', 'b'):
                if first_grade == 'f':
                    outcome = second_subject
                elif second_grade == 'f':
                    outcome = first_subject
            else:
                outcome = 'Not promoted'
        elif first_grade == second_grade:
            outcome = 'Choose'
        elif second_grade == 'a':
            outcome = second_subject
        elif second_grade == 'b' and first_grade != 'a':
            outcome = second_subject
        elif first_grade == 'a':
            outcome = first_subject
        elif first_grade == 'b' and second_grade != 'a':
            outcome = first_subject
        elif first_grade == 'c':
            outcome = first_subject
        elif second_grade == 'c':
            outcome = second_subject
        else:
            print('You dummy entered weird things and now you have to try the question again')
            outcome = 'Youre dum'

        time.sleep(self.SLEEP_SECONDS)
        print('Your result:', outcome)

    def add_commas(self, value):
        remaining = value
        formatted = ''

        while remaining > 0:
            if remaining // self.GRAMS_PER_KILOGRAM > 0:
                segment = str(remaining % self.GRAMS_PER_KILOGRAM).zfill(3)
            else:
                segment = str(remaining % self.GRAMS_PER_KILOGRAM)
            remaining = remaining // self.GRAMS_PER_KILOGRAM
            if formatted:
                formatted = segment + ',' + formatted
            else:
                formatted = segment

        time.sleep(self.SLEEP_SECONDS)
        return formatted

    def triangle(self, rows, start):
        current = start

        for i in range(rows):
            print('   ' * ((rows - i) * 2), end='')
            for _ in range(i * 2 + 1):
                print(current, end=' ')
                current += 2
            print()