
NSERT INTO groups  (title, start_date, end_date) VALUES ('Bugs', 'march 2025', 'jan 2026')
INSERT INTO students (name, second_name, group_id) VALUES ('Daria', 'Smirnova', 3151)
INSERT INTO books (title, taken_by_student_id) VALUES ('Bad habits', 4877)
INSERT INTO books (title, taken_by_student_id) VALUES ('3 cats', 4877)
INSERT INTO books (title, taken_by_student_id) VALUES ('The closed door', 4877)
INSERT INTO subjets (title) VALUES ('spanish grammar')
INSERT INTO subjets (title) VALUES ('spanish literature')
INSERT INTO lessons (title, subject_id) VALUES ('spanish for beginners', 5116)
INSERT INTO lessons (title, subject_id) VALUES ('spanish for intermediate', 5116)
INSERT INTO lessons (title, subject_id) VALUES ('spanish literature for beginners', 5117)
INSERT INTO lessons (title, subject_id) VALUES ('spanish literature for intermediate', 5117)
INSERT INTO marks (value, lesson_id, student_id) VALUES (5, 9251, 4877)
INSERT INTO marks (value, lesson_id, student_id) VALUES (4, 9252, 4877)
INSERT INTO marks (value, lesson_id, student_id) VALUES (3, 9253, 4877)
INSERT INTO marks (value, lesson_id, student_id) VALUES (2, 9254, 4877)

SELECT value FROM marks WHERE student_id = 4877
SELECT title FROM books WHERE taken_by_student_id = 4877

SELECT DISTINCT  
marks.value, books.title, lessons.title, subjets.title, group_id
FROM marks
JOIN books
ON marks.student_id = books.taken_by_student_id
JOIN students 
ON marks.student_id = students.id
JOIN lessons 
ON marks.lesson_id = lessons.id
JOIN subjets
ON subjets.id = lessons.subject_id
WHERE marks.student_id = 4877
ORDER BY books.title, lessons.title, subjets.title 
