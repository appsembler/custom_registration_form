from django.conf import settings
from django.db import models

# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, "AUTH_USER_MODEL", "auth.User")


class ExtraInfo(models.Model):
    """
    This model contains two extra fields that will be saved when a user registers.
    The form that wraps this model is in the forms.py file.
    """

    user = models.OneToOneField(USER_MODEL, null=True)
    MARKETS = (
        ("10", "Not Applicable"),
        ("36", "Australia - Melbourne"),
        ("39", "Australia - Sydney"),
        ("40", "Canada - Toronto"),
        ("47", "Canada - Vancouver"),
        ("35", "France - Paris"),
        ("115", "Germany"),
        ("92", "Japan - Fukuoka"),
        ("64", "Japan - Osaka"),
        ("79", "Japan - Nagoya"),
        ("44", "Japan - Tokyo"),
        ("43", "Netherlands - Amsterdam"),
        ("29", "UK - London"),
        ("120", "USA - Alabama"),
        ("122", "USA - Arkansas"),
        ("23", "USA - Atlanta"),
        ("60", "USA - Austin"),
        ("46", "USA - Baltimore"),
        ("102", "USA - Boise"),
        ("10", "USA - Boston"),
        ("61", "USA - Charlotte"),
        ("14", "USA - Chicago"),
        ("34", "USA - Connecticut"),
        ("22", "USA - Dallas"),
        ("27", "USA - Denver"),
        ("24", "USA - Detroit"),
        ("826", "USA - Houston"),
        ("58", "USA - Indianapolis"),
        ("116", "USA - Kentucky"),
        ("13", "USA - Los Angeles"),
        ("117", "USA - Louisiana"),
        ("33", "USA - Miami"),
        ("20", "USA - Minneapolis"),
        ("118", "USA - Mississippi"),
        ("807", "USA - Moline"),
        ("30", "USA - New Jersey"),
        ("11", "USA - New York City"),
        ("51", "USA - Northern Virginia"),
        ("32", "USA - Ohio"),
        ("119", "USA - Oklahoma"),
        ("19", "USA - Orange County"),
        ("72", "USA - Orlando"),
        ("121", "USA - Pensacola, FL"),
        ("18", "USA - Philadelphia"),
        ("31", "USA - Phoenix"),
        ("41", "USA - Portland, OR"),
        ("73", "USA - Providence"),
        ("803", "USA - Raleigh/Durham"),
        ("78", "USA - Richmond"),
        ("16", "USA - San Diego"),
        ("12", "USA - San Francisco"),
        ("17", "USA - Seattle"),
        ("15", "USA - Silicon Valley"),
        ("37", "USA - St. Louis"),
        ("68", "USA - Tampa"),
        ("63", "USA - Tennessee"),
        ("25", "USA - Washington, DC"),
        ("881", "USA - Wisconsin"),
    )
    market = models.CharField(
        verbose_name="Select Nearest Region",
        choices=MARKETS,
        blank=False,
        max_length=5,
    )
