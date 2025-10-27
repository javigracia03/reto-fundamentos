CREATE TABLE characters (
    id SERIAL PRIMARY KEY,
    name TEXT,
    status TEXT,
    species TEXT,
    type TEXT,
    gender TEXT,
    origin_name TEXT,
    location_name TEXT,
    image TEXT,
    url TEXT,
    created TIMESTAMPTZ
);

SELECT * FROM characters;