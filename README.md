# Task Pro: Your Ultimate Task Management Solution

Welcome to **Task Pro**, your go-to Django application for seamless task management! Task Pro empowers users to efficiently create, read, update, and delete tasks in a secure and user-friendly environment. This application is designed to streamline your task management process, ensuring that you stay organized and focused on what matters most.

## Key Features:

1. **User Authentication:** Task Pro prioritizes the security of your tasks. Users must log in to access and manage their tasks, ensuring that your information remains private and confidential.

2. **CRUD Operations:** With Task Pro, you can easily perform CRUD (Create, Read, Update, Delete) operations on your tasks. Whether you need to add a new task, check its details, update its status, or remove it, Task Pro has got you covered.

3. **Intuitive User Interface:** The user interface is designed with simplicity and efficiency in mind. Navigate through your tasks effortlessly and focus on what needs to be done without any unnecessary complexity.

4. **Task Categories:** Organize your tasks by assigning them to specific categories. This feature allows you to group related tasks together, making it even easier to manage and prioritize your responsibilities.

5. **Responsive Design:** Task Pro is built with a responsive design, ensuring a seamless experience across various devices. Whether you're accessing it from a desktop, tablet, or smartphone, Task Pro adapts to your screen size for optimal usability.

## Task Templates

### Base Template (`base.html`)

The `base.html` template serves as the foundational structure for all pages in Task Pro, providing a consistent and visually appealing layout. Here's a breakdown of its key components:

#### Meta Information:

- **Charset:** The template specifies the character set as UTF-8 for proper encoding.
- **Google Fonts:** Utilizes the Google Fonts API to load the Oswald and Roboto font families for a modern and stylish appearance.
- **Bootstrap:** Integrates Bootstrap 5.3.2 for responsive and mobile-friendly design, ensuring a consistent look across different devices.
- **CSS:** Includes a custom stylesheet (`style.css`) located in the `static/css` directory to enhance the visual presentation.

#### Navigation Bar:

- **Logo Link:** The "Task Pro" logo in the navigation bar acts as a link. When the user is authenticated, it links to the task view (`view_tasks`), and when not authenticated, it links to the home page (`home`).
- **Toggle Button:** The navigation bar includes a toggle button for responsive design, allowing users to access navigation links on smaller screens.
- **User Authentication Links:** Depending on the user's authentication status, it provides links for signing out, signing up, or signing in.
- **Theme Toggle Button:** Features a button to toggle between light and dark themes, enhancing user customization.

#### Main Content:

- **Alert Messages:** Displays alert messages to provide feedback to the user. These messages are shown at the top of the page and automatically dismiss after a brief period.

#### Script References:

- **Bootstrap JavaScript:** Integrates the Bootstrap JavaScript bundle for enhanced functionality, such as the responsive navigation toggle.
- **FontAwesome:** Includes FontAwesome for the use of scalable vector icons.
- **Custom JavaScript:** Links to a custom JavaScript file (`app.js`) located in the `static/js` directory for additional custom functionality.

### Index (Home) Page Template (`index.html`)

The `index.html` template serves as the home page for Task Pro and extends the `base.html` template. Here's an overview of its key components:

#### Meta Information:

- The template extends the `base.html` template to maintain a consistent layout and styling throughout the application.
- Utilizes `{% load static %}` to load static files.

#### Content:

- **Hero Section (Non-authenticated users):** The hero section welcomes users to Task Pro and encourages them to log and track their tasks. It includes:
  - **Hero Text Container:** Contains the main text header and a brief description.
    - **Hero Text Header:** Displays the heading "Welcome To Task Pro."
    - **Hero Text Description:** Provides a subheading "Log and track your tasks."
    - **Sign In and Sign Up Buttons:** Links to the sign-in and sign-up pages (`{% url 'login' %}` and `{% url 'register_user' %}`) through visually appealing buttons.
  - **Hero SVG Wrapper:** Contains an SVG illustration representing the Task Pro concept.
    - **Hero SVG:** Displays an SVG image sourced from the `static/svg/task-pro-hero.svg` file.

### Task List Page Template (`task_list.html`)

The `task_list.html` template extends the `base.html` template and is responsible for displaying a tabbed interface to manage tasks. Here's an overview of its key components:

#### Meta Information:

- The template extends the `base.html` template to maintain a consistent layout and styling throughout the application.
- Utilizes `{% load static %}` to load static files.

#### Content:

- **Tabbed Interface Section (`tabbed-interface`):** The section displays a tabbed interface for different task categories.
  - **Add Task Button:** A button to navigate to the "Add A New Task" page.
  - **Category Headers:** Headers for different task categories: "All," "Urgent," and "Completed."
  - **Line Separator:** A visual separator line beneath the category headers.

- **Task Content Boxes:** Three boxes corresponding to each task category with the following structure:
  - **Content Box (All Tasks):** Displays all tasks.
  - **Content Box (Urgent Tasks):** Displays only urgent tasks.
  - **Content Box (Completed Tasks):** Displays only completed tasks.

Within each content box:
  - **Category Heading:** Heading indicating the category of tasks being displayed.
  - **Task List:** Lists tasks for the specific category.
    - **Task Title:** Displays the title of each task.
      - If the task is completed, the title has a strikethrough style.
    - **Task Icons:** Icons to update or delete each task.
    - **Task Description:** Describes the details of each task.

  - **Empty Message:** Displayed when there are no tasks in a specific category.

### Add Task Form Template (`add_task_form.html`)

The `add_task_form.html` template extends the `base.html` template and is responsible for rendering a form to add a new task in Task Pro. Here's an overview of its key components:

#### Meta Information:

- The template extends the `base.html` template to maintain a consistent layout and styling throughout the application.
- Utilizes `{% load static %}` to load static files.

#### Content:

- **Form Header:** Displays a visually appealing header indicating the purpose of the form: "Add A New Task."

- **Task Form:** A form element with the method set to "post" and the action pointing to the URL for adding a new task (`{% url 'add_task' %}`). This form includes the following input fields:
  - **Task Title:** A text input field (`<input>`) for entering the title of the task.
  - **Task Description:** A textarea input field (`<textarea>`) for entering a detailed description of the task.
  - **Urgent Checkbox:** A checkbox input (`<input type="checkbox">`) allowing users to mark the task as urgent.
  
- **Form Submission Button:** A "Submit" button (`<button>`) with the class "btn btn-primary" to submit the form.

### Edit Task Page Template (`edit_task.html`)

The `edit_task.html` template extends the `base.html` template and is used for editing an existing task. Here's an overview of its key components:

#### Meta Information:

- The template extends the `base.html` template to maintain a consistent layout and styling throughout the application.
- Utilizes `{% load static %}` to load static files.

#### Content:

- **Form Header Container:** Displays a container with a header indicating that the user is editing the task.
- **Edit Form:** A form allowing the user to edit the task details.
  - **Task Title Field:** An input field displaying the current task title and allowing the user to modify it.
  - **Task Description Field:** A textarea displaying the current task description and allowing the user to modify it.
  - **Urgent Checkbox:** A checkbox indicating whether the task is urgent. It is checked if the task is currently marked as urgent.
  - **Completed Checkbox:** A checkbox indicating whether the task is completed. It is checked if the task is currently marked as completed.
  - **Update Task Button:** A button to submit the form and update the task.

#### Edit Task Page Template (`edit_task.html`)

The `edit_task.html` template extends the `base.html` template and is used for editing an existing task. Here's an overview of its key components:

#### Meta Information:

- The template extends the `base.html` template to maintain a consistent layout and styling throughout the application.
- Utilizes `{% load static %}` to load static files.

#### Content:

- **Form Header Container:** Displays a container with a header indicating that the user is editing the task.
- **Edit Form:** A form allowing the user to edit the task details.
  - **Task Title Field:** An input field displaying the current task title and allowing the user to modify it.
  - **Task Description Field:** A textarea displaying the current task description and allowing the user to modify it.
  - **Urgent Checkbox:** A checkbox indicating whether the task is urgent. It is checked if the task is currently marked as urgent.
  - **Completed Checkbox:** A checkbox indicating whether the task is completed. It is checked if the task is currently marked as completed.
  - **Update Task Button:** A button to submit the form and update the task.

### Delete Task Page Template (`delete_task.html`)

The `delete_task.html` template extends the `base.html` template and is used for deleting a task. Here's an overview of its key components:

#### Meta Information:

- The template extends the `base.html` template to maintain a consistent layout and styling throughout the application.
- Utilizes `{% load static %}` to load static files.

#### Content:

- **Form Header Container:** Displays a container with a header indicating that the user is deleting the task.
- **Delete Form:** A form allowing the user to confirm the deletion of the task.
  - **Task Title Field:** An input field displaying the current task title (disabled and non-editable).
  - **Task Description Field:** A textarea displaying the current task description (disabled and non-editable).
  - **Urgent Checkbox:** A checkbox indicating whether the task is urgent. It is checked if the task is currently marked as urgent (disabled).
  - **Completed Checkbox:** A checkbox indicating whether the task is completed. It is checked if the task is currently marked as completed (disabled).
  - **Delete Button:** A button to submit the form and confirm the deletion of the task.
