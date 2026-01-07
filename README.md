# Migration Engine

A command-line ETL pipeline tool that safely migrates legacy CSV data into PostgreSQL databases. Features data validation, transformation, duplicate handling, and rollback capabilities.

## Features

- **ETL Pipeline**: Extract, Transform, Load data from CSV to PostgreSQL
- **Data Validation**: Comprehensive validation with detailed warnings and error reporting
- **Data Transformation**: Automatic type detection, column cleaning, and data normalization
- **Duplicate Handling**: Configurable strategies for handling duplicate records
- **Rollback Support**: Safe rollback functionality for failed migrations
- **Batch Processing**: Configurable batch sizes for large datasets
- **Logging**: Detailed logging with configurable levels
- **Configuration**: YAML configuration files and environment variable support

## Installation

```bash
# Clone the repository
git clone https://github.com/okjazim/Migration-Engine.git
cd Migration-Engine

# Install dependencies
pip install -r requirements.txt

# Or install as a package
pip install -e .
```

## Quick Start

1. **Set up your database connection** (environment variables or config file):
```bash
export DB_HOST=localhost
export DB_PORT=5432
export DB_NAME=my_database
export DB_USER=my_user
export DB_PASSWORD=my_password
```

2. **Run a migration**:
```bash
python main.py migrate sample_data.csv --db-name my_database --db-user my_user --db-password my_password
```

## Usage

### Basic Migration

```bash
# Migrate CSV to PostgreSQL
python main.py migrate data.csv --db-name mydb --db-user postgres --db-password secret

# Use custom table name
python main.py migrate data.csv --table-name my_custom_table --db-name mydb --db-user postgres

# Dry run (validate without loading)
python main.py migrate data.csv --dry-run --db-name mydb --db-user postgres
```

### Configuration File

Create a `migration_config.yaml` file:

```yaml
database:
  host: localhost
  port: 5432
  name: my_database
  user: my_user
  password: my_password

migration:
  batch_size: 1000
  log_level: INFO
  create_table: true
  on_duplicate: skip  # skip, update, error
  validate_data: true

data_types:
  auto_detect: true
  date_formats: ['%Y-%m-%d', '%m/%d/%Y', '%d-%m-%Y']
  null_values: ['NULL', 'null', 'NA', 'N/A', '']
```

Use the config file:
```bash
python main.py migrate data.csv --config migration_config.yaml
```

### Validation Only

```bash
# Validate CSV without migrating
python main.py validate data.csv
```

### Generate Config Template

```bash
# Create a sample configuration file
python main.py init-config
```

## Command Reference

### `migrate`
Migrate CSV data to PostgreSQL database.

**Options:**
- `--db-host`: Database host (default: localhost)
- `--db-port`: Database port (default: 5432)
- `--db-name`: Database name (required)
- `--db-user`: Database username (required)
- `--db-password`: Database password (can use PGPASSWORD env var)
- `--table-name`: Target table name (defaults to CSV filename)
- `--batch-size`: Batch size for processing (default: 1000)
- `--dry-run`: Validate without loading data
- `--config`: Configuration file path
- `--log-level`: Logging level (DEBUG, INFO, WARNING, ERROR)

### `validate`
Validate CSV file structure and data quality.

### `init-config`
Generate a sample configuration file.

## Data Handling

### Data Types
The tool automatically detects and converts data types:
- **Numeric**: Integers and floats
- **Boolean**: true/false, yes/no, 1/0 values
- **DateTime**: Multiple date formats supported
- **Text**: String data with cleaning

### Missing Values
Configurable handling of missing/null values:
- Custom null value definitions
- Automatic detection and preservation

### Duplicates
Three strategies for handling duplicates:
- **skip**: Skip duplicate records (default)
- **update**: Update existing records
- **error**: Fail on duplicates

### Column Names
Automatic cleaning of column names:
- Convert to lowercase
- Replace special characters with underscores
- Handle duplicates

## Environment Variables

```bash
# Database
DB_HOST=localhost
DB_PORT=5432
DB_NAME=my_database
DB_USER=my_user
DB_PASSWORD=my_password

# Migration
MIGRATION_BATCH_SIZE=1000
LOG_LEVEL=INFO
```

## Sample Data

The `sample_data.csv` file demonstrates various data scenarios:
- Different data types (text, numbers, dates, booleans)
- Missing values
- Various date formats
- Mixed case column names

## Development

### Project Structure
```
migration-engine/
├── src/
│   ├── __init__.py
│   ├── cli.py           # Command-line interface
│   ├── core.py          # Main migration engine
│   ├── config.py        # Configuration management
│   ├── database.py      # PostgreSQL operations
│   ├── validators.py    # Data validation
│   └── transformers.py  # Data transformation
├── main.py              # Entry point
├── setup.py             # Package setup
├── requirements.txt     # Dependencies
├── sample_data.csv      # Sample data
└── README.md
```

### Running Tests
```bash
# Install development dependencies
pip install pytest

# Run tests
pytest
```

## License
This project is licensed under the **MIT License**.
See [`LICENSE`](LICENSE) for details. © 2026 okjazim
