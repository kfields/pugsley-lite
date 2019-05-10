"""empty message

Revision ID: 1a39e327a561
Revises: b6f61b196b53
Create Date: 2019-05-07 12:37:20.846345

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a39e327a561'
down_revision = 'b6f61b196b53'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('image', sa.Column('file', sa.String(length=100), nullable=True))
    op.add_column('image', sa.Column('uploaded_by', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'image', 'user', ['uploaded_by'], ['id'])
    op.drop_column('image', 'owner_id')
    op.drop_column('image', 'path')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('image', sa.Column('path', sa.VARCHAR(length=255), nullable=True))
    op.add_column('image', sa.Column('owner_id', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'image', type_='foreignkey')
    op.drop_column('image', 'uploaded_by')
    op.drop_column('image', 'file')
    # ### end Alembic commands ###