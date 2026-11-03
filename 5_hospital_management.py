
from mysql import connector

class HospitalManagement:

    def __init__(self):
        try:
            self.connection=connector.connect(
                host="localhost",
                user="root",
                password="M7@vQ9#Lp2!Xr8$Zn5&K",
                database="hospital_db"
            )

            if self.connection.is_connected():
                print("connected successfully")
        except Exception as e:
            print(e)

    def get_one_patient(self,id):
        try:
            cursor_connection=self.connection.cursor()

            query="""select * from patients where patient_id=%s"""

            value=(id,)

            cursor_connection.execute(query,value)

            result=cursor_connection.fetchone()

            if result==None:
                return None
            else:
                return result
        except Exception as e:
            print(e)

    def add_patient(self,**kwargs):
        try:
            cursor_connection=self.connection.cursor()

            query="""insert into patients(name,age,gender,phone,disease,admission_date)
            values(%s,%s,%s,%s,%s,%s)"""

            value=[v for v in kwargs.values()]

            cursor_connection.execute(query,value)

            self.connection.commit()
            print("patient details added")
        except Exception as e:
            print(e)

    def get_all_patient(self):

        try:

            cursor_connection=self.connection.cursor()

            query="""select * from patients"""

            cursor_connection.execute(query)

            result=cursor_connection.fetchall()
            return result
        except Exception as e:
            print(e)

    def update_patient(self,id,**kwarg):
        try:
            result=self.get_one_patient(id)

            if result!=None:

                cursor_connection=self.connection.cursor()
                placeholder=""
                for key in kwarg.keys():
                    placeholder+=key+"=%s,"
                placeholder=placeholder.rstrip(",")

                query=f"update patients set {placeholder} where patient_id=%s"

                values=[v for v in kwarg.values()]

                values.append(id)

                cursor_connection.execute(query,values)

                self.connection.commit()

                print("updated")
            else:
                print("patient doesn't exist")
        except Exception as e:
            print(e)

    def delete_patient(self,id):

        try:
            cursor_connection=self.connection.cursor()

            query="""delete from patients where patient_id=%s"""

            value=(id,)

            cursor_connection.execute(query,value)

            self.connection.commit()

            if cursor_connection.rowcount>0:
                print("deleted ")
            else:
                print("patient doesn't exist")
        except Exception as e:
            print(e)

hospital=HospitalManagement()