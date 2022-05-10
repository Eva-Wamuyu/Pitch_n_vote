"""update db

Revision ID: 7b5bbb61e799
Revises: 
Create Date: 2022-05-08 21:57:44.772120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b5bbb61e799'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('all_users',
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('pass_pass', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('comments',
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('comment_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('_id')
    )
    op.create_table('posts',
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=80), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('the_date', sa.DateTime(), nullable=False),
    sa.Column('votes', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['all_users._id'], ),
    sa.PrimaryKeyConstraint('_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    op.drop_table('comments')
    op.drop_table('all_users')
    # ### end Alembic commands ###