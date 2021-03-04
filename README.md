# Word Counter
The purpose of this application is to count the words of the webpage of the requested URL.

# Setup

## Config
```
export APP_SETTINGS="config.DevelopmentConfig"
```

## DB Migrations
Before running these commands make sure that there is db with name `wordcount_dev` created in your local postgress instance.

```
python manager.py db init
python manager.py db migrate
python manager.py db upgrade
```

## NLTK
This application depends on nltk for text processing. Run the commands below before running the application for first time.
```
mkdir nltk_data
python -m nltk.downloader
```
When the installation window appears, update the ‘Download Directory’ to whatever_the_absolute_path_to_your_app_is/nltk_data/.

Then click the ‘Models’ tab and select ‘punkt’ under the ‘Identifier’ column. Click ‘Download’. Check the official [documentation](https://www.nltk.org/data.html#command-line-installation) for more information.

## Start the application
```
python app.py
```
On running this command the server will start at `http://localhost:5000/`