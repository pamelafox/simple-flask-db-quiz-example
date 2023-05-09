"""empty message

Revision ID: 3be2cad8f098
Revises:
Create Date: 2023-05-06 19:55:52.098294

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "3be2cad8f098"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "questions",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("question", sa.String(length=255), nullable=False),
        sa.Column("answer", sa.String(length=255), nullable=False),
        sa.Column("data", sa.ARRAY(sa.String()), nullable=True),
        sa.Column("quiz_id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "quiz_scores",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("player", sa.String(length=255), nullable=False),
        sa.Column("score", sa.Integer(), nullable=False),
        sa.Column("quiz_id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "quizzes",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("quizzes")
    op.drop_table("quiz_scores")
    op.drop_table("questions")
    # ### end Alembic commands ###
