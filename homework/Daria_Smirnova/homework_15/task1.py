import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)
query = 'INSERT INTO students (name, second_name) VALUES (%s, %s)'
values = 'Dima', 'Smirnov'
cursor.execute(query, values)
student_id = cursor.lastrowid
print(student_id)

query1 = 'INSERT INTO `groups`  (title, start_date, end_date) VALUES (%s, %s, %s)'
values1 = 'chavales', 'april 2025', 'jan 2026'
cursor.execute(query1, values1)
group_id = cursor.lastrowid
print(group_id)

query2 = 'UPDATE students SET group_id = %s WHERE id = %s'
values2 = (group_id, student_id)
cursor.execute(query2, values2)

query3 = 'INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)'
values3 = [('Pedro Paramo', student_id),
           ('White heart', student_id),
           ('Shadow of wind', student_id)]
cursor.executemany(query3, values3)

query4 = 'INSERT INTO subjets (title) VALUES (%s)'
value4 = 'english',
cursor.execute(query4, value4)
subject1 = cursor.lastrowid
print(subject1)

query5 = 'INSERT INTO subjets (title) VALUES (%s)'
value5 = 'German',
cursor.execute(query5, value5)
subject2 = cursor.lastrowid
print(subject2)

query6 = 'INSERT INTO lessons (title, subject_id) VALUES (%s, %s)'
value6 = 'English literature', subject1
cursor.execute(query6, value6)
lesson1 = cursor.lastrowid
print(lesson1)

query7 = 'INSERT INTO lessons (title, subject_id) VALUES (%s, %s)'
value7 = 'English sport', subject1
cursor.execute(query7, value7)
lesson2 = cursor.lastrowid
print(lesson2)

query8 = 'INSERT INTO lessons (title, subject_id) VALUES (%s, %s)'
value8 = 'German books', subject2
cursor.execute(query8, value8)
lesson3 = cursor.lastrowid
print(lesson3)

query9 = 'INSERT INTO lessons (title, subject_id) VALUES (%s, %s)'
value9 = 'German writings', subject2
cursor.execute(query9, value9)
lesson4 = cursor.lastrowid
print(lesson4)

query10 = 'INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)'
value10 = 5, lesson1, student_id
cursor.execute(query10, value10)

query11 = 'INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)'
value11 = 4, lesson2, student_id
cursor.execute(query11, value11)

query12 = 'INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)'
value12 = 3, lesson3, student_id
cursor.execute(query12, value12)

query13 = 'INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)'
value13 = 2, lesson4, student_id
cursor.execute(query13, value13)

cursor.execute('SELECT value, lesson_id FROM marks WHERE student_id = %s', (student_id,))
for row in cursor.fetchall():
    print(f"Lesson ID {row['lesson_id']}: mark {row['value']}")

cursor.execute('SELECT title FROM books WHERE taken_by_student_id = %s', (student_id,))
for i in cursor.fetchall():
    print(f"Tittle of books for this student {i['title']}")

query = '''
SELECT DISTINCT  
    marks.value, 
    books.title AS book_title, 
    lessons.title AS lesson_title, 
    subjets.title AS subject_title, 
    students.group_id
FROM marks
JOIN books ON marks.student_id = books.taken_by_student_id
JOIN students ON marks.student_id = students.id
JOIN lessons ON marks.lesson_id = lessons.id
JOIN subjets ON subjets.id = lessons.subject_id
WHERE marks.student_id = %s
ORDER BY books.title, lessons.title, subjets.title
'''

cursor.execute(query, (student_id,))
print(cursor.fetchall())

db.commit()
cursor.close()
db.close()
