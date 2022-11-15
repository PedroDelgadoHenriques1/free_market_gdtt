from fastapi import FastAPI
from tests import *

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
    
@app.get("{dev_id}/projects/{id}")
def show_projects(id: int):
	try:
		return {"projects": devs[id].projetos}
	except:
		return "endpoint não encontrado"
	
@app.get("ads/all")
def show_ads():
	return {"ads": ads}
	
@app.get("{enterprise_id}/ads")
def enterprise_ads(enterprise_id: int):
	return {"ads": ads} #all ads of enterprise X

@app.get("{enterprise_id}/ads/{ad_id}")
def find_ad(enterprise_id: int, ad_id: int):
	return {"ads": ads} #one ad of one enterprise
	
@app.get("/devs")
def show_devs():
	return {"devs": devs}
	
@app.get("/devs/{dev_id}")
def find_dev(id: int):
	return {"devs": devs}
	
@app.get("/enterprises")
def show_enterprises():
	return {"enterprise": enterprises}

@app.get("/enterprises/{enterprise_id}")
def find_enterprise(id: int):
	return {"enterprise": enterprises[id]}
