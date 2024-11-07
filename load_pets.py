import sqlite3


DROP_TBL_PERSON = "DROP TABLE IF EXISTS person;"
CREATE_TBL_PERSON = """
CREATE TABLE person (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER
);
"""


def main():
    print("connecting to the database...")
    connection = sqlite3.connect("pets.db")
    cursor = connection.cursor()
    print("Creating person table...")
    cursor.execute(DROP_TBL_PERSON)
    cursor.execute(CREATE_TBL_PERSON)

    print("Inserting values into person...")
    cursor.execute("INSERT INTO person VALUES (1, 'James', 'Smith', 41);")
    cursor.execute("INSERT INTO person VALUES (2, 'Diana', 'Greene', 23);")

    connection.commit()

    # read all the data in the table person
    print("Reading data from table...")
    result = cursor.execute("select id, first_name, last_name, age from person")
    for row in result.fetchall():
        print(f"{row[1]} {row[2]} is {row[3]} years old.")



if __name__ == "__main__":
    main()
