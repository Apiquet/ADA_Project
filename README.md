# Finding an utopian richness level and politicial regime based on the protests

# Abstract
A 150 word description of the project idea, goals, dataset used. What story you would like to tell and why? What's the motivation behind your project?

We are going to take the **GDELT v2** dataset, it inspired us the following project:

#### Analysing the protests for leadership change, for rights and for change in institutions or regime around the world. 

First, we would like to find **correlations** between the number of each kind of protest and other variables (`richness` of the country, the `political regime`, the `date` (is there 
less and less protests in all countries?), etc).

Second, we want to find **how much the protests are heard** depending of the `country`, of the `political regime` or `date` (the dataset provides the number of mentions of the events
in sources, articles, etc). 

Third, finding a way to **visualize** each kind of protest on a world map would be interesting. 

Finally, the goal would be finding an **utopian richness level and political regime**. We could face to a wrong result cause of dictatorial regimes where there is no protest. 
The main point would be finding a way to determine our utopian regime. 

# Research questions

Are there **correlations** between number of protests (for rights or regime change) and other varibales like richness of the country, political regime, etc?

Are the protests based in poor countries **less heard** than the ones in rich countries?

Is the **new technologies** a good thing for protests? (are the protests more and more heard thanks to internet, media, etc?)

Are there more protests in countries with **many rights**? (people in countries with many rights are free to protests, contrary to other regime like dictatorship. It can lead to this paradox: more protests where there are more rights)

# Dataset
List the dataset(s) you want to use, and some ideas on how do you expect to get, manage, process and enrich it/them. Show us you've read the docs and some examples, and you've a clear idea on what to expect. Discuss data size and format if relevant.

#### 1- Dataset description

The "GDELT 2.0 Event Database" dataset is composed of all we need to achieve our project. Indeed, this main dataset is composed of:
> The date of the event (MonthYear)

> The code for the actor that includes geographic, class, ethnic, religious, and type classes (Actor1Code)

> The country code (Actor1CountryCode)

> The code which refers the event type (EventBaseCode)

> The number of mentions of the event (NumMentions) to see how much the event was covered/heard (there are also NumSources, NumArticles and AvgTone)

(There are more data but less relevant for our project)

#### 2- How are we going to manage the data

All these codes can be found in other table, for instance the code that refers the event type can be found here: https://www.gdeltproject.org/data/lookups/CAMEO.eventcodes.txt
For our project, the code that we are looking for is **"14XX"** for instance: "1413: Demonstrate for rights"

Thanks to these data we can find, through the `event code`, the `date` and the `country code`, all the demonstrates for rights per country with the date.
We also have the chance to have the **number of mentions**, articles and sources related to each event, thanks to that we can compare how much each protest are heard depending
on the country (maybe more the country is rich more the protest is heard), on the date (with the new technologies maybe the protests are much more heard now).

#### 3- Dataset usable size

As the dataset is pretty big, we expected from it to get enough data to avoid finding conclusions not representative of the real world. However, as there are many kinds of events,

we hoped that the "protests" ones are enough represented. We verified that through a query: SELECT COUNT(EventBaseCode) FROM [gdelt-bq:gdeltv2.events] WHERE EventBaseCode LIKE '14%'
(because the code for protests starts by '14'). Thanks to this query we found the number of events stored related to protests.

We got: **3 879 769**, that seems to be enough for our project.

# A list of internal milestones up until project milestone 2

**09/11/2018:** preprocess dataset (through GoogleBigData queries) to extract the usable data for our project (GDELT v2 data related to protests, tables with events code, country 
codes, etc). Getting all data we need to achieve our project.

**13/11/2018:** find a way to handle the data in its size (how to extract some statistics through a notebook).

**16/11/2018:** getting the first statistics and correlations we will need to answer the first reseach questions.

**18/11/2018:** we should have a better idea of the usable data at this point, it's time to define our definitive plan for the project.

**21/11/2018:** find a smart way to visualize a kind of protests (for instance: for rights) on a world map (thanks to folium).

**24/11/2018:** verifying the code quality, the comments, the documentations we provided for the milestone 2.

# Questions for TAa
Add here some questions you have for us, in general or project-specific.
