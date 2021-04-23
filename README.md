**Adapt I/O Scraping**

- This project will scrap company_index and company_profiles data from [adaptio](https://www.adapt.io/directory/industry/telecommunications/A-1) - - - By running scrapper/adaptio.py both company_index.json and company_profiles.json will be written with the scrapped data 
- The scrapped data is stored DB (In this project, I have used MySQL) 
- The scrapper/adaptio.py scrpit can be tested by running test.py 
- For data points validation, I have used [jsonschema](https://python-jsonschema.readthedocs.io/en/stable/)

**JSON Format**

**company_index.json**
```bash
[
    {
        'company_name':'A & L Personnel Services', 
        'source_url': '/company/a---l-personnel-services'
    },
    {
        'company_name':'A+ Conferencing', 
        'source_url': '/company/a--conferencing
    },
    ...
]
```

**company_profiles.json**
```bash
[
    {
        "company name": "A & L Personnel Services", 
        "company_location": "Gregory, Michigan",
        "company_website": "http://www.cac.net", 
        "company_webdomain": "cac.net",
        "company_industry": "Telecommunications", 
        "company_employee_size":None,
        "company_revenue" :None, 
        "contact_details": [
            {
                "contact_name": "Doug Waite",
                "contact_jobtitle": "owner", 
                "contact_email_domain": "cac.net", 
                "contact_department": "Finance and Administration"
            },
            {
                "contact_name": "Jim Mason", 
                "contact_jobtitle": "Club Directior", 
                "contact_email_domain": "cac.net", 
                "contact_department": "Other"
            }
        ]
    },
    ...
]
```

**Setting Up**

OS - Ubuntu 18.04 LTS

- At first, clone the project into your local machine by
```bash
$ git clone https://gitlab.com/aqifcse/adaptio-scraping.git adaptio
```

- Create and activate Virtual Environment with python 3.6.9

```bash
$ cd adaptio
~/adaptio$ virtualenv venv
~/adaptio$ source venv/bin/activate
```

**Install Required Packages**
Required packages are -
```
lxml==4.6.3
requests==2.25.1
requests_html==0.10.0
PyMySQL==1.0.2
jsonschema==3.2.0
jsonschema[format]
ipython==7.16.1
pandas==1.1.5
boto3
```
Noted that, installing requests-html will automatically install Beautifulsoup(bs4). If not, install it by pip
```bash
(venv) x@x:~/adaptio$ pip install bs4
```

- Install required packages from requirements.txt using pip
```bash    
(venv) x@x:~/adaptio$ pip install -r requirements.txt
```
- Run scrapper/adaptio.py and write the scrapped data in scrapper/company_index.json and scrapper/company_profiles.json
```bash
(venv) x@x:~/adaptio$ cd scrapper/
(venv) x@x:~/adaptio/scrapper$ python adaptio.py
```

** Data Processingin AWS S3 and Storing Data in MySQL**

**Data Processing**

Step 1 − First we need an AWS account which will provide us the secret keys for using in our Python script while storing the data. It will create a S3 bucket in which we can store our data.

Step 2 − Next, we need to install boto3 Python library for accessing S3 bucket. It can be installed with the help of the following command −
```bash
pip install boto3
```

Step 3 − Next, we can use the following Python script for scraping data from web page and saving it to AWS S3 bucket.

First, we need to import Python libraries for scraping, here we are working with requests, and boto3 saving data to S3 bucket.

```
import boto3
```

Now for storing data to S3 bucket, we need to create S3 client as follows −

```
s3 = boto3.client('s3')
bucket_name = "adaptio-content"
```
Next line of code will create S3 bucket as follows −

```
s3.create_bucket(Bucket = bucket_name, ACL = 'public-read')
s3.put_object(Bucket = bucket_name, Key = '', Body = data, ACL = "public-read")
```

Now you can check the bucket with name adaptio-content from your AWS account.


**Data Storing**

Step 1 − First, by using MySQL we need to create a database and table in which we want to save our scraped data. For example, we are creating the table with following query −

**company_index table**
```
CREATE TABLE company_index (id BIGINT(7) NOT NULL AUTO_INCREMENT,
company_name VARCHAR(1000), source_url VARCHAR(10000),PRIMARY KEY(id));
```
Step 2 − Next, we need to deal with Unicode. Note that MySQL does not handle Unicode by default. We need to turn on this feature with the help of following commands which will change the default character set for the database, for the table and for both of the columns −
```
ALTER DATABASE adaptio_scrap CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
ALTER TABLE company_index CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE company_index CHANGE company_name company_name VARCHAR(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

**Testing**
- Test the scrapper/adaptio.py script by running scrapper/test.py script
```bash
(venv) x@x:~/adaptio/scrapper$ python test.py
```
**Datapoints Validation**
- For validating company_index.json with jsonscema
```bash
(venv) x@x:~/adaptio/scrapper$ strace jsonschema -i company_index.json company_index.schema
```
- For validating company_profiles.json with jsonschema
```bash
(venv) x@x:~/adaptio/scrapper$ strace jsonschema -i company_profiles.json company_profiles.schema
```

**Loading JSON Data with Pandas**

- Make sure you have installed ipython and pandas in the virtual environment

```bash
(venv) x@x:~/adaptio/scrapper$ ipython
Python 3.6.9 (default, Oct  8 2020, 12:12:24) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.14.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import pandas as pd

In [2]: import json

```
**1. For loading company_index.json in dataframe**

```

In [3]: with open("company_index.json") as ci_datafile:
   ...:     ci_data = pd.read_json(ci_datafile)
   ...: ci_dataframe = pd.DataFrame(ci_data)

In [4]: ci_dataframe
Out[4]: 
                     company_name                                         source_url
0            A&A Technology Group  https://www.adapt.io/company/a-a-technology-group
1                 A Better Answer     https://www.adapt.io/company/a-better-answer-4
2                A Cheerful Giver  https://www.adapt.io/company/a-cheerful-giver-...
3                           A-CTI               https://www.adapt.io/company/a-cti-1
4                       A P G Inc             https://www.adapt.io/company/a-p-g-inc
...                           ...                                                ...
4369                          ZTE                 https://www.adapt.io/company/zte-8
4370                       Zultys          https://www.adapt.io/company/zultys--inc-
4371  Zurich Technology Solutions  https://www.adapt.io/company/zurich-technology...
4372                         ZVRS                  https://www.adapt.io/company/zvrs
4373             Zwicker Electric      https://www.adapt.io/company/zwicker-electric

[4374 rows x 2 columns]
```

**1. For loading company_profiles.json in dataframe**

```
In [5]: with open("company_profiles.json") as cp_datafile:
   ...:   cp_data = pd.read_json(cp_datafile)
   ...: cp_dataframe = pd.DataFrame(cp_data)

In [6]: cp_dataframe
Out[6]: 
              company_name                      company_location  ... company_revenue                                    contact_details
0     A&A Technology Group            Waco, Texas, United States  ...        $1 - 10M  [{'contact_name': 'Phillip Neely', 'contact_jo...
1          A Better Answer          Plano,  Texas, United States  ...        $1 - 10M  [{'contact_name': 'Vicki Young', 'contact_jobt...
2         A Cheerful Giver  San Diego, California, United States  ...         $0 - 1M  [{'contact_name': 'Tony Gross', 'contact_jobti...
3                    A-CTI       Tualatin, Oregon, United States  ...                  [{'contact_name': 'Michael Payne', 'contact_jo...
4                A P G Inc       Atlanta, Georgia, United States  ...                  [{'contact_name': 'Steve Deluco', 'contact_job...
...                    ...                                   ...  ...             ...                                                ...
4371                   ZTE            Shenzhen, Guangdong, China  ...           > $1B  [{'contact_name': 'Lixin Cheng', 'contact_jobt...
4372                                                              ...                                                                 []
4373                                                              ...                                                                 []
4374                  ZVRS    Clearwater, Florida, United States  ...       $10 - 50M  [{'contact_name': 'Caryn Bain', 'contact_jobti...
4375                                                              ...                                                                 []

[4376 rows x 8 columns]
```


**Question and Answer**
**1. The architecture of my application**

- The data extracted from adapt io site through requests-html by session.get(url)
- From url created a soup/page
- from page, extracted the texts, urls by tag
- Store two output JSON Files in to tables
- Build TestCases by unittesting
- Validation of the data points


**2. Which database engine I have chosen and why?**
I am using MySQL because 
- MySQL is a robust and secure database
- Here both of the JSON data can be stored as table row
- Can be established relation between the fields value and can be implemented different queries
- MySQL supports native JSON datatype
- Commented boto3 code for Data Processing using AWS S3 for massive scale data storing



