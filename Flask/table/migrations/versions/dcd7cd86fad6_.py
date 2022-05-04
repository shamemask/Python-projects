"""empty message

Revision ID: dcd7cd86fad6
Revises: ccfea89a0dc8
Create Date: 2022-05-03 12:43:08.281856

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dcd7cd86fad6'
down_revision = 'ccfea89a0dc8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tickers', sa.Column('dateCreated', sa.DATETIME(timezone=6), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tickers', 'dateCreated')
    # ### end Alembic commands ###