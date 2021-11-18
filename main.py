import psycopg2

query1 = ''' 
SELECT DISTINCT(ft.food_type_name),COUNT(f.food_name) FROM food f  JOIN food_types ft ON f.food_type_id = ft.food_type_id   GROUP BY ft.food_type_name
'''

query2 = '''
SELECT f.food_name, SUM(Cals_per100grams) AS sum_of_calories  FROM food f  JOIN energy_values_of_food e  ON f.food_id = e.food_id
GROUP BY f.food_name
'''

query3 = '''
SELECT ft.food_type_name,e.Cals_per100grams FROM food f  JOIN food_types ft ON f.food_type_id = ft.food_type_id JOIN energy_values_of_food e ON  f.food_id = e.food_id  
'''

connection = psycopg2.connect(database="Dbname", user="username", password="password", host="localhost", port=5432)

cursor = connection.cursor()
cursor.execute(query1)
record1 = cursor.fetchall()
print("Data from Database from the first query:- ", record1)

cursor.execute(query2)
record2 = cursor.fetchall()
print("Data from Database from the second query:- ", record2)

cursor.execute(query3)
record3 = cursor.fetchall()
print("Data from Database from the third query:- ", record3) 
