"""pokemon data

Revision ID: 6cfffaf7f900
Revises: 
Create Date: 2024-03-06 16:37:55.896653

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6cfffaf7f900'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "Pokemon",
    sa.Column("id", sa.Integer),
    sa.Column("image", sa.String),
    sa.Column("name", sa.String),
    sa.Column("type", sa.String),
    sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("Pokemon")
