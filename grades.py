import csv
from sys import argv
from os import makedirs

def parse_data(mode: str):
    with open("./Grade Distribution.csv", 'r') as input:
        reader = csv.reader(input)
        firstline = True
        gpasum = 0.0
        gpacount = 0
        name = ""
        name2 = ""
        instructors = {}
        if mode == "coursecode":
            name2 = f"{argv[1]}{argv[2]}"
            for row in reader:
                if firstline: # skip field names
                    firstline = False
                    continue
                if row[2] == argv[1] and row[3] == argv[2]:
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
        elif mode == "coursename":
            for row in reader:
                if firstline: # skip field names
                    firstline = False
                    continue
                if row[4] == argv[1]:
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
        # check that data was found
        if gpacount == 0:
            print("Course not found")
            exit()
        # write out the parsed data
        makedirs("results", exist_ok=True)
        filename = f"results/{name2}.txt"
        with open(filename, 'w') as output:
            header = name2 + " " + name
            output.write(header + '\n')
            line = ""
            for i in range(len(header)):
                line += '-'
            output.write(line + '\n')
            avg = round((gpasum / gpacount), 2)
            output.write("Average GPA: " + str(avg) + "\n\n")
            sorted_instructors = dict(sorted(instructors.items(), key=lambda x:x[1], reverse=True))
            for instname in sorted_instructors:
                instgpasum = sum(sorted_instructors[instname])
                instgpacount = len(sorted_instructors[instname])
                output.write(instname + ": " + str(round(instgpasum / instgpacount, 2)) + '\n')
            print(f"Average GPA for {header} is {str(avg)} with data from {len(sorted_instructors)} instructors.\nMore info in {filename}.")

def main():
    # check for correct number of arguments
    if len(argv) == 3: # subject + course number
        parse_data("coursecode")
    elif len(argv) == 2: # course name
        parse_data("coursename")
    else:
        print("Give the department and the course number as two arguments (ex. python3 grades.py CS 3214)")
        print("or give the name of the course as a single argument in quotes (ex. python3 grades.py \"Computer Systems\"")
        exit()
    


if __name__ == "__main__":
    main()