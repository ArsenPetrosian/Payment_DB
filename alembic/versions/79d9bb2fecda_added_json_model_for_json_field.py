"""added Json Model for json_field

Revision ID: 79d9bb2fecda
Revises: 
Create Date: 2023-12-13 10:19:59.112036

"""
from typing import Sequence, Union
from sqlalchemy.dialects.postgresql import JSONB
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '79d9bb2fecda'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'json_data',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('json_field', JSONB)
    )


def downgrade() -> None:
    op.drop_table('json_data')
