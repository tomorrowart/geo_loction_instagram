import sqlite3


def create_table(name):
    connection = sqlite3.connect(f'{name}.db')
    cursor = connection.cursor()
    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS userin
                      (userid INTEGER, username TEXT, biography TEXT, fullname TEXT, is_private TEXT, city TEXT, location INTEGER, privat INTEGER, edge_followed_by INTEGER, edge_follow INTEGER, sex TEXT, commercial TEXT, address TEXT, external_url TEXT,  business_address_json TEXT, business_category_name TEXT, business_contact_method TEXT, business_email TEXT, business_phone_number TEXT, category_enum TEXT, category_name TEXT, connected_fb_page TEXT, country_block TEXT, fbid TEXT,  guardian_id TEXT, has_ar_effects TEXT, has_blocked_viewer TEXT, has_channel TEXT, has_clips TEXT, has_guides TEXT, highlight_reel_count TEXT, is_business_account TEXT, is_embeds_disabled TEXT, is_guardian_of_viewer TEXT, is_joined_recently TEXT, is_professional_account TEXT, is_supervised_by_viewer TEXT, is_verified TEXT, overall_category_name TEXT, should_show_category TEXT, should_show_public_contacts TEXT, state_controlled_media_country TEXT, edge_owner_to_timeline_media_count INTEGER, taken_at_timestamp INTEGER)''')
        cursor.execute('''CREATE INDEX IF NOT EXISTS idx ON userin(userid)''')
    except Exception as ex:
        print(ex)
    connection.commit()
    connection.close()



def create_table_location(name):
    connection = sqlite3.connect(f'{name}.db')
    cursor = connection.cursor()
    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS locationuser
                      (userid INTEGER, locationid, name TEXT, slug)''')
        cursor.execute('''CREATE UNIQUE INDEX IF NOT EXISTS idx ON locationuser(userid)''')
    except Exception as ex:
        print(ex)
    connection.commit()
    connection.close()

def create_table_locationid(name):
    connection = sqlite3.connect(f'{name}.db')
    cursor = connection.cursor()
    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS locationid
                          (location, locationid INTEGER, location_address, location_city, location_region, location_zip, facebook_places_id, locatename, locatetype, category, name, has_menu, phone, website, lat, lng)''')
        cursor.execute('''CREATE UNIQUE INDEX IF NOT EXISTS idx ON locationid(locationid)''')
    except Exception as ex:
        print(ex)
    connection.commit()
    connection.close()

def create_table_user(name):
    connection = sqlite3.connect(f'{name}.db')
    cursor = connection.cursor()
    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS userin
                          (userid INTEGER, username, fullname, location, is_private, city, address)''')
    except Exception as ex:
        print(ex)
    connection.commit()
    connection.close()