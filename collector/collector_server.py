from fastapi import FastAPI  
import uvicorn
import json

app = FastAPI()  


def load_json_file( filename ) :
    with open( filename, 'r' ) as f :
        data = json.load( f )
    return data

@app.get("/")
def read_root():
    # return {"\n\nI am": "alive\n\n"}
    return "\n\n I am alive !!!\n\n"


@app.get("/system_info")
def get_and_send_system_info() : 
    system_info = load_json_file( "/var/Server_monitoring/collector/collected_data.json" )
    print( system_info )
    # return system_info
    return load_json_file( "/var/Server_monitoring/collector/collected_data.json" )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)