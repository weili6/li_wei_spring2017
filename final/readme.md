# Data Analysis of World Happiness Report 2015 & 2016

## Dataset Description
- The World Happiness Report is a landmark survey of the state of global happiness. The first report was published in 2012, the second in 2013, and the third in 2015. The World Happiness Report 2016 Update, which ranks 156 countries by their happiness levels, was released in Rome in advance of UN World Happiness Day, March 20th. The reports review the state of happiness in the world today and show how the new science of happiness explains personal and national variations in happiness. They reflect a new worldwide demand for more attention to happiness as a criteria for government policy.
- Resource: https://www.kaggle.com/unsdsn/world-happiness
- Dataset Preview

| Country     | Region         | Happiness Rank | Happiness Score | Lower Confidence Interval | Upper Confidence Interval | Economy (GDP per Capita) | Family  | Health (Life Expectancy) | Freedom | Trust (Government Corruption) | Generosity | Dystopia Residual |
|-------------|----------------|----------------|-----------------|---------------------------|---------------------------|--------------------------|---------|--------------------------|---------|-------------------------------|------------|-------------------|
| Denmark     | Western Europe | 1              | 7.526           | 7.46                      | 7.592                     | 1.44178                  | 1.16374 | 0.79504                  | 0.57941 | 0.44453                       | 0.36171    | 2.73939           |
| Switzerland | Western Europe | 2              | 7.509           | 7.428                     | 7.59                      | 1.52733                  | 1.14524 | 0.86303                  | 0.58557 | 0.41203                       | 0.28083    | 2.69463           |
| Iceland     | Western Europe | 3              | 7.501           | 7.333                     | 7.669                     | 1.42666                  | 1.18326 | 0.86733                  | 0.56624 | 0.14975                       | 0.47678    | 2.83137           |

## Analysis 1
- Goal: Compare regional distributions of countries in World Happiness Reports of 2015 and 2016
- Method: Add 'Year' variable to 2 datasets and concatenate them in pandas; use seaborn.violinplot
- Result:  
_1. most regions remain the same_  
_2. More countries in Central and Eastern Europe falls between 5-6 in 2016_  
_3. More countries in Sub-Saharan falls around 4 in 2016_  
![Alt text](analysis/ana_1/ana_1_output/plot_1.png)  

## Analysis 2
- Goal: Rank change of each country in Wordl Happiness Reports of 2015 and 2016
- Method: Calculate the difference between the columns of "Happiness Rank_2015" and "Happiness Rank_2016"; sort rows by the value of rank change; use seaborn.swarmplot
- Result:  
_1. Algeria has the highest rank increase_  
| Country | Happiness Rank_2015 | Happiness Rank_2016 | Region                          | Rank Change |
|---------|---------------------|---------------------|---------------------------------|-------------|
| Algeria | 68                  | 38                  | Middle East and Northern Africa | -30         |

_2. Liberia has the highest rank decrease_  
| Country | Happiness Rank_2015 | Happiness Rank_2016 | Region             | Rank Change |
|---------|---------------------|---------------------|--------------------|-------------|
| Liberia | 116                 | 150                 | Sub-Saharan Africa | 34          |

_3. New countries on 2016 list_  
| Country           | Region_2016                 | Happiness Rank_2016 |
|-------------------|-----------------------------|---------------------|
| Puerto Rico       | Latin America and Caribbean | 15.0                |
| Belize            | Latin America and Caribbean | 52.0                |
| Somalia           | Sub-Saharan Africa          | 76.0                |
| Somaliland Region | Sub-Saharan Africa          | 97.0                |
| Namibia           | Sub-Saharan Africa          | 113.0               |
| South Sudan       | Sub-Saharan Africa          | 143.0               |

_4. Countries off 2016 list; Note Oman ranks 22 in 2015, however it is off the list of 2016_  
| Country                  | Region_2015                     | Happiness Rank_2015 |
|--------------------------|---------------------------------|---------------------|
| Oman                     | Middle East and Northern Africa | 22.0                |
| Somaliland region        | Sub-Saharan Africa              | 91.0                |
| Mozambique               | Sub-Saharan Africa              | 94.0                |
| Lesotho                  | Sub-Saharan Africa              | 97.0                |
| Swaziland                | Sub-Saharan Africa              | 101.0               |
| Djibouti                 | Sub-Saharan Africa              | 126.0               |
| Central African Republic | Sub-Saharan Africa              | 148.0               |

_5. Most countries remain the same, while countries in Sub-Suharan Africa have more changes_  
![Alt text](analysis/ana_2/ana_2_output/plot_1.png)  
