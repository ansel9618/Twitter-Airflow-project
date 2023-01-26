# Twitter-Airflow-project

we'll use Twitter api to get the tweets of a particular user and write a ETL code in python to push the data into S3 bucket in csv format  and schedule it using airflow

![My Image](https://github.com/ansel9618/Twitter-Airflow-project/blob/main/images/Architecture.png)

## step1:

First we need a twitter account once account created go to developer portal and create an app
and get the credentials as mentioned here i.e the API Key and Secret and Access Token and Secret

![My Image](https://github.com/ansel9618/Twitter-Airflow-project/blob/main/images/Twitter_proj_devoper_portal.png)

## step2 :

write etl script in python to access the api and get the tweets of the mentioned user adn push it to s3 bucket
make sure s3 bucket is created.
refer [etl_script](https://github.com/ansel9618/Twitter-Airflow-project/blob/main/twitter_etl%20copy_github.py)


## step3:

Now we can write a dag file to trigger the etl script and the gmail notification refer [Dag_file](https://github.com/ansel9618/Twitter-Airflow-project/blob/main/twitter_dag.py)

## step 4:

create a EC2 instance make sure u take a resource with 2 cores and atleast 2gb ram for airflow to work (eg:t2.medium) also os should be ubuntu 22.04
and install the follo: libraries
```sudo apt-get update
sudo apt install python3-pip
sudo pip install apache-airflow
sudo pip install pandas
sudo pip install s3fs
sudo pip install tweepy
```
note:allow traffic from ur ip or anywhere

also make sure to test the 'airflow standalone' command in terminal 
## step 5: 
create dag folder and using the nano command as root user create files and copy the twitter dag and etl files in it as mentioned above
also make sure we have set the IAM policy in EC2 for s3 and ec2 to full access

also make sure ACL permission are enabled

s3 bucket policy added

![My Image](https://github.com/ansel9618/Twitter-Airflow-project/blob/main/images/s3_bucket_policy.png)

Acl enabling

![My Image](https://github.com/ansel9618/Twitter-Airflow-project/blob/main/images/ACL_enable.png)


EC2 policy added

![My Image](https://github.com/ansel9618/Twitter-Airflow-project/blob/main/images/EC2_policy_permission.png)

## step 6: now we can test the dag in airflow
Note: to set the gmail server make sure to make the changes in airflow.cfg file

```
(note: make sure to set smtp config in airflow.cfg
      smtp_user     --> your email
      smtp_password --> use the password from gmail generated from  App password (for this u need to enable 2 factor authentication)
                        using your mail password will lead to user credential error
      
      ```
      smtp_host = smtp.gmail.com
      smtp_starttls = True
      smtp_ssl = False
      # Example: smtp_user = airflow
      smtp_user = **************
      # Example: smtp_password = airflow
      smtp_password = **************
      smtp_port = 587
      smtp_mail_from = airflow@example.com
      smtp_timeout = 30
      smtp_retry_limit = 5
```

## Pipeline output

Airflow pipeline Fail

![My Image](https://github.com/ansel9618/Twitter-Airflow-project/blob/main/images/airflow_fail.png)


Gmail Failed msg

![My Image](https://github.com/ansel9618/Twitter-Airflow-project/blob/main/images/gmai_failed_msg.png)

Airflow pipeline success

![My Image](https://github.com/ansel9618/Twitter-Airflow-project/blob/main/images/airflow_success.png)

Gmail success msg

![My Image](https://github.com/ansel9618/Twitter-Airflow-project/blob/main/images/gmail_success_msg.png)

csv file written to s3 bucket

![My Image](https://github.com/ansel9618/Twitter-Airflow-project/blob/main/images/s3_bucket_csv_written.png)




## Credits
this project was done with help of Darshil parmar
