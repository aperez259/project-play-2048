from selenium import webdriver

from selenium.webdriver.common.keys import Keys

def play2048( times ):


    browser = webdriver.Firefox()
    browser.get('https://gabrielecirulli.github.io/2048/')
    
    htmlElem = browser.find_element_by_tag_name('html')
    FinalScoreElem = browser.find_element_by_class_name('score-container')
   
    moves = 0 
    for moves in range(times):
        htmlElem.send_keys(Keys.UP)
        htmlElem.send_keys(Keys.RIGHT)
        htmlElem.send_keys(Keys.DOWN)
        htmlElem.send_keys(Keys.LEFT)  
        moves += 1


    print('The final score was = '+FinalScoreElem.text)
