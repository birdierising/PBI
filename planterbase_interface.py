#!/usr/bin/python3

import argparse, datetime, pprint, sys
import mysql.connector as msc
from mysql.connector import errorcode

indoorconnection = msc.connect(option_files='/etc/mysql/conf.d/pbcli.cnf')

indoorcursor = indoorconnection.cursor()

def defaultsearch ( defaulttosearch ):
    defaulttosearch = sys.argv[1]

    defaultquery = f"SELECT plantid,common_name,location,notes FROM plants WHERE common_name like '%{defaulttosearch}%';"
    indoorcursor.execute(defaultquery)
    data = indoorcursor.fetchall()
    if not data:  
        print("No such plant in this collection yet")
    else:
        pprint.pprint(data)

def extrasdump ( extrastosearch ):
    extrastosearch = sys.argv[2]

    extrasquery = f"SELECT * FROM plants WHERE common_name like '%{extrastosearch}%';"
    indoorcursor.execute(extrasquery)
    data = indoorcursor.fetchall()
    if not data:  
        print("No such plant in this collection yet")
    else:
        pprint.pprint(data)

def flowersearch ( flowertosearch ):
    flowertosearch = sys.argv[2]

    flowerquery = f"SELECT common_name FROM plants WHERE flowering='{flowertosearch}';"
    indoorcursor.execute(flowerquery)
    data = indoorcursor.fetchall()
    if not data:  
        print("No such plant in this collection yet")
    else:
        pprint.pprint(data)

def idsearch ( idtosearch ):
    idtosearch = sys.argv[2]

    idquery = f"SELECT plantid,common_name FROM plants WHERE plantid='{idtosearch}';"
    indoorcursor.execute(idquery)
    data = indoorcursor.fetchall()
    if not data:  
        print("No such plant in this collection yet")
    else:
        pprint.pprint(data)

def latinnamesearch ( latinnametosearch ):
    latinnametosearch = sys.argv[2]

    latinnamequery = f"SELECT common_name,latin_name FROM plants WHERE latin_name like '%{latinnametosearch}%';"
    indoorcursor.execute(latinnamequery)
    data = indoorcursor.fetchall()
    if not data:  
        print("No such plant in this collection yet")
    else:
        pprint.pprint(data)

def locationsearch ( locationtosearch ):
    locationtosearch = sys.argv[2]

    locationquery = f"SELECT common_name,location FROM plants WHERE location like '%{locationtosearch}%';"
    indoorcursor.execute(locationquery)
    data = indoorcursor.fetchall()
    if not data:  
        print("No such plant in that location yet")
    else:
        pprint.pprint(data)

def commonnamesearch ( commonnametosearch ):
    commonnametosearch = sys.argv[2]

    commonnamequery = f"SELECT common_name FROM plants WHERE common_name like '%{commonnametosearch}%';"
    indoorcursor.execute(commonnamequery)
    data = indoorcursor.fetchall()
    if not data:  
        print("No such plant in this collection yet")
    else:
        pprint.pprint(data)

def datesearch ( datetosearch ):
    datetosearch = sys.argv[2]

    datequery = f"SELECT common_name,date_acquired FROM plants WHERE date_acquired like '%{datetosearch}%';"
    indoorcursor.execute(datequery)
    data = indoorcursor.fetchall()
    if not data:  
        print("No plant acquired on this date!")
    else:
        for (common_name, date_acquired) in data:
            print("{}: {:%b %d %Y}".format(
                common_name, date_acquired))

def notessearch ( notestosearch ):
    notestosearch = sys.argv[2]

    notesquery = f"SELECT common_name,notes FROM plants WHERE notes like '%{notestosearch}%';"
    indoorcursor.execute(notesquery)
    data = indoorcursor.fetchall()
    if not data:  
        print("No such plant with that note in this collection yet")
    else:
        pprint.pprint(data)

def plantgroupsearch ( plantgrouptosearch ):
    plantgrouptosearch = sys.argv[2]

    plantgroupquery = f"SELECT common_name FROM plants WHERE plant_group like '%{plantgrouptosearch}%';"
    indoorcursor.execute(plantgroupquery)
    data = indoorcursor.fetchall()
    if not data:  
        print("No such group in this collection yet")
    else:
        pprint.pprint(data)

def sunlightsearch ( sunlighttosearch ):
    sunlighttosearch = sys.argv[2]

    sunlightquery = f"SELECT common_name,sunlight FROM plants WHERE sunlight like '%{sunlighttosearch}%';"
    indoorcursor.execute(sunlightquery)
    data = indoorcursor.fetchall()
    if not data:  
        print("No such plant with those sunlight requirements in this collection yet")
    else:
        pprint.pprint(data)

def vendorsearch ( vendortosearch ):
    vendortosearch = sys.argv[2]

    vendorquery = f"SELECT common_name,vendor FROM plants WHERE vendor like '%{vendortosearch}%';"
    indoorcursor.execute(vendorquery)
    data = indoorcursor.fetchall()
    if not data:  
        print("No such plant from that vendor yet")
    else:
        pprint.pprint(data)

parser = argparse.ArgumentParser()
parser.add_argument("default",nargs='?',type=defaultsearch)
parser.add_argument('-b','--binomial','--latinname', type=latinnamesearch,action='store')
parser.add_argument('-c','--common-name', type=commonnamesearch,action='store')
parser.add_argument('-d', '--date', type=datesearch,action='store')
parser.add_argument('-e', '--extras', type=extrasdump,action='store')
parser.add_argument('-f', '--flowering', type=flowersearch,action='store')
parser.add_argument('-g', '--group', type=plantgroupsearch,action='store')
parser.add_argument('-i', '--id', type=idsearch,action='store')
parser.add_argument('-l', '--location', type=locationsearch,action='store')
parser.add_argument('-n', '--notes', type=notessearch,action='store')
parser.add_argument('-s', '--sunreqs', type=sunlightsearch,action='store')
parser.add_argument('-v', '--vendor', type=vendorsearch,action='store')

args = parser.parse_args()
