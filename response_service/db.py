#CREATING TABLES IN DATABASE
import psycopg2
conn = psycopg2.connect(database="sensor_data2", user="postgres", password="Ironman@3142", host="127.0.0.1", port="5432")

cur = conn.cursor()

#To create table when user first joins
cur.execute('''CREATE TABLE User_Data2
      (USER_ID INT PRIMARY KEY     NOT NULL,
      NAME           TEXT    NOT NULL,
      AGE            INT     NOT NULL,
      DEVICE_ID      INT     NOT NULL)
      ;''')
print("Table created successfully")


cur.execute('''CREATE TABLE HEALTH_DATA2
      (USER_ID INT PRIMARY KEY     NOT NULL,
      HR             INT           NOT NULL,
      BLOOD_OXYGEN_LEVEL    REAL   NOT NULL,
      TEMPERATURE     INT          NOT NULL,
      BP_SYSTOLIC    INT           NOT NULL,
      BP_DIASTOLIC    INT          NOT NULL,
      DATE_TIME        CHAR(50))
      ;''')
print("Table created successfully")

conn.commit()
conn.close()