import csv
from sys import argv
from os import makedirs

def main():
    # check for correct number of arguments
    if len(argv) != 3:
        print("Give the department and the course number as two arguments (ex. \"python grades.py CS 1114\")")
        exit()
    
    # parse data
    with open("./Grade Distribution.csv", 'r') as input:
        reader = csv.reader(input)
        firstline = True
        gpasum = 0.0
        gpacount = 0
        name = ""
        instructors = {}
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
        # check that data was found
        if gpacount == 0:
            print("Course not found")
            exit()
        # write out the parsed data
        makedirs("results", exist_ok=True)
        filename = f"results/{argv[1]}{argv[2]}.txt"
        with open(filename, 'w') as output:
            header = argv[1] + argv[2] + " " + name
            output.write(header + '\n')
            line = ""
            for i in range(len(header)):
                line += '-'
            output.write(line + '\n')
            output.write("Average GPA: " + str(round((gpasum / gpacount), 2)) + "\n\n")
            for instname in instructors:
                instgpasum = sum(instructors[instname])
                instgpacount = len(instructors[instname])
                output.write(instname + ": " + str(round(instgpasum / instgpacount, 2)) + '\n')


if __name__ == "__main__":
    main()