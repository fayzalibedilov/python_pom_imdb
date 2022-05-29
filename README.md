A test case using ***Page Object*** Model that:  
&emsp;  goes to IMDB ["Sign In"](https://www.imdb.com/registration/signin) link  
&emsp;  adds a movie to the "Watchlist"  
&emsp;  goes to "Watchlist" page and checks if the movie was added  
  
  
Requirements to run  
&emsp;  [Python.3x](https://www.python.org/downloads/)  
&emsp;  [Selenium WebDriver](https://www.selenium.dev/)  
&emsp;  [pytest](https://docs.pytest.org/en/7.1.x/)   
  
***Note*** if you want to run it in Windows Machine or different browser make sure to install the compatible webdriver, [chromedriver](https://chromedriver.chromium.org/downloads) choose according to your webdrowser version for Chrome browser, and [geckodriver](https://github.com/mozilla/geckodriver/releases) for Firefox browser, add to the path and mention the path to the webdriver in test_case.py file  

Use ```pytest -s``` to run from terminal to capture print statements in terminal  
Or ```python -m unittest```  

