"""empty message

Revision ID: e777cad60669
Revises: d48fb384c9a9
Create Date: 2018-08-02 20:01:48.865613

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e777cad60669'
down_revision = 'd48fb384c9a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('highlight_post', sa.Column('create_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('highlight_post', 'create_time')
    # ### end Alembic commands ###