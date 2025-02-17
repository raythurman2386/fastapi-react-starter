"""Auto migration

Revision ID: e33bb845793c
Revises: fc150bd13ee2
Create Date: 2025-02-16 20:06:09.782389

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e33bb845793c"
down_revision: Union[str, None] = "fc150bd13ee2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("username", sa.String(), nullable=False))
    op.add_column("users", sa.Column("hashed_password", sa.String(), nullable=False))
    op.add_column("users", sa.Column("role", sa.String(), nullable=True))
    op.add_column("users", sa.Column("is_superuser", sa.Boolean(), nullable=True))
    op.add_column("users", sa.Column("is_active", sa.Boolean(), nullable=True))
    op.add_column("users", sa.Column("email_verified", sa.Boolean(), nullable=True))
    op.add_column("users", sa.Column("created_at", sa.DateTime(), nullable=True))
    op.add_column("users", sa.Column("updated_at", sa.DateTime(), nullable=True))
    op.add_column("users", sa.Column("reset_token", sa.String(), nullable=True))
    op.alter_column("users", "email", existing_type=sa.VARCHAR(), nullable=False)
    op.drop_index("ix_users_email", table_name="users")
    op.drop_index("ix_users_name", table_name="users")
    op.create_unique_constraint(None, "users", ["reset_token"])
    op.create_unique_constraint(None, "users", ["email"])
    op.create_unique_constraint(None, "users", ["username"])
    op.drop_column("users", "name")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("name", sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, "users", type_="unique")
    op.drop_constraint(None, "users", type_="unique")
    op.drop_constraint(None, "users", type_="unique")
    op.create_index("ix_users_name", "users", ["name"], unique=False)
    op.create_index("ix_users_email", "users", ["email"], unique=True)
    op.alter_column("users", "email", existing_type=sa.VARCHAR(), nullable=True)
    op.drop_column("users", "reset_token")
    op.drop_column("users", "updated_at")
    op.drop_column("users", "created_at")
    op.drop_column("users", "email_verified")
    op.drop_column("users", "is_active")
    op.drop_column("users", "is_superuser")
    op.drop_column("users", "role")
    op.drop_column("users", "hashed_password")
    op.drop_column("users", "username")
    # ### end Alembic commands ###
