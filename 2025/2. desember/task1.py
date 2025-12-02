def find_repeating_digits(id_range):
    lower, upper = id_range.split('-')

    ids = list(range(int(lower), int(upper)+1))
    fakeid_sum = 0

    for id in ids:
        if len(str(id))%2 == 1:
            continue
        
        median = int(len(str(id))/2)

        left = str(id)[:median]
        right = str(id)[median:]

        if left == right:
            fakeid_sum += id
        continue

    return fakeid_sum

with open("2025\\2. desember\\input1.txt") as file:
    contents = file.read()

    comma = contents.find(',')

    counter = 0
    total_fakeidsum = 0
    while comma != -1 and counter < 10000:
        counter += 1

        id_range = contents[0:comma]
        total_fakeidsum += find_repeating_digits(id_range)
        print(f"range: {id_range}")

        contents = contents[comma+1:]
        comma = contents.find(',')

    id_range = contents[comma+1:]
    total_fakeidsum += find_repeating_digits(id_range)
    print(f"range: {id_range}")


    print(f"Svar: {total_fakeidsum}")