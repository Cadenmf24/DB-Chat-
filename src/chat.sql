DROP TABLE IF EXISTS user_info;
DROP TABLE IF EXISTS ban_logs;
DROP TABLE IF EXISTS chat_logs;


CREATE TABLE user_info(
    id SERIAL PRIMARY KEY, name TEXT UNIQUE NOT NULL DEFAULT '', num_id TEXT NOT NULL, date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE ban_logs(
    id SERIAL PRIMARY KEY, user_id INTEGER NOT NULL DEFAULT 0, ban_start DATE NOT NULL, ban_end DATE NOT NULL, server_name TEXT DEFAULT 'General'
);

CREATE TABLE chat_logs(
    id SERIAL PRIMARY KEY, sender INTEGER NOT NULL DEFAULT 0, receiver INTEGER NOT NULL DEFAULT 0, time_log DATE NOT NULL, 
    body TEXT NOT NULL DEFAULT '', message_read BOOLEAN NOT NULL DEFAULT FALSE, message_id SERIAL NOT NULL, 
    server_name TEXT NOT NULL DEFAULT 'General'
);

-- CREATE Table past_usernames(
--     id SERIAL PRIMARY KEY, contact INTEGER NOT NULL, current_username TEXT UNIQUE NOT NULL , past_usernames
-- );

INSERT INTO user_info(name, date_created, num_id) VALUES
    ('Abbott', CURRENT_TIMESTAMP, '0000'),
    ('Costello', CURRENT_TIMESTAMP, '1987'),
    ('Moe', CURRENT_TIMESTAMP, '1492'),
    ('Larry', CURRENT_TIMESTAMP, '1882'),
    ('Curly', CURRENT_TIMESTAMP, '1234'),
    ('DrMavin', '1991-05-16', '2345');

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

-- INSERT INTO past_usernames(contact, current_username, past_usernames) VALUES
--     (1, 'Abbott', {'George', 'Charlie', 'Synthia'})



-- To Do list

-- Each message is sent into a server specified by a parameter
-- If they are banned in that server, state so somehow (error or something)
-- Each ban log has a server, so certain people aren't banned completely
-- change id from numbers to discord like tags 
-- users can change their name but they can't change their id
-- each user has a date created and that date changes when a new name is chosen
-- possible old name list?, list
-- each chat has a date
-- chat_logs is one big table full of servers and shit
-- inner join to see if someone is banned on the ban log

    


