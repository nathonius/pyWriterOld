CREATE TABLE project(
  projectID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  title TEXT,
  description TEXT,
  tags TEXT,
  author TEXT,
  authorBio TEXT
);

CREATE TABLE deadline(
  deadlineID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  title TEXT,
  start INTEGER,
  end INTEGER
);

CREATE TABLE location(
  locationID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  title TEXT,
  shortName TEXT,
  description TEXT,
  tags TEXT
);

CREATE TABLE character(
  characterID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  title TEXT,
  shortName TEXT,
  major INTEGER,
  description TEXT,
  tags TEXT,
  bio TEXT,
  notes TEXT,
  goals TEXT
);

CREATE TABLE item(
  itemID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  title TEXT,
  shortName TEXT,
  description TEXT,
  tags TEXT
);

CREATE TABLE note(
  noteID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  title TEXT,
  note TEXT
);

CREATE TABLE scene(
  sceneID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  title TEXT,
  viewpoint TEXT,
  characters TEXT,
  tags TEXT,
  locations TEXT,
  items TEXT,
  start INTEGER,
  end INTEGER,
  file TEXT
);