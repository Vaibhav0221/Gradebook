# Gradebook Application Portal

Gradebook Application Portal is a simple Flask application used for maintaning student's detail and their enrolled cources

![Home](https://github.com/user-attachments/assets/8725b55f-042c-4aac-9c67-1245a465a204)

## Index
-   [Features](#Features)
-   [File Structure](#File-Structure)
-   [Database Structure](#Database-Structure)
    -   [Course Table Schema](#Course-Table-Schema)
    -   [Student Table Schema](#Student-Table-Schema)
    -   [Enrollment Table Schema](#Enrollment-Table-Schema)

## Features

- Add a student
- Update/ delete a student
- View particular student information



## File Structure

```bash
.
├── static
    └── css
        └── style.css
├── templates
    ├── create.html
    ├── create_exist.html
    ├── index.html
    ├── update.html
    └── view.html
├── README.md
├── app.py
├── database.sqlite3
└── requirements.txt
```
## Database Structure

### Course Table Schema

```bash
| Column Name        | Column Type | Constraints                      |  
|--------------------|-------------|----------------------------------|
| course_id          | Integer     | Primary Key, Auto Increment      |
| course_name        | String      | Not Null                         |   
| course_code        | String      | Unique, Not Null                 |
| course_description | String      |                                  |

```

### Student Table Schema

```bash
| Column Name        | Column Type | Constraints                      |
|--------------------|-------------|----------------------------------|
| student_id         | Integer     | Primary Key, Auto Increment      |
| roll_number        | String      | Unique, Not Null                 |
| first_name         | String      | Not Null                         |
| last_name          | String      |                                  |	
	
```

### Enrollment Table Schema

```bash
| Column Name        | Column Type | Constraints                                      |
|--------------------|-------------|--------------------------------------------------|
| enrollment_id      | Integer     | Primary Key, Auto Increment                      |
| student_id         | Integer     | Foreign Key (student.student_id), Not Null       |
| course_id          | Integer     | Foreign Key (course.course_id), Not Null         |

```
