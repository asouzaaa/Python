def fizz_buzz(start, end):
    if end <= start:
        print("O número final deve ser maior que o número inicial.")
        return

    for num in range(start, end + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

def main():
    start = int(input("Digite o número inicial: "))
    end = int(input("Digite o número final: "))

    fizz_buzz(start, end)

if __name__ == "__main__":
    main()

