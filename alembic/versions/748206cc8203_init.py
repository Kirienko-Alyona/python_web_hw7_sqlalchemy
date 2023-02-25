"""Init

Revision ID: 748206cc8203
Revises: d8dea8de6cc6
Create Date: 2023-02-25 21:16:49.388324

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '748206cc8203'
down_revision = 'd8dea8de6cc6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('grades')
    op.drop_table('disciplines')
    op.drop_table('teachers')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teachers',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('teachers_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('fullname', sa.VARCHAR(length=250), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='teachers_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('disciplines',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('disciplines_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('teacher_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], name='disciplines_teacher_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='disciplines_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('grades',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('discipline_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('student_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('date_of', sa.DATE(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['discipline_id'], ['disciplines.id'], name='grades_discipline_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], name='grades_student_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='grades_pkey')
    )
    # ### end Alembic commands ###
