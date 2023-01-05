from geopy.geocoders import Nominatim
from creatdb import create_table_locationid
from dbin import Database
import os

def set_proxy():
    with open("proxy.txt", 'r') as f:
        ff_proxy = f.readlines()[0]
    print(ff_proxy)
    proxy_addr = ff_proxy
    os.environ['http_proxy'] = proxy_addr
    os.environ['https_proxy'] = proxy_addr
def unset_proxy():
    os.environ.pop('http_proxy')
    os.environ.pop('https_proxy')
set_proxy()
def get_loc_in_locsity(geolocator, name):
    try:
        location = geolocator.geocode(f"{name}", language='en')
    except:
        return False
    return location
def pars_resul(location, i, new_database, ch):
    try:
        country = location.address.split(",")[-1].lstrip()
    except:
        return
    try:
        postcode = location.address.split(",")[-2].lstrip()
    except:
        postcode = None
    try:
        state = location.address.split(",")[-3].lstrip()
    except:
        state = None
    try:
        city = location.address.split(",")[-4].lstrip()
    except:
        city = None
    try:
        string_adress = ''
        for ii in location.address.split(",")[:-4]:
            string_adress = string_adress + f'{ii.lstrip()}, '
    except Exception as ex:
        print(ex)
        string_adress = None

    set_city(i, new_database, country, postcode, state, city, string_adress)
    if ch % 20 == 0:
        create_database(new_database)
        new_database = []
        return new_database
    return

def  export_base_local():
    create_table_locationid(f"database\\TestGeo_update")
    #Извлекаем из бд все значения
    data_database = Database('database\\data.db')
    datagood = Database('database\\TestGeo_update.db').select_locationid_from_locationid()
    for i in datagood:
        data_database.delete_from_licationid_where_locationid_none(int(i))
    ch = 0
    new_database = []
    for i in range(100):
        z = 50000
        x = i * z
        database = Database('database\\data.db').migrate_all_(x, z)
        print(len(database))
        for i in database:
            if ch % 1000 == 0:
                print(ch)
                ch += 1
            ch += 1
            geolocator = Nominatim(user_agent="mys-s2adsdasdr", timeout=5)
            #location = geolocator.reverse(f"{84.9283209295}, {-48.515625}", language='en')
            #location = geolocator.geocode(f"Van Chang, Ha Nam Ninh, Vietnam", language='en')
            if i[-1] == None or i[-1] or 'e' in str(i[-1]) or 'e' in str(i[-2]) == 0:
                if i[3] == "":
                    if i[2] == "":
                        if [1] == "":
                            continue
                        else:
                            location = get_loc_in_locsity(geolocator, i[0])  # получаем дату по названию места
                            pars_resul(location, i, new_database, ch)

                    else:
                        location = get_loc_in_locsity(geolocator, i[2]) #получаем дату по адресу
                        pars_resul(location, i, new_database, ch)
                        continue
                else:
                    location = get_loc_in_locsity(geolocator, i[3]) #получаем дату по городу
                    pars_resul(location, i, new_database, ch)
                    continue

            else:
                try:
                    location = geolocator.reverse(f"{i[-2]}, {i[-1]}", language='en')
                    pars_resul(location, i, new_database, ch)
                except Exception as ex:
                    print(f"{i[-2]}, {i[-1]}", ex, i)
                    continue
            if location is None:
                if i[3] == "":
                    if i[2] == "":
                        if [1] == "":
                            continue
                        else:
                            location = get_loc_in_locsity(geolocator, i[0])  # получаем дату по названию места
                            pars_resul(location, i, new_database, ch)

                    else:
                        location = get_loc_in_locsity(geolocator, i[2])  # получаем дату по адресу
                        pars_resul(location, i, new_database, ch)
                        continue
                else:
                    location = get_loc_in_locsity(geolocator, i[3])  # получаем дату по городу
                    pars_resul(location, i, new_database, ch)
                    continue
            data_database.delete_from_licationid_where_locationid_none(int(i[1]))
            print(i[1])


def create_database(new_database):
    database = Database('database\\TestGeo_update.db')
    database.migratelocation(new_database)
def set_city(a, new_database, country, postcode, state, city, string_adress):
    if a[3] == None and state != None:
        s3 = state
    else:
        s3 = a[3]
    if a[5] == None and postcode != None:
        s5 = postcode
    else:
        s5 = a[5]
    if a[2] == None or a[2] == '' and string_adress != None:
        s2 = string_adress
    else:
        s2 = a[2]
    return new_database.append((a[0], a[1], s2, s3, a[4], s5, a[6], country, city, a[9], a[10], a[11], a[12], a[13], a[14], a[15]))

export_base_local()