# AmiyaHttp

![PyPI](https://img.shields.io/pypi/v/amiyahttp)

对 [FastAPI](https://fastapi.tiangolo.com/) 进行二次封装的简易 HTTP Web 服务 SDK

```python
import asyncio
from amiyahttp import HttpServer

server = HttpServer(host='0.0.0.0', port=8088)


@server.controller
class Bot:
    @server.route(method='get')
    async def get_name(self):
        return 'AmiyaBot'

    @server.route(method='post')
    async def say_hello(self):
        return server.response(message='hello')


asyncio.run(server.serve())
```
