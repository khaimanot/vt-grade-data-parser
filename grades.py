import pandas
from sys import argv
from os import makedirs



def write_results(course: str, terms: str, header: str, filename: str, avg: float, totals: list, verbose: bool):
    makedirs("results", exist_ok=True)
    with open(filename, 'w') as output:
        output.write(header)
        output.write(f"Average GPA: {avg}\n\n")
        if verbose:
            print(header[:-1])
            print(f"Average GPA: {avg}\n")
        for total in totals:
            output.write(f"{total[0]}: {total[1]}\n")
            if verbose:
                print(f"{total[0]}: {total[1]}")
    if not verbose:
        print(f"Average GPA is {str(avg)} for \"{course}\" with data from {len(totals)} instructors in these terms: {terms}.")
        print(f"More info in {filename}.\n")


def term_key(term):
    if term == "Fall":
        return 0
    elif term == "Winter":
        return 1
    elif term == "Spring":
        return 2
    elif term == "Summer I":
        return 3
    elif term == "Summer II":
        return 4


def parse(data: pandas.DataFrame, arg: str, verbose: bool):
    if data.empty:
        print(f"No data found for {arg}.\n")
    else:
        coursename = data.iat[0, 4]
        coursecode = f"{data.iat[0, 2]}{data.iat[0, 3]}"
        header = f"{coursecode} {coursename}\n"
        course = f"{coursecode} {coursename}"
        namelen = len(header)

        term_list = sorted(data.Term.unique(), key=term_key)
        terms = ""
        for term in term_list:
            terms += f"{term}, "
        terms = terms[:-2]
        header += f"{terms}\n"
        for i in range(namelen):
            header += '-'
        header += '\n'
        filename = f"results/{coursecode}.txt"
        instructors = data.Instructor.unique()
        insttotals = [(inst, round(data[data["Instructor"] == inst]['GPA'].sum() / len(data[data["Instructor"] == inst].index), 2)) for inst in instructors]
        insttotals.sort(key=lambda x: x[1], reverse=True)
        avg_gpa = round(data.GPA.mean(), 2)
        write_results(course, terms, header, filename, avg_gpa, insttotals, verbose)


def process_arguments():
    # handle optional arguments
    if argv[1] == "--help" or argv[1] == "-h":
        print("Give the department and the course number of a course as two arguments (ex. python3 grades.py CS 3214)")
        print("or give the course name as a single argument in quotes (ex. python3 grades.py \"Computer Systems\").")
        print("You can give multiple courses at a time.\n")
        print("You can give any of these optional arguments before listing the courses:")
        print("-h or --help:    Display this help information")
        print("-t or --terms:   Give a list of any semester terms to limit the search (ex. python3 grades.py -t \"Fall,Spring,Winter,Summer I,Summer II\"...).")
        print("                 The quotes must be used, and a single comma must separate each term. You can give any number of the possible terms.")
        raise SystemExit()
    i = 1
    t = "Fall,Winter,Spring,Summer I,Summer II"
    v = False
    while argv[i].startswith("-"):
        if argv[i] == "--terms" or argv[i] == "-t":
            i += 1
            t = argv[i]
        elif argv[i] == "--verbose" or argv[i] == "-v":
            v = True
        i += 1
    terms = t.split(',')

    data = pandas.read_csv('Grade Distribution.csv')
    # rename columns so they can be accessed as fields of data in while loop
    data.rename(columns={'Course Title': 'CourseTitle', 'Course No.': 'CourseNo', 'Academic Year': 'AcademicYear'}, inplace=True)
    while i < len(argv):
        if i == len(argv) - 1: # final argument is single arg coursename
            d = data[data.CourseTitle == argv[i]]
            parse(d[d['Term'].isin(terms)], argv[i], v)
            break
        arg = ""
        d = None
        if argv[i + 1].isnumeric(): # current argument is part of subj + num
            d = data[data.Subject == argv[i]]
            d = d[d.CourseNo == int(argv[i + 1])]
            arg = argv[i] + argv[i + 1]
            i += 1
        else: # current argument is single arg coursename
            d = data[data.CourseTitle == argv[i]]
            arg = argv[i]
        parse(d[d['Term'].isin(terms)], arg, v)
        i += 1


def main():
    if len(argv) == 1: # no arguments have been given
        print("Use the -h or --help option for instructions on running this script.")
        raise SystemExit()

    # arguments have been given
    process_arguments()


if __name__ == "__main__":
    main()