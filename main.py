import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import base_models
import db

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/config/set-config/")
def set_config(data: base_models.SetConfig):
    return db.set_config(data.user_id, data.language, data.theme)


@app.post("/api/config/set-user-theme/")
def set_user_theme(data: base_models.SetTheme):
    return db.set_theme(data.user_id, data.theme)


@app.post("/api/config/set-user-language/")
def set_user_language(data: base_models.SetLanguage):
    return db.set_language(data.user_id, data.language)


@app.get("/api/config/get-user-config/")
def get_user_config(user_id: int):
    return db.get_user_config(user_id)


@app.post("/api/create-new-account/")
def create_new_account(data: base_models.CreateNewAccount):
    return db.create_new_account(data.user_id, data.name, data.description)


@app.get("/api/get-account-list/")
def get_account_list(user_id: int):
    return db.get_account_list(user_id)


@app.post("/api/add-new-income/")
def add_new_income(data: base_models.AddNewIncome):
    return db.add_new_income(data.account_id, data.sum, data.name, data.description, data.category)


@app.post("/api/add-new-outcome/")
def add_new_outcome(data: base_models.AddNewOutcome):
    return db.add_new_outcome(data.account_id, data.sum, data.name, data.description, data.category)


@app.post("/api/add-new-transaction/")
def add_new_transaction(data: base_models.AddNewTransaction):
    return db.add_new_transaction(data.from_account_id, data.to_account_id, data.sum, data.description)


@app.get("/api/get-user-balance/")
def get_account_balance(account_id: int):
    return round(db.get_account_balance(account_id), 2)


# example
# @app.post("/api/add-user/")
# def add_user(user_data: base_models.UserCreate):
#     user_list.append({"id": user_data.id, "name": user_data.name})
#     return {
#         "msg": "we got data succesfully",
#         "id": user_data.id,
#         "name": user_data.name
#     }
