#!/bin/python3

from fastapi import FastAPI  
import uvicorn
import json
import os

app = FastAPI()  
CWD = os.getcwd()
OUTPUT_FILE = "collected_data.json"

def load_json_file( filename ) :
    with open( filename, 'r' ) as f :
        data = json.load( f )
    return data

@app.get("/")
def read_root():
    return 'I am alive !!!'


@app.get("/system_info")
def get_and_send_system_info() :
    return load_json_file( os.path.join( CWD, OUTPUT_FILE ) )

if __name__ == "__main__":
    uvicorn.run( app, host="0.0.0.0", port=8000 )