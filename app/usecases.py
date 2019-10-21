from app.models import Fleet, User, Vehicle


class AbstractUsecase(object):
    def __init__(self, db):
        self.db = db

    def execute(self):
        raise NotImplementedError(f"{self.__class__} not implemented execute")


class SetFleetUsecase:
    def __init__(self, db, fleet):
        self.db = db
        self.fleet = fleet

    def execute(self):
        """ Insert into db """
        fleet_model = Fleet(name=self.fleet['name'], address=self.fleet['address'])
        self.db.session.add(fleet_model)
        # Commit all changes into db
        self.db.session.commit()
        # Close db connection
        self.db.session.close()
        return self.fleet


class GetFleetsUsecase(AbstractUsecase):
    def execute(self):
        """ Get all fleets from db """
        return Fleet.query.all()


class DeleteFleetUsecase:
    def __init__(self, db, fleet_id):
        self.db = db
        self.fleet_id = fleet_id

    def execute(self):
        """
        Delete fleet with some exact id
        :return: LIst of all fleets after delete
        """
        fleet = Fleet.query.filter_by(id=self.fleet_id).first()
        self.db.session.delete(fleet)
        self.db.session.commit()
        self.db.session.close()
        return Fleet.query.all()


class SetUserUsecase:
    def __init__(self, db, user):
        self.db = db
        self.user = user

    def execute(self):
        """ Insert into db """
        user_model = User(name=self.user['name'], surname=self.user['surname'], fleet_id=self.user['fleet_id'])
        self.db.session.add(user_model)
        # Commit all changes into db
        self.db.session.commit()
        # Close db connection
        self.db.session.close()
        return self.user


class GetUsersUsecase(AbstractUsecase):
    def execute(self):
        """ Get all fleets from db """
        return User.query.all()


class GetUsersByFleetIdUsecase():
    def __init__(self, db, fleet_id):
        self.db = db
        self.fleet_id = fleet_id

    def execute(self):
        """
        Get users by fleet id
        """
        user_models = User.query.filter_by(fleet_id=self.fleet_id).all()
        return user_models


class SetVehicleUsecase:
    def __init__(self, db, vehicle):
        self.db = db
        self.vehicle = vehicle

    def execute(self):
        """ Insert into db """
        vehicle_model = Vehicle(brand=self.vehicle['brand'], car_number=self.vehicle['car_number'],
                                fleet_id=self.vehicle['fleet_id'])
        self.db.session.add(vehicle_model)
        # Commit all changes into db
        self.db.session.commit()
        # Close db connection
        self.db.session.close()
        return self.vehicle


class GetVehiclesUsecase(AbstractUsecase):
    def execute(self):
        """ Get all fleets from db """
        return Vehicle.query.all()


class GetVehiclesByFleetIdUsecase():
    def __init__(self, db, fleet_id):
        self.db = db
        self.fleet_id = fleet_id

    def execute(self):
        """
        Get vehicles by fleet id
        """
        vehicle_models = Vehicle.query.filter_by(fleet_id=self.fleet_id).all()
        return vehicle_models
