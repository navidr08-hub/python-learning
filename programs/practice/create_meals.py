# Chapter 16 - SQLite Databases
# (Practice Program) - Meals Ingredients Database

import sqlite3
import re

MEAL_RE = re.compile(r'(.+):(.+)')

DB = 'meals.db'

CREATE_QUERY = """
CREATE TABLE IF NOT EXISTS meals (
    name TEXT
) STRICT;

CREATE TABLE IF NOT EXISTS ingredients (
    name TEXT,
    meal_id INTEGER,
    FOREIGN KEY(meal_id) REFERENCES meals(rowid)
) STRICT;
"""

INSERT_QUERY_MEAL = "INSERT INTO meals (name) VALUES (?)"
INSERT_QUERY_ING = "INSERT INTO ingredients (name, meal_id) VALUES (?, ?)"

MEAL_QUERY = "SELECT rowid FROM meals WHERE name = ?"
ING_QUERY = """
SELECT DISTINCT meals.name
FROM meals
JOIN ingredients ON meals.rowid = ingredients.meal_id
WHERE ingredients.name = ?
"""


def create_tables(conn: sqlite3.Connection):
    cur = conn.cursor()
    cur.executescript(CREATE_QUERY)


def create_meals(conn: sqlite3.Connection, meal: str, ingredients):
    if meal.replace(' ', '').isalpha():
        cur = conn.cursor()
        cur.execute(INSERT_QUERY_MEAL, (meal,))
        meal_id = cur.lastrowid

        for ing in ingredients:
            cur.execute(INSERT_QUERY_ING, (ing, meal_id))
    else:
        conn.close()
        raise Exception("Invalid meal name")


def main():
    # Create tables if they don't exist
    conn = sqlite3.connect(DB, isolation_level=None)
    create_tables(conn)

    print("Please enter recipes in the format:")
    print("meal:ingredient1,ingredient2,ingredient3...")
    print("Enter 'q' to quit\n")

    # Start reading user input
    while True:
        recipe = input("> ")
        if recipe == 'q':
            break
        if MEAL_RE.search(recipe):
            meal, ingredients = MEAL_RE.findall(recipe)[0]
            ingredients = str(ingredients).split(',')
            create_meals(conn, meal, ingredients)
        elif recipe.replace(' ', '').isalpha():
            cur = conn.cursor()
            cur.execute(MEAL_QUERY, (recipe,))
            meal_row = cur.fetchone()

            if meal_row:
                # List all ingredients for this meal
                cur.execute("SELECT name FROM ingredients WHERE meal_id = ?", (meal_row[0],))
                ingredients = [r[0] for r in cur.fetchall()]
                print(f"Ingredients of {recipe}:")
                for ing in ingredients:
                    print(" ", ing)
                continue

            # Otherwise, check if it's an ingredient
            cur.execute(ING_QUERY, (recipe,))
            meals = [r[0] for r in cur.fetchall()]

            if meals:
                print(f"Meals that use {recipe}:")
                for m in meals:
                    print(" ", m)
            else:
                print(f"No results found for '{recipe}'.")
        else:
            print("Invalid entry, please enter recipes in the format:")
            print("meal:ingredient1,ingredient2,ingredient3...\n")

    conn.close()


if __name__ == "__main__":
    main()