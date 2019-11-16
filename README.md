# Imdb_scrapper
> Web scrapper for IMDB    

**This script will receive a genre from user, then will tabularize top 50 movies as per US votes sorted in decreasing order of their Imdb ratings in a final_output.xlsx**

I have used web scrapping to get the data of various top rated movies of different genre from Imdb.    
I have implemented a **JSON file** to store the data from scraping and used **Pandas** to tabularize it.  

Use of the following genres are allowed (it makes up mostly all):  
  - Action
  - Adventure
  - Animation
  - Biography
  - Comedy
  - Crime
  - Documentary
  - Drama
  - Family
  - Fantasy
  - Film-Noir
  - History
  - Horror
  - Music
  - Musical
  - Mystery
  - Romance
  - Sci-Fi
  - Sport
  - Thriller
  - War
  - Western
  
  **Requirements**  
    - Platform: Linux    
      
  **Python Version >=3.7**
  
  **Installation**  
  Build form source:
  > $ git clone https://github.com/catchharsh/Imdb_scrapper  
  > $ cd Imdb_scrapper  
  > $ pip install beautifulsoup4  
  > $ pip install requests  
  > $ pip install openpyxl  

**TO RUN**
  > $ python3 scraper.py  
  > ('Enter your genre')  
  > $ python3 parse.py  
 
**NOTE**: It will create **final_output.xlsx** where the data is stored.
