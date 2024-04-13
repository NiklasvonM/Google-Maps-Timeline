import json
from pathlib import Path

from .models import GoogleMapsTimeline


def load_single_file(filepath: str | Path) -> GoogleMapsTimeline:
    with open(filepath, encoding="UTF-8") as file:
        data = json.load(file)
    return GoogleMapsTimeline(**data)


def load_directory_raw(directory: str | Path) -> list[GoogleMapsTimeline]:
    timelines = []
    for filepath in Path(directory).rglob("*.json"):
        timelines.append(load_single_file(filepath))
    return timelines


def load_directory(directory: str | Path) -> GoogleMapsTimeline:
    """
    Load all files in a specified directory and combine them into a single timeline.
    If a single file is provided, it will be loaded and returned as-is.
    """
    if Path(directory).is_file():
        return load_single_file(directory)
    timelines = load_directory_raw(directory)
    combined_timeline = GoogleMapsTimeline(
        timelineObjects=sum((timeline.timelineObjects for timeline in timelines), start=[])
    )
    return combined_timeline
