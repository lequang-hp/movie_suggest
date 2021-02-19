# このファイルはVSCodeで開発するとき、Debug用の目的でFlaskを起動するのEntryファイルです
# 本番にはこのファイルを使われてない
from src.app import app
if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
