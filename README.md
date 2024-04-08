# Payment DB

## Description
This project is a demonstration of CRUD operations on three entities: Payment, Flat, and Service, implemented using SQLAlchemy with a PostgreSQL database. It utilizes Docker for containerization, Venv for virtual environment management, Alembic for database migrations, and Faker library for generating dummy data. Additionally, it includes functionalities such as Group By, Sorting, Join operations, REST API for JsonField model, reading with pagination, and Swagger documentation.

## Entities
- **Payment:** Represents a payment transaction.
- **Flat:** Represents a residential unit.
- **Service:** Represents a service provided.

## Technologies Used
- SQLAlchemy
- PostgreSQL
- Docker
- Venv
- Alembic
- Faker

## Functionalities
- CRUD operations
- Group By operations
- Sorting operations
- Join operations
- REST API for JsonField model
- Reading with pagination
- Population script using Faker library

## Dependencies
- [SQLAlchemy](link)
- [PostgreSQL](link)
- [Docker](link)
- [Venv](link)
- [Alembic](link)
- [Faker](link)

## Usage
1. Install dependencies listed in requirements.txt.
2. Set up PostgreSQL database and configure the connection string in the application.
3. Run Alembic migrations to initialize the database schema.
4. Run the application.
5. Access the REST API endpoints for CRUD operations and other functionalities.

## Documentation
- Swagger documentation is available for API endpoints.

## Contributors
- Arsen Petrosian

## License
This project is licensed under the MIT License - see the [LICENSE](link) file for details.
