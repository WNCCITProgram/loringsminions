# Intro to Computer Science Flask Project

## Team Members

- Owen Osmera
- Christi Pendergraft
- Joe Scott
- Caleb Stewart
- Shawn Noon
- Eliezer Lamien
## AI ChatBot

Python Flask project to create an AI chatbot using an open-source model from Hugging Face, with tasks divided for a team.

This project uses the **Hugging Face Inference API**, which allows you to use powerful models for free without needing to download them or have a powerful computer.

### **Project Outline: Flask Chatbot with Hugging Face**

#### **1. Project Goal 🎯**

To build a web chatbot that uses a free, open-source AI model from Hugging Face to generate responses. The final product will be a simple, clean web page where a user can have a conversation with the AI.

#### **2. Key Technologies**

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **AI Service**: **Hugging Face Inference API** (Free Tier)
- **Python Libraries**: `requests`, `python-dotenv`

---

### **3. Implementation Plan**

This project is broken into four main phases to ensure a smooth workflow.

#### **Phase 1: Basic Flask Server & UI**

The first step is to create the skeleton of the application.

- Set up a basic Flask server in an `app.py` file.
- Create a simple HTML page (`index.html`) for the chat interface. This should include a chat history area, a text input box, and a "Send" button.
- Style the page using CSS (`style.css`) to make it look like a chat window.



#### **Phase 2: Frontend-Backend Communication**

Next, make the chat interface functional without any AI.

- Write JavaScript (`main.js`) to capture the user's message when they click "Send".
- Display the user's message in the chat history.
- Use the `fetch()` API in JavaScript to send the message to a new Flask route (e.g., `/chat`).
- In Flask, create the `/chat` route that receives the message and returns a simple, hardcoded response like `"I received your message."`
- The JavaScript should then display this hardcoded response in the chat window.

#### **Phase 3: Hugging Face API Integration**

This is where you connect the real AI.

- **Choose a Model**: Browse the [Hugging Face Hub](https://huggingface.co/models) and choose a suitable conversational model. A great starting point is **`google/gemma-2b-it`** or **`microsoft/DialoGPT-medium`**.
- **Get an API Token**: Create a free Hugging Face account and get a User Access Token from your settings.
- **Secure Your Token**: Store your token in a `.env` file to keep it safe and out of your code.
- **Update the Backend**: In your `/chat` route, write the Python code using the `requests` library to make a `POST` request to the model's Inference API endpoint. You'll need to include your API token in the authorization header.
- **Process the Response**: Parse the JSON response from Hugging Face to extract the generated text and send it back to your frontend.

---

### **4. Task Breakdown for 6 Students**

This project is perfect for a team of six, allowing students to specialize in different areas of web development.

#### **Pair 1: The Frontend Team (UI/UX)** 🎨

This pair is responsible for everything the user sees and interacts with.

- **Student 1 (HTML & Structure)**: Write the `index.html` file. Structure the chat window, message list, and input form using semantic HTML.
- **Student 2 (CSS & Styling)**: Own the `style.css` file. Design the chat bubbles, choose a color scheme, and make the interface responsive and visually appealing.

**Shared Goal**: Create an intuitive and attractive user interface.

#### **Pair 2: The Backend Team (Flask Core)** ⚙️

This pair builds the server-side foundation of the application.

- **Student 3 (Server & Routing)**: Set up the `app.py` file, initialize the Flask application, and create the routes for the home page (`/`) and the chat endpoint (`/chat`).
- **Student 4 (Request & Response Handling)**: Implement the logic within the routes to handle incoming `POST` requests from the frontend. Manage the data flow, ensuring that user input is correctly received and that responses are sent back in the proper JSON format.

**Shared Goal**: Build a stable and reliable server that connects the frontend to the AI logic.

#### **Pair 3: The AI Integration Team (API Connectors)** 🧠

This pair focuses on the "smart" part of the chatbot.

- **Student 5 (API Research & Logic)**: Research suitable conversational models on the Hugging Face Hub. Write the core Python function that takes a user's message, formats it correctly, and sends it to the Hugging Face Inference API.
- **Student 6 (Security & Data Parsing)**: Responsible for securely managing the Hugging Face API token using a `.env` file. They will also write the code to parse the complex JSON response from the API, extract the meaningful text, and handle potential errors (like if the API is down).

**Shared Goal**: Successfully connect to the Hugging Face API and reliably retrieve AI-generated responses.

## Project Ideas

### 1. Personal To-Do List ✅

A simple, single-user application to keep track of tasks. This avoids the complexity of collaboration and multiple accounts.

- **Key Features**: A user can register and log in. Once logged in, they can add tasks, mark tasks as complete, and delete them.
- **Task Breakdown**:
  - **Students 1 & 2 (Backend)**: Set up the database models for `User` and `Task`. Create the Flask routes to add, update, and delete tasks.
  - **Students 3 & 4 (Authentication & Forms)**: Handle the user registration and login logic. Create the web forms for adding and editing tasks.
  - **Students 5 & 6 (Frontend)**: Design the Jinja2 templates to display the task list and forms. Apply CSS to make it look clean.

---

### 2. Simple Recipe Book 🍲

A website to display a collection of recipes. This project focuses on reading data from a database and presenting it nicely.

- **Key Features**: A public homepage that lists all available recipes. Clicking a recipe shows a detailed view with ingredients and instructions. An admin page allows for adding or editing recipes.
- **Task Breakdown**:
  - **Students 1 & 2 (Backend & Database)**: Create the `Recipe` model in the database and populate it with a few examples. Write the routes to show all recipes and a single recipe detail page.
  - **Students 3 & 4 (Admin Panel)**: Build a simple admin page (no complex login needed at first) with a form to add new recipes to the database.
  - **Students 5 & 6 (Frontend)**: Design the templates for the recipe list and the detailed recipe view, focusing on readability.

---

### 3. Micro-Blog ✍️

A single-author blog where one person can log in to post updates, and the public can read them. This is a great introduction to content management.

- **Key Features**: A login page for the author. An interface for the author to create, edit, and delete posts. A public-facing page that lists all posts chronologically.
- **Task Breakdown**:
  - **Students 1 & 2 (Backend & Database)**: Create the `User` and `Post` models. Implement the routes for creating and deleting posts.
  - **Students 3 & 4 (Authentication)**: Implement a simple login/logout system for the single author. Protect the "new post" page so only the author can access it.
  - **Students 5 & 6 (Frontend)**: Design the templates for the main blog feed and the form for creating a new post.

---

### 4. Simple Guestbook 📖

A classic web project where visitors can leave a short message. It's a great way to learn how to handle form submissions.

- **Key Features**: A single page that displays a list of messages. A form where a visitor can enter their name and a message to be added to the list.
- **Task Breakdown**:
  - **Students 1 & 2 (Backend & Database)**: Create a simple `Message` model (name, content, timestamp). Write the single Flask route that both displays messages and handles the form submission for new ones.
  - **Students 3 & 4 (Form Handling)**: Create the web form for submitting a new message and add basic validation (e.g., name and message cannot be empty).
  - **Students 5 & 6 (Frontend)**: Design the single Jinja2 template that shows the list of messages and the submission form.

---

### 5. URL Shortener (Basic Version) 🔗

A tool that takes a long URL and generates a short link. This is an excellent project for understanding routes and database lookups.

- **Key Features**: A homepage with a form to submit a long URL. The app generates a unique short code, saves both URLs, and displays the new short link. When the short link is visited, the user is redirected to the original URL.
- **Task Breakdown**:
  - **Students 1 & 2 (Core Logic & Database)**: Design the `Link` model. Write the function to generate a random, unique short code.
  - **Students 3 & 4 (Routes)**: Create the main route for the submission form and the dynamic route that captures the short code and performs the redirect.
  - **Students 5 & 6 (Frontend)**: Design the simple HTML form and the result page that shows the user their shortened URL.

---

### 6. Event Calendar 📅

A simple site that lists upcoming events. This project avoids the complexity of ticketing and user roles.

- **Key Features**: A page that lists events with their date, time, and description. An admin area to add, edit, or delete events.
- **Task Breakdown**:
  - **Students 1 & 2 (Backend & Database)**: Create the `Event` model (title, date, description). Write the public route to display the list of all events.
  - **Students 3 & 4 (Admin Panel)**: Build the forms and routes for the admin to perform CRUD (Create, Read, Update, Delete) operations on events.
  - **Students 5 & 6 (Frontend)**: Design the Jinja2 templates for the public event list and style them to look like a calendar or agenda.

---

### 7. Simple Poll App 📊

An application where an admin can create a single poll and anyone can vote and see the results.

- **Key Features**: An admin page to create a poll with a question and a few options. A public voting page. A results page that shows how many votes each option received.
- **Task Breakdown**:
  - **Students 1 & 2 (Backend & Database)**: Design models for `Poll` and `Vote`. Create the route that handles saving a new poll created by the admin.
  - **Students 3 & 4 (Voting & Results)**: Create the routes for the voting page (which records a vote) and the results page (which counts the votes).
  - **Students 5 & 6 (Frontend)**: Design the three pages: the admin creation form, the public voting page, and the results page.

---

### 8. Digital Flashcard App 🧠

A study tool where a user can create decks of flashcards and quiz themselves.

- **Key Features**: A user can create a "deck." Within a deck, they can add "cards," each with a front (question) and a back (answer). A quiz mode displays the front and reveals the back on a button click.
- **Task Breakdown**:
  - **Students 1 & 2 (Backend & Database)**: Design the `Deck` and `Card` models. Create routes for viewing decks and the cards within them.
  - **Students 3 & 4 (Forms & Logic)**: Create the forms for adding new decks and new cards. Implement the logic for the "quiz" page.
  - **Students 5 & 6 (Frontend & Interactivity)**: Design the templates. Use a small amount of JavaScript to handle the "flip card" functionality on the quiz page.

---

### 9. Simple Contact Book 📇

A private, single-user address book to store contact information.

- **Key Features**: A user can log in. They can add contacts with a name, phone number, and email. They can view, edit, and delete their contacts.
- **Task Breakdown**:
  - **Students 1 & 2 (Backend & Database)**: Create `User` and `Contact` models. Write the routes for adding, editing, and deleting contacts.
  - **Students 3 & 4 (Authentication & Forms)**: Handle user login. Create the form for adding/editing a contact.
  - **Students 5 & 6 (Frontend)**: Design the main dashboard that lists all contacts and the form pages.

---

### 10. "Quote of the Day" Website 💬

A very simple website that displays a new, random quote each day.

- **Key Features**: A database of quotes. The homepage displays one random quote. An admin page allows adding new quotes to the database.
- **Task Breakdown**:
  - **Students 1 & 2 (Backend & Database)**: Create a `Quote` model (text, author). Write the main route that selects a random quote from the database and passes it to the template.
  - **Students 3 & 4 (Admin Panel)**: Build a simple form and route for an admin to add new quotes.
  - **Students 5 & 6 (Frontend)**: Design a visually appealing homepage to display the quote of the day.
