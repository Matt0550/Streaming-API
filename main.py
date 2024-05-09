###########################
###### STREAMING API ######
# Developed by: @Matt0550 #
###########################

import flask
import os
import sys

app = flask.Flask(__name__)
app.config["DEBUG"] = True

HOST = os.getenv('HOST', '0.0.0.0')
PORT = os.getenv('PORT', 5000)

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
    modulesString = ""
    for module in modules:
        modulesString += "<p>GET /" + module + "</p>"

    return """<h1>How to use this API</h1><p>Visit my GitHub page at: <a href='https://github.com/Matt0550/Streaming-API' target='_blank'>@Matt0550</a></p>
    <h2>Available modules</h2>
    """ + modulesString + """
    """

# List of available modules
@app.route('/modules', methods=['GET'])
def modulesGet():
    # List of registered blueprints
    blueprints = []
    for blueprint in app.blueprints.keys():
        # Remove the "app_" prefix
        blueprints.append(blueprint[4:])
    return {"modules": blueprints, "status": "success"}

# Run the application
app.run(host=HOST, port=PORT)