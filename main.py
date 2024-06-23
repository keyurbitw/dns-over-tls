from flask import Flask
from flask import request
import dnsOverTls

app = Flask(__name__)

@app.route('/DoT', methods=['GET', 'POST'])
def runDnsOverTlsBackend():
    domain = request.args.get('domain')
    
    if domain:
        response = dnsOverTls.queryDnsOverTls(domain)
    
    else:
        response = '''Please provide the required arguments.\nUsage: curl -XGET "<service-ip>:<service-port>/DoT?domain=<domain-name>"'''
        
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)