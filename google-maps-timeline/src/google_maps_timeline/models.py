"""
This file was generated with the help of https://github.com/NiklasvonM/config-adapter
and https://locationhistoryformat.com/reference/semantic/.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel

ActivityType = Literal[
    "BOATING",
    "CATCHING_POKEMON",
    "CYCLING",
    "FLYING",
    "HIKING",
    "HORSEBACK_RIDING",
    "IN_BUS",
    "IN_CABLECAR",
    "IN_FERRY",
    "IN_FUNICULAR",
    "IN_GONDOLA_LIFT",
    "IN_PASSENGER_VEHICLE",
    "IN_SUBWAY",
    "IN_TAXI",
    "IN_TRAIN",
    "IN_TRAM",
    "IN_VEHICLE",
    "IN_WHEELCHAIR",
    "KAYAKING",
    "KITESURFING",
    "MOTORCYCLING",
    "PARAGLIDING",
    "ROWING",
    "RUNNING",
    "SAILING",
    "SKATEBOARDING",
    "SKATING",
    "SKIING",
    "SLEDDING",
    "SNOWBOARDING",
    "SNOWMOBILE",
    "SNOWSHOEING",
    "STILL",
    "SWIMMING",
    "UNKNOWN_ACTIVITY_TYPE",
    "WALKING",
    "WALKING_NORDIC",
]
Confidence = Literal["HIGH_CONFIDENCE", "LOW_CONFIDENCE", "MEDIUM_CONFIDENCE", "USER_CONFIRMED"]
EditConfirmationStatus = Literal["CONFIRMED", "NOT_CONFIRMED"]
PlaceVisitType = Literal["SINGLE_PLACE"]
SourceType = Literal["BACKFILLED", "INFERRED", "RESNAPPED_FOR_EDIT"]


class GoogleMapsTimeline(BaseModel):
    timelineObjects: list[TimelineObjectsConfig]


class TimelineObjectsConfig(BaseModel):
    activitySegment: ActivitySegmentConfig | None = None
    placeVisit: PlaceVisitConfig | None = None


class ActivitySegmentConfig(BaseModel):
    startLocation: StartLocationConfig
    endLocation: StartLocationConfig
    duration: DurationConfig
    distance: int | None = None
    activityType: ActivityType | None = None
    confidence: Literal["HIGH", "LOW", "MEDIUM", "UNKNOWN_CONFIDENCE"] | None = None
    activities: list[ActivitiesConfig]
    waypointPath: WaypointPathConfig | None = None
    transitPath: TransitPathConfig | None = None
    simplifiedRawPath: SimplifiedRawPathConfig | None = None


class StartLocationConfig(BaseModel):
    latitudeE7: int | None = None
    longitudeE7: int | None = None
    sourceInfo: SourceInfoConfig | None = None


class SourceInfoConfig(BaseModel):
    deviceTag: int


class DurationConfig(BaseModel):
    startTimestamp: datetime
    endTimestamp: datetime


class ActivitiesConfig(BaseModel):
    activityType: ActivityType
    probability: float


class WaypointPathConfig(BaseModel):
    waypoints: list[WaypointsConfig]
    source: SourceType
    roadSegment: list[RoadSegmentConfig] | None = None
    distanceMeters: float | None = None
    travelMode: Literal["BICYCLE", "DRIVE", "WALK"] | None = None
    confidence: float | None = None


class WaypointsConfig(BaseModel):
    latE7: int
    lngE7: int


class RoadSegmentConfig(BaseModel):
    placeId: str | None = None
    duration: str | None = None


class PlaceVisitConfig(BaseModel):
    location: LocationConfig
    duration: DurationConfig | None = None
    placeConfidence: Confidence | None = None
    centerLatE7: int | None = None
    centerLngE7: int | None = None
    visitConfidence: int | None = None
    otherCandidateLocations: list[OtherCandidateLocationsConfig] | None = None
    editConfirmationStatus: EditConfirmationStatus
    locationConfidence: int | None = None
    placeVisitType: PlaceVisitType | None = None
    placeVisitImportance: Literal["MAIN", "TRANSITIONAL"] | None = None
    childVisits: list[PlaceVisitConfig] | None = None
    placeVisitLevel: int = 0


class LocationConfig(BaseModel):
    latitudeE7: int | None = None
    longitudeE7: int | None = None
    placeId: str | None = None
    address: str | None = None
    name: str | None = None
    sourceInfo: SourceInfoConfig | None = None
    locationConfidence: float | None = None
    calibratedProbability: float | None = None
    semanticType: (
        Literal["TYPE_ALIASED_LOCATION", "TYPE_HOME", "TYPE_SEARCHED_ADDRESS", "TYPE_WORK"] | None
    ) = None


class OtherCandidateLocationsConfig(BaseModel):
    latitudeE7: int | None = None
    longitudeE7: int | None = None
    placeId: str | None = None
    address: str | None = None
    name: str | None = None
    locationConfidence: float | None = None
    calibratedProbability: float | None = None
    isCurrentLocation: bool | None = None


class TransitPathConfig(BaseModel):
    transitStops: list[TransitStopsConfig]
    name: str
    hexRgbColor: str
    linePlaceId: str
    stopTimesInfo: list[StopTimesInfoConfig] | None = None
    source: SourceType
    confidence: float | None = None
    distanceMeters: float | None = None


class TransitStopsConfig(BaseModel):
    latitudeE7: int
    longitudeE7: int
    placeId: str
    address: str | None = None
    name: str


class StopTimesInfoConfig(BaseModel):
    scheduledDepartureTimestamp: datetime | None = None
    realtimeDepartureTimestamp: datetime | None = None
    scheduleArrivalTimestamp: datetime | None = None
    realtimeArrivalTimestamp: datetime | None = None


class SimplifiedRawPathConfig(BaseModel):
    points: list[PointsConfig]
    source: SourceType | None = None
    distanceMeters: float | None = None


class PointsConfig(BaseModel):
    latE7: int
    lngE7: int
    accuracyMeters: int
    timestamp: datetime
