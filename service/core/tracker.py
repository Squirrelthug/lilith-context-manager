from .models.py import Session


def create_new_session() -> Session:
    """
    Creates a new Session object with a unique ID.
    """
    # Generate a new session ID
    # This will use the default_factory of the session_id field in the Session model
    new_session = Session()
    return new_session

