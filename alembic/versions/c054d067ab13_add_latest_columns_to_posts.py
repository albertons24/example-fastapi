"""add latest columns to posts

Revision ID: c054d067ab13
Revises: f8b8c0dd6021
Create Date: 2022-11-08 23:24:56.416531

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c054d067ab13'
down_revision = 'f8b8c0dd6021'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column(
        "published", sa.Boolean(), nullable=False, server_default="TRUE"
    ))
    op.add_column("posts", sa.Column(
        "created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()"), nullable=False
    ))
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
