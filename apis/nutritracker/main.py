import requests
from data.env_vars import *
import datetime as dt


def get_exercises(text: str) -> list:
    """ Evaluate text to get exercises done """
    body = {"query": text}
    response = requests.post(NUTRITIONIX_ENDPOINT, headers=N_HEADER, json=body)
    response.raise_for_status()
    exercises = [exercise for exercise in response.json()["exercises"]]
    print(exercises)
    return exercises


def format_answer(exercise: list) -> list:
    """ Checks exercises from Nutritionix and formats the response for the spreadsheet """
    today = dt.datetime.now()
    day_exercises = []
    for wo in exercise:
        body = {
            "date": dt.date.strftime(today, "%d/%m/%Y"),
            "time": dt.date.strftime(today, "%H:%M:%S"),
            "exercise": wo["name"].title(),
            "duration": wo["duration_min"],
            "calories": wo["nf_calories"]
        }
        day_exercises.append(body)
    return day_exercises


def read_spreadsheet() -> dict:
    """ Reads the spreadsheet and returns its content """
    header = S_HEADER
    response = requests.get(SHEETY_ENDPOINT, headers=header)
    response.raise_for_status()
    return response.json()


def write_spreadsheet(workout: list):
    """ adds a row of workout """
    header = S_HEADER
    body = {"workout": workout}
    response = requests.post(SHEETY_ENDPOINT, headers=header, json=body)
    response.raise_for_status()
    print(response.json())


# Getting exercises
answer = input("What exercises did you do today? ")
workouts = format_answer(get_exercises(answer))
print(workouts)
for item in workouts:
    write_spreadsheet(item)
read_spreadsheet()
