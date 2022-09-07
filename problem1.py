from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import sqlite3

con=sqlite3.connect('Y:\Manish_Choudhary\Assignment\Assignment-9\Problem-1\IMDB_Data.db')
cur=con.cursor()

cur.execute('''create table IMDB_Table (Rank,Title,Rating,Release_Date,Genre,Runtime,Director,Star,
                Country_Of_Origin,Language,Budget)''')

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.imdb.com/chart/top/')
#If it is not immediate available then it should wait maximum 10 sec
driver.implicitly_wait(10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

movie_details={'Rank':None, 'Title':None, 'Rating':None, 'Release_Date':None, 'Genre':None,
                'Runtime':None, 'Director':None, 'Star':None, 'Country_Of_Origin':None,
                'Language':None, 'Budget':None}

movies_link=driver.find_elements(By.XPATH,'//td[@class="titleColumn"]')
movie_url=[ele.find_element(By.TAG_NAME,'a').get_attribute('href') for ele in movies_link]

ranking=driver.find_elements(By.XPATH,'//td[@class="titleColumn"]')
rank_of_movies=[ele.text.split(".") for ele in ranking]

for url,rank in zip(movie_url,rank_of_movies):
    try:
        driver.get(url)
        driver.implicitly_wait(30)

        title=driver.find_element(By.XPATH,'//h1[@data-testid="hero-title-block__title"]').text
        try:
            rating=driver.find_element(By.XPATH,'//div[@data-testid="hero-rating-bar__aggregate-rating__score"]//span').text
        except:
            rating='Not Found'
        try:
            release_date=driver.find_element(By.XPATH,'//li[@data-testid="title-details-releasedate"]//child::ul').text.split("(")
            release_date=release_date[0]
        except:
            release_date="Not Found"
        try:
            genres=[item.text for item in driver.find_elements(By.XPATH,'//li[@data-testid="storyline-genres"]//child::li')]
            genre=",".join(genres)
        except:
            genre="Not Found"
        try:
            runtime=driver.find_element(By.XPATH,'//li[@data-testid="title-techspec_runtime"]//child::div').text
        except:
            runtime="Not Found"
        try:    
            cast=driver.find_elements(By.XPATH,'//div[@data-testid="title-pc-wide-screen"]//child::ul[@class="ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content baseAlt"]')
            director=cast[0].text
            star=[item.text for item in cast[2].find_elements(By.TAG_NAME,'li')]
            star=",".join(star)
        except:
            director="Not Found"
            star="Not Found"
        try:
            country_of_origin=driver.find_element(By.XPATH,'//li[@data-testid="title-details-origin"]//child::li').text
        except:
            country_of_origin="Not Found"
        try:
            language=driver.find_element(By.XPATH,'//li[@data-testid="title-details-languages"]//child::li').text
        except:
            language="Not Found"
        try:
            budget=driver.find_element(By.XPATH,'//li[@data-testid="title-boxoffice-budget"]//child::li').text
        except:
            budget=driver.find_element(By.XPATH,'//li[@data-testid="title-boxoffice-cumulativeworldwidegross"]//child::li').text
            
    except:
        print("Data not found")


    movie_details={'Rank':rank[0], 'Title':title, 'IMDB_Rating':rating[0]+rating[1], 'Release_Date':release_date,
                    'Genre':genre, 'Runtime':runtime, 'Director':director, 'Star':star, 
                    'Country_Of_Origin':country_of_origin, 'Language':language, 'Budget':budget}
    value=list(movie_details.values())
    print(rank[0],title,sep=";  ")
    cur.execute('Insert into IMDB_Table values(?,?,?,?,?,?,?,?,?,?,?)',value)
    con.commit()


driver.close()
con.close()