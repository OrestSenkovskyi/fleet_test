from flask import g, Response, request
import json
import time

from app import app, db
from app.models import Fleet, User, Vehicle
from app.outputs import JsonOutput
import app.usecases as usecases


@app.route('/', methods=['GET', 'POST'])
def index():
    return "Fleet management coding test"


@app.route('/fleet', methods=['POST'])
def post_fleet_action():
    """ Add fleet
    :return:
    """
    output = JsonOutput()
    try:
        if not request.is_json:
            raise TypeError('Payload is not json')
        payload = request.json
        usecases.SetFleetUsecase(db=db, fleet=payload).execute()
        output.add(status=200, response=json.dumps({'data': request.json}))
    except Exception as error:
        db.session.rollback()
        app.logger.critical(str(error))
        output.add(status=400, response=json.dumps({'error': str(error)}))
    return output.show()


@app.route('/fleet/<id>', methods=['DELETE'])
def delete_fleet_action(id):
    """ Delete fleet
    :return:
    """
    output = JsonOutput()
    try:
        fleet = usecases.DeleteFleetUsecase(db=db, fleet_id=id).execute()
        if not fleet:
            raise FileNotFoundError(f"Fleet with id = {id} not found")
        output.add(status=200, response=repr(fleet))
    except Exception as error:
        db.session.rollback()
        app.logger.critical(str(error))
        output.add(status=400, response=json.dumps({'error': str(error)}))
    return output.show()


@app.route('/fleets', methods=['GET'])
def get_fleets_action():
    """ Get fleets
    :return:
    """
    output = JsonOutput()
    try:
        fleets = usecases.GetFleetsUsecase(db=db).execute()
        if not fleets:
            raise FileNotFoundError(f"Fleets list is empty")
        output.add(status=200, response=repr(fleets))
    except Exception as error:
        db.session.rollback()
        app.logger.critical(str(error))
        output.add(status=400, response=json.dumps({'error': str(error)}))
    return output.show()


@app.route('/user', methods=['POST'])
def post_user_action():
    """ Add user
    :return:
    """
    output = JsonOutput()
    try:
        if not request.is_json:
            raise TypeError('Payload is not json')
        payload = request.json
        usecases.SetUserUsecase(db=db, user=payload).execute()
        output.add(status=200, response=json.dumps({'data': request.json}))
    except Exception as error:
        db.session.rollback()
        app.logger.critical(str(error))
        output.add(status=400, response=json.dumps({'error': str(error)}))
    return output.show()


@app.route('/users', methods=['GET'])
def get_users_action():
    """ Get users
    :return:
    """
    output = JsonOutput()
    try:
        users = usecases.GetUsersUsecase(db=db).execute()
        if not users:
            raise FileNotFoundError(f"Users list is empty")
        output.add(status=200, response=repr(users))
    except Exception as error:
        db.session.rollback()
        app.logger.critical(str(error))
        output.add(status=400, response=json.dumps({'error': str(error)}))
    return output.show()


@app.route('/vehicle', methods=['POST'])
def post_vehicle_action():
    """ Add vehicle
    :return:
    """
    output = JsonOutput()
    try:
        if not request.is_json:
            raise TypeError('Payload is not json')
        payload = request.json
        usecases.SetVehicleUsecase(db=db, vehicle=payload).execute()
        output.add(status=200, response=json.dumps({'data': request.json}))
    except Exception as error:
        db.session.rollback()
        app.logger.critical(str(error))
        output.add(status=400, response=json.dumps({'error': str(error)}))
    return output.show()


@app.route('/vehicles', methods=['GET'])
def get_vehicles_action():
    """ Get vehicle
    :return:
    """
    output = JsonOutput()
    try:
        vehicle = usecases.GetVehiclesUsecase(db=db).execute()
        if not vehicle:
            raise FileNotFoundError(f"Vehicle list is empty")
        output.add(status=200, response=repr(vehicle))
    except Exception as error:
        db.session.rollback()
        app.logger.critical(str(error))
        output.add(status=400, response=json.dumps({'error': str(error)}))
    return output.show()


@app.route('/fleet/<id>/users', methods=['GET'])
def get_users_by_id_action(id):
    """ Get users
    :return:
    """
    output = JsonOutput()
    try:
        users = usecases.GetUsersByFleetIdUsecase(db=db, fleet_id=id).execute()
        if not users:
            raise FileNotFoundError(f"Users list is empty")
        output.add(status=200, response=repr(users))
    except Exception as error:
        db.session.rollback()
        app.logger.critical(str(error))
        output.add(status=400, response=json.dumps({'error': str(error)}))
    return output.show()


@app.route('/fleet/<id>/vehicles', methods=['GET'])
def get_vehicles_by_id_action(id):
    """ Get vehicles
    :return:
    """
    output = JsonOutput()
    try:
        vehicles = usecases.GetVehiclesByFleetIdUsecase(db=db, fleet_id=id).execute()
        if not vehicles:
            raise FileNotFoundError(f"Vehicles list is empty")
        output.add(status=200, response=repr(vehicles))
    except Exception as error:
        db.session.rollback()
        app.logger.critical(str(error))
        output.add(status=400, response=json.dumps({'error': str(error)}))
    return output.show()
