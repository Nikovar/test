Для запуска отдельного теста с визуальной отображением действий в браузере использовать команды: 
    pytest --html=report.html --browser chromium --headed case0.py 
    pytest --html=report.html --browser chromium --headed case1.py
    pytest --html=report.html --browser chromium --headed case2.py

Для запуска последовательных тестов:
    pytest --html=report.html --browser chromium --headed 

Для запуска тестов конкуретно:
    pytest --html=report.html --browser chromium --headed -n 3