CREATE TABLE 'user' (
  'id' INT AUTO_INCREMENT PRIMARY KEY,
  'name' VARCHAR(255) NOT NULL,
  'email' VARCHAR(255) NOT NULL,
  'password' VARCHAR(255) NOT NULL
);

-- ALTER TABLE users
-- RENAME TO user;

-- Insert INTO user (name, email, password) VALUES ('Mohamed', 'Mohamed',1);


CREATE TABLE 'Show' (
  'id' INT AUTO_INCREMENT PRIMARY KEY,
  'name' VARCHAR(255) NOT NULL,
  'description' VARCHAR(255) NOT NULL,
  'rating' INT NOT NULL,
  'time' VARCHAR(255) NOT NULL,
  'age_limit' INT NOT NULL,
  'Category' VARCHAR(255) NOT NULL,
  'image' VARCHAR(255) NOT NULL,
  'Category_id' INT NOT NULL,
  FOREIGN KEY (Category_id) REFERENCES Category(id)
);

CREATE TABLE 'Category' (
  'id' INT AUTO_INCREMENT PRIMARY KEY,
  'name' VARCHAR(255) NOT NULL
);


CREATE TABLE 'watch_later' (
  'id' INT AUTO_INCREMENT PRIMARY KEY,
  'user_id' INT NOT NULL,
  'show_id' INT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES user(id),
  FOREIGN KEY (show_id) REFERENCES Show(id)
);

-- drop table watch_later;
-- drop table user;
-- drop table Show;
-- drop table Category;
-- drop table like;
-- drop table dislike;


-- CREATE TABLE 'Comments' (
--   'id' INT AUTO_INCREMENT PRIMARY KEY,
--   'comment' VARCHAR(255) NOT NULL,
--   'user_id' INT NOT NULL,
--   'show_id' INT NOT NULL,
--   FOREIGN KEY (user_id) REFERENCES users(id),
--   FOREIGN KEY (show_id) REFERENCES Shows(id)
-- );


-- CREATE TABLE 

-- ALTER TABLE table_name
--   RENAME TO new_table_name;

CREATE Table dislike (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  show_id INT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES user(id),
  FOREIGN KEY (show_id) REFERENCES Show(id)
);

CREATE TABLE like (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  show_id INT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES user(id),
  FOREIGN KEY (show_id) REFERENCES Show(id)
);

-- fake
-- fake
-- fake
-- fake
-- fake
-- fake
-- fake
-- fake
-- fake


-- INSERT INTO user (name, email, password)
-- VALUES
--     ('Alice Johnson', 'alice.johnson@example.com', 'password123'),
--     ('Bob Smith', 'bob.smith@example.com', 'password456'),
--     ('Charlie Brown', 'charlie.brown@example.com', 'password789');

-- INSERT INTO Category (name)
-- VALUES
--     ('Drama'),
--     ('Comedy'),
--     ('Action'),
--     ('Horror'),
--     ('Sci-Fi');

-- INSERT INTO Show (name, description, rating, time, age_limit, Category, image, Category_id)
-- VALUES
--     ('Breaking Bad', 'A high school chemistry teacher turned methamphetamine producer.', 9, '9:00 PM', 18, 'Drama', 'breaking_bad.jpg', 1),
--     ('The Office', 'A mockumentary on a group of typical office workers.', 8, '8:00 PM', 13, 'Comedy', 'the_office.jpg', 2),
--     ('The Dark Knight', 'Batman faces off against the Joker in Gotham City.', 9, '10:00 PM', 16, 'Action', 'dark_knight.jpg', 3),
--     ('The Conjuring', 'Paranormal investigators work to help a family plagued by dark forces.', 7, '11:00 PM', 18, 'Horror', 'conjuring.jpg', 4),
--     ('Interstellar', 'A team of explorers travels through a wormhole in space to ensure humanity’s survival.', 8, '7:00 PM', 13, 'Sci-Fi', 'interstellar.jpg', 5);

-- INSERT INTO like (user_id, show_id)
-- VALUES
--     (1, 1),  -- Alice likes Breaking Bad
--     (1, 2),  -- Alice likes The Office
--     (2, 3),  -- Bob likes The Dark Knight
--     (2, 5),  -- Bob likes Interstellar
--     (3, 4);  -- Charlie likes The Conjuring


-- INSERT INTO dislike (user_id, show_id)
-- VALUES
--     (1, 3),  -- Alice dislikes The Dark Knight
--     (2, 4),  -- Bob dislikes The Conjuring
--     (3, 1);  -- Charlie dislikes Breaking Bad


INSERT INTO user (id, name, email, password)
VALUES
    (1, 'Alice Johnson', 'alice.johnson@example.com', 'password123'),
    (2, 'Bob Smith', 'bob.smith@example.com', 'password456'),
    (3, 'Charlie Brown', 'charlie.brown@example.com', 'password789');

INSERT INTO Category (id, name)
VALUES
    (1, 'Drama'),
    (2, 'Comedy'),
    (3, 'Action'),
    (4, 'Horror'),
    (5, 'Sci-Fi');

INSERT INTO Show (id, name, description, rating, time, age_limit, Category, image, Category_id)
VALUES
    (1, 'Breaking Bad', 'A high school chemistry teacher turned methamphetamine producer.', 9, '9:00 PM', 18, 'Drama', 'breaking_bad.jpg', 1),
    (2, 'The Office', 'A mockumentary on a group of typical office workers.', 8, '8:00 PM', 13, 'Comedy', 'the_office.jpg', 2),
    (3, 'The Dark Knight', 'Batman faces off against the Joker in Gotham City.', 9, '10:00 PM', 16, 'Action', 'dark_knight.jpg', 3),
    (4, 'The Conjuring', 'Paranormal investigators work to help a family plagued by dark forces.', 7, '11:00 PM', 18, 'Horror', 'conjuring.jpg', 4),
    (5, 'Interstellar', 'A team of explorers travels through a wormhole in space to ensure humanity’s survival.', 8, '7:00 PM', 13, 'Sci-Fi', 'interstellar.jpg', 5);

INSERT INTO like (id, user_id, show_id)
VALUES
    (1, 1, 1),  -- Alice likes Breaking Bad
    (2, 1, 2),  -- Alice likes The Office
    (3, 2, 3),  -- Bob likes The Dark Knight
    (4, 2, 5),  -- Bob likes Interstellar
    (5, 3, 4);  -- Charlie likes The Conjuring

INSERT INTO dislike (id, user_id, show_id)
VALUES
    (1, 1, 3),  -- Alice dislikes The Dark Knight
    (2, 2, 4),  -- Bob dislikes The Conjuring
    (3, 3, 1);  -- Charlie dislikes Breaking Bad


-- -- Bob likes one show from each category
-- INSERT INTO like (id, user_id, show_id)
-- VALUES
--     (6, 2, 1),  -- Drama: Breaking Bad
--     (7, 2, 2),  -- Comedy: The Office
--     (8, 2, 3),  -- Action: The Dark Knight (already liked earlier, so skip if needed)
--     (9, 2, 4),  -- Horror: The Conjuring
--     (10, 2, 5); -- Sci-Fi: Interstellar (already liked earlier, so skip if needed)

-- -- DELETE FROM like
-- WHERE id IN (6, 7, 8, 9, 10);


-- -- Bob dislikes different shows for variety
-- INSERT INTO dislike (id, user_id, show_id)
-- VALUES
--     (4, 2, 1),  -- Drama: Breaking Bad
--     (5, 2, 2),  -- Comedy: The Office
--     (6, 2, 4);  -- Horror: The Conjuring (already disliked earlier, so skip if needed)

-- DELETE FROM dislike
-- WHERE id IN (4, 5, 6);

-- Extra Drama
INSERT INTO Show (id, name, description, rating, time, age_limit, Category, image, Category_id)
VALUES
(6, 'Better Call Saul', 'The story of lawyer Jimmy McGill before Breaking Bad.', 8, '8:30 PM', 16, 'Drama', 'saul.jpg', 1),

-- Extra Comedy
(7, 'Brooklyn Nine-Nine', 'A funny police sitcom in Brooklyn.', 8, '9:30 PM', 13, 'Comedy', 'b99.jpg', 2),

-- Extra Action
(8, 'John Wick', 'A retired hitman seeks revenge.', 9, '10:30 PM', 18, 'Action', 'john_wick.jpg', 3),

-- Extra Horror
(9, 'It', 'A shape-shifting clown haunts children in a small town.', 7, '11:30 PM', 18, 'Horror', 'it.jpg', 4),

-- Extra Sci-Fi
(10, 'Stranger Things', 'Kids uncover supernatural mysteries in their town.', 9, '7:30 PM', 13, 'Sci-Fi', 'stranger_things.jpg', 5);


-- Bob likes 3 of the new shows
INSERT INTO like (id, user_id, show_id)
VALUES
(11, 2, 6),  -- Likes Better Call Saul (Drama)
(12, 2, 7),  -- Likes Brooklyn Nine-Nine (Comedy)
(13, 2, 10); -- Likes Stranger Things (Sci-Fi)

-- Bob dislikes the other 2 new shows
INSERT INTO dislike (id, user_id, show_id)
VALUES
(7, 2, 8),  -- Dislikes John Wick (Action)
(8, 2, 9);  -- Dislikes It (Horror)


INSERT INTO watch_later (id, user_id, show_id)
VALUES
(1, 2, 3),  -- Bob will watch The Dark Knight later
(2, 2, 9),  -- Bob will watch It later (even though he dislikes it — maybe he's curious)
(3, 2, 7);  -- Bob will watch Brooklyn Nine-Nine later


SELECT * FROM user;
SELECT * FROM Category;
SELECT * FROM Show;
SELECT * FROM like;
SELECT * FROM dislike;
SELECT * FROM watch_later;
SELECT * FROM Comments;