# NLP-project-Github

### Description 
- Project analyzing text scraped from github repos related to cryptocurrency

### Goals
- Analyze keywords from top 5 programming languages
- Predict primary programming language for repo

---------------------------------
### Data Dictionary
---
| Column | Definition | Data Type |
| ----- | ----- | ----- |
|repo| github url endpoint| object|
|readme_contents| text from repo README| object|

---------------------------------------------------
| Target | Definition | Data Type |
| ----- | ----- | ----- |
|language| primary language of repo| object|

--------------------------------------------------

### Project Plan
1. Scrape README data from Github repos using the github api to build a list of repos and use functions in acquire.py to scrape
2. Prepare data by using clean, lemmatize, and remove_stopword functions in prepare.py
3. Explore words and bigrams for top 5 programming languages
4. Create bar charts and word clouds
5. Create classification model to predict primary repo langauge using text from READMEs

---------------------------------------------------
### Project Takeaways
- As expected there a lot of repos for cryptocurrency core source code, wallets, nodes, mining software, and trading bots
- Linear support vector classification achieved the greatest results with limited data ~75% accuracy
- Python and Javascript were dominant languages

--------------------------------------------------
### How to re-create
- All necessary files are in this repository so the best method would be to git clone and run scrape_github_data()
- Add/remove any repo urls in the acquire.py file
- Data cleaning notebooks are available as well and can be experimented with.
- Run Final_NLP notebook. 
- Adjust exploration and modeling to your liking
