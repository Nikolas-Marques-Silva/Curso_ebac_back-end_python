from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.RenameField(
                    model_name='product',
                    old_name='Category',
                    new_name='category',
                ),
            ],
            database_operations=[],
        ),
    ]