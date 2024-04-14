from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
from google_maps_timeline.data_loader import load_directory


def main() -> None:
    data_path = Path(__file__).parent / "data"
    timeline_data = load_directory(data_path)
    transit_counter = Counter()
    for timeline_object in timeline_data.timelineObjects:
        if timeline_object.activitySegment:
            segment = timeline_object.activitySegment
            if segment.transitPath is not None:
                transit_counter[len(segment.transitPath.transitStops)] += 1
    print(transit_counter)
    plt.bar(transit_counter.keys(), transit_counter.values())
    plt.show()


if __name__ == "__main__":
    main()
