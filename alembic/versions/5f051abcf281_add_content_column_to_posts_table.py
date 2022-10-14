"""add content column to posts table

Revision ID: 5f051abcf281
Revises: c98e407c2fe0
Create Date: 2022-10-12 15:48:27.730474

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f051abcf281'
down_revision = 'c98e407c2fe0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
