# Generated by Django 4.1.3 on 2023-02-08 13:17

import content.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
        ("tags", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Source",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("0", "Other"),
                            ("1", "Book"),
                            ("2", "Course"),
                            ("3", "Video"),
                            ("4", "Article"),
                            ("5", "Lecture"),
                            ("6", "Tutorial"),
                        ],
                        default="0",
                        max_length=20,
                        verbose_name="Type",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        db_index=True, max_length=200, verbose_name="Title"
                    ),
                ),
                (
                    "link",
                    models.URLField(
                        blank=True,
                        default="",
                        max_length=255,
                        verbose_name="External link",
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=100,
                        verbose_name="Description",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(max_length=254, unique=True, verbose_name="Slug"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Note",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        db_index=True, max_length=100, verbose_name="Title"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        editable=False, max_length=255, unique=True, verbose_name="Slug"
                    ),
                ),
                (
                    "body_raw",
                    content.fields.MarkdownField(
                        blank=True,
                        rendered_field="body_html",
                        verbose_name="Markdown body",
                    ),
                ),
                (
                    "body_html",
                    content.fields.RenderedMarkdownField(
                        default="", max_length=70000, verbose_name="HTML body"
                    ),
                ),
                (
                    "summary",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="Write summary on the note in 250 symbols.",
                        max_length=250,
                        verbose_name="Summary",
                    ),
                ),
                (
                    "draft",
                    models.BooleanField(
                        default=False,
                        help_text="Only you can see the note.",
                        verbose_name="Draft",
                    ),
                ),
                (
                    "anonymous",
                    models.BooleanField(
                        default=False,
                        help_text="Others won't see that the note is yours.",
                        verbose_name="Anonymous",
                    ),
                ),
                (
                    "pin",
                    models.BooleanField(
                        default=False,
                        help_text="The note will appear in pin notes list.",
                        verbose_name="Pin",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created"),
                ),
                (
                    "modified",
                    models.DateTimeField(auto_now=True, verbose_name="Modified"),
                ),
                ("views", models.PositiveIntegerField(default=0, verbose_name="Views")),
                (
                    "lang",
                    models.CharField(
                        choices=[
                            ("en", "English"),
                            ("ru", "Russian"),
                            ("er", "Undetected"),
                        ],
                        default="er",
                        max_length=2,
                        verbose_name="Language",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Author",
                    ),
                ),
                (
                    "bookmarks",
                    models.ManyToManyField(
                        blank=True,
                        default=None,
                        related_name="bookmarked_notes",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "fork",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="content.note",
                        verbose_name="Parent",
                    ),
                ),
                (
                    "likes",
                    models.ManyToManyField(
                        blank=True,
                        related_name="liked_notes",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "source",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="notes",
                        to="content.source",
                        verbose_name="Source",
                    ),
                ),
                (
                    "tags",
                    taggit.managers.TaggableManager(
                        blank=True,
                        help_text='Add tags. Separate tags by using "Enter" or comma.\n        You can add maximum 3 tags, and length of tags should be less than 25\n        symbols.',
                        through="tags.UnicodeTaggedItem",
                        to="taggit.Tag",
                        verbose_name="Tags",
                    ),
                ),
            ],
            options={
                "ordering": ("-created",),
            },
        ),
    ]
