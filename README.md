<h1>WebPageTest-Data-Tabulator</h1>
Run the automation, and get tabulated on terminal and in a table on CSV file with the following data:

- Grade, 
- Name, 
- Link, 
- Currentimages sizes,
- ideal images sizes.

<H2>***IMPORTANT***</H2>
<H4>STEP 0:</H4>
<b>Go to official pages and install: </b>

- Python 3+ (https://www.python.org/downloads/);
- chromedriver (search for your chrome installed version, and download the chromedriver of same version on https://chromedriver.chromium.org/downloads).

<b>To install the dependencies on terminal, type "pip install" +: </b>

- Selenium;
- time;
- pandas;
- tdqm.

<h3>IF YOU HAVE EVERYTHING ALREADY INSTALLED, </h3>
<h4> STEP1:</h4> 

- Go to 16th line of this code and change the text 'wayOfChromedriverOnYourPC/chromedriver.exe' to the 'way of Chromedriver on your PC before the "/chromedriver.exe", for exemple: 'C:/Users/name/software/chromedriver.exe';
- Go to 20th line and change the text 'yourEntirePageLink' to 'your entire page link', for exemple: 'https://www.youtube.com/@dark_taylor';
- Go to 26th line and change the number on tdqm for or time.sleep for the better configuration to your specific test;
- Go to 55th line and change the 'nameYourTable.csv' to the name you want to save your new CSV file;
