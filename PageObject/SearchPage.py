from PageObject import BasePage


search_input_textbox = "//input[@name='q']"

class SearchPage(object):
    
    def __init__(self, driver):
        self.driver = driver
        base = BasePage.BasePage(driver)
        self.base = base

    def search_text(self, text):
        self.base.enter(search_input_textbox, text)
        self.base.submit(search_input_textbox)
        