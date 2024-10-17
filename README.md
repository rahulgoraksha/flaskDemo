markdown
Copy code
# Flask Website Using Python

This repository contains a simple website built using the **Flask** web framework in **Python**. The website includes multiple pages that display different book categories and their details.

## Features
- **Homepage**: Displays a welcome message and navigation options.
- **Book Categories**: Users can explore different book genres such as *Thriller*, *Fiction*, and *Young Adult*.
- **Book Details**: Each genre page lists books with information like title, author, price, and a brief description.
- **Hyperlinks**: Each genre is accessible through clickable links for easy navigation.
- **Static Assets**: Images and other static resources are properly managed using Flask's `url_for()` function.

## Project Structure

├── app.py ├── templates │ ├── books.html │ ├── book_thriller.html │ ├── book_fiction.html │ ├── book_adult.html ├── static │ └── images │ ├── book1.jpeg │ ├── book2.jpeg │ ├── book3.jpeg │ └── book5.jpeg └── README.md
markdown
Copy code

- **`app.py`**: The main Flask application file.
- **`templates/`**: Contains the HTML templates for the website pages.
- **`static/`**: Holds static resources like images and styles.
- **`README.md`**: This documentation file.

## Getting Started

Follow these instructions to run the project on your local machine.

### Prerequisites

- **Python 3.x**: Ensure Python is installed. Download it from [python.org](https://www.python.org/).
- **Flask**: Install Flask using the command below:

  ```bash
  pip install Flask
Installation
1.	Clone the repository:
bash
Copy code
git clone https://github.com/<your-username>/<your-repository>.git
2.	Navigate to the project directory:
bash
Copy code
cd <your-repository>
3.	Run the application:
bash
Copy code
python app.py
4.	Access the website:
Open a browser and go to http://127.0.0.1:5000.
Application Routes
The following routes are used in the application:
•	/: Homepage of the website.
•	/book_cat: Displays available book categories.
•	/book_thriller: Shows thriller book details.
•	/book_fiction: Shows fiction book details.
•	/book_adult: Shows young adult book details.
•	/book_back: Redirects back to the book categories page.

