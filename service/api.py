from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import uuid
from datetime import datetime

app = FastAPI()

class SessionRequest(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    context_type: Optional[str] = "general"

class SessionResponse(BaseModel):
    session_id: str
    name: str
    description: Optional[str]
    context_type: str
    created_at: str
    status: str

@app.post("/session", response_model=SessionResponse)
async def create_session(session_data: SessionRequest):
    """Create a new session"""
    try:
        session_id = str(uuid.uuid4())
        session_name = session_data.name or f"Session_{session_id[:8]}"
        
        session = SessionResponse(
            session_id=session_id,
            name=session_name,
            description=session_data.description,
            context_type=session_data.context_type,
            created_at=datetime.now().isoformat(),
            status="active"
        )
        
        return session
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create session: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)