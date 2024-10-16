"""
Connects to a SQL database using pymssql
"""
import pyodbc


SERVER = 'LAPTOP-EFO3HTGH'
DATABASE = 'AdventureWorks2012'
USERNAME = 'Adventure_Login'
PASSWORD = 'Poly01*'

connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
conn = pyodbc.connect(connectionString)


def test_table_address_duplicate():
    ## Name: Verify that there are not duplictae records in table Address
    ## Steps:
    ## Query table Person.Address and group by AddressID
    ## Find the count of records with the same AddressID
    ## Expected result:
    ## No counts bigger than 1
    sql_query = "SELECT count(AddressId), count(*) as cnt FROM PERSON.ADDRESS GROUP BY AddressID HAVING (count(*)) > 1; "
    cursor = conn.cursor()
    cursor.execute(sql_query)
    records = cursor.fetchall()
    assert len(records) == 0, 'Ids are not unique'

def test_table_address_completeness():
    ## Name: Verify the completeness of table Address
    ## Steps:
    ## Query table Person.Address filter by NULL values in column AddressID
    ## Query table Person.Address filter by NULL values in column AddressLine1
    ## Query table Person.Address filter by NULL values in column City
    ## Query table Person.Address filter by NULL values in column StateProvinceID
    ## Query table Person.Address filter by NULL values in column PostalCode
    ## Query table Person.Address filter by NULL values in column rowguid
    ## Query table Person.Address filter by NULL values in column ModifiedDate
    ## Expected result:
    ## The number of records with value NULL for each query is 0
    val = find_null_values("AddressID")
    assert val == 0, f'AddressID is not complete'
    val = find_null_values("AddressLine1")
    assert val == 0, f'AddressLine1 is not complete'
    val = find_null_values("City")
    assert val == 0, f'City is not complete'
    val = find_null_values("StateProvinceID")
    assert val == 0, f'StateProvinceID is not complete'
    val = find_null_values("PostalCode")
    assert val == 0, f'PostalCode is not complete'
    val = find_null_values("rowguid")
    assert val == 0, f'rowguid is not complete'
    val = find_null_values("ModifiedDate")
    assert val == 0, 'ModifiedDate is not complete'

def test_values_in_document_level_from_table_document():
    ## Name: Verify that the values in the column DocumentLevel from table Document are 0, 1 or 2
    ## Steps:
    ## Query table Production.Document and filter for DocumentLevel not in 0, 1 or 2
    ## Expected result:
    ## No records returned
    sql_query = "SELECT * FROM PRODUCTION.DOCUMENT WHERE DocumentLevel not in (0,1,2);"
    cursor = conn.cursor()
    cursor.execute(sql_query)
    records = cursor.fetchall()
    assert len(records) == 0, 'There are DocumentLevel fields with values different to 0, 1 or 2'

def test_title_assembly_exists_in_table_document():
    ## Name: Verify that the title Assembly exists in the table Document
    ## Steps:
    ## Query table Production.Document and filter by Title equal to Assembly
    ## Expected result:
    ## At least one records found with the Title Assembly
    sql_query = "SELECT Title FROM PRODUCTION.DOCUMENT WHERE Title = 'Assembly';"
    cursor = conn.cursor()
    cursor.execute(sql_query)
    records = cursor.fetchall()
    assert records[0][0] == 'Assembly', 'Title Assembly does not exist in table Document'

def test_the_unit_measure_code_for_kilometer_table_unitmeasure():
    ## Name: Verify that the UnitMeasureCode for Kilometer is KM
    ## Steps:
    ## Query table Production.UnitMeasure and filter by Name equal to Kilometer
    ## Expected result:
    ## One record found with the string KM in the column UnitMeasuerCode
    sql_query = "SELECT TRIM(UnitMeasureCode) FROM PRODUCTION.UNITMEASURE WHERE Name = 'Kilometer';"
    cursor = conn.cursor()
    cursor.execute(sql_query)
    records = cursor.fetchall()
    assert records[0][0] == 'KM', 'The UnitMeasure for Kilometer is not KM'

def test_the_number_of_records_in_table_unitmeasure():
    ## Name: Verify that there are 38 records in the table UnitMeasure
    ## Steps:
    ## Query table Production.UnitMeasure and find the count of records
    ## Expected result:
    ## Count of records is 38
    sql_query = "SELECT count(*) FROM PRODUCTION.UNITMEASURE;"
    cursor = conn.cursor()
    cursor.execute(sql_query)
    records = cursor.fetchall()
    assert records[0][0] == 38, 'The count of records is different to the expected'
def find_null_values(column_name) -> int:
    sql_query = f"SELECT count({column_name}) FROM PERSON.ADDRESS WHERE {column_name} = NULL;"
    cursor = conn.cursor()
    cursor.execute(sql_query)
    records = cursor.fetchall()
    return records[0][0]

