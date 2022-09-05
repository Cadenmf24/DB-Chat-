DROP TABLE IF EXISTS user_info;
DROP TABLE IF EXISTS ban_logs;
DROP TABLE IF EXISTS chat_logs;


Create TABLE user_info(
    id SERIAL PRIMARY KEY, name TEXT NOT NULL DEFAULT '', contact INTEGER NOT NULL DEFAULT 0
);

Create Table ban_logs(
    id SERIAL PRIMARY KEY, user_id INTEGER NOT NULL DEFAULT 0, ban_start date NOT NULL, ban_end date NOT NULL 
);

Create Table chat_logs(
    id SERIAL PRIMARY KEY, sender INTEGER NOT NULL DEFAULT 0, receiver INTEGER NOT NULL DEFAULT 0, time_log DATE NOT NULL, 
    body TEXT NOT NULL DEFAULT '', message_read BOOLEAN NOT NULL DEFAULT FALSE
);

INSERT INTO user_info(id, name, contact) VALUES
    (1, 'Abbott', 1234),
    (2,'Costello', 4321),
    (3, 'Moe', 2468),
    (4, 'Larry', 6969),
    (5, 'Curly', 9696);

INSERT INTO ban_logs(id, user_id, ban_start, ban_end) VALUES
    (1, 4, '1995-01-01', '2060-01-01'),
    (2, 5, '1990-01-01', '2000-01-01');

INSERT INTO chat_logs(id, sender, receiver, time_log, body, message_read) VALUES
    (1,1,2,'1922-01-01', 'Ayo', FALSE),
    (2,2,1,'1922-01-12', 'Dab me up', TRUE),
    (3,3,4,'1995-08-12', 'Ao bro, dont do what your thinking of doing', FALSE),
    (4,4,3,'1995-08-12', 'Yo buddy, that was a huge mistake man', TRUE),
    (5,4,3,'1996-08-12', 'America or something', TRUE),
    (6,3,4,'1994-08-12', 'Canada or something', TRUE),
    (7,5,1, '2000-08-24', 'Guys dont worry im still here', FALSE);




    


