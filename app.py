from flask import Flask, send_file, make_response
import io
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Разрешаем запросы с других доменов

@app.route('/download', methods=['GET'])
def download_file():
    # Создание текстового файла с содержанием "Hello World!"
    text = "Hello World!"
    
    # Создаем файл в памяти
    file = io.StringIO(text)
    file.seek(0)  # Возвращаем указатель в начало файла
    
    # Отправляем файл в ответе
    response = make_response(file.read())
    response.headers['Content-Disposition'] = 'attachment; filename=hello.txt'
    response.mimetype = 'text/plain'
    return response

if __name__ == '__main__':
    app.run(debug=True)
