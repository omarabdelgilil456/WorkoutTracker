from datetime import datetime
import requests


APP_ID = "xxxxxxxx"
APP_KEY = "xxxxxxxxxxxx"

exercise_endpoint = "https://trackapi.nutritionix.com//v2/natural/exercise"

header = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}
gfbbfj
info = {
    "query": input("what exercise you did today?: "),
    "gender": "male",
    "weight_kg": 92,
    "height_cm": 184,
    "age": 20,
}

response = requests.post(url=exercise_endpoint, headers=header, json=info)
exercise_info = response.json()["exercises"]



sheety_api = "https://api.sheety.co/5bfb930599e5698b325df2b05aebf054/myWorkouts/workouts"
authen = {
    "Authorization": "Bearer xxxxxxxxxx"
}
for exercise in exercise_info:
    ex_name = exercise["name"]
    ex_dur = exercise["duration_min"]
    ex_cal = exercise["nf_calories"]
    add = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise": ex_name.title(),
            "duration": ex_dur,
            "calories": ex_cal,
        }
    }
    print(exercise)
    sheety_resposnse = requests.post(url=sheety_api, headers=authen , json=add)
    print(sheety_resposnse.raise_for_status())
