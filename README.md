# Gradebook Application Portal

Gradebook Application Portal is a simple Flask application used for maintaning student's detail and their enrolled cources

![Home](https://github.com/user-attachments/assets/7db4c876-cf65-4cf8-b2ce-bd59af4eb556)


## Index
-   [Features](#Features)
-   [File Structure](#File-Structure)
-   [Database Structure](#Database-Structure)
    -   [Course Table Schema](#Course-Table-Schema)
    -   [Student Table Schema](#Student-Table-Schema)
    -   [Enrollment Table Schema](#Enrollment-Table-Schema)
-   [Getting Started](#Getting-Started)
	-   [Prerequisites](#Prerequisites)
	-   [Installation](#Installation)
-   [Screenshots](#Screenshots)
-   [Further Api Implementation](#Further-Api-Implementation)       	

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

## Getting Started

### Prerequisites
- Python 3.x
- Flask
- Flask-SQLAlchemy

### Installation
- Clone the repository:
```bash
    git clone https://github.com/Vaibhav0221/Gradebook.git
```

- Navigate to the project directory:
```bash
    cd Gradebook
```

- Install the required packages:
```bash
    pip install -r requirements.txt
```

- Run the app file
```bash
    flask run
```

## Screenshots

![Add_student](https://github.com/user-attachments/assets/8ba53ec0-2cb2-422d-9779-444b09f509bc)

![Student_details](https://github.com/user-attachments/assets/538ff960-0d12-4f9c-8e60-74e5ed088256)

## Further Api Implementation
| Method | Path | Description |
|--|--|---| 
| GET |/api/course/{course_id} |Operation to Read Course resource|
| GET |/api/student/{student_id} |Operation to Read Stduent resource |
| GET |/api/student/{student_id}/course |Operation to get the list of enrollments, the student is enrolled in. |
| PUT |/api/course/{course_id} |Operation to update the course |
| PUT |/api/student/{student_id} |Operation to update student resource |
| DELETE |/api/course/{course_id} |Operation to delete the course resource |
| DELETE |/api/student/{student_id} |Operation to delete the student resource |
| DELETE |  /api/student/{student_id}/course/{cource_id} |Operation to delete the student in particular enrolled course |
| POST |/api/course |Operation to create course resource |
| POST |/api/student |Operation to create student resource |
| POST |/api/student/{student_id}/course |Operation to add student enrollment |






