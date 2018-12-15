 # <u>IMPORTANT NOTICE: </u>
<br>

## 1 - How to see our visualizations:

### Please open: "visualizing_main_maps.html" 
 in the main folder to see our main visualizations in one HTML page format


## 2 - How to read our report:

### As we choose to make a blog, please go to: https://ada-project.school.blog/
</br>
==============================
</br>
</br>
</br>

# Finding an utopian richness level and politicial regime based on the protests

# Abstract
A 150 word description of the project idea, goals, dataset used. What story you would like to tell and why? What's the motivation behind your project?

We are going to take the **GDELT v2** dataset, it inspired us the following project:

#### Analyzing the protests for leadership change, for rights and for change in institutions or regime around the world. 

First, we would like to find **correlations** between the number of each kind of protest and other variables (`richness` of the country, the `political regime`, the `date` (is there 
less and less protests in all countries?), etc).

Second, we want to find **how much the protests are heard** depending of the `country`, of the `political regime` or `date` (the dataset provides the number of mentions of the events
in sources, articles, etc). 

Third, finding a way to **visualize** each kind of protest on a world map would be interesting. 

Finally, the goal would be finding the composition of a utopia along richness level and political regime. We could face to a wrong result cause of dictatorial regimes where
there is no protest. The main point would be finding a way to determine our utopian regime. 

# Research questions

Are there **correlations** between number of protests (for rights or regime change) and other variables like richness of the country, political regime, etc?

Are the protests based in poor countries **less heard** than the ones in rich countries?

Are the **new technologies** a good thing for protests? (are the protests more and more heard thanks to internet, media, etc?)

Are there more protests in countries where the citizens enjoy **many rights**? (people in countries with many rights are free to protests, contrary to other regime like dictatorship. 
It can lead to this paradox: more protests where there are more rights)

# Dataset
List the dataset(s) you want to use, and some ideas on how do you expect to get, manage, process and enrich it/them. Show us you've read the docs and some examples, and you've a clear idea on what to expect. 
Discuss data size and format if relevant.

#### 1- Dataset description
GDELT 2.0
The "GDELT 2.0 Event Database" dataset is composed of all we need to achieve our project. Indeed, this main dataset is composed of:
> The date of the event (MonthYear)

> The code for the actor that includes geographic, class, ethnic, religious, and type classes (Actor1Code)

> The country code (Actor1CountryCode)

> The code which refers the event type (EventBaseCode)

> The number of mentions of the event (NumMentions) to see how much the event was covered/heard (there are also NumSources, NumArticles and AvgTone)


#### 2- How are we going to manage the data

All these codes can be found in other table, for instance the code that refers the event type can be found here: https://www.gdeltproject.org/data/lookups/CAMEO.eventcodes.txt
For our project, the code that we are looking for is **"14XX"** for instance: "1413: Demonstrate for rights"

Thanks to these data we can find, through the `event code`, the `date` and the `country code`, all the demonstrates for rights per country with the date.
We also have the chance to have the **number of mentions**, articles and sources related to each event, thanks to that we can compare how much each protest are heard depending
on the country (maybe more the country is rich more the protest is heard), on the date (with the new technologies maybe the protests are much more heard now).

#### 3- Dataset usable size

As the dataset is pretty big, we expected from it to get enough data to avoid finding conclusions not representative of the real world. However, as there are many kinds of events,

we hoped that the "protests" ones are enough represented. We verified that through a query: `SELECT COUNT(EventBaseCode) FROM [gdelt-bq:gdeltv2.events] WHERE EventBaseCode LIKE '14%'`
(because the code for protests starts by '14'). Thanks to this query we found the number of events stored related to protests.

We got: **3 879 769**, that seems to be enough for our project.

#### 4- Data description

- We are using the data available at the following link: https://bigquery.cloud.google.com/table/gdelt-bq:gdeltv2.events
This is a context of `big data`: around **400 000 000** of rows.

- As we said above, we need to filter this rows based on `event code` column. To achieve that, we need to know the meaning of this code:
**eventcodes.csv** gives us this data.

- Then, we need to get data on all the countries. Anything can be good, we need to have many variables to compare the impact of each ones on the number of protests.
**country_by_income.csv** and **countries_stats.csv** give us what we need. Thanks to these files, we have access to the average income, area of the country, population 
density, net migration, infant mortality, deathrate, climate, etc of each country
Got from: http://datatopics.worldbank.org/world-development-indicators/the-world-by-income-and-region.html and https://www.kaggle.com/fernandol/countries-of-the-world/version/1

- As each data define the country either with a code in ISO2, either in ISO3 or with the country name we need to convert each ones with the same convention.
For example, to define the `United-States of America`, the csv files use "USA", "US" or "United-States of America", so we need to do some process to put for instance
"USA" everywhere to falicitate analysis.
**country_codes_iso2_to_iso3.csv** and **country_code_to_name.csv** allow us to achieve these conversions, 
there are from: https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes/blob/master/all/all.csv

Let's see the **countries_stats.csv** file: 

data got from: https://www.kaggle.com/fernandol/countries-of-the-world/version/1

Data available: Country,
Region,Population,Area (sq. mi.),Pop. Density (per sq. mi.),Coastline (coast/area ratio),Net migration,Infant mortality (per 1000 births),GDP ($ per capita),Literacy (%),
Phones (per 1000),Arable (%),Crops (%),Other (%),Climate,Birthrate,Deathrate,Agriculture,Industry,Service.

Most of the variables don't need to be explain as `population`, `Area (sq. mi.)`, `Infant mortality`, etc. 
As we wordered the meaning of climate, here the explanation we found:

Meaning of climate:
1= Dry tropical, 
2= Wet tropical, 
3= Temperate humid subtropical and temperate continental, 
4= Dry hot summers and wet winters

- A json file, **world-countries.json**, from folium github: https://github.com/python-visualization/folium/blob/master/examples/data/world-countries.json
This json file helps us visualizing data on a world map

- **GDP growth world bank.csv** and **GINI per country worldbank.csv**
https://data.worldbank.org
These two dataset are the estimations of the Gross Domestic Product (GDP) and the Index of Inequality        (GINI) for each country , from 1960 to 2017. These datasets will be usefull economical and social indicator to understand the protestation in different countries.
We have access to the country code and the GDP index


- **DataCorruptionPerceptionIndex2000_2017.xlsx**
https://www.transparency.org
This data set shows the estimated Corruption index (political and buisness corruption) for each country from 1998 to 2015. 
We have access to the country code and the corruption perception index

- **Human Development Index (HDI).csv**
http://hdr.undp.org/en/data
Dataset of the HDI for each country from 1990 to 2017.
HDI a good indicator of the life expectancy and education of people in the country.
The definition of HDI from wikipedia:
"The Human Development Index (HDI) is a statistic composite index of life expectancy, education, and per capita income indicators"
We have access to  the country code and the Human Developement Index


- **World press freedom.csv** : 
https://rsf.org/fr/donnees-classement
https://en.wikipedia.org/wiki/Press_Freedom_Index 
This data-set shows the score of each country concerning the press freedom from 2002 to 2018
We have access to  the country code and the press Freedom index



# A list of internal milestones up until project milestone 2

**09/11/2018:** preprocess dataset (through GoogleBigData queries) to extract the usable data for our project (GDELT v2 data related to protests, tables with events code, country 
codes, etc). Getting all needed data to achieve our project.

**13/11/2018:** find a way to handle the data in its size (how to extract some statistics through a notebook).

**16/11/2018:** getting the first statistics and correlations we will need to answer the first research questions.

**18/11/2018:** we should have a better idea of the usable data at this point, it's time to define our definitive plan for the project.

**21/11/2018:** find a smart way to visualize a kind of protests (for instance: for rights) on a world map (thanks to folium).

**24/11/2018:** verifying the code quality, the comments, the documentations we provided for the milestone 2.

# A list of internal milestones until the presentation:

**29/11/2018:** deadline for finding new statistics on the countries (already more than 20 but it could be interesting to find other variables to evaluate.

**31/11/2018:** doing the analysis on each country but depending on the year. Finding a way to visualize the evolution of the protests numbers year per year

**02/12/2018:** finding impact of each variables on the protests number on each country based on the year
As we have the number of protests per year and statistics on each country per year, we should be able to see the influence of each variable.
For instance, is a country increase a lot his GDP ($ per capita) and not the other variables, and the number of protests decrease we could assume that they are related, etc
(that's just a simple example).

**05/12/2018:** exploiting the `AvgTone` column that gives us the average “tone” of all documents containing one or more mentions of this event.
The score ranges from -100 (extremely negative) to +100 (extremely positive). We would like to find what influence how much a protest is heard in the world.
Is a protest in a country with better `income per cap` more heard than another in an other country? (doing that with many variables)
Remark: more mentions there are about a protest, more this protest is "heard" in the world (more the `AvgTone` is high, more a protest is heard)
We would also use: `NumArticles`, `NumSources` and `NumMentions`

**08/12/2018:** we though about implementing a dynamic world map that show the protests days by days in a quick way (to help you understanding what we mean, here an
example of the result we would like: https://www.globalforestwatch.org/map

**10/12/2018:** we got almost all the results we wanted, we wrote good comments and explanations. The documentation is well done. We choose the way to present our work:
a 4-page PDF document or a data story in a platform like a blog post.

**14/12/2018:** We got all the result we wanted. Our visualizations are good. The report or the data story through a platform is done. 

**15/12/2018:** Last verifications. 

**21/12/2018:** Design of the poster, presentation ready. 

**Presentation J-2:** Printing the poster.
