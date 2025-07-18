# Форма обратной связи

Сервисный портал для приёма обращений пользователей.

## Модель
Модель `Feedback` (приложение `feedback`):
- `feedback_type`: Тип обращения (пожелание, проблема, претензия, другое).
- `description`: Текстовое описание обращения (обязательное).
- `file`: Прикреплённый файл (опционально, до 5 МБ).
- `created_at`: Дата создания (автоматически).

## API
Эндпоинт: `POST /api/feedback/`
- **Формат данных**: `multipart/form-data`.
- **Поля**:
  - `feedback_type` (строка, обязательно): `wishlist`, `problem`, `claim`, `other`.
  - `description` (строка, обязательно): Описание обращения.
  - `file` (файл, опционально, до 5 МБ)
- **Ответ**:
  - Успех (201): `{ "message": "Обращение успешно отправлено", "data": {...} }`.
  - Ошибка (400): `{ "field": ["error message"] }`.

## Форма
Страница: `/`
- HTML-форма с полями: тип обращения (выпадающий список), описание (текстовое поле), файл (опционально).
- Валидация: обязательное описание, файл до 5 МБ.
- После отправки: сообщение об успехе/ошибке и перенаправление.

## Установка
1. Установите зависимости: `pip install django djangorestframework`.
2. Примените миграции: `python manage.py makemigrations && python manage.py migrate`.
3. Запустите сервер: `python manage.py runserver`.

## Админ-панель
- **URL**: `/admin/`
- **Функции**:
  - Просмотр списка обращений (тип, краткое описание, дата, ссылка на файл).
  - Фильтрация по типу и дате.
  - Поиск по описанию.
  - Редактирование и удаление записей.
- **Доступ**: Требуется аккаунт суперпользователя.
