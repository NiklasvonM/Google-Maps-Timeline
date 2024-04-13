from collections import Counter
from pathlib import Path

from google_maps_timeline.data_loader import load_directory


def main() -> None:
    data_path = Path(__file__).parent / "data"
    timeline_data = load_directory(data_path)
    counter = Counter()
    for timeline_object in timeline_data.timelineObjects:
        if timeline_object.activitySegment:
            counter[timeline_object.activitySegment.activityType] += 1
    print(counter)


if __name__ == "__main__":
    main()
