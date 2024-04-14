from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt
from google_maps_timeline.data_loader import load_directory


def main() -> None:
    data_path = Path(__file__).parent / "data"
    timeline_data = load_directory(data_path)
    ping_periods: dict[str, list[float]] = defaultdict(list)
    for timeline_object in timeline_data.timelineObjects:
        if timeline_object.activitySegment:
            segment = timeline_object.activitySegment
            if segment.simplifiedRawPath is not None:
                if segment.simplifiedRawPath.source is None:
                    current_source_type = "None"
                else:
                    current_source_type = segment.simplifiedRawPath.source
                last_timestamp = segment.simplifiedRawPath.points[0].timestamp
                for point in segment.simplifiedRawPath.points[1:]:
                    ping_period = (point.timestamp - last_timestamp).total_seconds()
                    ping_periods[current_source_type].append(ping_period)
                    # print(ping_period)
                    last_timestamp = point.timestamp
    fig, ax = plt.subplots(len(ping_periods), sharex=True)
    for idx, (source_type, data) in enumerate(ping_periods.items()):
        axis_cur: plt.Axes = ax[idx]
        # axis_cur.set_anchor("W")
        axis_cur.hist([period for period in data if period < 600], bins=100)
        axis_cur.set_title(f"Source Type {source_type}")
        # axis_cur.xaxis.set_label("Time in seconds")
        # axis_cur.yaxis.set_label("Occurences")
        # xlabel every 20 units
        axis_cur.xaxis.set_ticks(range(0, 600 + 1, 30))
    fig.text(0.08, 0.5, "Occurences", va="center", rotation="vertical")
    fig.subplots_adjust(hspace=0.5)
    plt.xlabel("Time in seconds")
    plt.show()


if __name__ == "__main__":
    main()
