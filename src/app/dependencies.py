from rodi import Container

from app.database import Engine, Transaction
from app.repositories import DataRepository
from app.services import DataService

container = Container()


def init_dependencies() -> None:
    container.add_singleton(Engine)
    container.add_scoped(Transaction)
    container.add_transient(DataService)
    container.add_scoped(DataRepository)


def get_data_service() -> DataService:
    return container.resolve(DataService)
