from flask import Flask, render_template_string, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
      <title>ANTMINER S9 | SOLO BITCOIN: Dashboard</title>
      <style>
      body {
        background: #0a0003;
        color: turquoise;
        font-family: 'Courier New', monospace;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        flex-direction: column;
      }
      .box {
        border: 1px solid #4affa1;
        padding: 10px;
        margin: 10px;
        text-align: center;
        width: 200px;
      }
      #hashrate1m {
        color: #FF7256;
      }
      #blockfound {
        color: #fad46b;
      }
      </style>
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
      <script type="text/javascript">
          $(document).ready(function(){
            setInterval(function(){
              $.get('/api/data', function(data){
                $('#workers').text('Workers: ' + data.workers);
                $('#hashrate1m').html('<span style="color: #FF7256;">Hashrate (1m): ' + data.hashrate1m + '</span>');
                $('#shares').text('Shares: ' + data.shares);
                $('#blockfound').text('Block Found: ' + (data.shares > 120000000 ? 'Yes' : 'No'));
              });
            }, 1000);
          });
      </script>
    </head>
    <body>
    <h1>S9 SOLO FARM | Data Dashboard</h1>
    <div id="workers" class="box">Loading...</div>
    <div id="hashrate1m" class="box">Loading...</div>
    <div id="shares" class="box">Loading...</div>
    <div id="blockfound" class="box">Loading...</div>
    </body>
    <iframe src="https://solo.ckpool.org/users/bc1qd33d0lpxkruz8dynv520nw52n53la3c3267444" width="20%" height="300" name="iframe" title="This is my FARM"></iframe>
    </html>
    """)

@app.route('/api/data')
def get_data():
    url = "https://solo.ckpool.org/users/bc1qd33d0lpxkruz8dynv520nw52n53la3c3267444"
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
