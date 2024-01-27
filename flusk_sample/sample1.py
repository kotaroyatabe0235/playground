from flask import Flask

# Flaskアプリケーションのインスタンスを作成
app = Flask(__name__)

# ルートURLに対するGETリクエストに応答するハンドラを定義
@app.route('/')

def hello_world():
    return 'Hello, World!'

# アプリケーションを実行するための条件

if __name__ == '__main__':
    app.run(debug=True)

