import re
import math

def find_repeating_digits(id_range):
    lower, upper = id_range.split('-')

    ids = list(range(int(lower), int(upper)+1))
    fakeid_sum = 0

    for id in ids:      
        median = math.floor(len(str(id))/2)

        for k in range(median+1):
            sub = str(id)[0:k]
            lis = re.findall(sub, str(id))

            if len("".join(lis)) == len(str(id)):
                print(f"fakeid: {id}")
                fakeid_sum += id
                break
    
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
    # print(f"range: {id_range}")


    print(f"Svar: {total_fakeidsum}")