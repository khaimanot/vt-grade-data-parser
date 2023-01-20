# Virginia Tech Grade Distribution Data Parser
### Computes and displays the overall average GPA for the given course, as well as that of each instructor for the course.  

### Takes the department and the course number of a course as two arguments. Reads data from "Grade Distribution.csv", which must be obtained by the user with the export to CSV function at https://udc.vt.edu/irdata/data/courses/grades and placed in the same directory as "grades.py". Output is written to a text file for the course in a directory called "results".
<br><br>
## HOW TO RUN
### Run the program in its root directory (with "Grade Distribution.csv" in the same directory) with
    python grades.py XX YYYY
### replacing XX with the department and YYYY with the course number (ex. "python grades.py CS 1114", "python grades.py MATH 1225"). You may need to use "python3" instead of "python".