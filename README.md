# Домашняя работа 6.7

<div align="center">
<a href="https://wakatime.com/@IldarGaleev/projects/fereckcopm"><img src="https://wakatime.com/badge/user/45799db8-b1f8-4627-9264-2c8d4c352567/project/018beb28-96ef-4887-b044-66638d506f2f.svg" alt="wakatime"></a>
<img src="https://img.shields.io/github/last-commit/IldarGaleevSkyProHomeworks/django_homeworks.svg"/>
</div>

1. Установите зависимости

``` PowerShell
poetry install
```

2. Создайте базу данных и пропишите настройки подключения в файле .env ([шаблон файла](.env.template))
3. Задайте необходимые [переменные окружения](#переменные-окружения)
4. Примените миграции


> [!IMPORTANT]
> 
> Если перед этим была развернута БД к предыдущим версиям. (Для первичной установки действия из примечания не требуются) 
> 
> Для миграции с версии [homework_6_6](https://github.com/IldarGaleevSkyProHomeworks/django_homeworks/tree/homework_6.6) на текущую необходимо:
> 
> 1. Отключить приложение `accounts_app`:
>
>   ```python
>   INSTALLED_APPS = [
>   	...
>   	# "accounts_app",
>   ]
>   
>   ...
>   
>   # AUTH_USER_MODEL = 'accounts_app.User'
>
>    ```
>
> 2. Отменить миграции для приложений `admin` и `auth`
>
>   ```PowerShell
>   python .\manage.py migrate admin zero
>   python .\manage.py migrate auth zero
>   ```
>
> 3. Включить приложение `accounts_app`
>
>   ```python
>   INSTALLED_APPS = [
>   	...
>   	"accounts_app",
>   ]
>   
>   ...
>   
>   AUTH_USER_MODEL = 'accounts_app.User'
>   ```
> 
> 4. Применить миграции
> 
>   ```PowerShell
>   python .\manage.py migrate
>   ```
> 
> 5. Создать новую учетную запись администратора
> 
>   ```PowerShell
>   python .\manage.py createadmin
>   ```
>
>   
> __P.S.__ миграция с более ранних версий не рекомендуется.
> Для начала пройдите процедуру миграции к версии [homework_6_6](https://github.com/IldarGaleevSkyProHomeworks/django_homeworks/tree/homework_6.6).

``` PowerShell 
 python .\manage.py migrate
```

5. Создайте учетную запись администратора

> [!IMPORTANT]
> 
> Не используйте встроенную команду `createsuperuser` - модели пользователей не совместимы!

``` PowerShell
python .\manage.py createadmin
```

6. Заполните базу, используя команды `mainfill` и `productfill`

``` PowerShell
python .\manage.py mainfill
python .\manage.py productfill
```

7. Запустите сервер
``` PowerShell
python .\manage.py runserver
```
8. Запустите менеджер фоновых задач для отправки e-mail сообщений
``` PowerShell
python .\manage.py process_tasks
```

## Команды

### mainfill

Заполняет таблицу с контактами и товарами

```PowerShell
python .\manage.py mainfill
```

### generatearticles

Генерирует статьи для блога

#### Аргументы

- `count` - позиционный аргумент. Указывает сколько статей сгенерировать. По-умолчанию: 1
- `-p`, `--publish` - опубликовать сгенерированные статьи

```PowerShell
# создать и опубликовать 15 статей
python .\manage.py generatearticles 15 -p
```

### process_tasks

Запуск менеджера фоновых задач для отправки сообщений на почту

```PowerShell
python .\manage.py process_tasks
```

### createadmin

Создание суперпользователя (замена встроенной команды `createsuperuser`).

```PowerShell
python .\manage.py createadmin
```


## Переменные окружения

> [!TIP]
> 
> Поддерживается файл `.env` для назначения переменных. [Шаблон файла](.env.template)
> 

### Postgres

| Переменная    | Файл настроек                            | Назначение                          |
|---------------|------------------------------------------|-------------------------------------|
| `PG_NAME`     | [config/settings.py](config/settings.py) | Имя базы данных                     |
| `PG_USER`     | [config/settings.py](config/settings.py) | Имя пользователя для подключения    |
| `PG_PASSWORD` | [config/settings.py](config/settings.py) | Пароль пользователя для подключения |
| `PG_HOST`     | [config/settings.py](config/settings.py) | Имя хоста с сервером                |
| `PG_PORT`     | [config/settings.py](config/settings.py) | Порт сервера                        |


### Страница товаров

| Переменная               | Файл настроек                          | Назначение                     |
|--------------------------|----------------------------------------|--------------------------------|
| `STORE_CATALOG_PER_PAGE` | [store_app/apps.py](store_app/apps.py) | Количество товаров на странице |


### Страница публикаций

| Переменная                     | Файл настроек                        | Назначение                                                                                                                |
|--------------------------------|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| `ARTICLES_PER_PAGE`            | [blog_app/apps.py](blog_app/apps.py) | Количество публикаций на странице                                                                                         |
| `ARTICLE_VIEW_COUNTS_CONGRATS` | [blog_app/apps.py](blog_app/apps.py) | Количество просмотров публикации, при котором отсылаестя сообщение. Переменная содержит список чисел, разделенных запятой |


### Background worker

| Переменная            | Файл настроек                            | Назначение                                      |
|-----------------------|------------------------------------------|-------------------------------------------------|
| `BGTASK_MAX_ATTEMPTS` | [config/settings.py](config/settings.py) | Количество попыток повторного выполнения задачи |


## Логирование

Для настройки логирования укажите путь к json файлу конфигурации в переменной окружения `LOGGING_CONFIG_FILE`.

Пример файла конфигурации для вывода отладочных сообщений в консоль от менеджера фоновых задач:

```json
{
  "version": 1,
  "disable_existing_loggers": false,
  "handlers": {
    "console": {
      "class": "logging.StreamHandler"
    }
  },
  "root": {
    "handlers": [
      "console"
    ],
    "level": "WARNING"
  },
  "loggers": {
    "tasks.send_mail": {
      "level": "DEBUG"
    }
  }
}
```

## Фильтр слов

Доступна проверка текста по регулярному выражению для добавляемого товара (в названии и описании) на предмет
наличия запрещенных слов.

Добавить фильтры можно в панели администрирования в разделе `магазин\фильтры слов`

Примеры фильтров:

<table>
    <tr>
        <th>Название</th>
        <th>Регулярное выражение</th>
    </tr>
    <tr>
        <td>Казино и ставки</td>
        <td><code>(казино|(^|\s)ставк[и|а]|букмекер)</code></td>
    </tr>
    <tr>
        <td>Мошенничество</td>
        <td><code>(обман|[ы|у]красть|радар|полиц[и|е|а])</code></td>
    </tr>
    <tr>
        <td>Криптовалюта</td>
        <td><code>((крипт|криптовалют|бирж)[е|а|у])|(cripto)</code></td>
    </tr>
</table>
