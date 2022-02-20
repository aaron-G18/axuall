# **Axuall Wiki-searcher**

## **Instructions for axuall.py Program**

### Requirements:  

- Python3  
- Selenium  
- Chrome WebDriver  
- Flask  

Above are the requirements to run axuall.py. Below are instructions for installing these requirements. 

<br>

### Installing Python3:  
RealPython has an in-depth tutorial on how to install Python3, depending on what operating system you are on. Please visit https://realpython.com/installing-python/ for installation instructions.

<br>

### Installing Selenium:  
Use pip to install the selenium package. Python 3 has pip available in the standard library. Using pip (in command line), you can install selenium like this:  
```
pip3 install selenium
```

*You may consider using virtualenv to create isolated Python environments. Python 3 has venv which is almost the same as virtualenv.
(above instructions are from: https://selenium-python.readthedocs.io/installation.html. Please visit their site for any issues with installing Selenium)*

<br>

### Installing Chrome WebDriver:  
Make sure that the most recent version of Chrome is installed on your machine (To check/update Chrome, go to the menu and select Help > About Google Chrome. Or, download and install it here.) Then, download the matching version of ChromeDriver here and add it to your system path. Assuming that the path ~/.local/bin is in your execution PATH, this is where you would need to move the driver file.

<br>

### Editting local host file
You will need to add a few entries to your host file so that the wiki-searcher GET requests can be resolved to your localhost ip address. If you are on macOS, there is a great walkthrough of editing your host file [here](https://help.nexcess.net/how-to-find-the-hosts-file-on-my-mac#:~:text=The%20Hosts%20file%20on%20a,the%20%2Fetc%2Fhosts%20folder.).
You will need to add the following entries to your host file:
```
127.0.0.1       wiki-search.com
127.0.0.1       dogs.wiki-search.com
127.0.0.1       ordinary.wiki-search.com
127.0.0.1       python.wiki-search.com
127.0.0.1       selenium.wiki-search.com
127.0.0.1       flask.wiki-search.com
```

<br>

## Running the Program:  
To run the axuall.py program, first place the file in the directory of your choice where you would like to store it. Open your terminal and navigate to the directory you placed axuall.py in.
Next, run the following command in your command line:
```
python3 axuall.py
```
You should get a message "Running on http://wiki-search.com:5000/ (Press CTRL+C to quit)" in your terminal. 
Once the server is running, open a web browser and enter "wiki-search.com:5000" in the address bar. This will take you to the main page of the wiki-searcher. Add a subdomain to the URL and hit enter to get a list with href link(s) resulting from a Wikipedia search using the entered subdomain as the search word. 
For example "python.wiki-search.com:5000" entered in the address bar will return all links that wikipedia returns when searching for "python." 
You can search for any of the subdomains added to your host file (e.g. "dogs", "ordinary", "python", "selenium", "flask")