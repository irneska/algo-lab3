def get_info_from_file():
    with open("input1.txt", "r") as file:
        n, b = list(map(int, file.readline().split(" ")))
        print(n, b)
        line = file.readline()
        employee_answer = list(line.split(" "))
        data = []

        for i in range(n):
            liked_beers = []
            for j in range(b):
                if employee_answer[i][j] == 'Y':
                    liked_beers.append(j + 1)
                elif employee_answer[i][j] != 'Y' and employee_answer[i][j] != 'N':
                    raise Exception("The worker's preferences ", i+1, " should include only letters Y and N")
            if liked_beers:
                data.append(liked_beers)

        print("Employees' preferences :", data, "\n")
    return data


def find_min_num_of_beer_types(preferences):
    preferences.sort(key=len)
    next_types_enjoyers = preferences
    counter_of_types = 0

    while next_types_enjoyers:
        preferences = next_types_enjoyers
        print(next_types_enjoyers)
        num_of_enjoyers_of_current_type = dict()
        for type_beer_selected in preferences[0]:
            count = 0
            for i in preferences:
                if type_beer_selected in i:
                    count += 1
            num_of_enjoyers_of_current_type[type_beer_selected] = count
        print(num_of_enjoyers_of_current_type)

        type_of_beer = max(num_of_enjoyers_of_current_type, key=num_of_enjoyers_of_current_type.get)

        print("BEER", type_of_beer, "is selected")
        next_types_enjoyers = []
        for i in preferences:
            if type_of_beer not in i:
                next_types_enjoyers.append(i)
        print(next_types_enjoyers)
        print("This beer is checked\n")
        counter_of_types += 1
    return counter_of_types


def output_create(output_result):
    with open("./output.txt", "w") as file:
        print("The number of types of beers needed ->", result_numbers_of_beers)
        file.write(f"{output_result}")


if __name__ == '__main__':
    received_input = get_info_from_file()
    result_numbers_of_beers = find_min_num_of_beer_types(received_input)
    output_create(result_numbers_of_beers)
