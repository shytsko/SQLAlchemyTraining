"""empty message

Revision ID: 3aa3a01665db
Revises: bb92b38cf263
Create Date: 2024-08-14 22:15:42.442393

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "3aa3a01665db"
down_revision: Union[str, None] = "bb92b38cf263"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        "workplace_department_id_fkey", "workplace", type_="foreignkey"
    )
    op.create_foreign_key(
        None,
        "workplace",
        "department",
        ["department_id"],
        ["id"],
        ondelete="CASCADE",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "workplace", type_="foreignkey")
    op.create_foreign_key(
        "workplace_department_id_fkey",
        "workplace",
        "department",
        ["department_id"],
        ["id"],
    )
    # ### end Alembic commands ###
