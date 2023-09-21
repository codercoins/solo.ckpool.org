# solo.ckpool.org
Upgraded solo.ckpool.org miner site

## SOLO.CKPOOL.ORG | FARM | Data Dashboard

This is a Flask application that provides a custom data dashboard for the solo.ckpool.org website and mining hardware. The dashboard displays real-time data including the number of workers, hashrate (1 minute), shares, and whether a block has been found. 

The app also includes an embedded iframe that displays the user's farm on Solo.CKPool.org. 

![Antminer S9  Solo FARM](images/Screenshot (31).png)

## How to Use

1. Clone this repository and navigate to the root directory.
2. Ensure that Flask and Requests are installed.
3. Replace the "REPLACE_WITH_WALLET" string in `templates/home.html` with your CKPool.org wallet address.
4. Run the app using `python app.py`.
5. Open a web browser and navigate to `http://localhost:5000`.
6. The dashboard should display in the browser. 

## Why it's Better

solo.ckpool.org has a web interface that provides some basic data, but it can be difficult to navigate and lacks customization. This Flask app provides a more visually appealing and user-friendly interface that is focused solely on the data that miners are most interested in. Additionally, the embedded iframe allows miners to easily monitor their farm on CKPool.org without having to switch between different tabs or windows.
