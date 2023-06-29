# Manipulation-of-CSV-Files

This consists of a Leopard class that allows you to read data from any CSV file and extract specific data from it. The class provides several methods for retrieving information and performing statistical analysis on the data.

# Create an instance of the Leopard class

__init__(self, filepath: str) -> None

This method reads a comma-separated CSV file specified by the filepath. It extracts the data from the CSV file into header and data variables. It handles potential errors, such as an empty file or a file not found.

get_header(self) -> list

This method returns the header part of the CSV file as a list. If the file is empty or not found, it returns None.

get_data(self) -> list

This method returns the data part of the CSV file as a list. If the file is empty or not found, it returns None.

stats(self) -> dict

This method returns a dictionary containing count, mean, minimum, and maximum values for each numerical column in the CSV file. It ignores missing values labeled as NA, -, or an empty string. The mean values are rounded to 2 decimal places.

html_stats(self, stats: dict, filepath: str) -> None

This method creates an HTML file specified by filepath and formats the data from the stats dictionary as an HTML table in the file.

count_instances(self, criteria, ...) -> int

This method returns the number of instances that meet the specified criteria.

JavaScript Modifications:

The JavaScript function encdec() in morsecode.html is modified to encode/decode Morse code/string in the input textarea based on the selection box. When the submit button is clicked, the encoded/decoded Morse code is displayed in the output text-area.
