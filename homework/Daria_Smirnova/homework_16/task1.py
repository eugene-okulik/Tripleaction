import mysql.connector as mysql
import os
import dotenv
import csv

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT')),
    database=os.getenv('DB_NAME')
)
base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
new_path = os.path.join(homework_path, "eugene_okulik", 'Lesson_16', "hw_data", "data.csv")
print(new_path)

with open(new_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)
    missing_rows = []

    for row in reader:
        query = '''
        SELECT COUNT(*) FROM marks
        JOIN students ON marks.student_id = students.id
        JOIN books ON books.taken_by_student_id = students.id
        JOIN lessons ON lessons.id = marks.lesson_id
        JOIN subjets ON lessons.subject_id = subjets.id
        JOIN `groups` ON students.group_id = `groups`.id
        WHERE students.name = %s
          AND students.second_name = %s
          AND `groups`.title = %s
          AND books.title = %s
          AND subjets.title = %s
          AND lessons.title = %s
          AND marks.value = %s
        '''
        cursor = db.cursor()
        cursor.execute(query, row)
        result = cursor.fetchone()[0]

        if result == 0:
            missing_rows.append(row)


print("Строки, которых нет в базе:")
for row in missing_rows:
    print(row)
