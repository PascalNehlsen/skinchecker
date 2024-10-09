# SkinChecker

SkinChecker is a Django application that retrieves data from the Skinport API and displays it on a web page. The application provides a simple interface to show information about various items and their prices.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Quickstart](#quickstart)
- [Security](#security)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin using this application, ensure you meet the following requirements:

- Python 3.12.5
- Django 5.1.2
- An API key for the Skinport API (set this as the environment variable `API_KEY`)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/pascalnehlsen/skinchecker.git
   cd skinchecker
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate  # For Windows
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set your API key as an environment variable**:

   ```bash
   export API_KEY='your_api_key'  # For macOS/Linux
   set API_KEY='your_api_key'  # For Windows
   ```

## Quickstart

Here are the steps to quickly get the application up and running:

- **Clone the repository**: Clone the repository as described above.
- **Activate the virtual environment**: Activate the virtual environment.
- **Install packages**: Install the required packages.
- **Set API key**: Make sure the API key is set as an environment variable.
- **Initialize the database**:

  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

- **Start the development server**:

  ```bash
  python manage.py runserver
  ```

- **Access the application**: Open your browser and go to http://127.0.0.1:8000/.

## Security

To ensure that no sensitive data (like API keys) gets into your Git repository, I recommend using [git-secrets](https://github.com/awslabs/git-secrets).

## Contributing

Contributions are welcome! If you find bugs or want to add new features, please open an issue or create a pull request.

## Contact

- Pascal Nehlsen - [LinkedIn](https://www.linkedin.com/in/pascal-nehlsen) - [mail@pascal-nehlsen.de](mailto:mail@pascal-nehlsen.de)
- Project Link: [https://github.com/PascalNehlsen/skinchecker](https://github.com/PascalNehlsen/skinchecker)
