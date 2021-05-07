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
### Hypotheses
**1. Is the mean defect rate significantly different for July/August than Sept/Oct?**
- null_hypothesis =  
- alternative_hypothesis = 

--------------------------------------------------

### Project Plan
1. Acquire data  
2. Prepare data by removing unnecessary/redundant columns, dealing with nulls, and scaling variables for use with ML models
3. Explore data using functions in explore.py as well as jointplot, pairplot, and heatmap, etc.
4. Cluster the data into relevant groups if possible
5. Create ML models based on clusters and choose best performing for test data

---------------------------------------------------
### Project Takeaways
- 

--------------------------------------------------
### How to re-create
- All necessary files are in this repository so the best method would be to git clone and run wrangle_semicon()
- If you would like to acquire manually, download the secom.data and labels.data files and use pd.read_csv() and merge the two
- Exploration and data cleaning notebooks are available as well and can be experimented with.
- Run Final_semicon notebook. 
- Adjust exploration and modeling to your liking
