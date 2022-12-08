###########################
###### STREAMING API ######
# Developed by: @Matt0550 #
###########################

import flask
import os
import sys

app = flask.Flask(__name__)
app.config["DEBUG"] = True

HOST = 'localhost'
PORT = 5000

# Import modules
modules = []
for module in os.listdir('modules'):
    if module.endswith('.py') and module.startswith("OFF_"):
        print("Module " + module + " is disabled")
        continue
    if module.endswith('.py') and module != '__init__.py':
        modules.append(module[:-3])

for module in modules:
    try:
        __import__('modules.' + module)
        # Register the blueprint
        app.register_blueprint(getattr(sys.modules['modules.' + module], 'app_' + module))

    except Exception as e:
        print('Error importing module: ' + module)
        print(e)

# Create a URL route in our application for "/"
@app.route('/', methods=['GET'])
def home():
    return "<h1>How to use this API</h1><p>Visit my GitHub page at: <a href='https://github.com/Matt0550/Streaming-API' target='_blank'>@Matt0550</a></p>"

# List of available modules
@app.route('/modules', methods=['GET'])
def modules():
    # List of registered blueprints
    blueprints = []
    for blueprint in app.blueprints.keys():
        # Remove the "app_" prefix
        blueprints.append(blueprint[4:])
    return {"modules": blueprints, "status": "success"}

# Run the application
app.run(host=HOST, port=PORT)