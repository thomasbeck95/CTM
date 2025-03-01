CREATE TABLE IF NOT EXiSTS "users"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "username" TEXT NOT NULL UNIQUE,
    "password_hash" TEXT NOT NULL,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "email" TEXT NOT NULL UNIQUE,
    "role" TEXT NOT NULL
);


CREATE TABLE IF NOT EXISTS "tasks"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "task_name" TEXT NOT NULL,
    "task_content" TEXT,
    "task_icon" TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS "assigned"(
    "user_id" INTEGER NOT NULL,
    "task_id" INTEGER NOT NULL,
    "active" INTEGER NOT NULL check(active = 1 OR active = 0),
    "order" INTEGER NOT NULL,
    PRIMARY KEY ("user_id", "task_id"),
    FOREIGN KEY ("user_id") REFERENCES "users" ("id"),
    FOREIGN KEY ("task_id") REFERENCES "tasks" ("id")
); 


