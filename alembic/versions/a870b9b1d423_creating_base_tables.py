"""creating base tables

Revision ID: a870b9b1d423
Revises: 
Create Date: 2022-06-10 17:25:40.674795

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a870b9b1d423'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String()),
        sa.Column('hashed_password', sa.String(), nullable=False),
        sa.Column('is_active', sa.Boolean())
    )

    op.create_table(
        'items',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String()),
        sa.Column('description', sa.String()),
        sa.Column('owner_id', sa.Integer,sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    )



def downgrade() -> None:
    op.drop_table('users')
    op.drop_table('items')
