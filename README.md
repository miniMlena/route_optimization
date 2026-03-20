# route_optimization
Сервис для генерации и оптимизации городских маршрутов доставки.
## Структура проекта

 <pre>
    .
    ├── route_optimization                     # Кодовая база проекта
    │   ├── src/                               # Исходный код
    |   │   ├── backend/                       # Серверная часть
    |   │   │   ├── app/                       
    |   │   │	  │   ├── API/  
    |   │   │	  │   │   ├── points.py
    |   │   │	  │   │   ├── routes.py           
    |   │   │	  │   ├── Models/    
    |   │   │	  │   │   ├── point.py
    |   │   │	  │   │   ├── route.py         
    |   │   │	  │   ├── db.py   
    |   │   │	  │   ├── generation.py
    |   │   │	  │   ├── optimization.py                  
    |   │   │   ├── database.db             
    |   │   │   ├── main.py                  
    |   │   ├── frontend/                	# Пользовательская часть
    |   │   │   ├── css/
    |   │   │	  │   ├── styles.css   
    |   │   │   ├── js/
    |   │   │	  │   ├── api.js
    |   │   │	  │   ├── app.js
    |   │   │	  │   ├── map.js 
    |   │   │	  ├── index.html              
    │   ├── tests/                             # Unit-тесты
    │   ├── .gitignore                         # git ignore файл
    │   ├── requiremenets.txt                  # Установленные зависимости
    │   ├── README.md                          # Описание проекта
</pre>
