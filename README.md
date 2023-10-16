# Task Pro: Your Ultimate Task Management Solution

Welcome to **Task Pro**, your go-to Django application for seamless task management! Task Pro empowers users to efficiently create, read, update, and delete tasks in a secure and user-friendly environment. This application is designed to streamline your task management process, ensuring that you stay organized and focused on what matters most.

## Key Features:

1. **User Authentication:** Task Pro prioritizes the security of your tasks. Users must log in to access and manage their tasks, ensuring that your information remains private and confidential.

2. **CRUD Operations:** With Task Pro, you can easily perform CRUD (Create, Read, Update, Delete) operations on your tasks. Whether you need to add a new task, check its details, update its status, or remove it, Task Pro has got you covered.

3. **Intuitive User Interface:** The user interface is designed with simplicity and efficiency in mind. Navigate through your tasks effortlessly and focus on what needs to be done without any unnecessary complexity.

4. **Task Categories:** Organize your tasks by assigning them to specific categories. This feature allows you to group related tasks together, making it even easier to manage and prioritize your responsibilities.

5. **Responsive Design:** Task Pro is built with a responsive design, ensuring a seamless experience across various devices. Whether you're accessing it from a desktop, tablet, or smartphone, Task Pro adapts to your screen size for optimal usability.

## Templates

### Base Template (`base.html`)

The `base.html` template serves as the foundational structure for all pages in Task Pro, providing a consistent and visually appealing layout. Here's a breakdown of its key components:

#### Meta Information:

- **Charset:** The template specifies the character set as UTF-8 for proper encoding.
- **Google Fonts:** Utilizes the Google Fonts API to load the Oswald and Roboto font families for a modern and stylish appearance.
- **Bootstrap:** Integrates Bootstrap 5.3.2 for responsive and mobile-friendly design, ensuring a consistent look across different devices.
- **FontAwesome:**  a versatile icon library, to enhance the visual elements of the application.
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

Feel free to customize the `base.html` template to suit your specific design preferences or functional requirements.

