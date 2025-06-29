from fastapi import FastAPI
from .core.tracker import create_new_session
from .core.models import Session

# create the app intance
app = FastAPI()

# the 'response_model=Session' tells FastAPI to expect a Session object
@app.post("/session", response_model=Session)
def create_session():
    """
    Handles the API request to create a new session.
    """
    # Call a function from tracker.py and return its result
    return create_new_session()