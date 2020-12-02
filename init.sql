-- mysql -uroot < init.sql
CREATE DATABASE IF NOT EXISTS app;
use app;
CREATE TABLE tweets (id INT AUTO_INCREMENT, tweet VARCHAR(100), PRIMARY KEY (id));
INSERT INTO tweets (tweet) VALUES ('1つめのツイート');
INSERT INTO tweets (tweet) VALUES ('2つめのツイート');
INSERT INTO tweets (tweet) VALUES ('3つめのツイート');
INSERT INTO tweets (tweet) VALUES ('4つめのツイート');
INSERT INTO tweets (tweet) VALUES ('5つめのツイート');
INSERT INTO tweets (tweet) VALUES ('6つめのツイート');
INSERT INTO tweets (tweet) VALUES ('7つめのツイート');
INSERT INTO tweets (tweet) VALUES ('8つめのツイート');
INSERT INTO tweets (tweet) VALUES ('9つめのツイート');
INSERT INTO tweets (tweet) VALUES ('10つめのツイート');