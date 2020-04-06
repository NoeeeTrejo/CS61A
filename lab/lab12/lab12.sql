.read fa19data.sql

CREATE TABLE obedience AS
  SELECT seven, instructor
  FROM students;

CREATE TABLE smallest_int AS
  SELECT time, smallest FROM students
  WHERE smallest > 2
  ORDER BY smallest
  limit 20;

CREATE TABLE matchmaker AS
  SELECT s_1.pet, s_1.song, s_1.color, s_2.color
  FROM students AS s_1, students AS s_2
  WHERE s_1.pet = s_2.pet and s_1.song = s_2.song and s_1.time != s_2.time;
