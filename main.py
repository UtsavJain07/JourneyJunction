import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Utsav#Jain07',database='railwaydb')

cur=mydb.cursor()
print(mydb.connection_id)

source=input("Enter Source: ")
destination=input("Enter destination: ")

# extract data from table
s='SELECT * FROM train_details'
s2='''
SELECT a.train_no,a.train_name,b.station_name,a.station_name,(a.distance-b.distance) AS total_distance, 
(a.distance-b.distance)*1.5 AS fare,
TIMEDIFF(STR_TO_DATE(a.arrival_time, '%H:%i'), STR_TO_DATE(b.departure_time, '%H:%i')) AS time_taken
FROM train_details AS a 
JOIN train_details AS b
ON a.train_no=b.train_no
WHERE b.station_name=%s AND a.station_name=%s AND (a.distance-b.distance)>0; 
'''

header=['Train_no','Train_Name','Source Station Name','Destination Station Name','Total Distance', 
'Fare','Time_Taken']
data=(source,destination)
cur.execute(s2,data)
result=cur.fetchall()
# c=1
# for row in result:
#     print(f"\n*****Result {c}*****\n")
#     for index,details in enumerate(row):
#         print(f"{header[index]} : {details}")
#         # if(header[index]=='Time_Taken'):
#         #     if(int(details)<0):
#         #         details=240000-int(details)
#     c+=1

for r in result:
    print(r)
    



# total_distance=0
# time=0

