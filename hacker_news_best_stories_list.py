import httpx
import asyncio

#Function to get the titles of Hacker News best stories from the Hacker News API. Function parameter number_stories is used to tell the
#function how many stories to return. Use Python's asyncio library and the async requests library httpx. 

async def hnews(number_stories):
    #The Hacker News API has an endpoint that lists the item numbers for the stories currently ranked
    #best. Use async requests library httpx to get the item numbers. 
    
    #The documentation for the httpx library formats async requests in a format like below. 
    async with httpx.AsyncClient() as client:
        a = await client.get("https://hacker-news.firebaseio.com/v0/beststories.json?print=pretty")       
        #Get the response as json.
        a_json = a.json()
        
        #Function parameter number_stories is used in a list slice. We use a list slice since the original response includes 200 stories, more
        #than we need.
        b = a_json[0:number_stories] 
        
        #Create an empty list. To get data for each story in the best story list, we need to make a request to the endpoint for each story.
        list = []
        #c is the item number for each best story. We create a list of all these API endpoints. 
        for c in b:
            list.append(f"https://hacker-news.firebaseio.com/v0/item/{c}.json?print=pretty")
    
        #Creat an empty list list_reponse to add all the responses. 
        list_response = []

        #Add the reponses to list_response. Use await for async requests.
        for e in list:
            list_response.append(await client.get(e))

        #Create a list list_title_json, append the parsed titles. 
        list_title_json = []
        for f in list_response:
            list_title_json.append(f.json()["title"])
        
        #Print the titles in the terminal.
        for item in list_title_json:
            print(item + '\n' + '\n')

        return list_title_json
    
#Run the function with a function parameter of 20 stories.
asyncio.run(hnews(20))
