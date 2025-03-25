# AmiyaHttp

![PyPI](https://img.shields.io/pypi/v/amiyahttp)

对 [FastAPI](https://fastapi.tiangolo.com/) 进行二次封装的简易 HTTP Web 服务 SDK

文档地址：[点击查看](https://www.amiyabot.com/develop/advanced/httpSupport.html)

```python
import asyncio
from pydantic import BaseModel
from amiyahttp import HttpServer


# 定义 POST 请求参数
class UserModel(BaseModel):
    username: str
    nickname: str


server = HttpServer(host='0.0.0.0', port=8088)


@server.controller
class Bot:
    @server.route(method='get')
    async def get_name(self):
        return 'AmiyaBot'

    @server.route(method='post')
    async def say_hello(self, params: UserModel):
        return server.response(message=f'hello, {params.nickname}')


asyncio.run(server.serve())
```
