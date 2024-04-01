python -m grpc_tools.protoc -I . --python_out=. --pyi_out=. --grpc_python_out=. ./grpc_pydantic_mongoengine/**/*.proto

python -m grpc_pydantic_mongoengine