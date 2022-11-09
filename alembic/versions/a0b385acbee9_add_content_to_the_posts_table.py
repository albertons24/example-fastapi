"""add content to the posts table

Revision ID: a0b385acbee9
Revises: b83f66f59967
Create Date: 2022-11-08 22:52:01.507532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0b385acbee9'
down_revision = 'b83f66f59967'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
