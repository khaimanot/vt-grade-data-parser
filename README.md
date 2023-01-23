# Virginia Tech Grade Distribution Data Parser

#### The latest release (as well as all others) can be found on the releases page at https://github.com/khaimanot/vt-grade-data-parser/releases.

#### Computes and displays the overall average GPA for the given course, as well as that of each instructor for the course (sorted by GPA in decreasing order). 

#### Takes the department and the course number of a course as two arguments, or a single course name in quotes. Multiple courses can be given at a time. Reads data from "Grade Distribution.csv", which must be obtained by the user with the export to CSV function at https://udc.vt.edu/irdata/data/courses/grades and placed in the same directory as "grades.py". Output is written to a text file for the course in a directory called "results".
<br><br>
## HOW TO RUN
#### Run the script in its root directory (with "Grade Distribution.csv" in the same directory) with
    python3 grades.py XX YYYY
#### replacing XX with the department and YYYY with the course number (ex. "python3 grades.py CS 1114", "python3 grades.py MATH 1225"), or with
    python3 grades.py "ZZZZZ"
#### replacing ZZZZZ with the name of a course (including the quotes).