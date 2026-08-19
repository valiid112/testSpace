from fastapi import FastAPI
from Pydantic import BaseModel
import autogui 

# get mouse position

class mouseInput (BaseModel): 
  x: int = 0
  y: int = 0
  

app = FastAPI()
# post request func for keyboard emulation 
# listener for post request buttons gamepad button 

# post request func for mouse emulation 
# listener for gamepad axis 
@app.post(/mouseInput)
def(accumulatedMouseMovement : mouseInput): 
   # get current mouseposition
   # add accumulatedMouseMovement to mouse position & set duration to the javascript interval
   pass accumulatedMouseMovement

#listen on port 5002
