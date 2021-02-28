# Pandemic-Insights
The purpose of this project is to analyze the spread of Covid-19 in countries all around the world and classify them into different groups based on the similarity of their daily cases patterns.

## Usage
### Prerequisites
Make sure you installed Python 3.8 and all the libraries used in this project.
### Run
Simply run
```
$ python3.8 main.py
````
Then you will be asked to choose a method for creating the distane matrix. After that, you will be asked to choose a clustering algorithm you want to apply. At the end, the output will be:
* List of all the countries with their labels
* Silhouette score of the result
* Graph of the result
### 
## Dataset
[CSSE COVID-19 Time Series](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series) - This project uses time series table for the global confirmed cases from the JHU CSSE COVID-19 Dataset.
### Note
Pandemic-Insights works with any version of this dataset. You can simply change the current one with another version of this dataset.
