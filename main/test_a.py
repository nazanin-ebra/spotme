import boto3
from pprint import pprint
from datetime import datetime

l_x ='35.886130662551494'
l_y = '31.96670420225861'
l_t ='256 Zahran St'
l2='35.85945240415428'
l3 ='31.94664179161133'

def lprint(map_dict:dict):
    with open("testing_los.txt",'a', encoding = 'utf-8') as f:
        pprint(map_dict, f)
        pprint(map_dict)
        f.write(f"\n{map_dict}\n")
        print("/n---------------------/n")
        
    
client = boto3.client('location')

    




list_indexes = client.list_place_indexes(
    MaxResults=50,
    # NextToken='string'
)



search_coords = client.search_place_index_for_position(
    IndexName='Teckathon',
    Language='en',
    MaxResults=50,
    Position=[
        float(l_x),float(l_y)
    ]
)
def ro(x,y,z,r):
    ctime = client.calculate_route(
        CalculatorName='Teckathon',
        CarModeOptions={
            'AvoidFerries':False,
            'AvoidTolls':False
        },
        DepartNow=True,
        DeparturePosition=[
            float(x),float(y)
        ],
        # DepartureTime=datetime.now(),
        DestinationPosition=[
            float(z),float(r)
        ])
        
    list_maps = client.list_maps()


    # lprint(list_maps)

    # lprint(list_indexes)

    # lprint(search_coords)

    # # create_place_index()
    # response = client.search_place_index_for_position(
    #     IndexName='string',
    #     Language='string',
    #     MaxResults=123,
    #     Position=[
    #         123.0,
    #     ]
    # )



# calculate_route()
