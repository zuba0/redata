"""Initial migration

Revision ID: fbf81437ae12
Revises: 
Create Date: 2021-01-15 16:23:22.555384

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'fbf81437ae12'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('metrics_data_delay',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('table_id', sa.Integer(), nullable=True),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_metrics_data_delay_created_at'), 'metrics_data_delay', ['created_at'], unique=False)
    op.create_index(op.f('ix_metrics_data_delay_table_id'), 'metrics_data_delay', ['table_id'], unique=False)
    op.create_table('metrics_data_values',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('table_id', sa.Integer(), nullable=True),
    sa.Column('column_name', sa.String(), nullable=True),
    sa.Column('column_value', sa.String(), nullable=True),
    sa.Column('check_name', sa.String(), nullable=True),
    sa.Column('check_value', sa.Float(), nullable=True),
    sa.Column('time_interval', sa.String(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_metrics_data_values_created_at'), 'metrics_data_values', ['created_at'], unique=False)
    op.create_index(op.f('ix_metrics_data_values_table_id'), 'metrics_data_values', ['table_id'], unique=False)
    op.create_table('metrics_data_volume',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('table_id', sa.Integer(), nullable=True),
    sa.Column('time_interval', sa.String(), nullable=True),
    sa.Column('count', sa.BigInteger(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_metrics_data_volume_created_at'), 'metrics_data_volume', ['created_at'], unique=False)
    op.create_index(op.f('ix_metrics_data_volume_table_id'), 'metrics_data_volume', ['table_id'], unique=False)
    op.create_table('metrics_data_volume_diff',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('table_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('count', sa.BigInteger(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_metrics_data_volume_diff_created_at'), 'metrics_data_volume_diff', ['created_at'], unique=False)
    op.create_index(op.f('ix_metrics_data_volume_diff_table_id'), 'metrics_data_volume_diff', ['table_id'], unique=False)
    op.create_table('metrics_table_schema_changes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('table_id', sa.Integer(), nullable=True),
    sa.Column('column_name', sa.String(), nullable=True),
    sa.Column('column_type', sa.String(), nullable=True),
    sa.Column('column_count', sa.Integer(), nullable=True),
    sa.Column('operation', sa.String(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_metrics_table_schema_changes_created_at'), 'metrics_table_schema_changes', ['created_at'], unique=False)
    op.create_index(op.f('ix_metrics_table_schema_changes_table_id'), 'metrics_table_schema_changes', ['table_id'], unique=False)
    op.create_table('monitored_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('source_db', sa.String(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('table_name', sa.String(), nullable=True),
    sa.Column('time_column', sa.String(), nullable=True),
    sa.Column('time_column_type', sa.String(), nullable=True),
    sa.Column('schema', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('monitored_table')
    op.drop_index(op.f('ix_metrics_table_schema_changes_table_id'), table_name='metrics_table_schema_changes')
    op.drop_index(op.f('ix_metrics_table_schema_changes_created_at'), table_name='metrics_table_schema_changes')
    op.drop_table('metrics_table_schema_changes')
    op.drop_index(op.f('ix_metrics_data_volume_diff_table_id'), table_name='metrics_data_volume_diff')
    op.drop_index(op.f('ix_metrics_data_volume_diff_created_at'), table_name='metrics_data_volume_diff')
    op.drop_table('metrics_data_volume_diff')
    op.drop_index(op.f('ix_metrics_data_volume_table_id'), table_name='metrics_data_volume')
    op.drop_index(op.f('ix_metrics_data_volume_created_at'), table_name='metrics_data_volume')
    op.drop_table('metrics_data_volume')
    op.drop_index(op.f('ix_metrics_data_values_table_id'), table_name='metrics_data_values')
    op.drop_index(op.f('ix_metrics_data_values_created_at'), table_name='metrics_data_values')
    op.drop_table('metrics_data_values')
    op.drop_index(op.f('ix_metrics_data_delay_table_id'), table_name='metrics_data_delay')
    op.drop_index(op.f('ix_metrics_data_delay_created_at'), table_name='metrics_data_delay')
    op.drop_table('metrics_data_delay')
    # ### end Alembic commands ###
