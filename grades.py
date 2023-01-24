import csv
from sys import argv
from os import makedirs


def search_by_coursecode(arg1: str, arg2: str, terms: str):
    values = {}

    gpasum = 0.0
    gpacount = 0
    name = ""
    name2 = f"{arg1}{arg2}"
    instructors = {}

    with open("./Grade Distribution.csv", 'r') as input:
        reader = csv.reader(input)
        firstline = True
        for row in reader:
            if firstline: # skip csv field names
                firstline = False
                continue
            if row[2] == arg1 and row[3] == arg2 and row[1] in terms: # check subject, number, and term
                # update overall gpa and course name
                gpasum += float(row[6])
                gpacount += 1
                if name != row[4]:
                    name = row[4]
                # update instructor gpa
                instname = row[5]
                if instname not in instructors:
                    instructors[instname] = []
                instructors[instname].append(float(row[6]))

    values['gpasum'] = gpasum
    values['gpacount'] = gpacount
    values['name'] = name
    values['name2'] = name2
    values['instructors'] = instructors
    return values


def search_by_coursename(arg: str, terms: str):
    values = {}

    gpasum = 0.0
    gpacount = 0
    name = ""
    name2 = ""
    instructors = {}

    with open("./Grade Distribution.csv", 'r') as input:
        reader = csv.reader(input)
        firstline = True
        for row in reader:
            if firstline: # skip field names
                firstline = False
                continue
            if row[4] == arg and row[1] in terms: # check coursename and term
                # update overall gpa and course name
                gpasum += float(row[6])
                gpacount += 1
                if name != row[4]:
                    name = row[4]
                if len(name2) == 0:
                    name2 = f"{row[2]}{row[3]}"
                # update instructor gpa
                instname = row[5]
                if instname not in instructors:
                    instructors[instname] = []
                instructors[instname].append(float(row[6]))

    values['gpasum'] = gpasum
    values['gpacount'] = gpacount
    values['name'] = name
    values['name2'] = name2
    values['instructors'] = instructors
    return values

def all_terms(terms: str):
    return terms == "Fall Winter Spring Summer I Summer II"

def print_results(results: dict, terms: str):
    gpasum = results['gpasum']
    gpacount = results['gpacount']
    name = results['name']
    name2 = results['name2']
    instructors = results['instructors']
    # write out the parsed data
    makedirs("results", exist_ok=True)
    filename = f"results/{name2}.txt"
    with open(filename, 'w') as output:
        header = name2 + " " + name
        output.write(f"{header}\n{terms}\n")
        line = ""
        for i in range(len(header)):
            line += '-'
        avg = round((gpasum / gpacount), 2)
        output.write(f"{line}\nAverage GPA: {str(avg)}\n\n")
        sorted_instructors = {}
        for instname in list(instructors.keys()):
            instgpasum = sum(instructors[instname])
            instgpacount = len(instructors[instname])
            sorted_instructors[instname] = round(instgpasum / instgpacount, 2)
        sorted_instructors = dict(sorted(sorted_instructors.items(), key=lambda x:x[1], reverse=True))
        for instname in sorted_instructors:
            output.write(instname + ": " + str(sorted_instructors[instname]) + '\n')
        print(f"Average GPA for {header} is {str(avg)} with data from {len(sorted_instructors)} instructors in these terms: {terms}.")
        print(f"More info in {filename}.")


def parse_data(arg1: str, arg2: str, terms: str):
    if arg2:
        results = search_by_coursecode(arg1, arg2, terms)
    else:
        results = search_by_coursename(arg1, terms)

    # check that data was found
    if results['gpasum'] == 0:
        print(f"No data found for {arg1}{arg2}.")
    else:
        print_results(results, terms)
    print() # place blank line between requested courses' results


def process_arguments():
    # handle optional arguments
    if argv[1] == "--help" or argv[1] == "-h":
        print("Give the department and the course number of a course as two arguments (ex. python3 grades.py CS 3214)")
        print("or give the course name as a single argument in quotes (ex. python3 grades.py \"Computer Systems\").")
        print("You can give multiple courses at a time.\n")
        print("You can give any of these optional arguments before listing the courses:")
        print("-h or --help:    Display this help information")
        print("-t or --terms:   Give a list of any semester terms to limit the search (ex. -t \"Fall Spring Winter Summer I Summer II\").")
        print("                 The quotes must be used, and you can give any number of the possible terms.")
        raise SystemExit()
    i = 1
    terms = "Fall Winter Spring Summer I Summer II"
    while argv[i].startswith("-"):
        if argv[i] == "--terms" or argv[i] == "-t":
            i += 1
            terms = argv[i]
        i += 1
    
    while i < len(argv):
        if i == len(argv) - 1: # final argument is single arg coursename
            parse_data(argv[i], "", terms)
            break
        if argv[i + 1].isnumeric(): # current argument is part of subj + num
            parse_data(argv[i], argv[i + 1], terms)
            i += 2
        else: # current argument is single arg coursename
            parse_data(argv[i], "", terms)
            i += 1

def main():
    if len(argv) == 1: # no arguments have been given
        print("Use the -h or --help option for instructions on running this script.")
        raise SystemExit()

    # arguments have been given
    process_arguments()


if __name__ == "__main__":
    main()