# Generated by Django 4.2.5 on 2023-10-08 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Report",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("chess_com_username", models.CharField(max_length=100)),
                ("lichess_username", models.CharField(max_length=100)),
                ("time_class", models.CharField(max_length=20)),
                ("games_num", models.IntegerField()),
                ("analyzed_games", models.IntegerField(default=0, null=True)),
                ("engine_depth", models.IntegerField(default=10)),
                (
                    "fail_reason",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SingleGamePlayer",
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
                    "evaluation",
                    models.JSONField(help_text="Evaluation of the player per phase."),
                ),
                ("elo", models.IntegerField(help_text="ELO rating of the player.")),
                (
                    "avg_move_time",
                    models.JSONField(
                        help_text="Average move time of the player per phase."
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ChessGame",
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
                    "date",
                    models.DateTimeField(help_text="Date and time of the game in UTC."),
                ),
                (
                    "host",
                    models.CharField(
                        help_text="Server where the game was played.", max_length=255
                    ),
                ),
                (
                    "opening",
                    models.CharField(
                        help_text="Opening name in ECO format.", max_length=255
                    ),
                ),
                (
                    "opening_short",
                    models.CharField(
                        help_text="Short opening name in ECO format.", max_length=50
                    ),
                ),
                (
                    "phases",
                    models.JSONField(
                        help_text="Phases in half moves in the format (opening, middle game, end game)."
                    ),
                ),
                (
                    "player_color",
                    models.CharField(
                        help_text="Player color in the game.", max_length=10
                    ),
                ),
                (
                    "result",
                    models.JSONField(
                        help_text="Result of the game in the format (result, reason)."
                    ),
                ),
                (
                    "time_class",
                    models.CharField(
                        help_text="Time class of the game.", max_length=50
                    ),
                ),
                (
                    "time_control",
                    models.CharField(
                        help_text="Time control in the format 'time+increment' in seconds. e.g., '600+0' or '180+2'",
                        max_length=50,
                    ),
                ),
                ("url", models.URLField(help_text="URL to the game.")),
                (
                    "username",
                    models.CharField(
                        help_text="Username of the player.", max_length=50
                    ),
                ),
                (
                    "opponent",
                    models.ForeignKey(
                        help_text="Opponent object.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="opponent",
                        to="analyze_app.singlegameplayer",
                    ),
                ),
                (
                    "player",
                    models.ForeignKey(
                        help_text="Player object.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="player",
                        to="analyze_app.singlegameplayer",
                    ),
                ),
                (
                    "report",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="games",
                        to="analyze_app.report",
                    ),
                ),
            ],
        ),
    ]