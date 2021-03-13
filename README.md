# Housing prices in Croatia

**This project scrapes data on housing prices on the most popular online marketplace in Croatia (www.njuskalo.hr). 
Data which is scraped is stored in `./Source/ML_Model/raw_data.json`. Raw data is then transformed to a pandas dataframe 
object and consumed by the machine learning models. The goal of this project is to create a web application which would 
accept user's input as a form, forward user's data to the chosen prediction model and return predicted price.**

### The project includes the following components:

#### 1. Web scraper (`./Source/Scraper_engine/`) 
#### 2. Machine learning models (`./Source/ML_Model/`)
#### 3. Django backend and JS, CSS, HTML front-end (`./Source/DjangoRoot/`)
#### 4. Data visualizations (`./Source/Visualizations/`)

#### How to run the project?
1. Clone the project.
2. Navigate to the project folder
   ```shell
   cd Web-scraper/
   
3. Create a new virtual environment and activate it.
4. Run the installation shell script
   ```shell
   pip3 install -r requirements.txt
   
5. Run ```cd Source/DjangoRoot && python3 manage.py runserver --insecure``` to start a localhost server on your machine. Please note that the `--insecure` flag is a Django option to force serving of static files with the staticfiles app even if the DEBUG setting is False. 
7. Navigate to `localhost:8000` and browse around. Try to input the specifications of the house you live in and check
how much would you pay for the same house in Croatia.
   
### Authors: 
Josip Dzidara & Mateo Ivan Radman
