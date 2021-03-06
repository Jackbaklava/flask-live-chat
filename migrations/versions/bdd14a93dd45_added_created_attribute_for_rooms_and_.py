"""Added created attribute for rooms and renamed message.posted to created

Revision ID: bdd14a93dd45
Revises: 3260c4609c3d
Create Date: 2022-07-25 15:18:07.211082

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bdd14a93dd45'
down_revision = '3260c4609c3d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('message', sa.Column('created', sa.DateTime(timezone=True), nullable=True))
    op.drop_column('message', 'posted')
    op.add_column('room', sa.Column('created', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('room', 'created')
    op.add_column('message', sa.Column('posted', sa.DATETIME(), nullable=True))
    op.drop_column('message', 'created')
    # ### end Alembic commands ###
