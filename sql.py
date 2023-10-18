import sqlite3

conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

# بيانات المستخدم الجديد
user_data = (None, "development")

# استخدم الأمر INSERT INTO لإدخال البيانات
cursor.execute("INSERT INTO myapp_category (id, name) VALUES (?, ?)", user_data)

# قم بحفظ التغييرات إلى قاعدة البيانات
conn.commit()


conn.close()

