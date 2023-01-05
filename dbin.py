import sqlite3
import time

class Database:
    def __init__(self, Database):
        self.conn = sqlite3.connect(Database, timeout=22)
        self.cursor = self.conn.cursor()
    def user(self, data):
        #userid, username, fullname, laction, privat, city, address
        try:
            with self.conn:
                self.cursor.executemany("""INSERT INTO userin VALUES (?,?,?,?,?,?,?)""",  data)
            return True
        except Exception as ex:
            print(ex)
    def location(self, location, locationid, category, name, location_address, location_city, location_region, location_zip, facebook_places_id, has_menu, phone, website, lat, lng):
        with self.conn:
            if False == (bool(len(self.cursor.execute("""SELECT * FROM locationid where locationid = ?""", (locationid,)).fetchall()))):
                self.cursor.execute("""INSERT INTO locationid (location, locationid, category, name, location_address, location_city, location_region, location_zip, facebook_places_id, has_menu, phone, website, lat, lng) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", (location, locationid, category, name, location_address, location_city, location_region, location_zip, facebook_places_id, has_menu, phone, website, lat, lng,))
                return "Основа записали новое"
            else:
                try:
                    if lat == None:
                        self.cursor.execute(
                            """UPDATE locationid SET location=?, category=?, name=?, location_address=?, location_city=?, location_region=?, location_zip=?, facebook_places_id=?, has_menu=?, phone=?, website=? WHERE locationid = ?""",
                            (location, category, name, location_address, location_city, location_region, location_zip,
                             facebook_places_id, has_menu, phone, website, locationid))
                    else:
                        self.cursor.execute(
                            """UPDATE locationid SET location=?, category=?, name=?, location_address=?, location_city=?, location_region=?, location_zip=?, facebook_places_id=?, has_menu=?, phone=?, website=?, lat=?, lng=? WHERE locationid = ?""",
                            (location, category, name, location_address, location_city, location_region,
                             location_zip, facebook_places_id, has_menu, phone, website, lat, lng, locationid))
                except Exception as ex:
                    print(ex, 'ошибка тут')

                return True
    def location_in_user(self, location, locationid, category, name, location_address, location_city, location_region, location_zip, facebook_places_id, has_menu, phone, website, lat, lng):
        with self.conn:

            if False == (bool(len(self.cursor.execute("""SELECT * FROM locationid WHERE locationid = ?""", (locationid,)).fetchall()))):
                self.cursor.execute("""INSERT INTO locationid (location, locationid, category, name, location_address, location_city, location_region, location_zip, facebook_places_id, has_menu, phone, website, lat, lng) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", (location, locationid, category, name, location_address, location_city, location_region, location_zip, facebook_places_id, has_menu, phone, website, lat, lng,))
                return 'Записали новое'
            else:
                try:
                    self.cursor.execute( """UPDATE locationid SET location=?, name=?, location_address=?, location_city=?, facebook_places_id=?, lat=?, lng=? WHERE locationid = ?""", (location, name, location_address, location_city, facebook_places_id, lat, lng, locationid))
                except Exception as ex:
                    print(ex, 'ин юзер локатион')
                return True

    def userscrape(self, userid, username, biography, external_url, business_address_json, business_category_name, business_contact_method, business_email, business_phone_number, category_enum, category_name, connected_fb_page, country_block, fbid, full_name, guardian_id, has_ar_effects, has_blocked_viewer, has_channel, has_clips, has_guides, highlight_reel_count, is_business_account, is_embeds_disabled, is_guardian_of_viewer, is_joined_recently, is_private, is_professional_account, is_supervised_by_viewer, is_verified, overall_category_name, should_show_category, should_show_public_contacts, state_controlled_media_country, edge_followed_by, edge_follow, edge_owner_to_timeline_media_count, taken_at_timestamp, city, sex):
        with self.conn:
            if False == (bool(len(self.cursor.execute("""SELECT * FROM userin where userid = ?""", (userid,)).fetchall()))):
                self.cursor.execute("""INSERT INTO userin (userid, username, biography, external_url,  business_address_json, business_category_name, business_contact_method, business_email, business_phone_number, category_enum, category_name, connected_fb_page, country_block, fbid, fullname, guardian_id, has_ar_effects, has_blocked_viewer, has_channel, has_clips, has_guides, highlight_reel_count, is_business_account, is_embeds_disabled, is_guardian_of_viewer, is_joined_recently, is_private, is_professional_account, is_supervised_by_viewer, is_verified, overall_category_name, should_show_category, business_phone_number, should_show_public_contacts, state_controlled_media_country, edge_followed_by, edge_follow, edge_owner_to_timeline_media_count, taken_at_timestamp, city, sex) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", (userid, username, biography, external_url, business_address_json, business_category_name, business_contact_method, business_email, business_phone_number, category_enum, category_name, connected_fb_page, country_block, fbid, full_name, guardian_id, has_ar_effects, has_blocked_viewer, has_channel, has_clips, has_guides, highlight_reel_count, is_business_account, is_embeds_disabled, is_guardian_of_viewer, is_joined_recently, is_private, is_professional_account, is_supervised_by_viewer, is_verified, overall_category_name, should_show_category, business_phone_number, should_show_public_contacts, state_controlled_media_country, edge_followed_by, edge_follow, edge_owner_to_timeline_media_count, taken_at_timestamp, city, sex,))
            else:

                self.cursor.execute("""UPDATE userin SET username=?, biography=?, external_url=?,  business_address_json=?, business_category_name=?, business_contact_method=?, business_email=?, business_phone_number=?, category_enum=?, category_name=?, connected_fb_page=?, country_block=?, fbid=?, fullname=?, guardian_id=?, has_ar_effects=?, has_blocked_viewer=?, has_channel=?, has_clips=?, has_guides=?, highlight_reel_count=?, is_business_account=?, is_embeds_disabled=?, is_guardian_of_viewer=?, is_joined_recently=?, is_private=?, is_professional_account=?, is_supervised_by_viewer=?, is_verified=?, overall_category_name=?, should_show_category=?, business_phone_number=?, should_show_public_contacts=?, state_controlled_media_country=?, edge_followed_by=?, edge_follow=?, edge_owner_to_timeline_media_count=?, taken_at_timestamp=?, city=? WHERE userid = ?""", (username, biography, external_url, business_address_json, business_category_name, business_contact_method, business_email, business_phone_number, category_enum, category_name, connected_fb_page, country_block, fbid, full_name, guardian_id, has_ar_effects, has_blocked_viewer, has_channel, has_clips, has_guides, highlight_reel_count, is_business_account, is_embeds_disabled, is_guardian_of_viewer, is_joined_recently, is_private, is_professional_account, is_supervised_by_viewer, is_verified, overall_category_name, should_show_category, business_phone_number, should_show_public_contacts, state_controlled_media_country, edge_followed_by, edge_follow, edge_owner_to_timeline_media_count, taken_at_timestamp, city, userid,))
                return True

    def userlocaton(self, userid, locationidslov, locationnames, locationslug):
        with self.conn:
            if False == (bool(len(self.cursor.execute("""SELECT * FROM locationuser where userid = ?""", (userid,)).fetchall()))):
                try:
                    self.cursor.execute("""INSERT INTO locationuser (userid, locationid, name, slug) VALUES (?,?,?,?)""", (userid, locationidslov, locationnames, locationslug,))
                except Exception as ex:
                    print(ex)
            else:
                self.cursor.execute("""UPDATE locationuser SET locationid=?, name=?, slug=? WHERE userid = ?""", (locationidslov, locationnames, locationslug, userid,))
                return True

    def userloctionname(self, locationidslov, locationnames, locationslug):
        with self.conn:
            if False == (bool(len(self.cursor.execute("""SELECT * FROM locationid where locationid = ?""", (locationidslov,)).fetchall()))):
                try:
                    self.cursor.execute("""INSERT INTO locationid (locationid, location, name) VALUES (?,?,?)""", (locationidslov, locationnames, locationslug,))
                except Exception as ex:
                    print(ex)
            else:
                #self.cursor.executemeany("""UPDATE userin SET (username, location, city, address) VALUES (?,?,?,?) WHERE userid = ?""", (username, laction, city, address, userid,))
                return True

    def usersex(self, userid, sex):
        with self.conn:
            a = self.cursor.execute("""SELECT * FROM userin where userid = ?""", (userid,)).fetchall()
            if True == (bool(len(a))):
                try:
                    print(userid, sex)
                    self.cursor.execute("""UPDATE userin SET sex = ? WHERE userid = ?""", (sex, userid, ))
                except Exception as ex:
                    print(ex)
    def checklocation(self, locationid):
        with self.conn:
            return self.cursor.execute("""SELECT * FROM locationid WHERE locationid = ?""", (locationid,)).fetchall()[0][2]


    def checkuser(self, username):
        with self.conn:
            av = self.cursor.execute("""SELECT edge_followed_by FROM userin WHERE username = ?""", (username,)).fetchall()[0][0]
            if av == None:
                return False
            else:
                print(f'нет в базе {username}')
                return True
    def dataset(self, sex):
        with self.conn:
            try:
                datasetsex = self.cursor.execute("""SELECT * FROM userin where sex = ?""", (sex,)).fetchall()
                if True == (bool(len(datasetsex))):
                    return datasetsex
            except Exception:
                print(Exception)

    def userAI(self):
        with self.conn:
            try:
                av = self.cursor.execute("""SELECT * FROM userin WHERE edge_followed_by != ?""", ('',)).fetchall()
                if True == (bool(len(av))):
                    return av
            except Exception:
                print(Exception, "Модуль dbin userAI")

    def singleAI(self, userid):
        with self.conn:
            try:
                if True == (bool(len(self.cursor.execute("""SELECT * FROM userin WHERE userid = ?""", (userid,)).fetchall()))):
                    return self.cursor.execute("""SELECT * FROM userin WHERE userid = ?""", (userid,)).fetchall()
            except Exception:
                print(Exception)

    def selectalldata(self,):
        with self.conn:
            return self.cursor.execute("""SELECT * FROM userin""", ()).fetchall()


    def allrow(self, ids):
        print(len(ids))
        with self.conn:
            mamba = []
            allrow = self.cursor.execute("""SELECT * FROM userin WHERE username IN (%s)""" % ','.join('?'*len(ids)), ids).fetchall()
            i = 1
            for row in allrow:
                if i % 5000 == 0:
                    print(f"Собрано 5000")
                mamba.append(row)
                i += 1
            return mamba
    def migrate(self,):
        with self.conn:
            try:
                mamba = []
                c = self.cursor.execute("""SELECT * FROM userin """).fetchall()
                if c == []:
                    return
                for i in c:
                    if i == None:
                        continue
                    mamba.append(i)
                return mamba
            except Exception as ex:
                print(ex)
            return
    def select_userid_from_userin(self,): #select_userid_from_userin
        try:
            with self.conn:
                a = self.cursor.execute("""SELECT userid FROM userin""").fetchall()
                return a
        except Exception as ex:
            print(ex)
            return
    def migratein(self,data):
        with self.conn:
                self.cursor.executemany("""INSERT INTO userin VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", data)

    def migrateinfullbase(self,data):
        with self.conn:
            self.cursor.executemany(
                """UPDATE userin SET username=?, biography=?, external_url=?,  business_address_json=?, business_category_name=?, business_contact_method=?, business_email=?, business_phone_number=?, category_enum=?, category_name=?, connected_fb_page=?, country_block=?, fbid=?, fullname=?, guardian_id=?, has_ar_effects=?, has_blocked_viewer=?, has_channel=?, has_clips=?, has_guides=?, highlight_reel_count=?, is_business_account=?, is_embeds_disabled=?, is_guardian_of_viewer=?, is_joined_recently=?, is_private=?, is_professional_account=?, is_supervised_by_viewer=?, is_verified=?, overall_category_name=?, should_show_category=?, should_show_public_contacts=?, state_controlled_media_country=?, edge_followed_by=?, edge_follow=?, edge_owner_to_timeline_media_count=? WHERE userid = ?""", data)

    def migratelocation(self,data):
        with self.conn:
                self.cursor.executemany("""INSERT OR IGNORE INTO locationid VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", data)

    def migrate_all_(self, x, z):
        with self.conn:
            b = f'SELECT * FROM locationid LIMIT {x}, {z}'
            a = self.cursor.execute(b).fetchall()
            return a

    def migratelocationuser(self,data):
            with self.conn:
                self.cursor.executemany("""INSERT INTO locationuser VALUES(?, ?, ?, ?)""", data)

    def migrate_all_locationuser(self, ):
        with self.conn:
            a = self.cursor.execute("""SELECT * FROM locationuser""").fetchall()
            return a

    def migratein_cityuser(self,data):
        with self.conn:
            self.cursor.executemany("""INSERT INTO userin VALUES(?, ?, ?, ?, ?, ?, ?)""", data)

    def usermigrate(self, data, start_time):
        with self.conn:
            s = 0
            for i in data:
                if s % 50 == 0:
                    print(f"Начал парсить базу  {100 / len(data) * s} %")
                    print(time.time() - start_time)
                s += 1
                if False == (bool(len(self.cursor.execute("""SELECT * FROM userin WHERE userid = ?""", (i[0],)).fetchall()))):
                    self.cursor.execute("""INSERT INTO userin (userid, username, fullname, location, is_private, city, address) VALUES (?,?,?,?,?,?,?)""",
                        (i[0], i[1], i[2], i[3], i[4], i[5], i[6],))
                else:
                    self.cursor.execute("""UPDATE userin SET username=?, fullname=?, location=?, is_private=?, city=?, address=? WHERE userid = ?""",
                                        ( i[1], i[2], i[3], i[4], i[5], i[6], i[0] ,))


    def user_copydb_check(self, userid):
        with self.conn:
            if False == (bool(len(self.cursor.execute("""SELECT * FROM userin where userid = ?""", (userid,)).fetchall()))):
                return False
            else:
                return True
    def user_copydb_insert(self, data):
        with self.conn:
            self.cursor.executemany("""INSERT INTO userin VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", data)

    def select_locationid_indb(self, locationid):
        with self.conn:
            a = self.cursor.execute("""SELECT * FROM locationid WHERE locationid = ?""", (locationid,)).fetchall()
            return a
    def update_locationid_indb(self,location, locationid, location_address, location_city, location_region, location_zip, facebook_places_id, locatename, locatetype, category, name):
        with self.conn:
            self.cursor.execute("""UPDATE locationid SET location=?, location_address=?, location_city=?, location_region=?, location_zip=?, facebook_places_id=?, locatename=?, locatetype=?, category=?, name=? WHERE locationid = ?""",
                (location, location_address, location_city, location_region, location_zip, facebook_places_id, locatename, locatetype, category, name, locationid,))

    def uddate_join_location(self, data):
        with self.conn:
            self.cursor.execute(
                """UPDATE locationid a JOIN data=? b ON a.locationid = b[1] SET a.location = b[0], location_address = b[2], location_city = b[3], location_region=b[4], location_zip=b[5], facebook_places_id=b[6], locatename=b[7], locatetype=b[8], category=b[9], name=b[10]""", data)
    def testdelete_location(self, locationid):
        with self.conn:
            self.cursor.execute("""DELETE FROM locationid WHERE locationid IN (%s)""" % ','.join('?'*len(locationid)), locationid)
    def copy_user(self, data):
        with self.conn:
            self.cursor.executemany("""INSERT INTO userin VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", data)

    def testdelete_user(self, userid):
        with self.conn:
            self.cursor.execute("""DELETE FROM userin WHERE userid IN (%s)""" % ','.join('?'*len(userid)), userid)
    def import_user_update(self, ids):
        with self.conn:
            mamba = []
            for row in self.cursor.execute("""SELECT * FROM userin WHERE userid IN (%s)""" % ','.join('?' * len(ids)),ids):
                mamba.append(row)
            print(f"Собрано для обновления {len(mamba)}")
            return mamba
    def select_locationid_indb__(self):
        with self.conn:
            a = self.cursor.execute("""SELECT * FROM locationid""").fetchall()
            #сделать проверку на вхождение
            return a
    def upadate_location_city(self, locationid, city):
        with self.conn:
            self.cursor.execute("""UPDATE locationid SET location_city = ? WHERE locationid = ?""", (city, locationid,))

    def all_location_user(self, data):
        with self.conn:
            mamba = []
            #try:
            base = self.cursor.execute("""SELECT * FROM locationuser WHERE userid IN (%s)""" % ','.join('?' * len(data)), data)
            for row in base:
                mamba.append(row)
            # except Exception as ex:
            #     print(ex)

            return mamba
#Достать username колонку логинов из таблицы
    def import_user_login(self,):
        with self.conn:
            a = self.cursor.execute("""SELECT username FROM userin""").fetchall()
            return a

    def user_updatetest(self, data):
        with self.conn:
            self.cursor.executemany("""UPDATE userin SET username=?, biography=?, fullname=?, is_private=?, edge_followed_by=?, edge_follow=?,
                    external_url=?, business_address_json=?, business_category_name=?, business_contact_method=?, business_email=?,
                    business_phone_number=?, category_enum=?, category_name=?, connected_fb_page=?, country_block=?,
                    fbid=?, guardian_id=?, has_ar_effects=?, has_blocked_viewer=?, has_channel=?,
                    has_clips=?, has_guides=?, highlight_reel_count=?, is_business_account=?, is_embeds_disabled=?,
                    is_guardian_of_viewer=?, is_joined_recently=?, is_professional_account=?,
                    is_supervised_by_viewer=?, is_verified=?, overall_category_name=?, should_show_category=?,
                    should_show_public_contacts=?, state_controlled_media_country=?,
                    edge_owner_to_timeline_media_count=?, taken_at_timestamp=? WHERE userid = ? """, data)
            return True

    # def user_updatetest(self, data):
    #     with self.conn:
    #         self.cursor.executemany("""UPDATE userin SET username=%s, biography=%s, fullname=%s, is_private=%s, edge_followed_by=%s, edge_follow=%s,
    #                 external_url=%s, business_address_json=%s, business_category_name=%s, business_contact_method=%s, business_email=%s,
    #                 business_phone_number=%s, category_enum=%s, category_name=%s, connected_fb_page=%s, country_block=%s,
    #                 fbid=%s, guardian_id=%s, has_ar_effects=%s, has_blocked_viewer=%s, has_channel=%s,
    #                 has_clips=%s, has_guides=%s, highlight_reel_count=%s, is_business_account=%s, is_embeds_disabled=%s,
    #                 is_guardian_of_viewer=%s, is_joined_recently=%s, is_professional_account=%s,
    #                 is_supervised_by_viewer=%s, is_verified=%s, overall_category_name=%s, should_show_category=%s,
    #                 should_show_public_contacts=%s, state_controlled_media_country=%s,
    #                 edge_owner_to_timeline_media_count=%s, taken_at_timestamp=%s WHERE userid=%s """, data)
    #         return True

    # def user_updatetest(self, data):
    #     with self.conn:
    #         self.cursor.executemany("""UPDATE userin SET username, biography, fullname, is_private, edge_followed_by, edge_follow,
    #                 external_url, business_address_json, business_category_name, business_contact_method, business_email,
    #                 business_phone_number, category_enum, category_name, connected_fb_page, country_block,
    #                 fbid, guardian_id, has_ar_effects, has_blocked_viewer, has_channel,
    #                 has_clips, has_guides, highlight_reel_count, is_business_account, is_embeds_disabled,
    #                 is_guardian_of_viewer, is_joined_recently, is_professional_account,
    #                 is_supervised_by_viewer, is_verified, overall_category_name, should_show_category,
    #                 should_show_public_contacts, state_controlled_media_country,
    #                 edge_owner_to_timeline_media_count, taken_at_timestamp, WHERE userid IN (%s)""" % ','.join('?'*len(data)), data)
    #         return True
    def select_locationuser_locationid(self, ):
        with self.conn:
            a = self.cursor.execute("""SELECT locationid FROM locationuser""").fetchall()
            return a

    def update_location_userin(self, userid, location):
        with self.conn:
            self.cursor.execute("""UPDATE userin SET location = ? WHERE userid = ?""", (location, userid,))
    def select_vse_from_userin_where_location(self, ids):
        with self.conn:
            mamba = []
            allrow = self.cursor.execute("""SELECT * FROM userin WHERE location = ?""", (ids,)).fetchall()
            i = 1
            for row in allrow:
                if i % 5000 == 0:
                    print(f"Собрано 5000")
                mamba.append(row)
                i += 1
            return mamba
    def delete_from_locationuser_where_userid(self, userid):
        with self.conn:
            self.cursor.execute("""DELETE FROM locationuser WHERE userid IN (%s)""" % ','.join('?'*len(userid)), userid)
    def select_from_locationid_where_locationid_in(self, ids):
        with self.conn:
            mamba = []
            for row in self.cursor.execute("""SELECT * FROM locationid WHERE locationid IN (%s)""" % ','.join('?' * len(ids)),ids):
                mamba.append(row)
            print(f"Собрано для обновления {len(mamba)}")
            return mamba
    def delete_from_locationid_where_locationid(self, locationid):
        with self.conn:
            self.cursor.execute("""DELETE FROM locationid WHERE locationid IN (%s)""" % ','.join('?'*len(locationid)), locationid)
    def delete_from_locationuser_where_userid_solo(self, userid):
        with self.conn:
            self.cursor.execute("""DELETE FROM locationuser WHERE userid= ?""", (userid,))
    def select_userid_from_locationuser(self, ):
        with self.conn:
            a = self.cursor.execute("""SELECT userid FROM locationuser""").fetchall()
            return a
    def select_username_from_userin(self,):
        try:
            with self.conn:
                a = self.cursor.execute("""SELECT username FROM userin""").fetchall()
                return a
        except Exception as ex:
            print(ex)
            return
    def select_locationid_from_locationid_where_location(self, ids):
        with self.conn:
            mamba = []
            allrow = self.cursor.execute("""SELECT locationid FROM locationid WHERE locatename = ?""", (ids,)).fetchall()
            i = 1
            for row in allrow:
                if i % 5000 == 0:
                    print(f"Собрано 5000")
                mamba.append(row)
                i += 1
            return mamba
    def select_all_from_locationid_where_locatename(self, locatename):
        with self.conn:
            a = self.cursor.execute("""SELECT * FROM locationid WHERE locatename = ?""", (locatename,)).fetchall()
            return a

    def select_username_from_userin_where_city(self, country):
        try:
            with self.conn:
                a = self.cursor.execute("""SELECT username FROM userin  = ?""", (country,)).fetchall()
                return a
        except Exception as ex:
            print(ex)
            return
    def select_locationid_from_locationid(self,):
        with self.conn:
            mamba = []
            allrow = self.cursor.execute("""SELECT locationid FROM locationid """).fetchall()
            for row in allrow:
                mamba.append(int(row[0]))
        return mamba
    def select_limit_from_userin(self,):
        with self.conn:
            mamba = []
            a = self.cursor.execute("""SELECT userid FROM userin LIMIT 0, 100000000""").fetchall()
            for row in a:
                mamba.append(row)
            return mamba

    def delete_from_userin_where_userid_in(self, locationid):
        with self.conn:
            self.cursor.execute("""DELETE FROM userin WHERE userid IN (%s)""" % ','.join('?' * len(locationid)),
                                locationid)
    def delete_from_userin_where_rowid_not_in(self,):
        with self.conn:
            self.cursor.execute("""DELEFT FROM userin WHERE ROWID NOT IN(SELECT ROWID FROM userin GROUP BY userid)""")
    def select_all_from_user_in_where_userid(self, ids):

        with self.conn:
            mamba = []
            allrow = self.cursor.execute("""SELECT * FROM userin WHERE userid IN (%s) """ % ','.join('?'*len(ids)), ids).fetchall()
            i = 1
            for row in allrow:
                if i % 5000 == 0:
                    print(f"Собрано 5000")
                mamba.append(row)
                i += 1
            return mamba
    def insert_into_userin_values_cityuser(self, data):
        with self.conn:
            self.cursor.execute("""INSERT INTO userin VALUES (?,?,?,?,?,?,?)""",  data)
            return True
    def select_all_from_userin_limit(self, isss):
        with self.conn:
            try:
                mamba = []
                x = isss * 10000000
                clu = f'SELECT * FROM userin LIMIT {x}, 10000000'
                print(clu)
                c = self.cursor.execute(clu).fetchall()
                print(len(c))
                if len(c) == 0:
                    return ''
                for i in c:
                    if i == None:
                        continue
                    mamba.append(i)
                return mamba
            except Exception as ex:
                print(ex)
            return
    def delete_from_licationid_where_locationid_none(self, id):
        with self.conn:
            a = self.cursor.execute("""DELETE FROM locationid WHERE locationid = ?""", (id,))
        return a