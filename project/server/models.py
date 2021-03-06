# project/server/models.py


import datetime

from flask import current_app

from project.server import db, bcrypt
from sqlalchemy import inspect
import jwt



class Expert(db.Model):

    __tablename__ = 'expert'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    nickname = db.Column(db.String(255), unique=True, nullable=False)
    active = db.Column(db.Boolean,  default=True)

    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}


# class User(db.Model):
#
#     __tablename__ = 'users'
#
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     email = db.Column(db.String(255), unique=True, nullable=False)
#     password = db.Column(db.String(255), nullable=False)
#     registered_on = db.Column(db.DateTime, nullable=False)
#     admin = db.Column(db.Boolean, nullable=False, default=False)
#
#     def __init__(self, email, password, admin=False):
#         self.email = email
#         self.password = bcrypt.generate_password_hash(
#             password, current_app.config.get('BCRYPT_LOG_ROUNDS')
#         ).decode()
#         self.registered_on = datetime.datetime.now()
#         self.admin = admin
#
#     def encode_auth_token(self, user_id):
#         """
#         Generates the Auth Token
#         :return: string
#         """
#         try:
#             payload = {
#                 'exp': datetime.datetime.utcnow() + datetime.timedelta(days=4, seconds=00),
#                 'iat': datetime.datetime.utcnow(),
#                 'sub': user_id
#             }
#             return jwt.encode(
#                 payload,
#                 current_app.config.get('SECRET_KEY'),
#                 algorithm='HS256'
#             )
#         except Exception as e:
#             return e
#
#     @staticmethod
#     def decode_auth_token(auth_token):
#         """
#         Validates the auth token
#         :param auth_token:
#         :return: integer|string
#         """
#         try:
#             payload = jwt.decode(auth_token, current_app.config.get('SECRET_KEY'))
#             is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
#             if is_blacklisted_token:
#                 return 'Token blacklisted. Please log in again.'
#             else:
#                 return payload['sub']
#         except jwt.ExpiredSignatureError:
#             return 'Signature expired. Please log in again.'
#         except jwt.InvalidTokenError:
#             return 'Invalid token. Please log in again.'
#
#
# class BlacklistToken(db.Model):
#     """
#     Token Model for storing JWT tokens
#     """
#     __tablename__ = 'blacklist_tokens'
#
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     token = db.Column(db.String(500), unique=True, nullable=False)
#     blacklisted_on = db.Column(db.DateTime, nullable=False)
#
#     def __init__(self, token):
#         self.token = token
#         self.blacklisted_on = datetime.datetime.now()
#
#     def __repr__(self):
#         return '<id: token: {}'.format(self.token)
#
#     @staticmethod
#     def check_blacklist(auth_token):
#         # check whether auth token has been blacklisted
#         res = BlacklistToken.query.filter_by(token=str(auth_token)).first()
#         if res:
#             return True
#         else:
#             return False
#
# class Alpha(db.Model):
#
#     __tablename__ = 'alpha'
#
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     expert = db.Column(db.String(255),unique=True, nullable=False)
#     company = db.Column(db.String(255))
#     date = db.Column(db.Date,nullable=False)
#     variable = db.Column(db.String(255))
#     lowerbound = db.Column(db.Integer)
#     upperbound = db.Column(db.Integer)
#
#     def toDict(self):
#         return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
