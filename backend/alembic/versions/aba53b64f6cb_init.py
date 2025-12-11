"""init
Revision ID: aba53b64f6cb
Revises: None
Create Date: 2025-12-10 17:53:04.899362
"""
from alembic import op
import sqlalchemy as sa

revision = 'aba53b64f6cb'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Create trends table first (no dependencies)
    op.create_table(
        'trends',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('source', sa.String(255), nullable=True),
        sa.Column('title', sa.String(500), nullable=False),
        sa.Column('url', sa.String(1000), nullable=True),
        sa.Column('content', sa.Text(), nullable=True),
        sa.Column('collected_at', sa.DateTime(), nullable=True),
    )
    op.create_index('ix_trends_id', 'trends', ['id'])
    
    # Create topics table
    op.create_table(
        'topics',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False, unique=True),
        sa.Column('type', sa.String(255), nullable=True),
    )
    op.create_index('ix_topics_id', 'topics', ['id'])
    
    # Create users table (no dependencies)
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('email', sa.String(255), nullable=False, unique=True),
        sa.Column('hashed_password', sa.String(255), nullable=False),
        sa.Column('role', sa.String(50), nullable=True),
        sa.Column('is_active', sa.Boolean(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
    )
    op.create_index('ix_users_email', 'users', ['email'])
    op.create_index('ix_users_id', 'users', ['id'])
    
    # Create keywords table (has foreign keys to trends and topics)
    op.create_table(
        'keywords',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('trend_id', sa.Integer(), nullable=True),
        sa.Column('topic_id', sa.Integer(), nullable=True),
        sa.Column('keyword', sa.String(255), nullable=False),
        sa.Column('confidence', sa.Float(), nullable=True),
        sa.ForeignKeyConstraint(['trend_id'], ['trends.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['topic_id'], ['topics.id'], ondelete='SET NULL'),
    )
    op.create_index('ix_keywords_id', 'keywords', ['id'])


def downgrade():
    op.drop_index('ix_keywords_id', 'keywords')
    op.drop_table('keywords')
    op.drop_index('ix_users_id', 'users')
    op.drop_index('ix_users_email', 'users')
    op.drop_table('users')
    op.drop_index('ix_topics_id', 'topics')
    op.drop_table('topics')
    op.drop_index('ix_trends_id', 'trends')
    op.drop_table('trends')
