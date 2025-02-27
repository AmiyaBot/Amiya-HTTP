import inspect
import asyncio
import uvicorn

from typing import List, Callable, Optional

default_logging_options = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'access': {
            '()': 'uvicorn.logging.AccessFormatter',
            'fmt': '%(client_addr)s - %(request_line)s %(status_code)s',
        },
        'default': {
            '()': 'uvicorn.logging.DefaultFormatter',
            'fmt': '%(asctime)s ｜ %(levelname)s ｜ %(message)s',
        },
    },
    'handlers': {
        'access': {
            'class': 'logging.StreamHandler',
            'formatter': 'access',
        },
        'default': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
    },
    'loggers': {
        'uvicorn': {'handlers': ['default'], 'level': 'INFO'},
        'uvicorn.error': {'level': 'INFO'},
        'uvicorn.access': {'handlers': ['access'], 'level': 'INFO', 'propagate': False},
    },
}


class ServerEventHandler:
    on_shutdown: List[Callable] = []


class ServerABCClass:
    def __init__(self):
        self.server: Optional[uvicorn.Server] = None

    async def serve(self):
        if self.server:
            await self.server.serve()


class ServerMeta(type):
    instances: List[ServerABCClass] = []
    shutdown_lock = False

    def __call__(cls, *args, **kwargs):
        inst = super().__call__(*args, **kwargs)

        cls.instances.append(inst)

        return inst

    def shutdown_all(cls, instance: ServerABCClass):
        if not cls.shutdown_lock:
            cls.shutdown_lock = True

            for inst in cls.instances:
                if inst != instance:
                    inst.server.should_exit = True

            for action in ServerEventHandler.on_shutdown:
                if inspect.iscoroutinefunction(action):
                    asyncio.create_task(action())
                else:
                    action()
