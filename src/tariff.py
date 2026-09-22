import re
from typing import Optional


class Tariff:
    def __init__(
        self,
        id: str,
        display_name: str,
        api_display_name: str,
        tariff_code_matcher: str,
        url_tariff_name: str,
        switchable: bool,
        product_code: Optional[str] = None,
    ):
        self.id = id
        self.display_name = display_name
        self.api_display_name = api_display_name
        self.tariff_code_matcher = tariff_code_matcher
        self.url_tariff_name = url_tariff_name
        self.switchable = switchable
        self.product_code = product_code
        self._regex = re.compile(tariff_code_matcher, re.IGNORECASE)

    def is_tariff(self, current_tariff_name: str) -> bool:
        """Check if the given tariff name matches the tariff code matcher."""
        return bool(self._regex.search(current_tariff_name))

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Tariff):
            return self.id == other.id
        return False

    def __hash__(self) -> int:
        return hash(self.id)

    def __repr__(self) -> str:
        return (
            f"Tariff(id={self.id!r}, display_name={self.display_name!r}, "
            f"switchable={self.switchable!r})"
        )


TARIFFS = [
    # Match specific specialist tariffs first
    Tariff("go", "Octopus Go", "Octopus Go", r"-go-var-", "go", True),
    Tariff("go-fix-12m", "Octopus Go 12M Fixed", "Octopus Go 12M Fixed", r"-go-fix-", "go", True),
    Tariff("agile", "Agile Octopus", "Agile Octopus", r"-agile-", "agile", True),
    Tariff("cosy", "Cosy Octopus", "Cosy Octopus", r"-cosy-(?!.*fix)", "cosy-octopus", True),
    Tariff(
        "intelligent-go",
        "Intelligent Octopus Go",
        "Intelligent Octopus",  # Matches the exact product display_name in Octopus REST API
        r"intelli-(?:var|fix)|iog-",
        "intelligent-go",
        False,  # Not auto-switchable via bot (requires in-app EV test charge)
    ),
    # Flexible should explicitly exclude other EV/heat pump variable products
    Tariff(
        "flexible",
        "Flexible Octopus",
        "Flexible Octopus",
        r"(?<!go-|cosy-|intelli-)var-",
        "",
        False,
    ),
]
    def __repr__(self) -> str:
        return (
            f"Tariff(id={self.id!r}, display_name={self.display_name!r}, "
            f"switchable={self.switchable!r})"
        )


TARIFFS = [
    # Match specific specialist tariffs first
    Tariff("go", "Octopus Go", "Octopus Go", r"-go-var-", "go", True),
    Tariff("go-fix-12m", "Octopus Go 12M Fixed", "Octopus Go 12M Fixed", r"-go-fix-", "go", True),
    Tariff("agile", "Agile Octopus", "Agile Octopus", r"-agile-", "agile", True),
    Tariff("cosy", "Cosy Octopus", "Cosy Octopus", r"-cosy-(?!.*fix)", "cosy-octopus", True),
    Tariff(
        "intelligent-go",
        "Intelligent Octopus Go",
        "Intelligent Octopus Go",
        r"intelli-(?:var|fix)|iog-",
        "intelligent-go",
        False,
    ),
    # Flexible should explicitly exclude other EV/heat pump variable products
    Tariff(
        "flexible",
        "Flexible Octopus",
        "Flexible Octopus",
        r"(?<!go-|cosy-|intelli-)var-",
        "",
        False,
    ),
]
