# RecipeLens

<p align="center"> 
<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Grinning%20Face.png" alt="Grinning Face" width="50" height="50" />
<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Robot.png" alt="Robot" width="150" height="150" />
</p>

## Overview

RecipeLens is a project designed to help people by providing recipes along with the required ingredients for various dishes. Users can simply take a picture of the food or upload an image, and RecipeLens will identify the dish and provide the corresponding recipe. This innovative approach leverages image recognition technology to simplify the process of finding recipes and preparing meals.

## Features

- **Image Recognition:** Upload a photo or take a picture of a dish, and RecipeLens will identify it.
- **Recipe Suggestions:** Get detailed recipes for the identified dishes, including a list of required ingredients.
- **User-Friendly Interface:** Easy-to-use interface for a seamless user experience.
  

## File Structure

    Final-Year-Project
    │
    ├── PPT
    │   └── Presentation on RecipeLens.pptx
    │
    ├── Documents
    │   ├── A Project Report on Recipelens.pdf
    │   └── A Project Report on Recipelens.docx
    │
    ├── Source Code
    │   ├── Info.txt
    │   ├── RecipeLens
    │   │   ├── src
    │   │   │   ├── main
    │   │   │   │   ├── migrations
    │   │   │   │   ├── static
    │   │   │   │   │   └── main
    │   │   │   │   │       ├── icons
    │   │   │   │   │       ├── indian_recipes.json
    │   │   │   │   │       └── style.css
    │   │   │   │   ├── templates
    │   │   │   │   │   └── main
    │   │   │   │   │       └── home.html
    │   │   │   │   ├── __init__.py
    │   │   │   │   ├── admin.py
    │   │   │   │   ├── apps.py
    │   │   │   │   ├── encoder.py
    │   │   │   │   ├── forms.py
    │   │   │   │   ├── models.py
    │   │   │   │   ├── tests.py
    │   │   │   │   ├── urls.py
    │   │   │   │   └── views.py
    │   │   │   ├── RecipeLens
    │   │   │   ├── db.sqlite3
    │   │   │   ├── enc_names.txt
    │   │   │   ├── encoding.txt
    │   │   │   └── manage.py
    │   ├── venv
    │   └── requirments.txt


## Setup Instructions

### 1. Create a Virtual Environment

To create a virtual environment named `venv` in the same location as it is in the file structure:

1. Open a terminal (Command Prompt, PowerShell, or terminal application on your operating system).
2. Navigate to the `Source Code/RecipeLens` directory using the `cd` command. Replace `path/to` with the actual path to the `Final-Year-Project` folder on your computer.

    ```sh
    cd path/to/Final-year-Project/Source Code/RecipeLens
    ```

3. Create a virtual environment named `venv` using the following command:

    ```sh
    python -m venv venv
    ```

### 2. Activate the Virtual Environment

To activate the virtual environment:

- **On Windows:**

    ```sh
    venv\Scripts\activate
    ```

- **On macOS/Linux:**

    ```sh
    source venv/bin/activate
    ```

When the virtual environment is activated, you will see `(venv)` at the beginning of your terminal prompt.

### 3. Install Required Libraries

To install all the libraries mentioned in the `requirments.txt` file:

1. Ensure you are still in the `Source Code/RecipeLens` directory and the virtual environment is activated.
2. Run the following command:

    ```sh
    pip install -r requirments.txt
    ```

This command will install all the dependencies listed in the `requirments.txt` file.

### 4. Run the Django Development Server

To start the Django development server:

1. Navigate to the `src` directory:

    ```sh
    cd src
    ```

2. Run the Django development server using the `manage.py` file:

    ```sh
    python manage.py runserver
    ```

### 5. Access the Localhost Address

After successfully running the command, you will see output similar to the following in your terminal:

```sh
Starting development server at http://127.0.0.1:8000/
```
Open a web browser and go to the address http://127.0.0.1:8000/ to view the running Django application.

## Contributors
- [![Biplab Gorain](https://github.com/BiplabGorain.png?size=50)](https://github.com/BiplabGorain) [Biplab Gorain](https://github.com/BiplabGorain)
- [![Bishnu Sharma](https://github.com/vishnusharma7.png?size=50)](https://github.com/vishnusharma7) [Bishnu Sharma](https://github.com/vishnusharma7)
- [![Sheela Bhattacharjee](https://github.com/Sheelabhattacharjee.png?size=50)](https://github.com/Sheelabhattacharjee) [Sheela Bhattacharjee](https://github.com/Sheelabhattacharjee)
- [![Projjal Mitra](https://github.com/PROJJALL.png?size=50)](https://github.com/PROJJALL) [Projjal Mitra](https://github.com/PROJJALL)
