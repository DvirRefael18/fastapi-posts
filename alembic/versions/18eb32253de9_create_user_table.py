"""create user table

Revision ID: 18eb32253de9
Revises: 5f051abcf281
Create Date: 2022-10-12 15:53:09.953439

"""
from time import time
from typing import Collection
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18eb32253de9'
down_revision = '5f051abcf281'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users", 
                    sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("email", sa.String(), nullable=False),
                    sa.Column("password", sa.String(), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()"), nullable=False),
                    sa.PrimaryKeyConstraint("id"),                             
                    sa.UniqueConstraint("email")
                    )
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
