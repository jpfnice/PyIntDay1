
"""
Given a file (you can use "measures.txt", see the github repo) with the following format:
    
    City name;time;date;temperature
    Geneva;12:34;2003/12/23;2.34;
    Lausanne;12:36;2003/12/23;3.34;
    Bern;12:36;2003/12/23;-3.34;
    ....
    
Write a python script to parse this file and store it's content into a "custom object".

You could define a class "Record" that will represent a line of this file and
a class "ListOfRecord" to represent a list of "Record".

This class "ListOfRecord" should offer:

a way to construct an instance of it with the help of a text file like the one above.

a ways to save/restore the list easily.

a method to compute the average of the temperature recorded for a given city name.

any other method you consider interesting to provide

"""

