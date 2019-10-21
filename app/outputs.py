from flask import Response


class AbstractOutput(object):
    def show(self):
        raise NotImplementedError(f"{self.__class__} must implement show()")


class JsonOutput(AbstractOutput):

    def __init__(self):
        self.status = 200
        self.response = ''
        self.mimetype = 'application/json'

    def add(self, status, response):
        self.status = status
        self.response = response

    def show(self):
        return Response(response=self.response, status=self.status, mimetype=self.mimetype)

