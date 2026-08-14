# Видимый Chrome (по умолчанию)
pytest tests/ --url=http://opencart.test --browser=chrome -v

# Видимый Firefox
pytest tests/ --url=http://opencart.test --browser=firefox -v

# Headless Chrome
pytest tests/ --url=http://opencart.test --browser=chrome --headless -v