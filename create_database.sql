CREATE DATABASE IF NOT EXISTS findyourprof;
USE findyourprof;

DROP TABLE IF EXISTS prof;
CREATE TABLE prof (
  id varchar(255) PRIMARY KEY,
  name varchar(255), school varchar(255), 
  createdAt timestamp NOT NULL default CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS user;
CREATE TABLE user (
  id varchar(255) PRIMARY KEY,
  email varchar(255) NOT NULL,
  createdAt timestamp NOT NULL default CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS review;
CREATE TABLE review (
  id varchar(255) PRIMARY KEY,
  rating float(2,1),
  comment text(1000),
  advice text(500),
  meetup text(100),
  userId varchar(255),
  profId varchar(255),
  createdAt timestamp NOT NULL default CURRENT_TIMESTAMP
  -- CONSTRAINT reviewFK1 FOREIGN KEY (userId) REFERENCES user(id),
  -- CONSTRAINT reviewFK2 FOREIGN KEY (profId) REFERENCES prof(id)
);
