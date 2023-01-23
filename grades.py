import csv
from sys import argv
from os import makedirs


def search_by_coursecode(arg1: str, arg2: str):
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
            if row[2] == arg1 and row[3] == arg2:
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


def search_by_coursename(arg: str):
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
            if row[4] == arg:
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


def parse_data(arg1: str, arg2: str):
    if arg2:
        results = search_by_coursecode(arg1, arg2)
    else:
        results = search_by_coursename(arg1)

    gpasum = results['gpasum']
    gpacount = results['gpacount']
    name = results['name']
    name2 = results['name2']
    instructors = results['instructors']
    # check that data was found
    if gpacount == 0:
        print(f"Course {arg1}{arg2} not found.")
    else:
        # write out the parsed data
        makedirs("results", exist_ok=True)
        filename = f"results/{name2}.txt"
        with open(filename, 'w') as output:
            header = name2 + " " + name
            output.write(f"{header}\n")
            line = ""
            for i in range(len(header)):
                line += '-'
            output.write(f"{line}\n")
            avg = round((gpasum / gpacount), 2)
            output.write(f"Average GPA: {str(avg)}\n\n")
            sorted_instructors = {}
            for instname in list(instructors.keys()):
                instgpasum = sum(instructors[instname])
                instgpacount = len(instructors[instname])
                sorted_instructors[instname] = round(instgpasum / instgpacount, 2)
            sorted_instructors = dict(sorted(sorted_instructors.items(), key=lambda x:x[1], reverse=True))
            for instname in sorted_instructors:
                output.write(instname + ": " + str(sorted_instructors[instname]) + '\n')
            print(f"Average GPA for {header} is {str(avg)} with data from {len(sorted_instructors)} instructors.")
            print(f"More info in {filename}.")
    print()


def main():
    if len(argv) == 1:
        print("Use the --help option for instructions on running this script.")
        raise SystemExit()
    elif argv[2] == "--help" or argv[2] == "-h":
        print("Give the department and the course number of a course as two arguments (ex. python3 grades.py CS 3214)")
        print("or give the course name as a single argument in quotes (ex. python3 grades.py \"Computer Systems\".")
        print("You can give multiple courses at a time.\n")
        raise SystemExit()
    # arguments have been given
    i = 1
    while i < len(argv):
        if i == len(argv) - 1: # final argument is single arg coursename
            parse_data(argv[i], "")
            break
        if argv[i + 1].isnumeric(): # current argument is part of subj + num
            parse_data(argv[i], argv[i + 1])
            i += 2
        else: # current argument is single arg coursename
            parse_data(argv[i], "")
            i += 1


if __name__ == "__main__":
    main()