# Customer Segmentation Analysis


## Introduction
This project focus on customer analysis and segmentation. Which help to generate specific marketing strategies targeting different groups. RFM Analysis, Cohort Analysis, and K-means Clusters were conducted on a UK-based online retail transaction dataset with 1,067,371 rows of records hosted on the UCI Machine Learning Repository.

<br>




<br>

## Content
|       | Item                             | Progress | Version | Links    |
| :---  | :---                             | :---     |:---     |   :---   |
|   1   | data                             |      DONE|    1    |- [Raw Dataset](https://github.com/coletangsy/Recommendation-System-with-NLP/blob/main/amazon_co-ecommerce_sample.zip) <br> - [for_dataframe.py](https://github.com/coletangsy/Recommendation-System-with-NLP/blob/main/for_dataframe.py) |
|   2   | Data preparation & EDA           |     DONE |   1     |- [Data_Preparation&RFM_analysis.ipynb](https://github.com/coletangsy/Customer-Segmentation-Analysis/blob/main/Data_Preparation%26RFM_analysis.ipynb)|
|   3   | Cohort Analysis                  | DONE     |    1     | - [cohort_analysis.ipynb](https://github.com/coletangsy/Customer-Segmentation-Analysis/blob/main/cohort_analysis.ipynb)|
|   4   | RFM Analysis                     | DONE     | 2        | - [Data_Preparation&RFM_analysis.ipynb](https://github.com/coletangsy/Customer-Segmentation-Analysis/blob/main/Data_Preparation%26RFM_analysis.ipynb)<br>- [Lato-Bold.ttf](https://github.com/coletangsy/Customer-Segmentation-Analysis/blob/main/Lato-Bold.ttf)<br>- [eda_function.py](https://github.com/coletangsy/Customer-Segmentation-Analysis/blob/main/eda_function.py)|
|   5   | K-means Cluster                  | DONE     |  1       |  - [K-means.ipynb](https://github.com/coletangsy/Customer-Analysis-Online-Retails/blob/main/K-means.ipynb)



<br>

## Cohort Analysis
The main target here is applying cohort analysis to find out the customers behavior changes over time and the behavior pattern, to generate marketing strategies.

<br>

![Retention_Cohorts](https://github.com/coletangsy/Customer-Analysis-Online-Retails/raw/main/example/Retention_Cohorts.jpeg)<br>

### Meaningful Finding 
***Special group***
- Group of *2009 Dec*, have a high retention rate, keep remaining around 20 - 40 % 
- Group of *2010 Dec*, have a relatively low retention rate that keeping under 12 % afterward


***Special period***
- All groups have a significant increase in retention rate in *Oct, Nov 2010, and Nov 2011*, we believe it may be related to the Black Friday events.


***Special trend***
- A notable increase in the retention of the group after *Jan 2011* can be observed from the cohort analysis.

<br>
<br>
<br>

## RFM Analysis
RFM is a method used for analyzing customer values, which is commonly used in marketing and has received particular attention in retail and professional services industries.

***RFM*** stands for:

**R**ecency (新客) - When is the last time the customer purchase?<br>
- Generally, a customer who interacted or transacted with the brand more recently, the more likely that the customer will be responsive to communication with the brand.

**F**requency (常客) - How often do they purchase?<br>
- Customer with frequent interacted or transacted with the brand are more engaged, and more likely to be loyal to the brand.

**M**onetay Value (貴客) - How much do they spend?<br>
- its refers to the total amounts a customer has spent with the brand during a particular period of time.

<br>

### Customer Segmentation - RFM Segment

|       | Customer Group                         | RFM Segment        | 
| :---  |:---                                    | :---               | 
|   1   | Best Customers                         | 1-1-1              |
|   2   | High-spending New Customers            | 1-4-1 ; 1-4-2      | 
|   3   | Lowest-spending Active Loyal Customers | 1-1-3 ; 1-1-4      | 
|   4   | Churned Best Customers                 | 4-1-1 ; 4-1-2 ; 4-2-1 ; 4-2-2      | 

<br>

### Customers Segmentation - RFM Score

|       | Customer Group   | No. of Customer | RFM Score | 
| :---  |:---              | :---            |  :---     | 
|   1   | Gold             |         794     | 3 -5      |  
|   2   | Sliver           |         3,178   | 6 - 8     |
|   3   | Gold             |         1,906   | 9 - 12    |

<br>

### Products Keywords in Different Group's Purchase History
#### Gold
![Gold.png](https://github.com/coletangsy/Customer-Segmentation-Analysis/blob/main/example/Gold.png)<br>

#### Silver
![Sliver.png](https://github.com/coletangsy/Customer-Segmentation-Analysis/blob/main/example/Sliver.png)<br>

#### Bronze
![Bronze.png](https://github.com/coletangsy/Customer-Segmentation-Analysis/blob/main/example/Bronze.png)<br>

<br>

<br>

## K-means Cluster

### From the above graph, we can find out that:
- Group 1 (Label 0) = Middle group in Monetary Value
- Group 2 (Label 1) = Lowest Monetary Value (mostly under $5,000), also lower in Frequency 
- Group 3 (Label 2) = Highest Monetary Value (mostly above $10,000), lower Recency (mostly lower than 100)

![3D-1.png](https://github.com/coletangsy/Customer-Analysis-Online-Retails/blob/main/example/3D-1.png)
![3D-2.png](https://github.com/coletangsy/Customer-Analysis-Online-Retails/blob/main/example/3D-2.png)
![3D-3.png](https://github.com/coletangsy/Customer-Analysis-Online-Retails/blob/main/example/3D-3.png)

<br>

<br>

#### Reach out to me
[Linkedin - Nicole Tang](https://www.linkedin.com/in/nicoletangsy/)<br>   [Kaggle - nicoletangsy](https://www.kaggle.com/nicoletangsy)<br>    [Matters - My study journal in Chinese](https://matters.news/@coletangsy)
