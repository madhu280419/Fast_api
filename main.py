import requests
import json
import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/Cars/")
def get_car_details(model: str):
    with open("data.json", "r") as json_file:
        result = json.load(json_file)
        total_result = result[model]["drive"][0]
    
    return total_result

@app.post("/Cars/Info")
async def add_car_details(model:str):
    url = 'https://api.api-ninjas.com/v1/cars?model={}'.format(model,)
    payload = ""
    headers = {
        'X-Api-Key': 'a4f6SlPqvwrWa/xRiW1sGg==L32QYXtSlyISzGk3',  
        }

    response = requests.request("GET", url, headers=headers, data=payload)

    print("line number 23",response.status_code)
    
    data = response.json()
    
    result = {
        data[0]['model']:{
        "year": data[0]['year'],
        "fuel_type": data[0]['fuel_type'],
        "drive": data[0]['drive']
    }}
    if os.path.exists("data.json"):
        with open("data.json", "r") as f:
            try:
                existing_data = json.load(f)
            except json.JSONDecodeError:
                existing_data = {}
    else:
        existing_data = {}

# Update with new entry
    existing_data.update(result)

# Write back to file
    with open("data.json", "w") as f:
        json.dump(existing_data, f, indent=4)

    info = {"car details": result}
    return info

   

@app.put("/cars/Update/")
async def update_car_details(model: str, year: int, drive: str):
    with open("data.json", "r") as json_file:
        data = json.load(json_file)
    data = {
        "year": year,
        "drive": drive     
        }
    data.update({model:data})
    if model in data:
        data[model]["year"] = year,
        data[model]["drive"] = drive,
              
        
    with open("data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
        
    
    return {"message": "Car details updated", "data": data}

 
@app.delete("/Cars/Delete")
async def delete_car_details(drive):
    data = {
        "drive": drive
    }
    return {"Message": "Car Details Deleted", "data" : data}
