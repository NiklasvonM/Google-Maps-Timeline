from pathlib import Path

import matplotlib.pyplot as plt
from google_maps_timeline.data_loader import load_directory


def main() -> None:
    data_path = Path(__file__).parent / "data"
    timeline_data = load_directory(data_path)
    ping_periods: list[float] = []
    for timeline_object in timeline_data.timelineObjects:
        if timeline_object.activitySegment:
            segment = timeline_object.activitySegment
            if segment.simplifiedRawPath is not None:
                last_timestamp = segment.simplifiedRawPath.points[0].timestamp
                for point in segment.simplifiedRawPath.points[1:]:
                    ping_period = (point.timestamp - last_timestamp).total_seconds()
                    ping_periods.append(ping_period)
                    # print(ping_period)
                    last_timestamp = point.timestamp
    plt.hist([period for period in ping_periods if period < 600], bins=100)
    plt.title("Histogram of Google Maps Ping Periods")
    plt.xlabel("Time in seconds")
    plt.ylabel("Occurences")
    plt.show()


if __name__ == "__main__":
    main()
