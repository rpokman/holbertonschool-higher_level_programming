# SQL - Introduction

A foundational project exploring database concepts and MySQL basics through practical SQL exercises.

## 📋 Overview

This project introduces core database concepts including relational databases, SQL syntax, and MySQL operations. Students learn to create, manipulate, and query databases through hands-on tasks.

## 🎯 Learning Objectives

- Understanding databases and relational database concepts
- MySQL installation and basic operations
- SQL syntax: DDL (Data Definition Language) and DML (Data Manipulation Language)
- Creating and modifying database structures
- Querying data with SELECT statements
- Data manipulation with INSERT, UPDATE, DELETE
- Using MySQL functions and subqueries

## 🛠 Technologies

- **MySQL 8.0** - Primary database system
- **Ubuntu 22.04 LTS** - Development environment
- **SQL** - Query language

## 📁 Project Structure

```
SQL_introduction/
├── 0-list_databases.sql          # List all databases
├── 1-create_database_if_missing.sql   # Create database
├── 2-remove_database.sql         # Delete database
├── 3-list_tables.sql             # List tables
├── 4-first_table.sql             # Create table
├── 5-full_table.sql              # Show table structure
├── 6-list_values.sql             # Select all data
├── 7-insert_value.sql            # Insert data
├── 8-count_89.sql                # Count specific records
├── 9-full_creation.sql           # Create and populate table
├── 10-top_score.sql              # Order by score
├── 11-best_score.sql             # Filter by score
├── 12-no_cheating.sql            # Update records
├── 13-change_class.sql           # Delete records
├── 14-average.sql                # Calculate average
├── 15-groups.sql                 # Group by score
└── 16-no_link.sql                # Filter null values
```

## 🚀 Getting Started

### Prerequisites

```bash
# Update system
sudo apt update

# Install MySQL Server
sudo apt install mysql-server

# Verify installation
mysql --version
```

### Usage

```bash
# Execute SQL scripts
cat script.sql | mysql -hlocalhost -uroot -p [database_name]

# Example
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
```

## 📝 Key Concepts Covered

- **Database Operations**: CREATE, DROP databases
- **Table Management**: CREATE, ALTER, DROP tables
- **Data Queries**: SELECT with WHERE, ORDER BY, GROUP BY
- **Data Modification**: INSERT, UPDATE, DELETE
- **Aggregate Functions**: COUNT, AVG
- **Data Filtering**: NULL handling, conditional queries

## ⚙️ Requirements

- All SQL keywords in uppercase
- Comments required for each script
- Ubuntu 22.04 LTS compatibility
- MySQL 8.0 compatibility
- Files must end with newline

## 📚 Resources

- [What is Database & SQL?](https://www.youtube.com/watch?v=FR4QIeZaDp8)
- [MySQL Basic Tutorial](https://www.mysqltutorial.org/mysql-basics/)
- [MySQL 8.0 Documentation](https://dev.mysql.com/doc/refman/8.0/en/)

## 🏆 Tasks Overview

| Task | Description | File |
|------|-------------|------|
| 0 | List databases | `0-list_databases.sql` |
| 1 | Create database | `1-create_database_if_missing.sql` |
| 2 | Delete database | `2-remove_database.sql` |
| 3 | List tables | `3-list_tables.sql` |
| 4 | Create first table | `4-first_table.sql` |
| 5 | Show table description | `5-full_table.sql` |
| 6 | List table values | `6-list_values.sql` |
| 7 | Insert data | `7-insert_value.sql` |
| 8 | Count records | `8-count_89.sql` |
| 9 | Create and populate table | `9-full_creation.sql` |
| 10 | Order by score | `10-top_score.sql` |
| 11 | Filter by score | `11-best_score.sql` |
| 12 | Update records | `12-no_cheating.sql` |
| 13 | Delete records | `13-change_class.sql` |
| 14 | Calculate average | `14-average.sql` |
| 15 | Group by score | `15-groups.sql` |
| 16 | Filter NULL values | `16-no_link.sql` |

---