from app.models import *
from flask import request
import logging
import traceback


class SQLAlchemyHandler(logging.Handler):
    """
    Handler to log into db
    """
    def emit(self, record):
        trace = None
        exc = record.__dict__['exc_info']
        if exc:
            trace = traceback.format_exc(exc)

        path = request.path
        method = request.method
        ip = request.remote_addr

        log = Log(logger=record.__dict__['name'],
                  level=record.__dict__['levelname'],
                  trace=trace,
                  message=record.__dict__['msg'],
                  path=path,
                  method=method,
                  ip=ip
        )
        db.session.add(log)
        db.session.commit()
