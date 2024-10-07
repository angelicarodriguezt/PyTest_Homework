# PyTest_Homework
To run this project please follow these instructions:

1. Clone the repository
***Activate the virtual environment .venv by going to .\PyTest_Homework\PyTestHomework\.venv\Scripts and then running the command .\activate  OR create your own virtual environment and follow steps 4 and 5***
3. Install the ODBC Driver 17 for SQL Server
4. Install the following:
pip install pyodbc,
pip install pytest,
pip install pytest-html
5. Execute 'pip list' to confirm you have the previous packages installed
6. Restore AdventureWorks2012 in SQL Server Management Studio
7. Create a Login and then an User for the DB AdventureWorks2012
8. Go to .\PyTest_Homework\PyTestHomework\tests.py and modify the following variables according to yours:
SERVER, DATABASE, USERNAME, PASSWORD
10. In the terminal, go to .\PyTest_Homework\PyTestHomework and run the command: **pytest tests.py **  

You will get a report like this:

![image](https://github.com/user-attachments/assets/8d1db365-4e83-4d21-82f2-25eb5456ffd5)

