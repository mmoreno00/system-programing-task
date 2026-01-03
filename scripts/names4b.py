import sqlite3

connection = sqlite3.connect( 'myThirdDataBase.sqlite' )
cursor = connection.cursor()

cursor.execute( "SELECT children.name, families.surname, children.date FROM families, children WHERE families.id = children.familyID ORDER BY children.date DESC" )
data = cursor.fetchall()
# print( data )

No = 0
for myData in data :
   No += 1
   print( "%3d: %-15s %-15s %-15s" % ( No, myData[ 0 ], myData[ 1 ], myData[ 2 ] ) )

connection.close()


