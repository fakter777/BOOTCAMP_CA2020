from django.db import migrations, models




class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAPI'
            fields=[
                (('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
                (('name', models.CharField(max_lenght=50),
                (('email', models.EmailField(max_lenght=254, unique=True),
                (('password', models.Charfield(max_lenght=50)),
        ];
    ),
)


        )
    ]