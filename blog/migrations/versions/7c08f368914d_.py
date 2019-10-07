"""empty message

Revision ID: 7c08f368914d
Revises: 
Create Date: 2019-05-07 17:41:02.794847

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c08f368914d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blogtype',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type_name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cate_name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('ID', sa.Integer(), nullable=False),
    sa.Column('loginname', sa.String(length=50), nullable=False),
    sa.Column('uname', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=200), nullable=False),
    sa.Column('url', sa.String(length=200), nullable=True),
    sa.Column('upwd', sa.String(length=30), nullable=False),
    sa.Column('is_author', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('ID')
    )
    op.create_table('topic',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=False),
    sa.Column('pub_date', sa.DateTime(), nullable=False),
    sa.Column('read_num', sa.Integer(), nullable=True),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('images', sa.Text(), nullable=True),
    sa.Column('blogtype_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['blogtype_id'], ['blogtype.id'], ),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.ID'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reply',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('reply_time', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('topic_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['topic_id'], ['topic.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.ID'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('voke',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('topic_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['topic_id'], ['topic.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.ID'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('voke')
    op.drop_table('reply')
    op.drop_table('topic')
    op.drop_table('user')
    op.drop_table('category')
    op.drop_table('blogtype')
    # ### end Alembic commands ###
