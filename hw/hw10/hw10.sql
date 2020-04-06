CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT d.name, s.size
  FROM dogs AS d, sizes AS s
  WHERE d.height <= s.max AND d.height > s.min;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT p.child
  FROM parents AS p, dogs AS d
  WHERE p.parent = d.name
  ORDER BY height DESC;



-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT p.child AS child, p1.child AS child2
  FROM  parents AS p, parents as p1
  WHERE p.parent = p1.parent AND p.child != p1.child AND p.child < p1.child;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT siblings.child || ' and ' || siblings.child2 || ' are ' || s.size || ' siblings'
  FROM siblings, size_of_dogs as s, size_of_dogs as s2
  WHERE s.size = s2.size AND siblings.child = s.name AND siblings.child2 = s2.name;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height);

-- Add your INSERT INTOs here
INSERT INTO stacks_helper SELECT name, height, height FROM dogs;

INSERT INTO stacks_helper
SELECT s.dogs || ', ' || d.name, s.stack_height + d.height, d.height
FROM stacks_helper AS s, dogs as d
WHERE s.last_height < d.height;

INSERT INTO stacks_helper
SELECT s.dogs || ', ' || d.name, s.stack_height + d.height, d.height
FROM stacks_helper AS s, dogs as d
WHERE s.last_height < d.height;

INSERT INTO stacks_helper
SELECT s.dogs || ', ' || d.name, s.stack_height + d.height, d.height
FROM stacks_helper AS s, dogs as d
WHERE s.last_height < d.height;

CREATE TABLE stacks AS
  SELECT dogs, stack_height
   FROM stacks_helper
   WHERE stack_height > 170
   ORDER BY stack_height;
