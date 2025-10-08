import sqlite3


DB = 'sweigartcats.db'

QUERY1 = """
SELECT c.name
FROM Cats AS c
WHERE c.id NOT IN (
    SELECT v.cat_id
    FROM Vaccinations AS v
    WHERE v.vaccine IN ('rabies', 'FeLV', 'FVRCP')
    GROUP BY v.cat_id
    HAVING COUNT(DISTINCT v.vaccine) = 3
);
"""

QUERY2 = """
SELECT c.name, v.vaccine, v.date, c.birth
FROM Cats AS c
JOIN Vaccinations AS v ON c.id = v.cat_id
WHERE v.date < c.birth;
"""


def check_cat_vax():
    conn = sqlite3.connect(DB, isolation_level=None)
    cursor = conn.cursor()
    cursor.execute(QUERY1)
    missing = cursor.fetchall()
    for row in missing:
        print("-", row[0])

    cursor.execute(QUERY2)
    invalid = cursor.fetchall()
    for name, vaccine, vdate, birth in invalid:
        print(f"{name} - {vaccine} given on {vdate} (before birth {birth})")

    conn.close()



def main():
    check_cat_vax()


if __name__ == "__main__":
    main()