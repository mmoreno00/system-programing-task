import sqlite3, sys

connection = sqlite3.connect( 'mySecondDataBase.sqlite' )
cursor = connection.cursor()

cursor.execute( "SELECT children.name, families.surname, families.husbandName, families.wifeName FROM families, children WHERE families.id = children.familyID ORDER BY families.surname" )

data = cursor.fetchall()

connection.close()

print( data )

for myRecord in data :
   print( " %-15s  %-15s %-15s %-15s" % myRecord )

myOutputFile = str.split( sys.argv[ 0 ], '.' )[ 0 ] + '.txt'
out = open( myOutputFile, "w" )

print( data, file = out )
for myRecord in data :
   print( " %-15s  %-15s %-15s %-15s" % myRecord, file = out )
out.close( )
