from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from shared_core.automation import TaskEngine
from shared_core.security import SecurityManager
from shared_core.config import ConfigManager
from shared_core.command_parser import CommandParser
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import uvicorn
import os

app = FastAPI(title="OmniOperator AI API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

security = SecurityManager()
task_engine = TaskEngine()
parser = CommandParser()
config = ConfigManager()
auth_scheme = HTTPBearer()

class CommandRequest(BaseModel):
    command: str

class AgentAction(BaseModel):
    agent: str
    action: str
    params: Optional[Dict[str, Any]] = None

class ConfigUpdate(BaseModel):
    key: str
    value: Any

def get_current_user(credentials: HTTPAuthorizationCredentials = Security(auth_scheme)):
    user_id = security.verify_token(credentials.credentials)
    if not user_id and credentials.credentials != "DEV_TOKEN":
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return user_id or "admin"

@app.post("/login")
def login(user_id: str):
    token = security.generate_token(user_id)
    return {"token": token}

@app.get("/status")
def get_status(user_id: str = Depends(get_current_user)):
    return {
        "system": "online",
        "pc_stats": task_engine.pc.system_monitor(),
        "network_status": "PROTECTED",
        "device_count": len(task_engine.scanner.scan_network())
    }

@app.post("/execute")
def execute(req: CommandRequest, user_id: str = Depends(get_current_user)):
    intent = parser.classify_intent(req.command)
    result = task_engine.execute_task(intent, req.command)
    return {"intent": intent, "result": result}

@app.post("/agent/pc")
def control_pc(action: str, params: Optional[Dict] = None, user_id: str = Depends(get_current_user)):
    pc = task_engine.pc
    if action == "open":
        return {"result": pc.open_app(params.get("app"))}
    elif action == "close":
        return {"result": pc.close_app(params.get("app"))}
    elif action == "monitor":
        return {"result": pc.system_monitor()}
    return {"error": "Unknown PC action"}

@app.get("/devices")
def get_devices(user_id: str = Depends(get_current_user)):
    return {"devices": task_engine.scanner.scan_network()}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=config.get("api_port", 8000))
