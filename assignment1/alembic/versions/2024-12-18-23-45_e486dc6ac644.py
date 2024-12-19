"""Create Sensor data table

Revision ID: e486dc6ac644
Revises: 
Create Date: 2024-12-18 23:45:05.385837

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e486dc6ac644'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    """Create the sensor_data table."""
    op.create_table(
        "sensor_data",
        sa.Column("id", sa.String, primary_key=True, nullable=False),
        sa.Column("message_id", sa.String, nullable=False),
        sa.Column("publish_time", sa.DateTime(timezone=True), nullable=False, index=True),
        sa.Column("v0", sa.String, nullable=False),
        sa.Column("v11", sa.String, nullable=False),
        sa.Column("v18", sa.String, nullable=False),
        sa.Column("time", sa.DateTime, nullable=False),
        sa.Column('created_on', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_on', sa.DateTime(timezone=True), nullable=True),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    """Drop the sensor_data table."""
    op.drop_table("sensor_data")
    # ### end Alembic commands ###