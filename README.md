# Конфигурационное управление. Домашнее задание
# Hi there, I'm [ksen](https://daniilshat.ru/) ![](https://github.com/blackcater/blackcater/raw/main/images/Hi.gif) 
### Задание №3
### Постановка задачи:
Задание №3 
Разработать инструмент командной строки для учебного конфигурационного языка, синтаксис которого приведен далее. Этот инструмент преобразует текст из входного формата в выходной. Синтаксические ошибки выявляются с выдачей сообщений. <br />
Входной текст на учебном конфигурационном языке принимается из файла, путь к которому задан ключом командной строки. Выходной текст на языке toml попадает в стандартный вывод.  <br />
##Однострочные комментарии:  <br />
" Это однострочный комментарий  <br />
##Многострочные комментарии:  <br />
<# <br />
Это многострочный <br />
комментарий <br />
#> <br />
##Массивы: <br />
[ значение; значение; значение; ... ] <br />
##Словари: <br />
begin <br />
имя := значение; <br />
имя := значение; <br />
имя := значение; <br />
... <br />
end <br />
##Имена: <br />
[a-zA-Z][_a-zA-Z0-9]* <br />
Значения: <br />
• Числа. <br />
• Массивы. <br />
• Словари. <br />
##Объявление константы на этапе трансляции: <br />
имя is значение <br />
##Вычисление константного выражения на этапе трансляции (префиксная 
форма), пример: <br />
$(+ имя 1) <br />
Результатом вычисления константного выражения является значение. 
Для константных вычислений определены операции и функции:<br /> 
1. Сложение. <br />
2. Вычитание. <br />
3. mod(). <br />
Все конструкции учебного конфигурационного языка (с учетом их 
возможной вложенности) должны быть покрыты тестами.<br />

### Содердание файла
```
[employee]
name = "John Doe"
age = 35

[job]
title = "Software Engineer"
department = "IT"
years_of_experience = 10

[address]
street = "123 Main St."
city = "San Francisco"
state = "CA"
zip = 94102

["game configuration"]
resolution_width = 1920
resolution_height = 1080
fullscreen = "true"
music_volume = 0.5
characters = "player, enemy, npd"

["web-site configuration"]
port = 1920
timeout = 30[employee]
name = "John Doe"
age = 35

[job]
title = "Software Engineer"
department = "IT"
years_of_experience = 10

[address]
street = "123 Main St."
city = "San Francisco"
state = "CA"
zip = 94102

["game configuration"]
resolution_width = 1920
resolution_height = 1080
fullscreen = "true"
music_volume = 0.5
characters = "player, enemy, npd"

["web-site configuration"]
port = 1920
timeout = 30
```
### Содержание output.dot
```
cat employee.toml | python main.py
set v1 = 1920;
dict(
employee = dict(name = John Doe, age = 35),
job = dict(title = Software Engineer, department = IT, years_of_experience = 10),
address = dict(street = 123 Main St., city = San Francisco, state = CA, zip = 94102),
game configuration = dict(resolution_width = |v1|, resolution_height = 1080, fullscreen = true, music_volume = 0.5, characters = player, enemy, npd),
web-site configuration = dict(port = |v1|, timeout = 30),
```
### Результат тестов main.py
![image](https://github.com/user-attachments/assets/2294e97e-dd15-4a59-9673-c4f5c9981494)

### Результат тестов tests.py
![image](https://github.com/user-attachments/assets/6fb741f3-048a-4eb1-a7bf-c28b07321b92)

