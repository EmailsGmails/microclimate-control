import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'microclimate_control.settings')
django.setup()

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from microclimate_control_app.models import Project, BuildingObject, Metric, DataType, Device, DataPoint, User

def populate_database():
    # Create Projects
    sia_avots, created = Project.objects.get_or_create(name='SIA Avots')
    print(f"{sia_avots} - Freshly created: {created}")
    sia_figura, created = Project.objects.get_or_create(name='SIA Figura')
    print(f"{sia_figura} - Freshly created: {created}")
    as_ferma, created = Project.objects.get_or_create(name='A/S Ferma')
    print(f"{as_ferma} - Freshly created: {created}")

    # Create building objects for SIA Avots
    sia_avots_building_1, created = BuildingObject.objects.get_or_create(name='Aglonas Rupnica' , project=sia_avots, location='Aglonas street 21')
    print(f"{sia_avots_building_1} - Freshly created: {created}")
    sia_avots_building_2, created = BuildingObject.objects.get_or_create(name='Vairogu Ofiss', project=sia_avots, location='Vairogu street 45')
    print(f"{sia_avots_building_2} - Freshly created: {created}")
    sia_avots_building_3, created = BuildingObject.objects.get_or_create(name='Hospitalu Ofiss', project=sia_avots, location='Hospitalu street 77')
    print(f"{sia_avots_building_3} - Freshly created: {created}")

    # Create building objects for SIA Figura
    sia_figura_building_1, created = BuildingObject.objects.get_or_create(name='Gremzdes Rupnica', project=sia_figura, location='Gremzdes street 33')
    print(f"{sia_figura_building_1} - Freshly created: {created}")

    # Create building objects for A/S Ferma
    as_ferma_building_1, created = BuildingObject.objects.get_or_create(name='Fabrika "Cirulisi"', project=as_ferma, location='Cirulisi')
    print(f"{as_ferma_building_1} - Freshly created: {created}")
    as_ferma_building_2, created = BuildingObject.objects.get_or_create(name='Fabrika "Caunes"', project=as_ferma, location='Caunes')
    print(f"{as_ferma_building_2} - Freshly created: {created}")

    # Create Metrics
    degrees_celsius, created = Metric.objects.get_or_create(name='°C')
    print(f"{degrees_celsius} - Freshly created: {created}")
    parts_per_million, created = Metric.objects.get_or_create(name='ppm')
    print(f"{parts_per_million} - Freshly created: {created}")
    percentage, created = Metric.objects.get_or_create(name='%')
    print(f"{percentage} - Freshly created: {created}")
    kilowatt_hours, created = Metric.objects.get_or_create(name='kWh')
    print(f"{kilowatt_hours} - Freshly created: {created}")

    # Create Data Types
    temperature, created = DataType.objects.get_or_create(code='TEMP', name='Temperature', metric=degrees_celsius)
    print(f"{temperature} - Freshly created: {created}")
    co2, created = DataType.objects.get_or_create(code='CO2', name='CO2', metric=parts_per_million)
    print(f"{co2} - Freshly created: {created}")
    humidity, created = DataType.objects.get_or_create(code='HUM', name='Humidity', metric=percentage)
    print(f"{humidity} - Freshly created: {created}")
    electricity_counter, created = DataType.objects.get_or_create(code='EC', name='Electricity Counter', metric=kilowatt_hours)
    print(f"{electricity_counter} - Freshly created: {created}")

    # Create measuring devices
    device_1, created = Device.objects.get_or_create(name='dev1'); device_1.data_collected.set([temperature, co2, humidity])
    device_2, created = Device.objects.get_or_create(name='dev2'); device_2.data_collected.set([temperature, humidity, electricity_counter])
    device_3, created = Device.objects.get_or_create(name='dev3'); device_3.data_collected.set([temperature, co2, humidity])
    device_4, created = Device.objects.get_or_create(name='dev4'); device_4.data_collected.set([temperature, co2, humidity])
    device_5, created = Device.objects.get_or_create(name='dev5'); device_5.data_collected.set([temperature, co2, humidity, electricity_counter])
    device_6, created = Device.objects.get_or_create(name='dev6'); device_6.data_collected.set([temperature, co2, humidity, electricity_counter])

    # Create Data Points
    data_points_created_counter = 0
    sia_avots_building_1_dp_1, created = DataPoint.objects.get_or_create(value=23.35, data_type=temperature, device=device_1, building_object=sia_avots_building_1); data_points_created_counter += created
    sia_avots_building_1_dp_2, created = DataPoint.objects.get_or_create(value=14.5, data_type=co2, device=device_1, building_object=sia_avots_building_1); data_points_created_counter += created
    sia_avots_building_1_dp_3, created = DataPoint.objects.get_or_create(value=0.32, data_type=humidity, device=device_1, building_object=sia_avots_building_1); data_points_created_counter += created
    
    sia_avots_building_2_dp_1, created = DataPoint.objects.get_or_create(value=25.0, data_type=temperature, device=device_2, building_object=sia_avots_building_2); data_points_created_counter += created
    sia_avots_building_2_dp_2, created = DataPoint.objects.get_or_create(value=22.1, data_type=humidity, device=device_2, building_object=sia_avots_building_2); data_points_created_counter += created
    sia_avots_building_2_dp_3, created = DataPoint.objects.get_or_create(value=0.92, data_type=electricity_counter, device=device_2, building_object=sia_avots_building_2); data_points_created_counter += created

    sia_avots_building_3_dp_1, created = DataPoint.objects.get_or_create(value=12.2, data_type=temperature, device=device_3, building_object=sia_avots_building_3); data_points_created_counter += created
    sia_avots_building_3_dp_2, created = DataPoint.objects.get_or_create(value=11.0, data_type=co2, device=device_3, building_object=sia_avots_building_3); data_points_created_counter += created
    sia_avots_building_3_dp_3, created = DataPoint.objects.get_or_create(value=0.09, data_type=humidity, device=device_3, building_object=sia_avots_building_3); data_points_created_counter += created

    sia_figura_building_1_dp_1, created = DataPoint.objects.get_or_create(value=24.1, data_type=temperature, device=device_4, building_object=sia_figura_building_1); data_points_created_counter += created
    sia_figura_building_1_dp_2, created = DataPoint.objects.get_or_create(value=15.0, data_type=co2, device=device_4, building_object=sia_figura_building_1); data_points_created_counter += created
    sia_figura_building_1_dp_3, created = DataPoint.objects.get_or_create(value=0.99, data_type=humidity, device=device_4, building_object=sia_figura_building_1); data_points_created_counter += created

    as_ferma_building_1_dp_1, created = DataPoint.objects.get_or_create(value=19.0, data_type=temperature, device=device_5, building_object=as_ferma_building_1); data_points_created_counter += created
    as_ferma_building_1_dp_2, created = DataPoint.objects.get_or_create(value=6, data_type=co2, device=device_5, building_object=as_ferma_building_1); data_points_created_counter += created
    as_ferma_building_1_dp_3, created = DataPoint.objects.get_or_create(value=12, data_type=humidity, device=device_5, building_object=as_ferma_building_1); data_points_created_counter += created
    as_ferma_building_1_dp_4, created = DataPoint.objects.get_or_create(value=55, data_type=electricity_counter, device=device_5, building_object=as_ferma_building_1); data_points_created_counter += created

    as_ferma_building_2_dp_1, created = DataPoint.objects.get_or_create(value=16, data_type=temperature, device=device_6, building_object=as_ferma_building_2); data_points_created_counter += created
    as_ferma_building_2_dp_2, created = DataPoint.objects.get_or_create(value=0.5, data_type=co2, device=device_6, building_object=as_ferma_building_2); data_points_created_counter += created
    as_ferma_building_2_dp_3, created = DataPoint.objects.get_or_create(value=21, data_type=humidity, device=device_6, building_object=as_ferma_building_2); data_points_created_counter += created
    as_ferma_building_2_dp_4, created = DataPoint.objects.get_or_create(value=250, data_type=electricity_counter, device=device_6, building_object=as_ferma_building_2); data_points_created_counter += created
    print(f"{data_points_created_counter} data points freshly created")

    # Create Users
    superuser, created = User.objects.get_or_create(username='admin', full_name='Administrator', email='admin@example.com', phone='+32325345933', is_superuser=True, is_staff=True)
    if created:
        superuser.set_password('admin')
        superuser.save()
    print(f"{superuser} - Freshly created: {created}")
    aivars_ozols, created = User.objects.get_or_create(username='a.ozols', full_name='Aivars Ozols', phone='+37122299933', email='aivars.ozols@siaavots.lv')
    if created:
        aivars_ozols.set_password('a.ozols')
        aivars_ozols.save()
    print(f"{aivars_ozols} - Freshly created: {created}")
    janis_rensis, created = User.objects.get_or_create(username='j.rensis', full_name='Janis Rensis', phone='+37122299944', email='janis.rensis@siaavots.lv')
    if created:
        janis_rensis.set_password('j.rensis')
        janis_rensis.save()
    print(f"{janis_rensis} - Freshly created: {created}")
    harijs_atbildigais, created = User.objects.get_or_create(username='h.atbildigais', full_name='Harijs Atbildigais', phone='+37122266633', email='harijs.atbildigais@siafigura.lv')
    if created:
        harijs_atbildigais.set_password('h.atbildigais')
        harijs_atbildigais.save()
    print(f"{harijs_atbildigais} - Freshly created: {created}")
    harijs_verotajs, created = User.objects.get_or_create(username='h.verotajs', full_name='Harijs Verotajs', phone='+37122266644', email='harijs.verotajs@siafigura.lv')
    if created:
        harijs_verotajs.set_password('j.rensis')
        harijs_verotajs.save()
    print(f"{harijs_verotajs} - Freshly created: {created}")
    garijs_cirulis, created = User.objects.get_or_create(username='g.cirulis', full_name='Garijs Cirulis', phone='+37122266699', email='garijs.cirulis@asferma.lv')
    if created:
        garijs_cirulis.set_password('g.cirulis')
        garijs_cirulis.save()
    print(f"{garijs_cirulis} - Freshly created: {created}")

    sia_avots_building_1.users.set([aivars_ozols, janis_rensis])
    sia_avots_building_2.users.set([aivars_ozols])
    sia_avots_building_3.users.set([aivars_ozols, janis_rensis])
    sia_figura_building_1.users.set([harijs_atbildigais, harijs_verotajs])
    as_ferma_building_1.users.set([garijs_cirulis])
    as_ferma_building_2.users.set([garijs_cirulis])


    # Create Permissions
    premissions_created_counter = 0
    permission_access_project_1, created = Permission.objects.get_or_create(
        codename='can_access_project_1',
        name='Can Access Project "SIA Avots"',
        content_type=ContentType.objects.get_for_model(Project)
    ); premissions_created_counter += created

    permission_update_project_1, created = Permission.objects.get_or_create(
        codename='can_update_project_1',
        name='Can Update Project "SIA Avots"',
        content_type=ContentType.objects.get_for_model(Project)
    ); premissions_created_counter += created

    permission_access_project_2, created = Permission.objects.get_or_create(
        codename='can_access_project_2',
        name='Can Access Project "SIA Figura"',
        content_type=ContentType.objects.get_for_model(Project)
    ); premissions_created_counter += created

    permission_update_project_2, created = Permission.objects.get_or_create(
        codename='can_update_project_2',
        name='Can Update Project "SIA Figura"',
        content_type=ContentType.objects.get_for_model(Project)
    ); premissions_created_counter += created

    permission_access_project_3, created = Permission.objects.get_or_create(
        codename='can_access_project_3',
        name='Can Access Project "A/S Ferma"',
        content_type=ContentType.objects.get_for_model(Project)
    ); premissions_created_counter += created

    permission_update_project_3, created = Permission.objects.get_or_create(
        codename='can_update_project_3',
        name='Can Update Project "A/S Ferma"',
        content_type=ContentType.objects.get_for_model(Project)
    ); premissions_created_counter += created

    permission_create_project_1_buildings, created = Permission.objects.get_or_create(
        codename='can_create_buildings_project_1',
        name='Can Access Building Objects for "SIA Avots"',
        content_type=ContentType.objects.get_for_model(BuildingObject)
    ); premissions_created_counter += created

    permission_update_project_1_buildings, created = Permission.objects.get_or_create(
        codename='can_update_buildings_project_1',
        name='Can Update Building Objects for "SIA Avots"',
        content_type=ContentType.objects.get_for_model(BuildingObject)
    ); premissions_created_counter += created

    permission_delete_project_1_buildings, created = Permission.objects.get_or_create(
        codename='can_delete_buildings_project_1',
        name='Can Delete Building Objects for "SIA Avots"',
        content_type=ContentType.objects.get_for_model(BuildingObject)
    ); premissions_created_counter += created

    permission_create_project_2_buildings, created = Permission.objects.get_or_create(
        codename='can_create_buildings_project_2',
        name='Can Access Building Objects for "SIA Figura"',
        content_type=ContentType.objects.get_for_model(BuildingObject)
    ); premissions_created_counter += created

    permission_update_project_2_buildings, created = Permission.objects.get_or_create(
        codename='can_update_buildings_project_2',
        name='Can Update Building Objects for "SIA Figura"',
        content_type=ContentType.objects.get_for_model(BuildingObject)
    ); premissions_created_counter += created

    permission_delete_project_2_buildings, created = Permission.objects.get_or_create(
        codename='can_delete_buildings_project_2',
        name='Can Delete Building Objects for "SIA Fiugra"',
        content_type=ContentType.objects.get_for_model(BuildingObject)
    ); premissions_created_counter += created

    permission_create_project_3_buildings, created = Permission.objects.get_or_create(
        codename='can_create_buildings_project_3',
        name='Can Access Building Objects for "A/S Ferma"',
        content_type=ContentType.objects.get_for_model(BuildingObject)
    ); premissions_created_counter += created

    permission_update_project_3_buildings, created = Permission.objects.get_or_create(
        codename='can_update_buildings_project_3',
        name='Can Update Building Objects for "A/S Ferma"',
        content_type=ContentType.objects.get_for_model(BuildingObject)
    ); premissions_created_counter += created

    permission_delete_project_3_buildings, created = Permission.objects.get_or_create(
        codename='can_delete_buildings_project_3',
        name='Can Delete Building Objects for "A/S Ferma"',
        content_type=ContentType.objects.get_for_model(BuildingObject)
    ); premissions_created_counter += created

    permission_access_building_1, created = Permission.objects.get_or_create(
        codename='can_access_project_1_building_1',
        name='Can Access Building 1 of SIA Avots',
        content_type=ContentType.objects.get_for_model(BuildingObject)
    ); premissions_created_counter += created

    permission_access_building_2, created = Permission.objects.get_or_create(
        codename='can_access_project_1_building_2',
        name='Can Access Building 2 of SIA Avots',
        content_type=ContentType.objects.get_for_model(BuildingObject)
    ); premissions_created_counter += created

    permission_access_building_3, created = Permission.objects.get_or_create(
        codename='can_access_project_1_building_3',
        name='Can Access Building 3 of SIA Avots',
        content_type=ContentType.objects.get_for_model(BuildingObject)
    ); premissions_created_counter += created

    permission_access_building_4, created = Permission.objects.get_or_create(
        codename='can_access__project_2_building_1',
        name='Can Access Building 1 of SIA Figura',
        content_type=ContentType.objects.get_for_model(BuildingObject)
    ); premissions_created_counter += created

    permission_access_building_5, created = Permission.objects.get_or_create(
        codename='can_access_project_3_building_1',
        name='Can Access Building 1 of A/S Ferma',
        content_type=ContentType.objects.get_for_model(BuildingObject)
    ); premissions_created_counter += created

    permission_access_building_6, created = Permission.objects.get_or_create(
        codename='can_access_project_3_building_2',
        name='Can Access Building 2 of A/S Ferma',
        content_type=ContentType.objects.get_for_model(BuildingObject)
    ); premissions_created_counter += created

    print(f"{data_points_created_counter} permission objects freshly created")

    # Apply permissions
    aivars_ozols.user_permissions.add(
        permission_access_project_1,
        permission_update_project_1,
        permission_create_project_1_buildings,
        permission_update_project_1_buildings,
        permission_delete_project_1_buildings,
    )
    janis_rensis.user_permissions.add(
        permission_access_building_1,
        permission_access_building_3,
        permission_update_project_1_buildings,
    )
    harijs_atbildigais.user_permissions.add(
        permission_access_project_2,
        permission_update_project_2,
        permission_create_project_2_buildings,
        permission_update_project_2_buildings,
        permission_delete_project_2_buildings,
    )
    harijs_verotajs.user_permissions.add(
        permission_access_project_2,
    )
    garijs_cirulis.user_permissions.add(
        permission_access_project_3,
        permission_update_project_3,
        permission_create_project_3_buildings,
        permission_update_project_3_buildings,
        permission_delete_project_3_buildings,
    )

if __name__ == '__main__':
    populate_database()
