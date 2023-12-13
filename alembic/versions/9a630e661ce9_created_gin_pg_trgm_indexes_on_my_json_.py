"""created GIN + pg_trgm indexes on my json field

Revision ID: 9a630e661ce9
Revises: 79d9bb2fecda
Create Date: 2023-12-13 13:36:40.311064

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9a630e661ce9'
down_revision: Union[str, None] = '79d9bb2fecda'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('CREATE EXTENSION IF NOT EXISTS pg_trgm;')
    op.execute("CREATE INDEX idx_json_data_json_field_gin_trgm ON json_data USING gin (json_field jsonb_path_ops);")


def downgrade() -> None:
    op.execute('DROP INDEX idx_json_field_gin;')
    op.execute('DROP INDEX idx_json_field_trgm;')

