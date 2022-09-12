DROP TABLE IF EXISTS user_info;
DROP TABLE IF EXISTS ban_logs;
DROP TABLE IF EXISTS chat_logs;


CREATE TABLE user_info(
    id SERIAL PRIMARY KEY, name TEXT UNIQUE NOT NULL DEFAULT '', contact SERIAL NOT NULL, date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE ban_logs(
    id SERIAL PRIMARY KEY, user_id INTEGER NOT NULL DEFAULT 0, ban_start DATE NOT NULL, ban_end DATE NOT NULL 
);

CREATE TABLE chat_logs(
    id SERIAL PRIMARY KEY, sender INTEGER NOT NULL DEFAULT 0, receiver INTEGER NOT NULL DEFAULT 0, time_log DATE NOT NULL, 
    body TEXT NOT NULL DEFAULT '', message_read BOOLEAN NOT NULL DEFAULT FALSE, message_id SERIAL NOT NULL
);

INSERT INTO user_info(name, date_created) VALUES
    ('Abbott', CURRENT_TIMESTAMP),
    ('Costello', CURRENT_TIMESTAMP),
    ('Moe', CURRENT_TIMESTAMP),
    ('Larry', CURRENT_TIMESTAMP),
    ('Curly', CURRENT_TIMESTAMP),
    ('DrMavin', '1991-05-16');

INSERT INTO ban_logs(user_id, ban_start, ban_end) VALUES
    (4, '1995-01-01', '2060-01-01'),
    (5, '1990-01-01', '2000-01-01');

INSERT INTO chat_logs(sender, receiver, time_log, body, message_read) VALUES
    (1,2,'1922-01-01', 'Ayo', TRUE),
    (2,1,'1922-01-12', 'Dab me up', FALSE),
    (3,4,'1995-08-12', 'Ao bro, dont do what your thinking of doing', FALSE),
    (4,3,'1995-08-12', 'Yo buddy, that was a huge mistake man', TRUE),
    (4,3,'1996-08-12', 'America or something', TRUE),
    (3,4,'1994-08-12', 'Canada or something', TRUE),
    (5,1, '2000-08-24', 'Guys dont worry im still here', TRUE);




    


