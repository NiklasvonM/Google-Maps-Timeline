from pathlib import Path

from google_maps_timeline.data_loader import load_directory
from google_maps_timeline.visualization import visualize_timeline


def main():
    data_path = Path(__file__).parent / "data/Semantic Location History/2023/2023_OCTOBER.json"
    timeline = load_directory(data_path)
    map = visualize_timeline(timeline)
    map.save("output_map.html")


if __name__ == "__main__":
    main()
