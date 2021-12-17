# Generated by Django 4.0 on 2021-12-17 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('number_of_students', models.IntegerField()),
                ('number_of_lessions_per_week', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('courses', models.ManyToManyField(to='Timetable.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('inst_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('capacity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('timetable_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('session_id', models.AutoField(primary_key=True, serialize=False)),
                ('number_of_students', models.IntegerField()),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], max_length=20)),
                ('timeslots', models.CharField(choices=[('07:00', '07:50'), ('07:50', '08:40'), ('08:40', '09:30'), ('09:40', '10:30'), ('10:40', '11:30')], max_length=20)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Timetable.course')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Timetable.department')),
                ('instructor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Timetable.instructor')),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Timetable.room')),
                ('timetable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Timetable.timetable')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='instructors',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Timetable.instructor'),
        ),
    ]
