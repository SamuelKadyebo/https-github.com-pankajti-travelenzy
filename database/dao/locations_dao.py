from database.connection.mysql_connection import get_session,get_connection
from database.schema import location

sql_locations_without_distance="select l1.name as source ,l2.name as destination,lm.id  from location_mat lm join location l1 on l1.id=lm.source join location l2 on l2.id=lm.destination where lm.id  not in  (select location_mat_id from location_mat_attrs )"

sql_locations_without_details="select id ,name  from location where id not in (select location_id  from location_Details)"


sql_attractios='select * from attractions where location_name'

class LocationsDao():
    def get_locations_without_distance(self):
        result=get_connection().execute(sql_locations_without_distance)
        records=result.fetchall()
        return records

    def get_all_locations_without_details(self):
        result = get_connection().execute(sql_locations_without_details)
        records = result.fetchall()
        return records

    def find_location_by_name(self, name):
        return get_session().query(location).filter_by(name=name)

    def find_details_by_location_name(self, name):
        location=self.find_location_by_name(name).all()[0]
        return get_session().query(location_details).filter_by(location_id=location.id).all()









