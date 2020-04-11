# Generated by Django 2.2.4 on 2019-12-10 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import organizations.base
import organizations.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="The name of the organization", max_length=200
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                (
                    "created",
                    organizations.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "modified",
                    organizations.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "slug",
                    organizations.fields.SlugField(
                        blank=True,
                        editable=False,
                        help_text="The name in all lowercase, suitable for URL identification",
                        max_length=200,
                        populate_from="name",
                        unique=True,
                    ),
                ),
                ("monthly_subscription", models.IntegerField(default=1000)),
            ],
            options={
                "verbose_name": "organization",
                "verbose_name_plural": "organizations",
                "ordering": ["name"],
                "abstract": False,
            },
            bases=(organizations.base.UnicodeMixin, models.Model),
        ),
        migrations.CreateModel(
            name="AccountUser",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    organizations.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "modified",
                    organizations.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                ("is_admin", models.BooleanField(default=False)),
                ("user_type", models.CharField(default="", max_length=1)),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="organization_users",
                        to="accounts.Account",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="accounts_accountuser",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "organization user",
                "verbose_name_plural": "organization users",
                "ordering": ["organization", "user"],
                "abstract": False,
                "unique_together": {("user", "organization")},
            },
            bases=(organizations.base.UnicodeMixin, models.Model),
        ),
        migrations.CreateModel(
            name="AccountOwner",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    organizations.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "modified",
                    organizations.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "organization",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="owner",
                        to="accounts.Account",
                    ),
                ),
                (
                    "organization_user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.AccountUser",
                    ),
                ),
            ],
            options={
                "verbose_name": "organization owner",
                "verbose_name_plural": "organization owners",
                "abstract": False,
            },
            bases=(organizations.base.UnicodeMixin, models.Model),
        ),
        migrations.CreateModel(
            name="AccountInvitation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("guid", models.UUIDField(editable=False)),
                (
                    "invitee_identifier",
                    models.CharField(
                        help_text="The contact identifier for the invitee, email, phone number, social media handle, etc.",
                        max_length=1000,
                    ),
                ),
                (
                    "created",
                    organizations.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "modified",
                    organizations.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "invited_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="accounts_accountinvitation_sent_invitations",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "invitee",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="accounts_accountinvitation_invitations",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="organization_invites",
                        to="accounts.Account",
                    ),
                ),
            ],
            options={"abstract": False},
            bases=(organizations.base.UnicodeMixin, models.Model),
        ),
        migrations.AddField(
            model_name="account",
            name="users",
            field=models.ManyToManyField(
                related_name="accounts_account",
                through="accounts.AccountUser",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
