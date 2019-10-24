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

## Building a task list.

1. Open excel file in ./src/data/base_excel_file.xlsx 
2. Add relevant information, it is fine to leave empty lines but all fields are expected.
3. Copy the content of excel file except the header row
4. Open ./src/data/excel_to_yaml.py 