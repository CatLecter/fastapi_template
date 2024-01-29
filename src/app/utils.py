from app.models.base import Base


def to_dict(model: Base, exclude: set[str] | None = None) -> dict:
    delattr(model, '_sa_instance_state')
    if exclude:
        for field in exclude:
            delattr(model, field)
    return model.__dict__
