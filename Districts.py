from cowin_api import CoWinAPI

state_id = '21' #Enter the State ID of your state
cowin = CoWinAPI()
districts = cowin.get_districts(state_id)
print(districts)