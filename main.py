from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import (
    login,
    signup,
    submit_daily_report,
    submit_status_report,
    upload_cycle_count_image,
    check_receivables,
    transfer_laundry
)

from model import (
    UserCreate, 
    DailyReportCreate, 
    StatusReportCreate, 
    CycleCountCreate, 
    ReceivablesCheck, 
    TransferLaundryUpdate
)

app = FastAPI()

origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ROUTES

# Root

@app.get("/")
def read_root():
    return {"Hello":"World"}

# Main Menu

@app.get("/main")
def main_page_loaded():
    return {"message": "Main Menu Page loaded successfully"}

# Pages

# Pages - Login

@app.get("/login")
def login_page_loaded():
    return {"message": "Login Page loaded successfully"}

@app.post("/login")
async def user_login(username: str, password: str):
    user = await login(username, password)
    if user:
        return {"message": "Login successful", "user": user}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")

# Pages - Sign Up
    
@app.get("/signup")
def signup_page_loaded():
    return {"message": "Sign Up Page loaded successfully"}

@app.post("/signup")
async def user_signup(user_data: UserCreate):
    user_id = await signup(user_data)
    return {"message": "User created successfully", "user_id": user_id}

# Pages - Daily Report

@app.get("/daily")
def daily_page_loaded():
    return {"message": "Daily Report Page loaded successfully"}

@app.post("/daily")
async def daily_report_submission(daily_report_data: DailyReportCreate):
    report_id = await submit_daily_report(daily_report_data)
    return {"message": "Daily report submitted successfully", "report_id": report_id}

# Pages - Status Report

@app.get("/status")
def status_page_loaded():
    return {"message": "Status Report Page loaded successfully"}

@app.post("/status")
async def status_report_submission(status_report_data: StatusReportCreate):
    report_id = await submit_status_report(status_report_data)
    return {"message": "Status report submitted successfully", "report_id": report_id}

# Pages - Branch Time-In

@app.get("/time_in")
def time_in_page_loaded():
    return {"message": "Branch Time-In Page loaded successfully"}

# Pages - Cycle Count Upload

@app.get("/cycle_count")
def cycle_count_page_loaded():
    return {"message": "Cycle Count Upload Page loaded successfully"}

@app.post("/cycle_count")
async def cycle_count_image_upload(cycle_count_data: CycleCountCreate):
    image_id = await upload_cycle_count_image(cycle_count_data)
    return {"message": "Cycle count image uploaded successfully", "image_id": image_id}


# Pages - Check Receivables

@app.get("/receivables")
def receivables_page_loaded():
    return {"message": "Check Receivables Page loaded successfully"}

@app.post("/receivables")
async def check_receivables_endpoint(client_code_data: ReceivablesCheck):
    receivables_data = await check_receivables(client_code_data)
    return {"message": "Receivables data retrieved successfully", "receivables_data": receivables_data}


# Pages - Transfer Laundry

@app.get("/transfer")
def transfer_page_loaded():
    return {"message": "Transfer Laundry Page loaded successfully"}

@app.put("/transfer")
async def transfer_laundry_endpoint(update_data: TransferLaundryUpdate):
    modified_count = await transfer_laundry(update_data)
    return {"message": f"Laundry transferred successfully. Modified count: {modified_count}"}