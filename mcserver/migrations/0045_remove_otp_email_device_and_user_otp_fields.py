# Remove OTP email device and User OTP fields. Apply on production after this
# release is deployed while django_otp / otp_email remain in INSTALLED_APPS
# (same graph production already ran through 0009–0044). After 0045 is applied
# everywhere, you can drop django-otp and simplify migrations in a follow-up.

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mcserver', '0044_auto_20250606_1629'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomEmailDevice',
        ),
        migrations.RemoveField(
            model_name='user',
            name='otp_verified',
        ),
        migrations.RemoveField(
            model_name='user',
            name='otp_skip_till',
        ),
    ]
