"""
This file will be run as the app for a flask server, it's responsible
for recieving/parsing POST'd firewall rules from hosts and writing 
them to files
disclaimer: this doesn't work yet
@author: degenerat3
"""
from flask import Flask, request
app = Flask(__name__)

@app.route('/api/rule_send', methods=['GET','POST'])
def get_rules():
	content = request.json
	print content
	return "we got some rules"

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
