"""empty message

Revision ID: 20d5f541707c
Revises: e777cad60669
Create Date: 2018-08-03 22:47:23.991078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20d5f541707c'
down_revision = 'e777cad60669'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('praise',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('fuser_id', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['fuser_id'], ['frontuser.id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('post', sa.Column('praise_count', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'praise_count')
    op.drop_table('praise')
    # ### end Alembic commands ###
