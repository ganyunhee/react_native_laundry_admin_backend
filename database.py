from model import UserCreate, DailyReportCreate, StatusReportCreate, CycleCountCreate, ReceivablesCheck, TransferLaundryUpdate

# MongoDB driver
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
database = client.LaundryAdmin
collection = database.admin

async def login(username: str, password: str):
    user = await collection.find_one({"username": username, "password": password})
    return user

async def signup(user_data: UserCreate):
    user = user_data.model_dump()
    result = await collection.insert_one(user)
    return str(result.inserted_id)

async def submit_daily_report(daily_report_data: DailyReportCreate):
    report = daily_report_data.model_dump()
    result = await collection.insert_one(report)
    return str(result.inserted_id)

async def submit_status_report(status_report_data: StatusReportCreate):
    report = status_report_data.model_dump()
    result = await collection.insert_one(report)
    return str(result.inserted_id)

async def upload_cycle_count_image(cycle_count_data: CycleCountCreate):
    image_data = cycle_count_data.dict()
    result = await collection.insert_one(image_data)
    return str(result.inserted_id)

async def check_receivables(client_code_data: ReceivablesCheck):
    query = {"client_code": client_code_data.client_code}
    receivables_data = await collection.find_one(query, {"receivable_amt": 1, "_id": 0})
    return receivables_data

async def transfer_laundry(update_data: TransferLaundryUpdate):
    query = {"client_code": update_data.client_code}
    update_value = {"$set": {"client_code": f"{update_data.branch}{update_data.client_code}"}}
    result = await collection.update_one(query, update_value)
    return result.modified_count
