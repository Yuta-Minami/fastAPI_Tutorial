from controllers import *


# FastAPIのルーティング用関数，URLを登録する
app.add_api_route('/', index)

# 管理者用のURLを登録する
app.add_api_route('/admin', admin)