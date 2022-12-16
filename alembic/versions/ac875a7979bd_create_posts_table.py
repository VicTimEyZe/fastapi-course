"""create posts table

Revision ID: ac875a7979bd
Revises: 
Create Date: 2022-12-16 10:49:44.259973

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac875a7979bd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), primary_key=True))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
