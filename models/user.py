from db import db


class UserModel(db.Model):
    """
    This is the user model
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String())

    def __init__(self, username, password):
        """
        Initialization of the user object
        """
        self.username = username
        self.password = password

    def save_to_db(self):
        """
        This method will save object into db
        """

        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        """
        This method will remove element from db
        @return:
        """
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, user_name):
        """
        This class method will allow to find the user
        in db by the user name
        """

        return cls.query.filter_by(username=user_name).first()

    @classmethod
    def find_user_by_id(cls, _id):
        """
        This is a class method which will find
        the user by id.
        """
        return cls.query.filter_by(id=_id).first()
