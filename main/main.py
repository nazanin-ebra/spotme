



from typing import Union

from fastapi import FastAPI
import test_a

l_x ='35.886130662551494'
l_y = '31.96670420225861'
l_t ='256 Zahran St'
l2='35.85945240415428'
l3 ='31.94664179161133'

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Amazon"}


@app.get("/get/location/")
def loc():
    return ro(l_x,l_y)
        
    
    