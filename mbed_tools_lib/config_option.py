"""Common way of describing configuration options."""
import dataclasses


@dataclasses.dataclass(frozen=True)
class ConfigOption:
    """Configuration option."""

    name: str
    doc: str
