from rodi import Container

from app.database import Engine, Transaction
from app.repositories import TicketRepository, UserRepository
from app.services import TicketService, UserService

container = Container()


def init_dependencies() -> None:
    container.add_singleton(Engine)
    container.add_scoped(Transaction)
    container.add_scoped(TicketRepository)
    container.add_scoped(UserRepository)
    container.add_transient(TicketService)
    container.add_transient(UserService)


def get_ticket_service() -> TicketService:
    return container.resolve(TicketService)


def get_user_service() -> UserService:
    return container.resolve(UserService)
