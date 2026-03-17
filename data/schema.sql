CREATE TABLE IF NOT EXISTS folders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    path TEXT UNIQUE,
    guess_date TEXT,
    location TEXT,
    status TEXT
);
CREATE TABLE IF NOT EXISTS video_files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    folder_id INTEGER,
    name TEXT,
    extension TEXT,
    size_gb REAL,
    FOREIGN KEY(folder_id) REFERENCES folders(id)
);
CREATE TABLE IF NOT EXISTS technical_metadata (
    file_id INTEGER PRIMARY KEY,
    duration REAL,
    width INTEGER,
    height INTEGER,
    fps TEXT,
    codec TEXT,
    FOREIGN KEY(file_id) REFERENCES video_files(id)
);
CREATE TABLE IF NOT EXISTS sync_status (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_id INTEGER,
    master_path TEXT,
    is_synced INTEGER DEFAULT 0,
    is_duplicate INTEGER DEFAULT 0,
    FOREIGN KEY(file_id) REFERENCES video_files(id)
);
