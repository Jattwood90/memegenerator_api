
<!-- ABOUT THE PROJECT -->

[![rest api](https://user-images.githubusercontent.com/56833060/113520193-5a1f7000-9589-11eb-9781-ca573adc27b7.gif)]

Here's a blank template to get started:
Basic RESTapi that serves images in a JSON format (for example: http://127.0.0.1:8000/%5Eapi/item/). A GET request can be made to fetch a promise, before each of the images are rendered into your project.

Note, there are no security credentials required for this API to work. Should this be required beyond demonstration purposes, API tokens and logins will need to be configured.

There are several images uploaded to this git account to use. However, should you require more or if they do not load automatically feel free to check out https://api.imgflip.com/get_memes to download your favourite meme templates!


### Built With

* [Django Rest Framework]()


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Jattwood90/memegenerator_api.git
   ```
2. Create virtual environment
   ```sh
   python3 -m venv djangoenv
   ```
3. Activate environment
   ```sh
   source djangoenv/bin/activate (windows users djangoenv venv\Scripts\activate.bat)
   ```
4. Install pip dependencies
   ```sh
   cd pip install -r requirements.txt
   ```
5. Activate localhost server (ensure your current directory is correct)
   ```sh
   python manage.py runserver
   ```


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.
