# Customer Segmentation Analysis
<br>

## Introduction
This repository holds a Customer Segmentation Analysis project which utilizing RFM Analysis, Cohort Analysis and K-means Cluster in python, which generates insights on customers purchasing preferences.<br><br>

<br>

## Content
|       | Item                             | Progress | Version | Links    |
| :---  | :---                                 | :---     |:---     |   :---   |
|   1   | data                        |      DONE|    1    |- [Raw Dataset](https://github.com/coletangsy/Recommendation-System-with-NLP/blob/main/amazon_co-ecommerce_sample.zip) <br> - [for_dataframe.py](https://github.com/coletangsy/Recommendation-System-with-NLP/blob/main/for_dataframe.py) |
|   2   | Data preparation    |     DONE |   1     |- [Data_Preparation&RFM_analysis.ipynb](https://github.com/coletangsy/Customer-Segmentation-Analysis/blob/main/Data_Preparation%26RFM_analysis.ipynb)|
|   3   | RFM Analysis and Key Finding | DONE     | 1       | - [Data_Preparation&RFM_analysis.ipynb](https://github.com/coletangsy/Customer-Segmentation-Analysis/blob/main/Data_Preparation%26RFM_analysis.ipynb)<br>- [Lato-Bold.ttf](https://github.com/coletangsy/Customer-Segmentation-Analysis/blob/main/Lato-Bold.ttf)<br>- [eda_function.py](https://github.com/coletangsy/Customer-Segmentation-Analysis/blob/main/eda_function.py)|
|   4   | Cohort Analysis | DONE |         | |
|   5   | K-means Cluster | ON-GOING |         | |


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

## Customer Segmentation - RFM Segment

|       | Customer Group                         | RFM Segment        | 
| :---  |:---                                    | :---               | 
|   1   | Best Customers                         | 1-1-1              |
|   2   | High-spending New Customers            | 1-4-1 ; 1-4-2      | 
|   3   | Lowest-spending Active Loyal Customers | 1-1-3 ; 1-1-4      | 
|   4   | Churned Best Customers                 | 4-1-1 ; 4-1-2 ; 4-2-1 ; 4-2-2      | 

<br>

## Customers Segmentation - RFM Score

|       | Customer Group   | No. of Customer | RFM Score | 
| :---  |:---              | :---            |  :---     | 
|   1   | Gold             |         794     | 3 -5      |  
|   2   | Sliver           |         3,178   | 6 - 8     |
|   3   | Gold             |         1,906   | 9 - 12    |


## Products Keywords in Different Group's Purchase History
### Gold
![Gold.png](https://github.com/coletangsy/Customer-Segmentation-Analysis/blob/main/example/Gold.png)<br>

### Silver
![Sliver.png](https://github.com/coletangsy/Customer-Segmentation-Analysis/blob/main/example/Sliver.png)<br>

### Bronze
![Bronze.png](https://github.com/coletangsy/Customer-Segmentation-Analysis/blob/main/example/Bronze.png)<br>

<br>

## Cohort Analysis


<br>

## K-means Cluster


<br>

<br>

#### Reach out to me
[Linkedin - Nicole Tang](https://www.linkedin.com/in/nicoletangsy/)<br>   [Kaggle - nicoletangsy](https://www.kaggle.com/nicoletangsy)<br>    [Matters - My study journal in Chinese](https://matters.news/@coletangsy)
