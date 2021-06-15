
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movies_from_tastedive("Bridesmaids")
# get_movies_from_tastedive("Black Panther")
import requests
import requests_with_caching

def get_movies_from_tastedive(movie_name):
    result=requests_with_caching.get("https://tastedive.com/api/similar", params= {"type":"movies", "limit":"5", "q":movie_name}) 
    results=result.json()
    return results
print(get_movies_from_tastedive('Captain Marvel'))
print(get_movies_from_tastedive('Sherlock Holmes'))



# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))
# extract_movie_titles(get_movies_from_tastedive("Black Panther"))
import requests
import requests_with_caching

def get_movies_from_tastedive(movie_name):
    result=requests_with_caching.get("https://tastedive.com/api/similar", params= {"type":"movies", "limit":"5", "q":movie_name}) 
    results=result.json()
    return results
def extract_movie_titles(results):
    output=[]
    for i in results['Similar']['Results']:
        output.append(i['Name'])
    return output
          



# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_related_titles(["Black Panther", "Captain Marvel"])
# get_related_titles([])
import requests
import requests_with_caching

def get_movies_from_tastedive(movie_name):
    result=requests_with_caching.get("https://tastedive.com/api/similar", params= {"type":"movies", "limit":"5", "q":movie_name}) 
    results=result.json()
    return results
def extract_movie_titles(results):
    output=[]
    for i in results['Similar']['Results']:
        output.append(i['Name'])
    return output


        
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_related_titles(["Black Panther", "Captain Marvel"])
# get_related_titles([])
import requests
import requests_with_caching

def get_movies_from_tastedive(movie_name):
    result=requests_with_caching.get("https://tastedive.com/api/similar", params= {"type":"movies", "limit":"5", "q":movie_name}) 
    results=result.json()
    return results
def extract_movie_titles(results):
    output=[]
    for i in results['Similar']['Results']:
        output.append(i['Name'])
    return output


def get_related_titles(titles):
    out=[]
    for i in titles:
        result= get_movies_from_tastedive(i)
        header= extract_movie_titles(result)
        for j in header:
            if j in out:
                continue
            else:
                out.append(j)
    return out          
   
        
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_data("Venom")
# get_movie_data("Baby Mama")
import requests
import requests_with_caching
import json 

def get_movie_data(data):
    result=requests_with_caching.get('http://www.omdbapi.com/', params={"t": data , "r":"json" })
    get=result.json()
    return get                                 
            
    
    
    # some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_rating(get_movie_data("Deadpool 2"))
import requests
import requests_with_caching
import json 

def get_movie_data(data):
    result=requests_with_caching.get('http://www.omdbapi.com/', params={"t": data , "r":"json" })
    get=result.json()
    return get  
def get_movie_rating(name):
    rating=0
    for i in name["Ratings"]:
        if i['Source']== "Rotten Tomatoes":
            rating =i['Value']
            rating=rating.strip("%")
    return int(rating)
        
    
    

    
    
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])

import requests
import requests_with_caching

def get_movies_from_tastedive(movie_name):
    result=requests_with_caching.get("https://tastedive.com/api/similar", params= {"type":"movies", "limit":"5", "q":movie_name}) 
    results=result.json()
    return results
def extract_movie_titles(results):
    output=[]
    for i in results['Similar']['Results']:
        output.append(i['Name'])
    return output


def get_related_titles(titles):
    out=[]
    for i in titles:
        result= get_movies_from_tastedive(i)
        header= extract_movie_titles(result)
        for j in header:
            if j in out:
                continue
            else:
                out.append(j)
    return out          
   
# get_movie_rating(get_movie_data("Deadpool 2"))
import requests
import requests_with_caching
import json 

def get_movie_data(data):
    result=requests_with_caching.get('http://www.omdbapi.com/', params={"t": data , "r":"json" })
    get=result.json()
    return get  
def get_movie_rating(name):
    rating=0
    for i in name["Ratings"]:
        if i['Source']== "Rotten Tomatoes":
            rating =i['Value']
            rating=rating.strip("%")
    return int(rating)
        
def get_sorted_recommendations(L):
    output=[]
    titles=get_related_titles(L)
    d={}
    for i in titles:
        data = get_movie_data(i)
        recomend= get_movie_rating(data)
        d[i]=recomend
    s=sorted(d , key =lambda x:(d[x] ,x ),reverse=True)
   
    return s
    

        
    

    
    

        
       
        
          
        
   







































