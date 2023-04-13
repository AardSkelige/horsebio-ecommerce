# Описание проекта Django интернет-магазина
Этот проект представляет собой интернет-магазин, созданный на фреймворке Django. В проекте реализована верстка шаблонов страниц с помощью библиотеки Bootstrap, а также функциональность для работы с товарами. Для управления базой данных используется Django SQLite.

В проекте существует возможность запуска как в стандартном режиме без Docker, так и с помощью Docker Compose, с использованием базы данных PostgreSQL.

Сейчас не все функции проекта реализованы, в частности, не сделано добавление товаров в корзину и покупка. Но уже реализованы карточки товаров и хлебные крошки с помощью библиотеки mptt.

Для запуска проекта без Docker необходимо склонировать проект на свой компьютер, создать и активировать виртуальное окружение, установить все необходимые зависимости из файла requirements.txt и запустить проект с помощью команды python3 manage.py runserver.

Для запуска проекта в Docker необходимо использовать Docker Compose, который также создаст базу данных PostgreSQL и подключит ее к проекту. Однако, так как база данных пустая, могут возникнуть некоторые особенности при работе с проектом. В проекте также присутствуют файлы для переменных среды с авторизационными данными.


# Django internet shop project
The project includes templates designed using Bootstrap, breadcrumbs using the MPTT library, and product cards. The project connects to a Django SQLite database. Additionally, the project includes Dockerfile and docker-compose files for running the project in Docker, including a PostgreSQL database. Environment variables with authorization data are also included.

To run the project, there are two options. The first option is to clone the project to your computer, create and activate a virtual environment, install all dependencies from the requirements.txt file, and run the project using python3 manage.py runserver.

The second option is to run the project using Docker with a PostgreSQL database. However, since the database is empty, there may be some specific issues.
