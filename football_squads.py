import requests
import config

on = True
repeat=""
while(on):


  # prints a list of all the countries
  url = f"https://v3.football.api-sports.io/countries"
  payload={}
  headers = {
    #Please not that this API Key is limited to 100 calls per day
    'x-rapidapi-key':config.api_key,
    'x-rapidapi-host': 'v3.football.api-sports.io'
  }
  response = requests.request("GET", url, headers=headers, data=payload)
  data = response.json()['response']
  for value in data: 
    print(value['name']) 


  #Prints a list of all the leagues (with id codes) from the chosen country
  inp = False
  country = input("\nPlease type a country from the list above: ")
  while(inp==False):
    for i in data: 
      if (i['name'] == country):
        inp=True
        url = f'https://v3.football.api-sports.io/leagues?country={country}'
        response = requests.request("GET", url, headers=headers, data=payload)
        data = response.json()['response']
        print("\n")
        for value in data: 
          print(value['league']['id'], ":", value['league']['name']) 
    if inp==False:
      country = input("\nWrong choice!\nPlease type a correct country from the list above: ")


  # Prints all the available seasons of the league
  league_id = input("\nPlease type a league Id: ")
  inp=False
  while(inp==False):
    try:
      for i in data:
        if (i['league']['id'] == int(league_id)):
          inp=True
          url = f'https://v3.football.api-sports.io/leagues?id={league_id}'
          response = requests.request("GET", url, headers=headers, data=payload)
          data = response.json()['response']
          print("\n")
          for value in data:
            for i in range (0, len(value['seasons']), 1):
              print(value['seasons'][i]['year'])
      if inp==False:
        league_id = input("\nWrong choice!\nPlease type a correct league Id from the list above: ")
    except:
      league_id = input("\nWrong choice!\nPlease type a correct league Id from the list above (use numbers only): ")
  

  # Prints all teams (and teams' id) from the chosen league and season 
  season = input("\nPlease type a season: ")
  inp=False
  while(inp==False):
    try: 
      for i in data:
        for z in range (0, len(value['seasons']), 1):
          if (value['seasons'][z]['year'] == int(season)):
            inp=True
            url = f'https://v3.football.api-sports.io/teams?league={league_id}&season={season}'
            response = requests.request("GET", url, headers=headers, data=payload)
            data = response.json()['response']
            print("\n")
            for value in data: 
              print(value['team']['id'], ":", value['team']['name'])
            break
      if inp==False:
        season = input("\nWrong choice!\nPlease type a season from the list above: ")      
    except:
      season = input("\nWrong choice!\nPlease type a correct season from the list above (use numbers only): ")


  #Prints the squad of a team in a specific season 
  team_id = input("\nPlease type a team id from the list above: ")
  inp=False
  while(inp==False):
    try:
      for i in data:
        if (i['team']['id'] == int(team_id)):
          inp=True
          url = f'https://v3.football.api-sports.io/players?team={team_id}&season={season}'
          response = requests.request("GET", url, headers=headers, data=payload)
          data = response.json()['response']
          if len(data)<=1:
            print("\nWe are sorry, the requested squad doesn't exist in our data")
          else: 
            print("\nHere is your requested squad:")
            for value in data: 
              print(value['player']['name'])
          repeat = input("\nDo you wish to see more squads? Yes/ No\n")
          while(repeat!="Yes" and repeat!="No"):
            repeat = input("\nWrong choice!\nPlease type a correct answer: Yes/ No\n")  
      if inp==False:
        team_id = input("\nWrong choice!\nPlease type a correct team id from the list above: ")      
    except:
      team_id = input("\nWrong choice!\nPlease type a correct team id from the list above (use numbers only): ")  

  if repeat == "Yes":
    on = True
  else:
    on = False
    print("\nThank you for using our service. We hope to see you back again!")