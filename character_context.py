import sqlite3
from character import Character

def create_characters():
    characters = []

    connection = sqlite3. connect(":memory:")
    cursor = connection.cursor()
    sql_file = open("character_attributes.sql")
    sql_as_string = sql_file.read()
    cursor.executescript(sql_as_string)

    for row in cursor.execute("select * from character_attributes"):
        new_character = Character(row)
        characters.append(new_character)

    characters.sort(key=lambda x: x.characterName)
    return characters