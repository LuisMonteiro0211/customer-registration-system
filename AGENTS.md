# AGENTS.md

## Cursor Cloud specific instructions

### Overview

Customer Registration System — CLI-based Python CRUD app backed by MySQL.
Architecture: Models → DTOs → Repositories → Services → Views (CLI).

### MySQL setup (one-time, not in update script)

MySQL 8.0 must be installed and running. In this environment (no systemd), start it manually:

```bash
sudo mkdir -p /var/run/mysqld && sudo chown mysql:mysql /var/run/mysqld
sudo mysqld --user=mysql --datadir=/var/lib/mysql &
sleep 3
sudo mysqladmin ping  # verify it's alive
```

Then create the database, user, and tables:

```bash
sudo mysql -e "
CREATE DATABASE IF NOT EXISTS customer_registration;
CREATE USER IF NOT EXISTS 'app_user'@'localhost' IDENTIFIED BY 'app_password';
GRANT ALL PRIVILEGES ON customer_registration.* TO 'app_user'@'localhost';
FLUSH PRIVILEGES;
"

sudo mysql customer_registration -e "
CREATE TABLE IF NOT EXISTS customer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    birth_date DATE NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS address (
    id INT AUTO_INCREMENT PRIMARY KEY,
    street_customer VARCHAR(255) NOT NULL,
    number VARCHAR(20) NOT NULL,
    neighborhood VARCHAR(100) NOT NULL,
    cep VARCHAR(10) NOT NULL,
    customer_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customer(id) ON DELETE CASCADE
);
"
```

### .env file

The app reads DB credentials from a `.env` file (gitignored) in the project root. Create it with:

```
DB_HOST=localhost
DB_USER=app_user
DB_PASSWORD=app_password
DB_NAME=customer_registration
DB_PORT=3306
```

### Running tests

- **Unit tests** (no DB required): `python3 -m pytest test/test_customer_service.py -v`
- **All tests**: `python3 -m pytest test/ -v`

### Known issue

`test/test_connection.py` has a pre-existing bug: it calls `get_connection()` without a `with` statement and tries to access `.is_connected()` on the context manager object instead of the yielded cursor. This test will fail regardless of environment setup.

### Running the application

The CLI entry point is `src/view/welcome_page.py`:

```bash
python3 -m src.view.welcome_page
```

Note: this is an interactive CLI app that reads from stdin — not suitable for non-interactive testing.

### Gotchas

- This environment uses no systemd; MySQL must be started manually via `mysqld`.
- No SQL migration files exist in the repo (`.sql` is gitignored). Schema must be created manually as shown above.
- No linter is configured in the project (no flake8, pylint, ruff, or mypy config).
