"""Dictionary related utility functions."""

__author__ = "730477669"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read a CSV file into a list of rows with each row as a dict[str, str]."""
    rows: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        rows.append(row)
    
    file_handle.close()

    return rows


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Given a table read in rows return the values of the column."""
    values: list[str] = []
    i: int = 0

    while i < len(table):
        for key in table[i]:
            if key == column:
                values.append(table[i][key])
        i += 1

    return values


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Change table read in rows to table read in columns."""
    columns: dict[str, list[str]] = {}
    
    for key in table[0]:
        columns[key] = column_values(table, key)

    return columns


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Given entire table produce first N number of rows of data in a new table."""
    new_table: dict[str, list[str]] = {}
    values: list[str] = []
    i: int = 0

    for key in table:
        values = []
        i = 0

        if rows > len(table[key]):
            return table

        while i < rows:
            values.append(table[key][i])
            i += 1

        new_table[key] = values

    return new_table


def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Select only the columns that you care about."""
    new_table: dict[str, list[str]] = {}

    for key in columns:
        new_table[key] = table[key]

    return new_table


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combine two tables to make a new column-based table."""
    new_table: dict[str, list[str]] = {}

    for key in table1:
        new_table[key] = table1[key]

    for key in table2:
        if key in new_table:
            new_table[key] += table2[key]

        else:
            new_table[key] = table2[key]

    return new_table


def count(values: list[str]) -> dict[str, int]:
    """Given a list of values count the number of times that value is in the list."""
    result: dict[str, int] = {}

    for key in values:
        if key in result:
            result[key] += 1

        else:
            result[key] = 1

    return result