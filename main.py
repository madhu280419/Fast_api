import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/Cars/")
def get_car_details(model):
    return {"message": "Welcome to the car info"}

@app.post("/Cars/Info")
async def add_car_details(model):
    return {"Car details Received" }

@app.put("/Cars/Update")
async def update_car_details(year,drive ):
    data = {
        "year": year,
        "drive":drive     
        }
    return {"message": "Car details updated", "data": data}

    
    url = 'https://api.api-ninjas.com/v1/cars?model={}'.format(model)
    payload = ""
    headers = {
        'X-Api-Key': 'a4f6SlPqvwrWa/xRiW1sGg==L32QYXtSlyISzGk3',  
        }

    response = requests.request("GET", url, headers=headers, data=payload)

    print("line number 23",response.status_code)
    data = response.json()
    
    result =  {data[0].get['make'],
        data[0].get['year'],
        data[0].get['transmission'],
        data[0].get['fuel_type'],
        data[0].get['model']
            }
        
    info = {"car details": result}
    return info

@app.delete("/Cars/Delete")
async def delete_car_details(drive):
    data = {
        "drive": drive
    }
    return {"Car Details Deleted": data}
