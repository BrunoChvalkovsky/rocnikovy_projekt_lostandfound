# Repozitář ročníkové práce
Rok 2025/26
Autor: Bruno Chvalkovský 4.E
# Téma:
Stránka pro sdílení ztrát a nálezů.
# Popis:
Realizace webové aplikace pro komunitní sdílení informací o nalezených predmétech. Systém umožňuje uživatelům efektivně vyhledávat v databázi, vkládat nové záznamy, procházet příspěvky uživatelů, spravovat vlastní apod.
# Platformy:
- CSS
- Django
- HTML
- JavaScript
- Python
- SQL
# How to run:
1. Clone the repository:
    ```sh
    git clone https://github.com/brunochvalk/rp_lostandfound.git
    ```
2. Navigate to the project directory:
    ```sh
    cd rp_lostandfound
    ```
3. Create a virtual environment:
    ```sh
    python -m venv .venv
    ```
4. Activate the virtual environment:

    - On Windows:
        ```sh
        .venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source .venv/bin/activate
        ```
5. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
6. Apply the database migrations:
    ```sh
    python manage.py migrate
    ```
7. Load data from fixture
    ```sh
    python manage.py loaddata fixture.json
    ```
8. Run the development server:
    ```sh
    python manage.py runserver
    ```
