def main():
    num = int(input())
    fatorial = 1
    count = num

    while count > 0:
        fatorial = fatorial * count
        count -= 1
    print(fatorial)
if __name__ == "__main__":
    main()