import os, random
import sqlite3   #MySQLdb

nameMaleList = [ capitalLetter + smallLeters for line in open( os.path.join( '..', 'names.txt' ), "r" ).readlines() if len( str.split( line ) ) == 4 for capitalLetter in str.split( str.split( line )[ 1 ], '/' )[ 0 ][ 0 ]  for smallLeters in  map( str.lower, [ str.split( str.split( line )[ 1 ], '/' )[ 0 ][ 1 : ]  ] )  ]

nameFemaleList = [ capitalLetter + smallLeters for line in open( os.path.join( '..', 'names.txt' ), "r" ).readlines() if len( str.split( line ) ) == 4 for capitalLetter in str.split( str.split( line )[ 3 ], '/' )[ 0 ][ 0 ]  for smallLeters in  map( str.lower, [ str.split( str.split( line )[ 3 ], '/' )[ 0 ][ 1 : ]  ] )  ]

surNameList = [ str.split( line )[ 1 ] for line in open( os.path.join( '..', 'surnames.txt' ), "r" ).readlines() if ',' in str.split( line )[ 2 ] ]

######################################################################################

myDataBase = 'myFirstDataBase.sqlite'

myFolder = '.'
myFiles = os.listdir( myFolder )

if myDataBase in myFiles :
    answer = str.lower( input( 3 * '\n' + 'DataBase: "' + myDataBase + '" exists. Delete? (Y/n) \n') )
    if answer == '' :
        answer = 'y'
    if str.lower( answer[ 0 ] ) == 'y' :
        os.remove( myDataBase )

######################################################################################

connection = sqlite3.connect( myDataBase )
cursor = connection.cursor()

sql = "CREATE TABLE IF NOT EXISTS families ( id INTEGER PRIMARY KEY AUTOINCREMENT, husbandName TEXT, wifeName TEXT, surname TEXT, childrenNumber INTEGER )"
cursor.execute( sql )

for i in range( 200 ) :
    myNumber = random.randint( 0, 99 )
    husbandName = nameMaleList[ myNumber ]
    myNumber = random.randint( 0, 99 )
    wifeName = nameFemaleList[ myNumber ]
    myNumber = random.randint( 0, 99 )
    surName = surNameList[ myNumber ]
    myNumber = random.randint( 0, 4 )
    sql = "%s ( '%s', '%s', '%s', '%1d' )" % ( 'INSERT INTO families ( husbandName, wifeName, surname, childrenNumber ) VALUES', husbandName, wifeName, surName, myNumber )
    print( sql )
    cursor.execute( sql )

connection.commit()
connection.close()


