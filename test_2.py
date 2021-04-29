"""
The program will display the student grades, average grade, and the percentage of grades that are above the average grade. An input text file which contains the grades will be used in this program.  

A main() function will be created to initialize the application. 

Then a calculate_percent_above_average() function will be created to calculate the percentage of grades that are above the average grade. 

The grades in the input text file will be read using the open() method and then the grades will be assigned to a list of integers.

Lastly the information, which contains the student grades, average grade, and the percentage of grades that are above average, will be outputted to the user.
"""

"""
main
    infile = open("Final.txt")
    copy individual grades
    close infile

calculate_percent_above_average
    average = sum of grades / total number of grades
    num = 0
    For grade in grades
        if the grade is > average
            num += 1
    print("Number of grades: ", total number of grades)
    print("Average grade: ", average)
    print("Percentage of grades above average: {0:.2f}%)
        format 100 * num / total number of grades

main
""" 

def main():
    infile = open("Final.txt", 'r')
    grades = [int(line.rstrip()) for line in infile]
    infile.close()
    for i in range(len(grades)):
        grades[i] = int(grades[i])

def calculate_percent_above_average():
    average = sum(grades) / len(grades)
    num = 0
    for grade in grades:
        if grade > average:
            num += 1
    print("Number of grades:", len(grades))
    print("Average grade:", average)
    print("Percentage of grades above average: {0:.2f}%".format(100 * num / len(grades)))

main()