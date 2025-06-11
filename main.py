import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/cars/welcome")
def get_car_details():
    return {"message": "Welcome to the car info"}

@app.post("/cars/info")
async def update_car_details(model):


    url = 'https://api.api-ninjas.com/v1/cars?model={}'.format(model)
    payload = ""
    headers = {
    'X-Api-Key': 'a4f6SlPqvwrWa/xRiW1sGg==L32QYXtSlyISzGk3',  
    
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print("line number 23",response.status_code)
    data = response.json()
 
    result =  {data[0]['make'],
               data[0]['year'],
               data[0]['transmission'],
               data[0]['fuel_type'],
               data[0]['model']
              }
    
    ph = {"car details": result}
    return ph