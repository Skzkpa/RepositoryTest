## gfi-vue-gantt-elastic


## Building a task list.

0. Run relevant query in VSTS with columns:
    * ID	Title	Status	Tags	Story Points
    * supported Tags:
        * Milestone X ex. Milestone C
        * Sprint X  ex. Sprint 2  
        * PIXY    ex. PI10
1. Open excel file in ./src/data/excel.xlsx 
2. Add relevant information for your team in relevant sheet and update your velocity and date in `teams` sheet, it is fine to leave empty lines but all fields are expected.
    * Custom fields for Gantt are in red
3. \* Run the script:
    ```
    python excel_to_yaml.py 
    ```
4. \* You can also run the development server with `npm run serve` to check if the outcome of You work is as expected.
5. Add all files to git with
    ```
    git add *
    git commit -m "updates data for infra"
    git push
    ``` 

\* Steps 3,4 are optional, this will allow you to check the outcome of your changes, but it requires full project setup.


## Requirements:
Mandatory:
- git

Optional:
- npm 6.9.0
- python3.5+


## Project setup - JS
Run in 
```
npm install
```

#### Compiles and hot-reloads for development
```
npm run serve
```

#### Compiles and minifies for production
```
npm run build
```

#### Run your tests
```
npm run test
```

#### Lints and fixes files
```
npm run lint
```

## Project setup - Python
#### Install Python dependencies
```
pip install -r ./src/data/requirements
```
#### Run your tests
There is a simple test writen in ./src/data/commons/tests.py
```
python tests.py
```

 
## Instruction how to Use for Product Owners

Keep in mind that You need to run before hand following steps:
* Installation of optional dependencies
* Install Python dependencies
* Project setup - JS

#### To run the server
press windos+R and type cmd, enter

change the directory using `cd` command to the one You have the package unzpied - example below and than run the second command.
```
cd C:\Users\Piotr\gfi-vue-gantt
npm run serve
```

## To rebuild the data source from excel file
Rember to save the excel file.
 
press windos+R and type cmd, enter

change the directory using `cd` command to the one .\data\src under your unzpied package  - example below and than run the second command.
```
cd C:\Users\Piotr\gfi-vue-gantt\data\src
python excel.py
```