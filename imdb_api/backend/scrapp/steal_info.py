import json
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.imdb.com/chart/top/')
films = driver.find_elements_by_css_selector("tbody.lister-list tr")
films_info = []
for film in films:
    films_info.append({
        "Title": film.find_element_by_css_selector("td.titleColumn a").text,
        "Rating": film.find_element_by_css_selector("td.ratingColumn.imdbRating strong").text,
        "Year": int(film.find_element_by_css_selector("td.titleColumn span").text.replace("(", "").replace(")", "")),
    })
    
ejson = json.dumps(films_info)
with open('ejson.json', 'w') as f:
    json.dump(films_info, f)
    
print('Saved to file')
