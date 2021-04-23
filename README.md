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
jsonschema==3.2.0
jsonschema[format]
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

**Storing Data in MySQL**

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
- MySQL is a robust and secure 
- Here both of the JSON data can be stored as table row
- Can be established relation between the fields value.
- MySQL supports JSON



