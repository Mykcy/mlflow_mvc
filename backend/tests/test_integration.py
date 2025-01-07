import unittest
from flask import Flask, request
from flask_testing import TestCase

class MyTest(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True

        @app.route('/')
        def home():
            return 'Hello, World!'

        @app.route('/upload', methods=['POST'])
        def upload():
            if 'file' not in request.files:
                return 'No file part', 400
            file = request.files['file']
            if file.filename == '':
                return 'No selected file', 400
            return 'File uploaded successfully', 200

        @app.route('/log', methods=['POST'])
        def log():
            with mlflow.start_run():
                mlflow.log_param('param1', request.json['param1'])
                mlflow.log_metric('metric1', request.json['metric1'])
            return 'Logged successfully', 200


        return app

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello, World!')

    def test_file_upload(self):
        data = {'file': (io.BytesIO(b'my file contents'), 'test.txt')}
        response = self.client.post('/upload', data=data, content_type='multipart/form-data')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'File uploaded successfully')
    def test_mlflow_integration(self):
        data = {'param1': 'value1', 'metric1': 0.5}
        response = self.client.post('/log', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Logged successfully')

if __name__ == '__main__':
    unittest.main()





