# Study Planner

#### Video Demo: https://youtu.be/cseqX9r92qs

#### Description:

Study Planner is a web-based application designed to help students organize their academic tasks, subjects, deadlines, and priorities in one place.

The application allows users to create their own accounts and log in securely. Each user has a personal dashboard where they can add tasks and specify a subject, deadline, and priority level. Tasks can be marked as completed, edited, or deleted.

The dashboard displays all tasks in an organized table and clearly shows their current status. Priority levels are visually distinguished to make important tasks easier to identify. Users can also filter their tasks by status to display all tasks, pending tasks, or completed tasks.

The project was built using Python and Flask for the backend, SQLite for storing users and tasks, and HTML, CSS, and JavaScript for the frontend.

## Features

Study Planner includes the following features:

- User registration with securely hashed passwords.
- User login and logout using sessions.
- A personal dashboard for each user.
- Adding new study tasks.
- Assigning a subject to each task.
- Setting a deadline for tasks.
- Choosing a priority level: Low, Medium, or High.
- Marking tasks as completed.
- Editing existing tasks.
- Deleting tasks.
- Filtering tasks by All, Pending, or Completed.
- A simple and clean interface for managing tasks.

## Project Files

### app.py

This is the main Python file of the application. It contains the Flask application and handles the main functionality of Study Planner.

The file contains routes for registration, login, logout, displaying the dashboard, adding tasks, editing tasks, completing tasks, and deleting tasks.

It also connects the application to the SQLite database using the CS50 SQL library. Sessions are used to keep track of the currently logged-in user.

Each database operation involving tasks uses the user's ID. This ensures that users can only view and modify their own tasks.

### planner.db

This is the SQLite database used by the application.

The database stores registered users and their study tasks. User passwords are not stored directly. Instead, password hashes are generated and stored for better security.

Each task is connected to the user who created it using a user ID.

### schema.sql

This file contains the SQL structure used to create the tasks table.

Each task contains an ID, user ID, title, subject, deadline, priority, and completion status.

The completed field is used to determine whether a task is still pending or has already been completed.

### templates/index.html

This template displays the main Study Planner dashboard.

It shows the user's tasks in a table containing the task title, subject, deadline, priority, status, and available actions.

Users can complete, edit, or delete tasks directly from this page.

The page also contains filtering buttons that allow the user to display all tasks, only pending tasks, or only completed tasks. JavaScript is used to perform this filtering without requiring the page to reload.

### templates/add.html

This template contains the form used to create a new study task.

The user can enter a task title and subject, choose a deadline, and select a priority level.

After the form is submitted, the information is stored in the SQLite database and the user is redirected back to the dashboard.

### templates/edit.html

This template allows the user to modify an existing task.

The current information about the task is displayed inside the form so the user can change the title, subject, deadline, or priority.

After saving the changes, the database is updated and the user returns to the dashboard.

### templates/login.html

This template contains the login form.

Users enter their username and password. The application checks the submitted information against the users stored in the database before creating a session for the user.

### templates/register.html

This template contains the registration form for new users.

A user chooses a username and password and confirms the password. The application checks the submitted information before creating the account.

Passwords are hashed before being stored in the database.

### static/styles.css

This file contains the visual styling for Study Planner.

It defines the appearance of the page background, navigation area, tables, forms, links, buttons, and other interface elements.

Different priority levels are displayed using different visual styles so that users can quickly identify important tasks.

### requirements.txt

This file contains the Python packages required for the project.

It allows the required dependencies to be identified when the application is installed or run in another environment.

## Design Choices

I decided to build Study Planner because students often have several assignments, exams, projects, and study goals at the same time. Keeping these tasks in one organized application makes it easier to see what needs to be completed.

I chose Flask because it provides a simple way to connect Python backend logic with HTML templates. SQLite was selected because the application needs persistent storage for users and tasks while remaining lightweight and easy to manage.

The tasks are associated with individual user IDs rather than being stored globally. This was an important design decision because each registered user should have a separate task list.

I included three priority levels: Low, Medium, and High. This allows users to distinguish between tasks based on importance instead of treating every task in the same way.

I also included deadlines so users can see when each task needs to be completed. Tasks are ordered on the dashboard to make the list easier to manage.

Instead of deleting a task when it is completed, the application stores its completion status. This allows completed tasks to remain visible and gives users a record of what they have finished.

The filtering feature was implemented with JavaScript. It allows the user to switch between All, Pending, and Completed tasks immediately without sending another request to the Flask server.

The interface was intentionally kept simple. The main goal of the design is to make the application easy to understand and quick to use rather than adding unnecessary visual complexity.

## How to Use the Application

A new user begins by creating an account on the registration page. After registration, the user can log in using their username and password.

Once logged in, the user is taken to the dashboard. From there, the user can create a new task and provide its title, subject, deadline, and priority.

The task then appears on the dashboard. A pending task can be marked as completed when it is finished.

Users can also edit a task if its information changes or delete a task if it is no longer needed.

The All, Pending, and Completed buttons can be used to filter the tasks displayed on the dashboard.

When finished using the application, the user can log out. The session is cleared and the user is returned to the login page.

## Conclusion

Study Planner combines user authentication, database storage, backend routing, HTML templates, CSS styling, and JavaScript interaction in a single web application.

The project provided an opportunity to apply concepts learned throughout CS50, including Python, SQL, Flask, HTML, CSS, JavaScript, databases, authentication, and web application development.

The final result is a functional study management application where different users can securely organize and manage their own academic tasks.
