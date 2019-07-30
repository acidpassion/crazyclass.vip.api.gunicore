"""initial database migration

Revision ID: 061a967d0310
Revises: 72f572a0aa8c
Create Date: 2019-07-28 19:27:56.118222

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '061a967d0310'
down_revision = '72f572a0aa8c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blacklist_tokens',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=500), nullable=False),
    sa.Column('blacklisted_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('registered_on', sa.DateTime(), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=True),
    sa.Column('avatarUrl', sa.String(length=255), nullable=True),
    sa.Column('city', sa.String(length=50), nullable=True),
    sa.Column('country', sa.String(length=50), nullable=True),
    sa.Column('gender', sa.Integer(), nullable=True),
    sa.Column('language', sa.String(length=50), nullable=True),
    sa.Column('nickName', sa.String(length=50), nullable=True),
    sa.Column('province', sa.String(length=50), nullable=True),
    sa.Column('child_school_id', sa.Integer(), nullable=True),
    sa.Column('child_name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('avatarUrl'),
    sa.UniqueConstraint('public_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('blacklist_tokens')
    # ### end Alembic commands ###
