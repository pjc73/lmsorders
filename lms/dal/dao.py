__author__ = 'paul'

import os
import logging
import lms.dal.dao
import MySQLdb

from google.appengine.api import rdbms
from google.appengine.api import rdbms_mysqldb

CLOUDSQL_INSTANCE = 'lmsordersbeta:ordersdb'
DATABASE_NAME = 'lms_orders'
USER_NAME = 'root'
PASSWORD_CLOUD = 'secret01'
PASSWORD_LOCAL = ''


def get_connection():

    if (os.getenv('SERVER_SOFTWARE') and
        os.getenv('SERVER_SOFTWARE').startswith('Google App Engine/')):
        return MySQLdb.connect(unix_socket='/cloudsql/' + CLOUDSQL_INSTANCE, db=DATABASE_NAME, user='root')
        #return MySQLdb.connect(instance=CLOUDSQL_INSTANCE, db=DATABASE_NAME, user='root', passwd=PASSWORD_CLOUD)
    else:
        #rdbms_mysqldb.SetConnectKwargs(host='localhost', port=3306, user=USER_NAME, passwd=PASSWORD_LOCAL)
        #return rdbms.connect(instance=CLOUDSQL_INSTANCE, db=DATABASE_NAME)
        return MySQLdb.connect(host='localhost', port=3306, user=USER_NAME, passwd=PASSWORD_LOCAL, db=DATABASE_NAME)


            #db = MySQLdb.connect(host='127.0.0.1', port=3306, user='root')
            # Alternately, connect to a Google Cloud SQL instance using:
            # db = MySQLdb.connect(host='ip-address-of-google-cloud-sql-instance', port=3306, user='root')


    #cloudconfig
    #return rdbms.connect(instance=CLOUDSQL_INSTANCE, database=DATABASE_NAME,
    #    user=USER_NAME, password=PASSWORD_CLOUD)

    #local config


class Dao:
    def get_all_ids(self,pk_def,table_def):
        conn = get_connection()
        cursor = conn.cursor()
        select_sql = "SELECT " + pk_def +" FROM " + table_def
        cursor.execute(select_sql)
        rows = cursor.fetchall()
        conn.close()
        return rows

    def count_all(self,table_def):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM " + table_def)
        count = cursor.fetchone()[0]
        return count

    def get_rows_from_ids(self,ids,select_sql):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('CREATE TEMPORARY TABLE id_table (fk_id INT)')
        cursor.executemany('INSERT INTO id_table (fk_id) VALUES (%s)',ids)
        cursor.execute(select_sql)
        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_rows_from_ids2(self,ids,table_def, pk_def , field_defs):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('CREATE TEMPORARY TABLE id_table (fk_id INT)')
        cursor.executemany('INSERT INTO id_table (fk_id) VALUES (%s)',ids)

        a = 'SELECT address_id, line_1,line_2,line_3,city,region,fk_country FROM lms_orders.Address INNER JOIN id_table ON id_table.fk_id = lms_orders.Address.address_id'

        select_sql = 'SELECT ' + pk_def +' ,'

        for d in field_defs:
            select_sql = select_sql + d[0] + ' ,'

        select_sql = select_sql[:-1]

        select_sql = select_sql + " FROM " +  table_def + " INNER JOIN id_table ON id_table.fk_id = " + table_def + "." + pk_def

        logging.info("***SELECT SQL***")
        logging.info(select_sql)

        cursor.execute(select_sql)
        rows = cursor.fetchall()
        conn.close()
        return rows

    def insert_rows_from_fields_and_data(self, table_def, field_defs ,data):
        conn = get_connection()
        cursor = conn.cursor()

        insertCount = len(data)

        temp_table_create = 'CREATE TEMPORARY TABLE insert_table ('
        temp_table_insert = 'INSERT INTO insert_table ( '
        temp_table_values = ' VALUES ( '

        insert_into = 'INSERT INTO ' + table_def + ' ( '
        insert_select = 'SELECT '

        for d in field_defs:
            temp_table_create = temp_table_create + d[0] + ' ' + d[1] + ' ,'
            temp_table_insert = temp_table_insert + d[0] + ' ,'
            temp_table_values = temp_table_values + '%s ,'
            insert_into = insert_into + d[0] + ' ,'
            insert_select = insert_select + d[0] + ' ,'

        temp_table_create = temp_table_create[:-1]
        temp_table_insert = temp_table_insert[:-1]
        temp_table_values = temp_table_values[:-1]
        insert_into = insert_into[:-1]
        insert_select = insert_select[:-1]

        temp_table_create = temp_table_create + ') '
        temp_table_insert = temp_table_insert + ') '
        temp_table_values = temp_table_values + ') '
        insert_into = insert_into + ') '
        insert_select = insert_select + ' FROM insert_table  '

        logging.info("***INSERT TEMP SQL***")
        logging.info(temp_table_create)
        logging.info(temp_table_insert + temp_table_values)
        logging.info("***INSERT SQL***")
        logging.info(insert_into + insert_select)

        cursor.execute(temp_table_create)

        for d in data:
            logging.info("***DATA***")
            logging.info(str(d[0]))


        cursor.executemany(temp_table_insert + temp_table_values,data)

        cursor.execute(insert_into + insert_select)
        #GET AND COUNT BACK


        end_id = conn.insert_id()
        start_id = end_id + insertCount

        logging.info("***Id Range***")
        logging.info(end_id)
        logging.info(start_id)

        conn.commit()
        conn.close()
        return range(end_id,start_id)

    def update_rows_from_fields_and_data(self, table_def, pk_def , field_defs ,data):
        conn = get_connection()
        cursor = conn.cursor()


        temp_table_create = 'CREATE TEMPORARY TABLE insert_table (' + pk_def + ' INT ,'
        temp_table_insert = 'INSERT INTO insert_table ( ' + pk_def + ' ,'
        temp_table_values = ' VALUES ( %s ,'

        insert_update = 'UPDATE ' + table_def + ' ut INNER JOIN insert_table it ON it.' + pk_def + ' = ut.'+pk_def+' '
        insert_set = 'SET ut.' + pk_def + ' = it.' + pk_def + ' ,'

        for d in field_defs:
            temp_table_create = temp_table_create + d[0] + ' ' + d[1] + ' ,'
            temp_table_insert = temp_table_insert + d[0] + ' ,'
            temp_table_values = temp_table_values + '%s ,'
            insert_set = insert_set + ' ut.' + d[0] + ' = it.' + d[0] + ' ,'

        temp_table_create = temp_table_create[:-1]
        temp_table_insert = temp_table_insert[:-1]
        temp_table_values = temp_table_values[:-1]
        insert_set = insert_set[:-1]

        temp_table_create = temp_table_create + ') '
        temp_table_insert = temp_table_insert + ') '
        temp_table_values = temp_table_values + ') '

        logging.info("***INSERT TEMP SQL***")
        logging.info(temp_table_create)
        logging.info(temp_table_insert + temp_table_values)
        logging.info("***INSERT SQL***")
        logging.info(insert_update + insert_set)

        for d in data:
            logging.info("***DATA***")
            logging.info(str(d[0]))
            logging.info(str(d[1]))


        logging.info("***CREATE TEMP***")
        cursor.execute(temp_table_create)

        logging.info("***EXECUTE TEMP INSERT***")
        cursor.executemany(temp_table_insert + temp_table_values,data)

        logging.info("***UPDATE SQL***")
        cursor.execute(insert_update + insert_set)

        conn.commit()
        conn.close()

    def insert_join_table(self,join_table,fk_join_left,fk_join_right,value_left,value_right):
        conn = get_connection()
        cursor = conn.cursor()

        table_insert = 'INSERT INTO '+join_table+' ( '+fk_join_left+','+fk_join_right+') VALUES ( '+value_left+','+value_right+') '
        cursor.execute(table_insert)

        conn.commit()
        conn.close()

    def insert_join_table2(self,join_table,fk_join_left,fk_join_right,values):
        conn = get_connection()
        cursor = conn.cursor()

        table_insert = 'INSERT INTO '+join_table+' ( '+fk_join_left+','+fk_join_right+') VALUES '

        for v in values:
            table_insert = table_insert + ' ( ' + str(v[0]) + ',' + str(v[1]) + ' ) ,'

        table_insert = table_insert[:-1]

        logging.info(table_insert)

        cursor.execute(table_insert)

        conn.commit()
        conn.close()
# CMS Data Access Objects


#TODO Refactor CompanyDao to use GernicDao where possible
class CompanyDao:
    table_def = "lms_orders.Company"
    pk_def = "company_id"

    def joinPerson(self,c_id,p_id):
        fk_join_left = 'fk_company'
        fk_join_right = 'fk_person'
        join_table = 'lms_orders.CompanyToPerson'
        Dao().insert_join_table(join_table,fk_join_left,fk_join_right,str(c_id),str(p_id))

    def joinAddress(self,c_id,a_id):
        fk_join_left = 'fk_company'
        fk_join_right = 'fk_address'
        join_table = 'lms_orders.CompanyToAddress'
        Dao().insert_join_table(join_table,fk_join_left,fk_join_right,str(c_id),str(a_id))


    def get(self,ids,idlist):
#        conn = get_connection()
#        cursor = conn.cursor()
#        logging.info("dao company ids")
#        logging.info(ids)

#        cursor.execute('CREATE TEMPORARY TABLE id_table (fk_id INT)')
#        cursor.executemany('INSERT INTO id_table (fk_id) VALUES (%s)',idlist)
#        cursor.execute('SELECT company_id, name FROM lms_orders.Company INNER JOIN id_table ON id_table.fk_id = lms_orders.Company.company_id')
#
#        rows = cursor.fetchall()
#        conn.close()

        select_sql = 'SELECT company_id, name , code , vat_number FROM lms_orders.Company INNER JOIN id_table ON id_table.fk_id = lms_orders.Company.company_id'
        return Dao().get_rows_from_ids(idlist,select_sql)

    #TODO THIS IS BAD FILTER FOR COMPANIES PASSED IN NOT GET ALL, may result in error if used incorrectly
    #Refactor to generic method

    def getRoleIds(self,ids):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT fk_company,fk_company_type FROM lms_orders.CompanyToCompanyType')
        rows = cursor.fetchall()
        conn.close()
        return rows

    def getAddressIds(self,ids):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT fk_company,fk_address FROM lms_orders.CompanyToAddress')
        rows = cursor.fetchall()
        conn.close()
        return rows

    def getPersonIds(self,ids):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT fk_company,fk_person FROM lms_orders.CompanyToPerson')
        rows = cursor.fetchall()
        conn.close()
        return rows

    def updateTypes(self,id,roles):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM lms_orders.CompanyToCompanyType WHERE fk_company = %s',str(id))

        table_insert = 'INSERT INTO lms_orders.CompanyToCompanyType ( fk_company, fk_company_type) VALUES '

        for r in roles:
            table_insert = table_insert + ' ( ' + str(id) + ',' + str(r) + ' ) ,'

        table_insert = table_insert[:-1]

        logging.info('******UPDATE TYPE******')
        logging.info(table_insert)

        cursor.execute(table_insert)
        conn.commit()
        conn.close()


    def update(self,id,name,vat_number,code):
        update = (
                "UPDATE lms_orders.Company SET name = %s, vat_number = %s, code  = %s WHERE company_id = %s"
            )
        data = (name,vat_number,code,id)
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(update,data)
        conn.commit()
        conn.close()

        #get lists of attributes,
        #add to attribute lists to single list in same order as list of fields
        #generic method will then insert the field lists in in to a table mapping to field names
        #then does a join to real table to update
        #pass to function list update_rows(table_name, field_list, list_of_lists_of_field_values) note the order of the field_list and list_of_lists must be the same may be a dictionary might be better with key as field name and list of values as dictionary value

    def insert(self,name,vatNumber,code):
        insert = (
            "INSERT INTO lms_orders.Company (name,vat_number,code) VALUES (%s,%s,%s)"
            )
        data = (name,vatNumber,code)
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(insert, data)
        new_id = conn.insert_id()
        conn.commit()
        conn.close()
        return new_id



    def get_all_ids(self):
        return Dao().get_all_ids(self.pk_def,self.table_def)

    def count_all(self):
        return Dao().count_all(self.table_def)


class PersonDao:
    table_def = "lms_orders.Person"
    pk_def = "person_id"

    def __init__(self):
        self.table_def = "lms_orders.Person"
        self.pk_def = "person_id"
        self.field_defs = [  ("first_name","VARCHAR(45)"),
                             ("last_name","VARCHAR(45)"),
                             ("job_title","VARCHAR(255)"),
                             ("salutation","VARCHAR(45)")]

    def get(self,ids):

        select_sql = 'SELECT person_id, first_name, last_name,job_title,salutation,address_id FROM lms_orders.Person INNER JOIN id_table ON id_table.fk_id = lms_orders.Person.person_id'
        return Dao().get_rows_from_ids(ids,select_sql)

    #TODO THIS IS BAD FILTER FOR PEOPLE PASSED IN NOT GET ALL
    #Refactor to generic method

    def get_email_ids(self,ids):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT fk_person,fk_email FROM lms_orders.PersonToEmail')
        rows = cursor.fetchall()
        conn.close()
        return rows

    #TODO THIS IS BAD FILTER FOR PEOPLE PASSED IN NOT GET ALL
    #Refactor to generic method

    def get_phone_ids(self,ids):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT fk_person,fk_phone FROM lms_orders.PersonToPhone')
        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_role_ids(self,ids):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT fk_person,fk_person_role FROM lms_orders.PersonToPersonRole')
        rows = cursor.fetchall()
        conn.close()
        return rows

    def insert(self,first_name,last_name,job_title,salutation):
        insert = (
            "INSERT INTO lms_orders.Person (first_name,last_name,job_title,salutation) VALUES (%s,%s,%s,%s)"
            )
        data = (first_name,last_name,job_title,salutation)

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(insert, data)
        new_id = conn.insert_id()
        conn.commit()
        conn.close()
        return new_id

    def updateRoles(self,id,roles):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM lms_orders.PersonToPersonRole WHERE fk_person = %s',str(id))

        table_insert = 'INSERT INTO lms_orders.PersonToPersonRole ( fk_person, fk_person_role) VALUES '

        for r in roles:
            table_insert = table_insert + ' ( ' + str(id) + ',' + str(r) + ' ) ,'

        table_insert = table_insert[:-1]

        logging.info("****** TYPES ******")
        logging.info(table_insert)

        cursor.execute(table_insert)
        conn.commit()
        conn.close()

    def update(self,id,first_name,second_name,job_title,salutation):
        logging.info ('UPDATING PERSON 3')
        logging.info (id)
        logging.info (first_name)
        logging.info (second_name)
        logging.info (job_title)
        logging.info (salutation)
        logging.info ('FINISHED UPDATING')
        update = (
            "UPDATE lms_orders.Person SET first_name = %s, last_name = %s , job_title = %s,salutation = %s  WHERE person_id = %s"
            )
        data = (first_name,second_name,job_title,salutation,id)
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(update,data)
        conn.commit()
        conn.close()

    def get_all_ids(self):
        conn = get_connection()
        cursor = conn.cursor()
        select_sql = "SELECT " + self.pk_def +" FROM " + self.table_def
        cursor.execute(select_sql)
        rows = cursor.fetchall()
        conn.close()
        return rows

    def count_all(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM " + self.table_def)
        count = cursor.fetchone()[0]
        return count

    def insertPhones(self,person_to_phone):
        fk_join_left = 'fk_person'
        fk_join_right = 'fk_phone'
        join_table = 'lms_orders.PersonToPhone'
        Dao().insert_join_table2(join_table,fk_join_left,fk_join_right,person_to_phone)

    def insertEmails(self,person_to_email):
        fk_join_left = 'fk_person'
        fk_join_right = 'fk_email'
        join_table = 'lms_orders.PersonToEmail'
        Dao().insert_join_table2(join_table,fk_join_left,fk_join_right,person_to_email)

class AddressDao:
    table_def = "lms_orders.Address"
    pk_def = "address_id"
    field_defs = [  ("name","VARCHAR(255)"),
                    ("line_1","VARCHAR(255)"),
                    ("line_2","VARCHAR(255)"),
                    ("line_3","VARCHAR(255)"),
                    ("city","VARCHAR(255)"),
                    ("region","VARCHAR(255)"),
                    ("fk_country","INT"),
                    ("postal_code","VARCHAR(50)")]

    def get(self,ids):
        return Dao().get_rows_from_ids2(ids,self.table_def,self.pk_def,self.field_defs)

    def update(self,data):
        Dao().update_rows_from_fields_and_data(self.table_def, self.pk_def , self.field_defs ,data)

    def insert(self,data):
        return Dao().insert_rows_from_fields_and_data(self.table_def, self.field_defs,data)


class GenericDao:
    table_def = ""
    pk_def = ""
    field_defs = ""

    def get(self,ids):
        return Dao().get_rows_from_ids2(ids,self.table_def,self.pk_def,self.field_defs)

    def update(self,data):
        Dao().update_rows_from_fields_and_data(self.table_def, self.pk_def , self.field_defs ,data)

    def insert(self,data):
        return Dao().insert_rows_from_fields_and_data(self.table_def, self.field_defs,data)

    def count_all(self):
        return Dao().count_all(self.table_def);

    def get_all_ids(self):
        return Dao().get_all_ids(self.pk_def,self.table_def);

class EmailDao(GenericDao):
    #table_def = "lms_orders.Email"
    #pk_def = "email_id"
    #field_defs = [  ("email","VARCHAR(255)")]
    def __init__(self):
        self.table_def = "lms_orders.Email"
        self.pk_def = "email_id"
        self.field_defs = [  ("email","VARCHAR(45)"), ("fk_email_type","int")]

class PhoneDao(GenericDao):
    #table_def = "lms_orders.Phone"
    #pk_def = "phone_id"
    #field_defs = [  ("number","VARCHAR(255)") , ("fk_phone_type","int")]

    def __init__(self):
        self.table_def = "lms_orders.Phone"
        self.pk_def = "phone_id"
        self.field_defs = [  ("number","VARCHAR(45)"), ("fk_phone_type","int")]

        logging.info("****INIT****")
        logging.info(self.table_def)
        logging.info(self.pk_def)

# LMS Order Data Access Objects

class OrderDao(GenericDao):
    table_def = "lms_orders.Order"
    pk_def = "order_id"

class OrderItemDao:
    table_def = "lms_orders.OrderItem"
    pk_def = "orderitem_id"
