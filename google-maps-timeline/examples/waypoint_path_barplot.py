from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
from google_maps_timeline.data_loader import load_directory


def main() -> None:
    data_path = Path(__file__).parent / "data"
    timeline_data = load_directory(data_path)
    waypoint_counter = Counter()
    for timeline_object in timeline_data.timelineObjects:
        if timeline_object.activitySegment:
            segment = timeline_object.activitySegment
            if segment.waypointPath is not None:
                waypoint_counter[len(segment.waypointPath.waypoints)] += 1
    print(waypoint_counter)
    plt.bar(waypoint_counter.keys(), waypoint_counter.values())
    plt.xticks(range(0, 600 + 1, 30))
    plt.show()


if __name__ == "__main__":
    main()
