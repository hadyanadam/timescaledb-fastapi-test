"""create hypertable

Revision ID: 3f74890dc8b0
Revises: 7e7b52a0d4f5
Create Date: 2021-01-15 15:02:16.807413

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f74890dc8b0'
down_revision = '7e7b52a0d4f5'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("CREATE EXTENSION IF NOT EXISTS timescaledb;")
    op.execute("SELECT create_hypertable('sensor_data', 'time');")
    op.execute("create index on sensor_data (sensor_id, time desc);")


def downgrade():
    pass
