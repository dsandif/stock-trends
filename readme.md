# 📈 Stock Price Trend Analysis

A quick python script to analyze price trends

Steps to run the script on MacOS:

1. Type “cmd + shift” to open spotlight and search for “Terminal”
2. Run the following commands

```bash
brew install pyenv
pyenv install 3.11.0
pyenv global 3.11.0
```

3. Next install the required dependencies: requests for api calls, pandas and matplotlib for the chart

```bash
pip install requests
pip install pandas
pip install matplotlib
```

4. Navigate to the stock chart directory and run the stocks.py script

```bash
cd stock\ chart/
python stocks.py
```

5. If you see the error “Invalid API KEY” you need to follow the link  shown in the terminal to sign up and add your api key to the variable yourAPIKEY on line 8 in stocks.py

When the script completes, it creates a chart named trendy.png in the project that looks similar to the one below. The y-axis will display stock prices as a percentage difference over time.  Play with the ticker symbols on line 6 and repeat step 4 to try out new symbols. You may also play with the date range on line 11. Enjoy!

<img src="https://user-images.githubusercontent.com/3058101/211236779-596a9571-ebf8-4486-8818-d459b9ad0b7e.png" style="height: 300px; width;500px"></img>


