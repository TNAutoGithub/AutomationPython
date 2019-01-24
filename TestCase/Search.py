from PageObject import SearchPage
from selenium import webdriver

class SearchAction:
    
    dr = webdriver.Chrome()
    dr.get("http://www.google.com")
    
    def verify_user_can_search(self):
        search = SearchPage.SearchPage(self.dr)
        search.search_text("search text")

    dr.close()