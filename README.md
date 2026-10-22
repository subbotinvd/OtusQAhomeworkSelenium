# UI-автотесты на PrestaShop (Selenium + pytest + Allure)

Автоматизированные UI-тесты интернет-магазина [PrestaShop](https://www.prestashop.com/) 9 (тема Hummingbird).
Стек: Selenium WebDriver, pytest, Allure, паттерн Page Object.

Магазин разворачивается локально в Docker (контейнеры MariaDB + PrestaShop), тесты запускаются
как локально, так и в собственном Docker-контейнере с передачей параметров запуска.

## Структура проекта

```
tests/
  conftest.py            # фикстуры и опции запуска (--browser, --url, --headless)
  pages/                 # Page Object: страницы магазина и админки
  test_elements.py       # проверка элементов страниц (5 тестов)
  test_search.py         # поиск по каталогу
  test_registration.py   # регистрация нового покупателя
  test_admin_product.py  # CRUD товаров в админке
  test_scenarios.py      # e2e-сценарии: логин/логаут админа, корзина
Dockerfile               # образ с тестами (Python + Chromium + Firefox)
docker-compose.yml       # MariaDB + PrestaShop + контейнер тестов
```

## Запуск тестов в Docker

### Вариант 1: всё сразу одной командой

Поднимает MariaDB, дожидается установки PrestaShop (1–2 минуты при первом старте),
собирает образ тестов и прогоняет весь сьют:

```shell
docker compose up --build
```

### Вариант 2: сборка образа и запуск, как в задании

Сначала поднимаем магазин, затем собираем образ тестов и запускаем его
с нужными опциями:

```shell
docker compose up -d db shop

docker build -t tests .

# по умолчанию Chrome
docker run -it tests

# тесты в браузере Firefox — опция из conftest.py
docker run -it tests --browser firefox

# можно комбинировать любые опции pytest
docker run -it tests --browser firefox -v
```

Образ по умолчанию работает в headless-режиме и обращается к магазину,
опубликованному на хосте `http://host.docker.internal:8080`.

> На Linux `host.docker.internal` не резолвится из коробки — добавьте
> `--add-host=host.docker.internal:host-gateway` к `docker run`.

### Вариант 3: запуск через compose с параметрами

Тестовый контейнер подключён к сети compose и ходит в магазин по адресу `http://shop`:

```shell
docker compose run --rm tests --browser firefox
```

## Запуск тестов локально

Магазин уже должен быть запущен на `http://localhost:8080` (например, `docker compose up -d db shop`).

```shell
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Linux/macOS

pip install -r requirements.txt

# видимый Chrome
pytest --browser=chrome --url=http://localhost:8080 -v

# видимый Firefox
pytest --browser=firefox -v

# headless-режим
pytest --browser=chrome --headless -v
```

## Параметры запуска (conftest.py)

| Параметр    | Значение по умолчанию                        | Описание                          |
|-------------|----------------------------------------------|-----------------------------------|
| `--browser` | `chrome`                                      | Браузер: `chrome` или `firefox`   |
| `--url`     | `$SHOP_URL` или `http://localhost:8080`       | Адрес магазина                    |
| `--headless`| `$HEADLESS` или выкл.                         | Headless-режим (в Docker включён) |

Дополнительно читаются переменные окружения:
- `ADMIN_EMAIL` (по умолчанию `admin@prestashop.com`) — логин админки;
- `ADMIN_PASSWORD` (по умолчанию `AdminDemo-2026-Pass`) — пароль админки;
- `ADMIN_FOLDER` (по умолчанию `admin`) — имя папки админки.

## Магазин и админка

- Витрина: http://localhost:8080
- Админка: http://localhost:8080/admin — `admin@prestashop.com` / `AdminDemo-2026-Pass`

## Отчёт Allure

```shell
pytest --alluredir=allure-results
allure serve allure-results
```

При запуске через `docker compose up` результаты складываются в volume `allure_results`.
