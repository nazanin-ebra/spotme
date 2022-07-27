import boto3
from pprint import pprint

def log(map_dict:dict):
    with open("testing_logs.txt",'a', encoding = 'utf-8') as f:
        pprint(map_dict, f)
        
    
        
    
client = boto3.client('location')


list_maps = client.list_maps()
pprint(list_maps)
log(list_maps)



