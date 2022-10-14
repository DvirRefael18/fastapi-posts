"""auto-add-phone_number_column_to_user

Revision ID: e0cd1540abeb
Revises: fc1ca16e36f7
Create Date: 2022-10-13 10:15:54.610367

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0cd1540abeb'
down_revision = 'fc1ca16e36f7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###
