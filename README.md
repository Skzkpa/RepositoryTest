# gfi-vue-gantt-elastic

## Requirements:
- npm 6.9.0
- python3.5+

## Project setup - JS
Run in 
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Run your tests
```
npm run test
```

### Lints and fixes files
```
npm run lint
```

## Project setup - Python
### Install Python dependencies
```
pip install -r ./src/data/requirements
```
### Run your tests
There is a simple test writen in ./src/data/commons/tests.py
```
python tests.py
```


## Building a task list.

1. Open excel file in ./src/data/base_excel_file.xlsx 
2. Add relevant information, it is fine to leave empty lines but all fields are expected.
3. Copy the content of excel file except the header row
4. Open ./src/data/excel_to_yaml.py 
5. Past data to marked place from excel.
6. Fill the velocity.
7. Run the script:
```
python excel_to_yaml.py 
```
8. Replace the content of ./src/data/tasks.yaml with the outcome of above script. 
9. Now You can adjust the Yaml directly.
10. You can also run the development server with `npm run serve` to check if the outcome of You work is as expected.