from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username, password):
    """
    The function which gets called when an user calls the /auth endpoint
    with their user name and password
    @param username: User's name in string type
    @param password: User's un-encrypted password in string type
    @return: A UserModel object if authentication was successful, None otherwise
    """

    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    """
    Function that gets called when user has been already authenticated,
    and Flask-JWT verified their authorization header is correct.
    @param payload: A dictionary with 'identity' key, which is the user id
    @return: UserModel obj
    """

    user_id = payload['identity']
    return UserModel.find_user_by_id(user_id)


