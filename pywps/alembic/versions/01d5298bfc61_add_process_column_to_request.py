"""Add process column to Request

Revision ID: 01d5298bfc61
Revises: eead25e2ad3a
Create Date: 2019-12-31 13:00:47.887848

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01d5298bfc61'
down_revision = 'eead25e2ad3a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pywps_stored_requests', sa.Column('process', sa.LargeBinary(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pywps_stored_requests', 'process')
    # ### end Alembic commands ###