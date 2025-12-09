"""create keywords table

Revision ID: 0001_initial
Revises: 
Create Date: 2025-12-08
"""
from alembic import op
import sqlalchemy as sa

revision = '0001_initial'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'keywords',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), unique=True),
    )


def downgrade():
    op.drop_table('keywords')
