# Project Geospatial

![portada](https://github.com/daniela-arias/Taller_Geo/blob/main/Data/0_iOecJNnpG0Pz1y0t.png)
​
# Objetivo
The objective of this project is to determine the perfect location for a new company in the gaming industry. 
​
- **Designers** --> near to companies that do design.
- **30% of the company** --> have at least 1 child.
- **Developers** --> to be near tech startups that have raised at least 1 Million dollars.
- **Executives** --> like Starbucks.
- **Account managers** --> travel a lot.
- **Average age between 25 and 40** -->some place to go party.
- **CEO** --> vegan.
- **Maintenance guy** --> basketball court
- **Dog—"Dobby"** --> hairdresser every month. 
​


Based on previous knowledge of the tech industry, the decision was made to analyze the requirements imposed by the company, in 3 cities:

Madrid, Bucharest and Dublin.
​

# Working plan 
​
The coordinates were chosen because they are key points in each of the chosen cities, which will bring strategic positioning to the company.
​

From the requirements presented to us by the company, a selection was made of those considered most relevant, both in terms of employee satisfaction and in relation to the work flow they should have. The analysis was determined in relation to the following variables: Schools, Starbucks, Airport, Nightclubs, dog grooming.


I made use of the Foursquare API to make the calls and obtain the data for each of our variables. To continue, the information was downloaded in json format, to be grouped in the Mongo DB tool. For this purpose, a collection was created for each city and all the information of the different variables was dumped into it.




​
​
The following resources have been used to achieve the objective of this project: 
​
-  [Foursquare API](https://foursquare.com/): get access to global data and  content from thousands trusted sources. To access all the necessary information about the resources surrounding the possible locations of the enterprise. 
- [MongoDB](https://www.mongodb.com/): is a document database with the scalability and flexibility that we want using querying and indexing.
​
​
### Structure of the project files
​
The structure of this project is composed of:
 1. A folder of notebooks: 
    
    a) **Cleaning_data.ipynb** -->the call is made to the Api of "Foursquare Developers", where we will get some preferred conditions where we want our company to be located

    b) **Geospatial_queries.ipynb** --> 


    c) **Results.ipynb** --> 
​
   

​
 2. scr folder: folder where all the .py files are stored with all the explained functions used during the whole project. The .py files included are: 
    a) CleaningFunctions used in the Cleaning_data.ipynb
    b) GeospatialFunctions used in the Geospatial_queries.ipynb
    c) ResultsFunctions used in the Results.ipynb
​
 3. Output: all the dataframes imported and saved in csv format. 
​
​
# Libraries

[sys](https://docs.python.org/3/library/sys.html)
​

[requests](https://pypi.org/project/requests/2.7.0/)
​

[pandas](https://pandas.pydata.org/)
​

[dotenv](https://pypi.org/project/python-dotenv/)
​

[pymongo](https://www.mongodb.com/2)
​

[json](https://docs.python.org/3/library/json.html)
​

[os](https://docs.python.org/3/library/os.html)
​

[geopandas](https://geopandas.org/)
​

[shapely](https://pypi.org/project/Shapely/)
​

[reduce](https://docs.python.org/3/library/functools.html)
​

[operator](https://docs.python.org/3/library/operator.html)
​

[import dumps](https://pymongo.readthedocs.io/en/stable/api/bson/json_util.html)
​
 
[re](https://docs.python.org/3/library/re.html)