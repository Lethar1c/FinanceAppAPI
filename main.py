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





# example
# @app.post("/api/add-user/")
# def add_user(user_data: base_models.UserCreate):
#     user_list.append({"id": user_data.id, "name": user_data.name})
#     return {
#         "msg": "we got data succesfully",
#         "id": user_data.id,
#         "name": user_data.name
#     }
