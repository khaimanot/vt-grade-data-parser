# Virginia Tech Grade Distribution Data Parser

Computes and displays the overall average GPA for the given course, as well as that of each instructor for the course (sorted by GPA in decreasing order). 

Takes the department and the course number of a course as two arguments, or a single course name in quotes. Multiple courses can be given at a time, and semester terms can be specified. Reads data from "Grade Distribution.csv", which must be obtained by the user with the export to CSV function at https://udc.vt.edu/irdata/data/courses/grades and placed in the same directory as "grades.py". Output is written to a text file for the course in a directory called "results", and it can also be printed to standard output.
#### Requirements:
* Python 3.8 or beyond
* The 'Grade Distribution.csv' file obtainable from https://udc.vt.edu/irdata/data/courses/grades
## HOW TO INSTALL
 Clone this repository with<br>
`git clone https://github.com/khaimanot/vt-grade-data-parser.git`.

Then enter the directory.

If you'd like, create a Python virtual environment with <br>
`python3 -m venv env`<br> and then activate it with<br>
`source env/bin/activate`.

Then, install the script's dependencies with<br> `pip install -r requirements.txt`.

Don't forget to deactivate the virtual environment (if you're using it) with<br>
`deactivate`.

## HOW TO RUN
#### Run the script in its root directory (with "Grade Distribution.csv" in the same directory) with
    python3 grades.py XX YYYY
#### replacing XX with the department and YYYY with the course number (ex. "python3 grades.py CS 1114", "python3 grades.py MATH 1225"), or with
    python3 grades.py "ZZZZZ"
#### replacing ZZZZZ with the name of a course (including the quotes).
### Optional arguments can also be given before any courses:

#### -h or --help:    Display help information. Cannot be used with any other arguments.
    python3 grades.py -h

#### -v or --verbose: Print all results to standard output in addition to the normal text file.
    python3 grades.py -v MATH 1225

#### -t or --terms:   Give a list of any semester terms to limit the search. 
#### The quotes must be used, and a single comma must separate each term. You can give any number of the possible terms.
    python3 grades.py -t "Fall,Spring,Winter,Summer I,Summer II" MATH 1225