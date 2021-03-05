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

## Dataset
[CSSE COVID-19 Time Series](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series) - This project uses time series table for the global confirmed cases from the JHU CSSE COVID-19 Dataset.
### Note
Pandemic-Insights works with any version of this dataset. You can simply change the current one with another version of this dataset.

## Results
One of the best results that could be obtained is shown below with graphs of 5 representatives of each cluster. Most of the clusters are mainly consists of countries that are geographically close to each other. Cluster 1 is mostly consists of Western European countries, cluster 2: mostly South American countries, cluster 3: mostly African countries, cluster 4: mostly Eastern European countries, cluster 5: China regions, cluster 6: mostly states of Australia.

<img width="555" alt="1" src="https://user-images.githubusercontent.com/41535744/110163493-502d1480-7e05-11eb-9d02-cb4a8a05e1e9.png">
<img width="555" alt="2" src="https://user-images.githubusercontent.com/41535744/110163633-8a96b180-7e05-11eb-8fc9-373c9fe452a5.png">
<img width="555" alt="3" src="https://user-images.githubusercontent.com/41535744/110163742-b1ed7e80-7e05-11eb-8b38-01663dfc226c.png">
<img width="555" alt="4" src="https://user-images.githubusercontent.com/41535744/110163940-eeb97580-7e05-11eb-8d9e-23fcf8be0c30.png">
<img width="555" alt="5" src="https://user-images.githubusercontent.com/41535744/110168986-3db6d900-7e0d-11eb-9cc1-440bd4599857.png">
<img width="555" alt="6" src="https://user-images.githubusercontent.com/41535744/110169094-6939c380-7e0d-11eb-825c-dba892a6d7b0.png">
<img width="555" alt="7" src="https://user-images.githubusercontent.com/41535744/110169148-81114780-7e0d-11eb-93cf-cee74e98e815.png">

