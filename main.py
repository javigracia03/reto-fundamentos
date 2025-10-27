import os, psycopg

import requests

url = os.getenv("DATABASE_URL")
print(url)
connection = psycopg.connect(url)
cur = connection.cursor()
print("BD conectada con éxito")

RM_PAGES = 1

response = requests.get(f"https://rickandmortyapi.com/api/character/?page=19")

data = response.json()


# print(data)

INSERT_SQL = """
INSERT INTO characters (
    id, name, status, species, type, gender,
    origin_name, location_name, image, url, created
) VALUES (
    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
)
ON CONFLICT (id) DO NOTHING;
"""

characters_data = [
    (
        character['id'],
        character['name'],
        character['status'],
        character['species'],
        character['type'],
        character['gender'],
        (character['origin'] or {}).get('name'),
        (character['location'] or {}).get('name'),
        character['image'],
        character['url'],
        character['created'],
    )
    for character in data['results']
]
cur.executemany(INSERT_SQL, characters_data)


cur.execute("SELECT id, name, species FROM characters LIMIT 10;")
print(cur.fetchall())




import matplotlib.pyplot as plt

cur.execute("SELECT species, COUNT(*) FROM characters GROUP BY species;")
rows = cur.fetchall()

species = [r[0] for r in rows]
counts = [r[1] for r in rows]

plt.bar(species, counts)
plt.title("Número de personajes por especie")
plt.xlabel("Especie")
plt.ylabel("Cantidad")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("grafico.png")

print("[OK] Gráfico guardado como grafico.png")


connection.commit()
cur.close()
connection.close()