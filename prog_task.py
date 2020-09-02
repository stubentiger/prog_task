from collections import defaultdict
import csv

def main():
    with open("product.template.csv") as opned_file:
        reader = csv.reader(opned_file)
        # skip header
        next(reader, None)
        # empty dict, when using for the first time sets default value of int (0)
        groups = defaultdict(int)

        # Each row read from the csv file is returned as a list of strings
        for row in reader:
            # for the first occurence of the group name
            # the key will be auto created and 0 + row[7] will be put as a value
            # if we already have the key simply accumulate the values
            groups[row[9]] += int(row[7])

    # get a list of tuples instead of a dict (for sorting)
    groups_list = groups.items()

    #sorting by the second item in tuple (item[1]) + selecting the first 3
    top3_gropus = sorted(groups_list, key=lambda item: item[1])[:3]

    print(top3_gropus)


if __name__ == "__main__":
    main()
