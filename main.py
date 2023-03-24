#!/usr/bin/env python3


def main() -> None:
    number_of_queries = int(input())
    for _ in range(number_of_queries):
        query = input().split()
        match query[0]:
            case "add":
                number = query[1]
                name = query[2]
                phonebook[number] = name
            case "del":
                number = query[1]
                phonebook.pop(number, None)
            case "find":
                number = query[1]
                print(phonebook.get(number, "not found"))


if __name__ == "__main__":
    phonebook = {}
    main()
