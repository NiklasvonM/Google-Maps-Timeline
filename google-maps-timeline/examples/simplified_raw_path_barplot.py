from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
from google_maps_timeline.data_loader import load_directory


def main() -> None:
    data_path = Path(__file__).parent / "data"
    timeline_data = load_directory(data_path)
    simplified_raw_counter = Counter()
    for timeline_object in timeline_data.timelineObjects:
        if timeline_object.activitySegment:
            segment = timeline_object.activitySegment
            if segment.simplifiedRawPath is not None:
                simplified_raw_counter[len(segment.simplifiedRawPath.points)] += 1
    print(simplified_raw_counter)
    plt.bar(simplified_raw_counter.keys(), simplified_raw_counter.values())
    plt.show()


if __name__ == "__main__":
    main()
