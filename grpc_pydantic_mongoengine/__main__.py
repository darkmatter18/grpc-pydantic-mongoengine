import asyncio
import logging
import logging.config

import grpc
from mongoengine import connect, disconnect

from grpc_pydantic_mongoengine.proto.blog import blog_pb2_grpc
from grpc_pydantic_mongoengine.services.blog import BlogServicer
from grpc_pydantic_mongoengine.settings.log import DEFAULT_LOGGING

logging.config.dictConfig(DEFAULT_LOGGING)

logger = logging.getLogger(__name__)


def add_services(server: grpc.aio.Server):
    blog_pb2_grpc.add_BlogServicer_to_server(BlogServicer(), server)


async def serve():
    server = grpc.aio.server()
    add_services(server)
    server.add_insecure_port('[::]:50051')
    logger.debug('Start Listening on: [::]:50051')

    await server.start()
    await server.wait_for_termination()


async def start():
    logger.info('Startup')
    host = "mongodb://identity:pzD358aGgq8WnBmonGtf@172.174.4.229:27017/identity?authSource=admin"  # TODO
    connect(host=host, uuidRepresentation='standard')
    await serve()
    logger.info('Shutdown')
    disconnect()


if __name__ == "__main__":
    asyncio.run(start())
