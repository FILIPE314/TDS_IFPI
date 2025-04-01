def main():
    n = int(input())
    i = 0
    valorH = 0

    while i < n:
        i += 1
        valorH = valorH + (1 / i)  

    print(f'{valorH:.4f}')

if __name__ == "__main__":
    main()