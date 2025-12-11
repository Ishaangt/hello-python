from flask import Flask, request, jsonify, Response
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString
import os
import argparse

app = Flask(__name__)

BASE_URL_PREFIX = '/api/v1'


@app.route(BASE_URL_PREFIX + '/hello/json', methods=['POST'])
def hello_json():
    data = request.get_json(force=True, silent=True)
    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON payload"}), 400
    message = data.get('message')
    name = data.get('name')
    return jsonify({"message": message, "name": name})


@app.route(BASE_URL_PREFIX + '/hello/xml', methods=['POST'])
def hello_xml():
    data = request.get_json(force=True, silent=True)
    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON payload"}), 400
    message = data.get('message')
    name = data.get('name')
    root = ET.Element('xmlroot')
    m = ET.SubElement(root, 'message')
    m.text = '' if message is None else str(message)
    n = ET.SubElement(root, 'name')
    n.text = '' if name is None else str(name)

    # Pretty-print XML
    raw = ET.tostring(root, encoding='utf-8')
    pretty = parseString(raw).toprettyxml(indent='    ')

    # Ensure XML declaration includes encoding
    # parseString.toprettyxml returns a declaration without encoding when not asked,
    # so add an explicit declaration with UTF-8 which matches the example.
    declaration = "<?xml version='1.0' encoding='UTF-8'?>\n"
    xml_text = declaration + '\n'.join(pretty.splitlines()[1:])

    return Response(xml_text, mimetype='application/xml')


def _get_port_from_env_or_args() -> int:
    """Return port from CLI -p/--port if provided, otherwise from PORT env var, else 8081."""
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-p', '--port', type=int, help='Port to run the server on')
    args, _ = parser.parse_known_args()
    if args.port:
        return int(args.port)
    env_port = os.getenv('PORT')
    if env_port:
        try:
            return int(env_port)
        except ValueError:
            pass
    return 8081


if __name__ == '__main__':
    port = _get_port_from_env_or_args()
    app.run(host='0.0.0.0', port=port, debug=True)
