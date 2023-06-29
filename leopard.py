"""
Please write your name
Siddesh R Ohri

"""

# Reminder: You are only allowed to import the csv module (done it for you).
# OTHER MODULES ARE NOT ALLOWED (NO OTHER IMPORT!!!).

import csv  # importing the module


class Leopard:
    def __init__(self, filepath: str) -> None:
        try:
            self.data = []  # To store the data of the file
            self.header = []  # To store the header of the file
            with open(filepath, 'r') as file:  # Opening the file to read it
                csvreader = csv.reader(file, delimiter=',')  # Readfile
                for i in next(csvreader):  # Accessing header of file
                    self.header.append(i)  # Appending value of header
                    for row in csvreader:  # Accessing data of file
                        self.data.append(row)  # Appending value of data
                if (len(self.header) == 0):
                    print("Empty File")
        except FileNotFoundError:
            print("file not found")  # Checks whether the file is found or not

    def get_header(self) -> list:
        try:
            return self.header  # Returns the header of the file
        except FileNotFoundError:
            return None

    def get_data(self) -> list:
        try:
            return self.data  # Returns the data of the file
        except FileNotFoundError:
            return None

    def stats(self) -> dict:
        test = []  # To store digit elemts of file
        for r in self.data:  # Looping variable to access the rows in the data
            for i in list(enumerate(r)):
                if i[1].isdigit():  # checking if it is digit
                    test.append(i)  # Appending the number
        stats = {}  # Creating a dictionary to store the values
        for i in range(len(self.header)):  # Range of length of header
            temp = []  # Stores the index of the element
            for j in test:  # Access the digit elements
                if j[0] == i:  # To check for the index of the element
                    temp.append(int(j[1]))  # Append index of element

            if len(temp) != 0:  # Checks the length of indices
                dic = {'count': len(temp),
                       'mean': round(sum(temp)/len(temp), 2),
                       'min': min(tuple(temp)),
                       'max': max(tuple(temp))}  # Calculating
            else:
                dic = 0  # Dictionary is empty

            if dic != 0:   # Checks the value of the variable d
                stats.update({self.header[i]: dic})  # Store header and dict
        print('  ')
        return stats  # Returns the dictionary statss

    def html_stats(self, stats: dict, filepath: str) -> None:
        with open(filepath, 'w') as html:  # Opening a html file
            html.write("<html>")  # Writing into the html file
            html.write("<head>\n")
            html.write("<meta charset = \"UTF-8\">\n")
            html.write("<style>\n")
            html.write("table, th, td{\n")
            html.write("border: 1px solid black;\n")
            html.write("}\n")
            html.write("</style>\n")
            html.write("</head>\n")
            html.write("<body>\n")
            html.write("<table>\n")
            html.write("<tr>\n")
            html.write("<ht><pre> </pre></th>\n")

            for i in stats:  # Looping variable to access the dictionary
                html.write("<th>"+i+"</th>\n")  # Writing contents of dict
            for i in stats:
                j = str(stats[i]['count'])
                html.write("<td>"+j+"</td>\n")  # Writing the calculated count
            html.write("</tr>\n")
            html.write("<th> Mean </th>\n")

            for i in stats:
                j = str(stats[i]['mean'])
                html.write("<td>"+j+"</td>\n")  # Writing the calculated mean
            html.write("</tr>\n")
            html.write("<th> Min </th>\n")

            for i in stats:
                j = str(stats[i]['min'])
                html.write("<td>"+j+"</td>\n")  # Writing calculated min value
            html.write("</tr>\n")
            html.write("<th> Max </th>\n")

            for i in stats:
                j = str(stats[i]['max'])
                html.write("<td>"+j+"</td>\n")  # Writing calculated maxvalue

    def count_instances(self) -> int:
        ind = []  # Stores the index value
        test_Temp = []  # Stores the variable swap
        temp = self.data  # Variable to store the value of the data
        values = []  # Stores the inputted values

        for i in self.header:
            print("Enter 1 for YES and 2 for NO")
            print("Do you want to enter", i, "?")
            yes_no = int(input())  # Input from the user

            if yes_no == 1:  # If the input from the user is 1
                ind.append(self.header.index(i))  # Appending index value
                print("Enter", i, ": ")
                val = input()  # Input the criteria value from the user
                val = val.upper()  # Convert the user input to upper case
                values.append(val)  # Appending the user input
                for j in values:  # Looping through the values
                    start = ind[0]  # Zeor'th element of the list
                    for r in temp:  # Looping through the values of the data
                        if j == r[start].upper():  # Checks the value entered
                            test_Temp.append(r)  # append entire row
                    temp = test_Temp  # Stores the appended value in a variable
                    test_Temp = []  # Clears list to check for next criteria
                    values.remove(values[0])
                    ind.remove(ind[0])
            print(len(temp))  # Printing the nubmer of instances


"""
COUNT INSTANCES DOC STRING

For every column of the file, the program asks the user to enter the criteria.
For this, the user can enter 1 for 'YES' and 2 for 'NO'
the program will ask the user to enter the value for that criteria if the user
enters 1 and the program skips to the next criteria if
the user enters 2. The loop will run till the end of the file and then
returns the number of instances matching the given criteria.
"""

if __name__ == "__main__":
    # DO NOT COMMENT ALL WHEN SUBMIT YOUR FILE, cannot have an if statement
    # with nothing afterwards.

    # test diabetes_data.csv
    test = Leopard("diabetes_data.csv")
    print(test.get_header())
    print(test.get_data())
    stats = test.stats()
    print(stats)
    test.html_stats(stats, "diabetes.html")
    print()

    # test fide2021.csv
    test2 = Leopard("fide2021.csv")
    print(test2.get_header())
    print(test.get_data())
    stats2 = test2.stats()
    print(stats2)
    test2.html_stats(stats2, "fide2021.html")
    print()

    # test student.csv
    test3 = Leopard("student.csv")
    print(test3.get_header())
    print(test.get_data())
    stats3 = test3.stats()
    print(stats3)
    test3.html_stats(stats3, "student.html")