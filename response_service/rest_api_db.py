import psycopg2

conn = psycopg2.connect(database="sensor_data2", user="postgres", password="Ironman@3142", host="127.0.0.1", port="5432")
cur = conn.cursor()

cur.execute("SELECT * from HEALTH_DATA2 where USER_ID=3")
rows = cur.fetchall()
for row in rows:
   print("USER_ID = ",row[0])
   print("HR = ",row[1])
   print("BLOOD_OXYGEN_LEVEL = ",row[2])
   print("TEMPERATURE = ",row[3])
   print("BP_SYSTOLIC = ",row[4])
   print("BP_DIASTOLIC = ",row[5])
   print("DATE_TIME = ",row[6])

conn.close()