from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from shared_core.automation import TaskEngine
from shared_core.security import SecurityManager
from shared_core.config import ConfigManager
from shared_core.command_parser import CommandParser
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="OmniOperator AI API")
security = SecurityManager()
task_engine = TaskEngine()
parser = CommandParser()
config = ConfigManager()
auth_scheme = HTTPBearer()

class CommandRequest(BaseModel):
    command: str

def get_current_user(credentials: HTTPAuthorizationCredentials = Security(auth_scheme)):
    user_id = security.verify_token(credentials.credentials)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return user_id

@app.post("/login")
def login(user_id: str):
    # Simplified login for now
    token = security.generate_token(user_id)
    return {"token": token}

@app.post("/execute")
def execute(req: CommandRequest, user_id: str = Depends(get_current_user)):
    intent = parser.classify_intent(req.command)
    result = task_engine.execute_task(intent, req.command)
    return {"intent": intent, "result": result}

@app.get("/status")
def get_status(user_id: str = Depends(get_current_user)):
    return {
        "system": "online",
        "pc_stats": task_engine.pc.system_monitor(),
        "network": "secure",
        "devices_count": len(task_engine.scanner.scan_network())
    }

@app.get("/memory/search")
def search_memory(query: str, user_id: str = Depends(get_current_user)):
    return {"results": task_engine.memory.search_memory(query)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=config.get("api_port", 8000))
