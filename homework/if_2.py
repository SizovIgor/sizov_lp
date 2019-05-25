string_list = [str, 3, "learn python", "learn python", "learn", "learn python"]


def compare(str1: str, str2: str) -> int:
    if not (isinstance(str1, str) and isinstance(str2, str)):
        return 0
    elif str1 == str2:
        return 1
    elif len(str1) > len(str2):
        return 2
    elif 'learn' in str2:
        return 3


if __name__ == "__main__":
    for i in range(len(string_list)):
        print(
            compare(
                string_list[i - 1],
                string_list[i]
            ),
            string_list[i - 1],
            string_list[i]
        )
