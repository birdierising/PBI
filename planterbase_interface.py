#!/usr/bin/python3

import argparse, pprint, sys
import mysql.connector as msc
from mysql.connector import errorcode

indoorconnection = msc.connect(option_files='/etc/mysql/conf.d/pbcli.cnf')

indoorcursor = indoorconnection.cursor()

def defaultsearch ( defaulttosearch ):
    defaulttosearch = sys.argv[1]

    defaultquery = f"SELECT plantid,common_name,location,notes FROM plants WHERE common_name like '%{defaulttosearch}%';"
    indoorcursor.execute(defaultquery)
    data = indoorcursor.fetchall()
    if data != None:
        pprint.pprint(data)
    else:
        print("No such plant in this collection yet")

def namesearch ( nametosearch ):
    nametosearch = sys.argv[2]

    namequery = f"SELECT common_name FROM plants WHERE common_name like '%{nametosearch}%';"
    indoorcursor.execute(namequery)
    data = indoorcursor.fetchall()
    if data != None:
        pprint.pprint(data)
    else:
        print("No such plant in this collection yet")

def idsearch ( idtosearch ):
    idtosearch = sys.argv[2]

    idquery = f"SELECT plantid,common_name FROM plants WHERE plantid='{idtosearch}';"
    indoorcursor.execute(idquery)
    data = indoorcursor.fetchall()
    if data != None:
        pprint.pprint(data)
    else:
        print("No such plant in this collection yet")

def latinnamesearch ( latinnametosearch ):
    latinnametosearch = sys.argv[2]

    latinnamequery = f"SELECT common_name,latin_name FROM plants WHERE latin_name like '%{latinnametosearch}%';"
    indoorcursor.execute(latinnamequery)
    data = indoorcursor.fetchall()
    if data != None:
        pprint.pprint(data)
    else:
        print("No such plant in this collection yet")

def vendorsearch ( vendortosearch ):
    vendortosearch = sys.argv[2]

    vendorquery = f"SELECT common_name,vendor FROM plants WHERE vendor like '%{vendortosearch}%';"
    indoorcursor.execute(vendorquery)
    data = indoorcursor.fetchall()
    if data != None:
        pprint.pprint(data)
    else:
        print("No such plant in this collection yet")

def planttypesearch ( planttypetosearch ):
    planttypetosearch = sys.argv[2]

    planttypequery = f"SELECT common_name,plant_group FROM plants WHERE plant_group like '%{planttypetosearch}%';"
    indoorcursor.execute(planttypequery)
    data = indoorcursor.fetchall()
    if data != None:
        pprint.pprint(data)
    else:
        print("No such plant in this collection yet")

def extrainfodump ( extrainfotosearch ):
    extrainfotosearch = sys.argv[2]

    extrainfoquery = f"SELECT * FROM plants WHERE common_name like '%{extrainfotosearch}%';"
    indoorcursor.execute(extrainfoquery)
    data = indoorcursor.fetchall()
    if data != None:
        pprint.pprint(data)
    else:
        print("No such plant in this collection yet")

def flowersearch ( flowertosearch ):
    flowertosearch = sys.argv[2]

    flowerquery = f"SELECT common_name FROM plants WHERE flowering='{flowertosearch}';"
    indoorcursor.execute(flowerquery)
    data = indoorcursor.fetchall()
    if data != None:
        pprint.pprint(data)
    else:
        print("No such plant in this collection yet")

def locationsearch ( locationtosearch ):
    locationtosearch = sys.argv[2]

    locationquery = f"SELECT common_name,location FROM plants WHERE location like '%{locationtosearch}%';"
    indoorcursor.execute(locationquery)
    data = indoorcursor.fetchall()
    if data != None:
        pprint.pprint(data)
    else:
        print("No such plant in this collection yet")

def notessearch ( notestosearch ):
    notestosearch = sys.argv[2]

    notesquery = f"SELECT common_name,notes FROM plants WHERE notes like '%{notestosearch}%';"
    indoorcursor.execute(notesquery)
    data = indoorcursor.fetchall()
    if data != None:
        pprint.pprint(data)
    else:
        print("No such plant in this collection yet")

def sunlightsearch ( sunlighttosearch ):
    sunlighttosearch = sys.argv[2]

    sunlightquery = f"SELECT common_name,sunlight FROM plants WHERE sunlight like '%{sunlighttosearch}%';"
    indoorcursor.execute(sunlightquery)
    data = indoorcursor.fetchall()
    if data != None:
        pprint.pprint(data)
    else:
        print("No such plant in this collection yet")

parser = argparse.ArgumentParser()
parser.add_argument("default",nargs='?',type=defaultsearch)
parser.add_argument('-b', type=latinnamesearch,action='store')
parser.add_argument('-c', type=namesearch,action='store')
parser.add_argument('-d', action='store')
parser.add_argument('-e', type=extrainfodump,action='store')
parser.add_argument('-f', type=flowersearch,action='store')
parser.add_argument('-i', type=idsearch,action='store')
parser.add_argument('-l', type=locationsearch,action='store')
parser.add_argument('-n', type=notessearch,action='store')
parser.add_argument('-s', type=sunlightsearch,action='store')
parser.add_argument('-t', type=planttypesearch,action='store')
parser.add_argument('-v', type=vendorsearch,action='store')

args = parser.parse_args()

#generalquery = "select * from plants"
#indoorcursor.execute(generalquery)
#
#indoordata = indoorcursor.fetchall()
#indoorrecords = indoorcursor.rowcount

#print("Total number of indoor plant records: ",indoorrecords)
#
#for row in indoordata:
#    print(row[1])
