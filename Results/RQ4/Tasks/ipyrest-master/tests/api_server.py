#!/usr/bin/env python

"""
A simple HTTP server implementing a minimal RESTful API for testing ipyrest.
"""

import json
import time

from flask import Flask, Response, request, jsonify, send_file

from ipyrest.utils import find_free_port, run_flask_app


app = Flask(__name__)


# In the app routes below, without any methods parameter the default one is 'GET'.

# GET

@app.route('/')
def home():
    resp = Response('')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/head', methods=['HEAD'])
def head():
    resp = app.make_response('')
    resp.mimetype = "text/plain"
    return resp


@app.route('/get_json')
def get_json():
    obj = {'foo': 23, 'bar': 'b a r'.split()}
    return jsonify(obj)


@app.route('/get_json_param/<int:param>')
def get_json_param(param: int):
    obj = {'foo': 'bar', 'param': param}
    return jsonify(obj)


@app.route('/get_json_query/')
def get_json_query():
    args = request.args
    return jsonify(args)


@app.route('/post_json_data/', methods=['POST'])
def post_json_data():
    data = request.data
    print(data)
    return jsonify(data)


@app.route('/get_json_3d/')
def get_json_3d():
    import numpy as np
    x, y, z = np.random.random((3, 100))
    data = dict(x=x.tolist(), y=y.tolist(), z=z.tolist())
    return jsonify(data)


@app.route('/get_image')
def get_image():
    filename = 'resources/jupyter.jpg'
    return send_file(filename, mimetype='image/jpeg')


@app.route("/get_header")
def get_header():
    resp = Response("Foo bar baz")
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route("/get_header_echo")
def get_header_echo():
    return jsonify(dict((k, v) for (k, v) in request.headers.items()))


@app.route('/get_mimetype')
def get_mimetype():
    xml = '<xml>foo</xml>'
    resp = app.make_response(xml)
    resp.mimetype = "text/xml"
    return resp


@app.route('/get_slow/sleep/<float:period>')
def get_slow(period):
    time.sleep(period)
    return f'Sorry for being {period} seconds late!'


@app.route('/get_protobuf')
def get_protobuf():
    person_ser = b'\n\x08John Doe\x10\xd2\t\x1a\x10jdoe@example.com"\x0c\n\x08555-4321\x10\x01'
    resp = app.make_response(person_ser)
    resp.mimetype = "application/x-protobuf"
    return resp


@app.route('/get_protobuf/person/<int:id>')
def get_protobuf_person(id):
    import addressbook_pb2

    with open('resources/addressbook_pb', "rb") as f:
        address_book = addressbook_pb2.AddressBook()
        address_book.ParseFromString(f.read())

    person = None
    for per in address_book.people:
        if per.id == id:
            break

    person_ser = person.SerializePartialToString() if person else b''

    resp = app.make_response(person_ser)
    resp.mimetype = "application/x-protobuf"
    return resp


@app.route('/get_svg')
def get_svg():
    resp = app.make_response(open('resources/Cuba.svg').read())
    resp.mimetype = "image/svg+xml"
    return resp


@app.route('/get_gpx')
def get_gpx():
    gpx_body = open('resources/sample.gpx').read()
    resp = app.make_response(gpx_body)
    resp.mimetype = "application/gpx+xml"
    return resp


# POST

@app.route("/post_data_echo", methods=['POST'])
def post_data_echo():
    return jsonify(json.loads(request.data.decode('utf-8')))


# Multi-method

@app.route('/echo/<path:subpath>', methods=['HEAD', 'GET', 'POST'])
def echo(subpathstr):
    "Echo everything we can inside as a JSON result."
    return jsonify(dict(
        method=request.method,
        headers=request.headers,
        args=request.args,
        params=request.params,
        data=request.data,
    ))


if __name__ == "__main__":
    port = find_free_port()
    kwargs = dict(host='0.0.0.0', port=port, debug=False)
    run_flask_app(app, kwargs, daemon=False)
