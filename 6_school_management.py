from mysql import connector
import datetime


class School_Management:

    def __init__(self):
        try:
            self.connection_to_db = connector.connect(
                host='localhost',
                user='root',
                password='M7@vQ9#Lp2!Xr8$Zn5&K',
                database='school_management'
            )
            if self.connection_to_db.is_connected():
                print("Database is connected!")
        except Exception as e:
            print(e)

    def get_obj(self,id):
        try:
            self.cursor_obj=self.connection_to_db.cursor()

            query="""select * from student where student_id=%s"""

            value=(id,)

            self.cursor_obj.execute(query,value)
            result=self.cursor_obj.fetchone()
            return result
        except Exception as e:
            print(e)

    def post(self, **kwarg):

        try:
            cursor_ob = self.connection_to_db.cursor()
            query = """insert into student(student_name,student_age,date_of_join,mobile_number)
                                        values(%s,%s,%s,%s)"""

            values=[v for v in kwarg.values()]
            cursor_ob.execute(query,values)
            self.connection_to_db.commit()
            print("datas added successfully in the tabel")
        except Exception as e:
            print(e)

    def get(self):
        try:
            self.cursor_obj=self.connection_to_db.cursor()

            query="""select * from student"""
            self.cursor_obj.execute(query)
            result=self.cursor_obj.fetchall()

            for i in result:
                print(i)
        except Exception as e:
            print(e)

    def retrive(self,id=None):

        try:
            result=self.get_obj(id=id)
            print(result)
        except Exception as e:
            print(e)

    def delete(self,id=None):

        try:
            self.cursor_obj=self.connection_to_db.cursor()
            query="""delete from student where student_id=%s"""
            value=(id,)

            self.cursor_obj.execute(query,value)
            self.connection_to_db.commit()

            if self.cursor_obj.rowcount>0:
                print("Deleted successfully")
            else:
                print("There is not data with this id")
        except Exception as e:
            print(e)

    def put(self,id,**kwargs):

        result=self.get_obj(id=id)

        try:
            if result!=None:
                self.cursor_obj=self.connection_to_db.cursor()

                placeholder=""

                for key in kwargs.keys():
                    placeholder+=key+"=%s,"

                placeholder=placeholder.rstrip(",")

                query=f"""update student set {placeholder} where student_id=%s"""

                values=[v for v in kwargs.values()]
                values.append(id)

                self.cursor_obj.execute(query,values)
                self.connection_to_db.commit()
                if self.cursor_obj.rowcount>0:
                    print("updated successfully")
        except Exception as e:
            print(e)

class_object=School_Management()

# class_object.post(name='prabhakaran',age=25,date=datetime.datetime.today(),mobile=9495181028)
# class_object.post(name='prabha',age=23,date=datetime.datetime.today(),mobile=9495181029)
# class_object.retrive(2)
# class_object.delete(2)
class_object.put(2,student_age=100)