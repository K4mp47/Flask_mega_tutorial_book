"""followers

Revision ID: 801526f5119c
Revises: 5a895625faef
Create Date: 2023-07-07 17:44:31.167435

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '801526f5119c'
down_revision = '5a895625faef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
