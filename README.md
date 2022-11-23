<h1> Check-Password </h1> 
<h2> Библиотека для быстрой проверки паролей, почт и дат на корректность </h2>

***

<h2>Установка</h2>

    pip install check-password

***


<h2> check-Password | Check </h2>
Класс <code> Check(lang="ru") </code> позволяет проверить пароли, почты и даты на корректность ввода
<h3>check-Password | Check | password </h3>
Метод <code> password() -> bool | str | list </code> принимает на вход пароль и критерии проверки, возвращая True/False, str или список <br>
<br>
Основной параметр: <code>password: str</code>  <br>
Критерии проверки (дополнительные параметры): <br>
<br>



|          Название           | Тип данных  |                                                                                                                        Описание                                                                                                                        | Значение по умолчанию |
|:---------------------------:|:-----------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------:|
|      <code>result_type      |     str     |                                                                                             Тип результата, принимает одну стоку из "bool", "str", "list"                                                                                              |        "bool"         |
|         <code>upper         | int or bool |                                                                                                    Наличие и/или количество букв верхнего регистра                                                                                                     |         True          |
|         <code>lower         | int or bool |                                                                                                     Наличие и/или количество букв нижнего регистра                                                                                                     |         True          |
|        <code>numbers        | int or bool |                                                                                                             Наличие и/или количество цифр                                                                                                              |         True          |
|        <code>symbols        | int or bool |                                                                                                        Наличие и/или количество спец. символов                                                                                                         |         True          |
|    <code>required_symbol    |     str     |                                                                                                   Символы, которые обязательно должны быть в пароле                                                                                                    |         None          |
|      <code>min_length       |     int     |                                                                                                                Минимальная длина пароля                                                                                                                |           6           |
|      <code>max_length       |     int     |                                                                                                               Максимальная длина пароля                                                                                                                |          128          |
| <code>check_simple_password |   open()    | Проверка на простоту пароля, для проверки необходимо передать функцию <code>open&#40;'filename.txt'&#41;</code>, файл можно скачать по [ссылке](https://github.com/pavelglazunov/Check-Password/blob/main/common-passwords.txt "common-passwords.txt") |         None          |
|    <code>max_similarity     |     int     |                                                                                     Коэффициент схожести пароля с паролями из указанного файла, рекомендуется 0.7                                                                                      |          0.7          |

<h4> Примеры </h4>

```python
from check_password import Check

check = Check(lang="ru")

print(check.password("qwerty")) # False
print(check.password("Q1wer@ty")) # True
print(check.password("qwerty", result_type="list")) # ['В пароле должны быть символы верхнего регистра', 'В пароле должны быть цифры', 'В пароле должны быть специальные символы']
print(check.password("Q1wer@ty", check_simple_password=open("filename.txt"), result_type="list")) # ['Пароль слишком простой']
print(check.password("qWERty1!", upper=3)) # True
```


<h3>check-Password | Check | email </h3>
Метод <code> email() -> bool | str | list </code> принимает на вход почту и критерии проверки, возвращая True/False, str или список <br>
<br>
Основной параметр: <code>email: str</code>  <br>
Дополнительные параметр: <code>result_type: str</code> | Тип результата, принимает одну стоку из "bool", "str", "list"<br>

<h4> Примеры </h4>

```python
from check_password import Check

check = Check(lang="ru")

print(check.email("ivan@gmail.com"))  # True
print(check.email("-ivan-@gmail.com"))  # False
print(check.email("ivan@gmail.com", result_type="list"))  # []
print(check.email(".ivan@gmail.com", result_type="list"))  # ['Недопустимый первый или последний символ']

```
<br>
<h3>check-Password | Check | date </h3>
Метод <code> date() -> bool | str | list </code> принимает на вход пароль и критерии проверки, возвращая True/False, str или список <br>
<br>
Основной параметр: <code>date: str</code>  <br>
Критерии проверки (дополнительные параметры): <br>

|     Название      | Тип данных |                                                    Описание                                                     |      Значение по умолчанию      |
|:-----------------:|:----------:|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------:|
| <code>date_split  |    str     |                                                   Разделитель                                                   |                -                |
| <code>date_format |    str     |           Формат даты, принимает одну строку из "d/m/y", "d/y/m", "m/d/y", "m/y/d", "y/m/d", "y/d/m"            |              d/m/y              |
|  <code>min_year   |    str     |                                      Минимальная дата, в формате %d-%m-%Y                                       |           01-01-1900            |
|  <code>max_year   |    str     |                                      Максимальная дата, в формате %d-%m-%Y                                      |           01-01-3000            |
| <code>result_type |    str     |                          Тип результата, принимает одну стоку из "bool", "str", "list"                          |             "bool"              |

<h4> Примеры </h4>

```python
from check_password import Check

check = Check(lang="ru")

print(check.date("01-01-2022"))  # True
print(check.date("01-01-2022", max_year="01-01-2021"))  # False
print(check.date("01-01-2022", min_year="01-01-2021"))  # True
print(check.date("01-01-2022", result_type="list"))  # []
print(check.date("54-32-2022", result_type="list"))  # ['Неверная дата']


```
<br>

<h2> check-Password | Generate </h2>
Класс <code>Generate()</code> позволяет создавать сложные пароли с необходимыми условиями
<h3>check-Password | Generate | passwords </h3>
Метод <code>passwords() -> list()</code> возвращает список сложных паролей.
При необходимости можно указать условия для пароля:


<br>

|   Название    | Тип данных |                   Описание                    | Значение по умолчанию |
|:-------------:|:----------:|:---------------------------------------------:|:---------------------:|
| <code>length  |    int     |     Длина пароля, минимальное значение: 6     |          11           |
|  <code>count  |    int     | Количество паролей, минимальное количество: 1 |           1           |
|  <code>upper  |    bool    |            Наличие заглавных букв             |         True          |
| <code>number  |    bool    |                 Наличие цифр                  |         True          |
| <code>symbol  |    bool    |         Наличие специальных символов          |         True          |



<h3> Пример </h3>

```python
from check_password import Generate

print(Generate().passwords())  # -> ['KieSI6:65tg']
print(Generate().passwords(length=20))  # -> ['SD_qOC~v{ip07GA5WISA']
print(Generate().passwords(count=3))  # -> ['TiaZA3:42bt', 'BaoKE7^70cj', 'JuyVO9@69zd']
print(Generate().passwords(upper=False, number=False))  # -> ['pjpawb*yj=a']

```