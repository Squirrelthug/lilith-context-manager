import os
import pathlib
from .models import Session


def create_new_session() -> Session:
    """
    Creates a new Session object, creates a dedicated directory for it, and persists the session data to a JSON file within that directory using an atomic write.
    """
    # Generate a new session ID
    # This will use the default_factory of the session_id field in the Session model
    new_session = Session()
    session_id = new_session.session_id

    # Create a directory for the session
    session_dir = pathlib.Path(f"active_sessions/{session_id}")
    session_dir.mkdir(parents=True, exist_ok=True)

    # Define the final and temp paths inside the new directory
    final_file_path = session_dir / "session.json"
    temp_file_path = session_dir / "session.json.tmp"

    # --- ATOMIC WRITE ---
    try:
        # Write the complete session data to the temporary file
        with open(temp_file_path, "w") as f:
            f.write(new_session.model_dump_json(indent=4))
            
        # If the write is successful, attomically rename the temp file.
        os.rename(temp_file_path, final_file_path)
        
    except IOError as e:
        print(f"Error saving session {session_id}: {e}")
        raise


    return new_session

