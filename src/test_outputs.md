### How to execute
* create a virtual environment and activate it
* install requirements
    >`pip install -r requirements.txt`
* `cd` into the directory which has `manage.py` in it.
* run `python manage.py runserver` in terminal
* open postman or similar tool and make a GET request in this fashion to `http://127:0:0.1:8000/`
>   http://127.0.0.1:8000/?src=https://storage.googleapis.com/bizupimg/profile_photo/IMG_20200917_190810.jpg

___
### Outputs

1. src = "https://storage.googleapis.com/bizupimg/profile_photo/IMG_20200917_190810.jpg"
* **Output**
    ```json
    {
        "logo_border": "#e0d9fe",
        "dominant_color": "#fadae1"
    }
    ```
2. src = "https://storage.googleapis.com/bizupimg/profile_photo/Screenshot%202020-08-16%20at%205.02.30%20PM%20-%20Nikunj%20Daruka.png"
* **Output**
    ```json
    {
        "logo_border": "#f6f4ef",
        "dominant_color": "#ecf2f1"
    }
    ```

3. src = "https://storage.googleapis.com/bizupimg/profile_photo/DigiKarobar-black.jpeg"
* **Output**
    ```json
    {
        "logo_border": "#1a1a1a",
        "dominant_color": "#1b1b1b"
    }
    ```
4. src = "https://storage.googleapis.com/bizupimg/profile_photo/WhatsApp%20Image%202020-08-23%20at%203.11.46%20PM%20-%20Himanshu%20Kohli.jpeg"
* **Output**
    ```json
    {
        "logo_border": "#14fb95",
        "dominant_color": "#080b08"
    }
    ```


___
### Contact Developer
**Animesh Kumar**
Email: 24animesh11@gmail.com
Mob: +91 7985851496
