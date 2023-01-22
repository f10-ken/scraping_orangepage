
import requests
from bs4 import BeautifulSoup


def recipes_menus(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser') 


    recipes_class = soup.find('div', id = 'recipe_list', class_ = 'recipesList')
    h2_tit_tags = recipes_class.find_all('h2', class_='tit')
    h2_tit_strs = [x.string for x in h2_tit_tags ]
    return h2_tit_strs


if __name__ == "__main__":
    url = "https://www.orangepage.net/recipes/search?search_recipe%5Bkeyword%5D=%E9%B6%8F%E8%82%89"
    print(recipes_menus(url))
    
    
    