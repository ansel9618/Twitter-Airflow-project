# Twitter-Airflow-project
we'll use Twitter api to get the tweets of a particular user and write a ETL code in python to push the data into S3 bucket in csv format  and schedule it using airflow

![My Image](https://github.com/ansel9618/Twitter-Airflow-project/blob/main/images/Architecture.png)

## step1:

First we need a twitter account once account created go to developer portal and create an app
and get the credentials as mentioned here i.e the API Key and Secret and Access Token and Secret

![My Image](https://github.com/ansel9618/Twitter-Airflow-project/blob/main/images/Twitter_proj_devoper_portal.png)

## step2 :
write etl script in python to access the api and get the tweets of the mentioned user
refer [etl_script](https://github.com/ansel9618/Twitter-Airflow-project/blob/main/twitter_etl%20copy_github.py)
