from fastapi import FastAPI
from starlette.requests import Request
from starlette.templating import Jinja2Templates


app = FastAPI(
    title='FastAPIでつくるtoDoアプリケーション',
    description='FastAPIチュートリアル：FastAPI(とstarlette)でシンプルなtoDoアプリを作りましょう．',
    version='0.9 beta'
)

# new テンプレート関連の設定 (jinja2)
templates = Jinja2Templates(directory="templates")

# Jinja2.Environment : filterやglobalの設定用
jinja_env = templates.env  


def index(request: Request):

    # templates/index.htmlを返す
    return templates.TemplateResponse('index.html',
                                      {'request': request})

def admin(request: Request):
    return templates.TemplateResponse('admin.html',
                                      {'request': request,
                                       'username': 'admin'})