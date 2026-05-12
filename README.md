# URL Shortener

A simple and efficient URL shortener service built with Django and SQLite.

## Features

- Shortens long URLs into compact links.
- Custom alias support (optional).
- Redirects users to the original URL.
- Tracks usage statistics (clicks, etc.).
- REST API for programmatic access.
- Powered by Django and uses SQLite as the default database (easy to switch to other databases).

## Getting Started

### Prerequisites

- [Python 3.x](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/)
- [Django](https://www.djangoproject.com/) (installed as part of requirements)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ratnakarguru/url_shortener.git
   cd url_shortener
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations to set up the SQLite database:
   ```bash
   python manage.py migrate
   ```

### Usage

1. Run the Django development server:
   ```bash
   python manage.py runserver
   ```

2. Access the application at [http://localhost:8000/](http://localhost:8000/).

### API Reference

| Endpoint                   | Method | Description                 |
|----------------------------|--------|-----------------------------|
| /shorten/                  | POST   | Create a short URL          |
| /<short-code>/             | GET    | Redirect to original URL    |
| /stats/<short-code>/       | GET    | Get usage statistics        |

### Example

To shorten a URL, send a POST request to `/shorten/` with a JSON body like:
```json
{
  "url": "https://example.com/very/long/url"
}
```

## Database

- **Default:** SQLite (db.sqlite3 - good for development and lightweight use)
- To use another database (like MySQL or PostgreSQL), modify the `DATABASES` setting in `settings.py`.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request with improvements or bug fixes.

## License

This project is licensed under the MIT License.
