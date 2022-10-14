"""add foreign-key to posts table

Revision ID: 476661a72eb6
Revises: 18eb32253de9
Create Date: 2022-10-12 16:00:34.118486

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '476661a72eb6'
down_revision = '18eb32253de9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("post_users_fk", source_table="posts", referent_table="users", local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
