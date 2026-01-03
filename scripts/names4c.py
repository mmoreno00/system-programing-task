import sqlite3

connection = sqlite3.connect( 'myThirdDataBase.sqlite' )
cursor = connection.cursor()

cursor.execute( "SELECT children.name, families.surname, children.date FROM families, children WHERE families.id = children.familyID AND children.sex = 0 ORDER BY children.date DESC" )
data = cursor.fetchall()
# print( data )

for myData in data :
   print( " %-15s %-15s %-15s" % myData )

print( '\n' + 80 * '=' + '\n' )
cursor.execute( "SELECT children.name, families.surname, children.date FROM families, children WHERE families.id = children.familyID AND children.sex = 1 ORDER BY children.date DESC" )
data = cursor.fetchall()
# print( data )

for myData in data :
   print( " %-15s %-15s %-15s" % myData )

connection.close()


