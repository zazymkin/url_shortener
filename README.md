# url_shortener
Приложение для сокращения Url-адресов на основе python с использованием aiohttp и postgresql

# Запуск
    docker-compose up -d --build
    docker-compose exec server alembic upgrade head

# Запуск тестов
    docker-compose exec server pytest