import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect("Lesson14/Apple.sqlite")
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER
    );
''')

def search(b, key):
    found = False
    for child in b:
        if found: return child.text
        if child.tag == "key" and child.text == key:
            found = True
    return None

fname = input("Enter file name: ")
stuff = ET.parse(fname)
all = stuff.findall("dict/dict/dict")
for entry in all:
    if(search(entry, "Track ID") is None): continue 
    name = search(entry, "Name")
    artist = search(entry, "Artist")
    album = search(entry, "Album")
    genre = search(entry, "Genre")

    if name is None or artist is None or album is None or genre is None:
        continue

    cur.execute("INSERT OR IGNORE INTO Artist(name) VALUES(?)", (artist,))
    cur.execute("SELECT id FROM Artist WHERE name = ?", (artist,))
    artist_id = cur.fetchone()[0]
    
    cur.execute("INSERT OR IGNORE INTO Genre(name) VALUES(?)", (genre,))
    cur.execute("SELECT id FROM Genre WHERE name = ?", (genre,))
    genre_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO Album(title, artist_id) VALUES(?, ?)", (album, artist_id))
    cur.execute("SELECT id FROM Album WHERE title = ?", (album,))
    album_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO Track(title, album_id, genre_id) VALUES(?, ?, ?)", (name, album_id, genre_id))
    
conn.commit()

