"""Initial migration

Revision ID: 3260c4609c3d
Revises: 
Create Date: 2022-07-15 22:36:12.323471

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "3260c4609c3d"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(length=16), nullable=True),
        sa.Column("password_hash", sa.String(length=256), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "room",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=64), nullable=False),
        sa.Column("description", sa.Text(length=4096), nullable=True),
        sa.Column("host_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["host_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "message",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("body", sa.Text(length=1024), nullable=False),
        sa.Column("posted", sa.DateTime(timezone=True), nullable=True),
        sa.Column("author_id", sa.Integer(), nullable=True),
        sa.Column("room_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["author_id"],
            ["user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["room_id"],
            ["room.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "room_participants",
        sa.Column("room_id", sa.Integer(), nullable=True),
        sa.Column("participant_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["participant_id"],
            ["user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["room_id"],
            ["room.id"],
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("room_participants")
    op.drop_table("message")
    op.drop_table("room")
    op.drop_table("user")
    # ### end Alembic commands ###
