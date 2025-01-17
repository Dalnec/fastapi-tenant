"""init

Revision ID: 43275e112071
Revises: 
Create Date: 2024-06-18 10:51:47.610186

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '43275e112071'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    public_users = """
    CREATE TABLE IF NOT EXISTS public.public_users (
       id int GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
       email varchar(256) UNIQUE,
       password varchar(256),
       is_active BOOLEAN NOT NULL,
       is_verified BOOLEAN NOT NULL,
       tenant varchar(64),
       created TIMESTAMPTZ NOT NULL DEFAULT NOW(),
       updated TIMESTAMPTZ
      );
    """
    op.execute(public_users)

    public_companies = """
    CREATE TABLE IF NOT EXISTS public.public_companies (
       id int GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
       name varchar(256),
       short_name varchar(256),
       ruc varchar(16),
       tenant varchar(64) UNIQUE,
       created TIMESTAMPTZ NOT NULL DEFAULT NOW(),
       updated TIMESTAMPTZ
      );
    """
    op.execute(public_companies)


def downgrade() -> None:
    pass
