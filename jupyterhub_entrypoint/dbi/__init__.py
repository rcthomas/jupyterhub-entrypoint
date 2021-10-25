
from sqlalchemy.ext.asyncio import create_async_engine

from .model import metadata

from .entrypoints import (
    create_entrypoint,
    retrieve_one_entrypoint,
    retrieve_many_entrypoints,
    update_entrypoint,
    tag_entrypoint,
    untag_entrypoint,
    delete_entrypoint
)

from .selections import (
    update_selection,
    retrieve_selection,
    delete_selection
)

from .contexts import (
    create_context,
    retrieve_contexts,
    delete_context
)

def async_engine(*args, **kwargs):
    return create_async_engine(*args, **kwargs)

async def init_db(conn, drop_all=False):
    if drop_all:
        await conn.run_sync(metadata.drop_all)
    await conn.run_sync(metadata.create_all)