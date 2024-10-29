# Телеграм-бот Чё готовим
Бот принимает голосовое сообщение и по распознанному перечню продуктов подбирает из базы список блюд, которые можно приготовить

## Установка
1. Загрузить бота на сервер
`git clone https://github.com/poivian/Cho_gotovim_bot.git`
2. Перейти в склонированную директорию
`cd Cho_gotovim_bot`
3. Распаковать архивы с файлом базы > dump.7z и файлы модели и эмбеддингов > /search/search_db.7z
3. Заполнить файл .env-EXAMPLE своими данными и переименовать файл в .env
4. Собрать образы контейнеров
`sudo docker compose build`
5. Запустить контейнеры
`sudo docker compose up -d`
6. Загрузить дамп базы
`sudo docker exec -i pg_database /bin/bash -c "PGPASSWORD={пароль от базы} psql --username {имя пользователя в базе} database" < dump.sql`