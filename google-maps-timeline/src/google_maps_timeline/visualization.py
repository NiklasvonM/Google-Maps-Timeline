import folium

from .models import GoogleMapsTimeline


def visualize_timeline(timeline: GoogleMapsTimeline, map=None):
    if map is None:
        map = folium.Map()  # Default map

    for item in timeline.timelineObjects:
        if item.activitySegment:
            start = item.activitySegment.startLocation
            end = item.activitySegment.endLocation
            if (
                not start.latitudeE7
                or not end.latitudeE7
                or not start.longitudeE7
                or not end.longitudeE7
            ):
                continue
            folium.Marker(
                [start.latitudeE7 / 1e7, start.longitudeE7 / 1e7], tooltip="Start"
            ).add_to(map)
            folium.Marker([end.latitudeE7 / 1e7, end.longitudeE7 / 1e7], tooltip="End").add_to(map)
            folium.PolyLine(
                [
                    (start.latitudeE7 / 1e7, start.longitudeE7 / 1e7),
                    (end.latitudeE7 / 1e7, end.longitudeE7 / 1e7),
                ],
                color="blue",
            ).add_to(map)

    return map
