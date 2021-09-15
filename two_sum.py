def twosum(numbers, target):
    map = {}

    for i in range(len(numbers)):
        if target-numbers[i] not in map:
            map[numbers[i]] = i
        else:
            print(list(map[target-numbers[i]]+1, i+1))


def main():
    twosum([2, 7, 11, 15], 9)
    twosum([2, 3, 4], 6)
    twosum([-1, 0], -1)


if __name__ == "__main__":
    main()
