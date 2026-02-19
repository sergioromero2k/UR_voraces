#!/usr/bin/env python3

def main() -> None:
    try:
        entrance_c = int(input())
        numbers = {}
        if 10 <= entrance_c <= 1000:
            for i in range(entrance_c):
                values = input().split(" ")
                values_form = [item.strip() for item in values]
                numbers[values_form[0]] = values_form[1]

            for index, value in enumerate(numbers):

        else:
            raise Exception("Limits of range.")

        # Result values maxime
        first_max = max(numbers.values())
        id_max = numbers.in(first_max)
        numbers.remove(first_max)
        print(id_max, end=" ")

        second_max = max(numbers)
        id_second_max = numbers.index(second_max)
        print(id_second_max+1, end=" ")

        print(first_max + second_max)

    except ValueError as e:
        print("Value Error: ", e)
    except Exception as e:
        print("Error: ", e)



if __name__ == "__main__":
    main()