import asyncio
import csv
import json
import os
import time

from datetime import datetime, timezone
from pathlib import Path

import websockets
from dotenv import load_dotenv


# ==========================================
# 1. Project Configuration
# ==========================================

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data" / "raw"

DATA_DIR.mkdir(parents=True, exist_ok=True)

load_dotenv(BASE_DIR / ".env")

API_KEY = os.getenv("AISSTREAM_API_KEY")

WS_URL = "wss://stream.aisstream.io/v0/stream"

COLLECTION_DURATION = 300  # Seconds


# Singapore Strait bounding box
BOUNDING_BOXES = [
    [
        [0.8, 103.3],
        [1.6, 104.5]
    ]
]


# ==========================================
# 2. Output Configuration
# ==========================================

FILE_TIMESTAMP = datetime.now(timezone.utc).strftime(
    "%Y%m%d_%H%M%S"
)

OUTPUT_FILE = (
    DATA_DIR / f"ais_positions_{FILE_TIMESTAMP}.csv"
)

FIELDNAMES = [
    "received_at_utc",
    "mmsi",
    "ship_name",
    "latitude",
    "longitude",
    "speed_over_ground",
    "course_over_ground",
    "true_heading",
    "navigation_status",
    "rate_of_turn",
    "position_accuracy",
    "message_type"
]


# ==========================================
# 3. Parse AIS Messages
# ==========================================

def parse_position_report(message):

    if message.get("MessageType") != "PositionReport":
        return None

    metadata = message.get("MetaData", {})

    position = message.get(
        "Message", {}
    ).get("PositionReport", {})

    if position.get("Valid") is False:
        return None

    latitude = position.get(
        "Latitude", metadata.get("Latitude")
    )

    longitude = position.get(
        "Longitude", metadata.get("Longitude")
    )

    mmsi = metadata.get(
        "MMSI", position.get("UserID")
    )

    if latitude is None or longitude is None or not mmsi:
        return None

    if not (-90 <= latitude <= 90):
        return None

    if not (-180 <= longitude <= 180):
        return None

    return {
        "received_at_utc": datetime.now(
            timezone.utc
        ).isoformat(),

        "mmsi": mmsi,
        "ship_name": str(
            metadata.get("ShipName") or ""
        ).strip(),

        "latitude": latitude,
        "longitude": longitude,
        "speed_over_ground": position.get("Sog"),
        "course_over_ground": position.get("Cog"),
        "true_heading": position.get("TrueHeading"),

        "navigation_status": position.get(
            "NavigationalStatus"
        ),

        "rate_of_turn": position.get("RateOfTurn"),

        "position_accuracy": position.get(
            "PositionAccuracy"
        ),

        "message_type": message.get("MessageType")
    }


# ==========================================
# 4. AIS Data Collection Engine
# ==========================================

async def collect_ais_data():

    if not API_KEY:
        raise ValueError(
            "AISStream API key missing from .env"
        )

    subscription = {
        "APIKey": API_KEY,
        "BoundingBoxes": BOUNDING_BOXES,
        "FilterMessageTypes": ["PositionReport"]
    }

    record_count = 0
    vessel_ids = set()

    print("=" * 55)
    print("GLOBAL VESSEL INTELLIGENCE SYSTEM")
    print("AIS Data Collection Engine")
    print("=" * 55)

    print("Region: Singapore Strait")
    print(f"Duration: {COLLECTION_DURATION} seconds")
    print(f"Output: {OUTPUT_FILE}")
    print("Connecting to AISStream...")

    with open(
        OUTPUT_FILE,
        mode="w",
        newline="",
        encoding="utf-8"
    ) as csv_file:

        writer = csv.DictWriter(
            csv_file,
            fieldnames=FIELDNAMES
        )

        writer.writeheader()

        async with websockets.connect(
            WS_URL,
            compression="deflate",
            open_timeout=60
        ) as websocket:

            await websocket.send(
                json.dumps(subscription)
            )

            print("Connected. Subscription sent.")
            print("Collecting vessel data...\n")

            deadline = (
                time.monotonic() + COLLECTION_DURATION
            )

            while time.monotonic() < deadline:

                remaining = deadline - time.monotonic()

                try:

                    raw_message = await asyncio.wait_for(
                        websocket.recv(),
                        timeout=min(10, remaining)
                    )

                    message = json.loads(raw_message)

                    if message.get("error"):

                        print("AISStream rejected the request.")
                        break

                    if (
                        message.get("MessageType")
                        == "SubscriptionConfirmation"
                    ):

                        print("Subscription confirmed.")
                        continue

                    record = parse_position_report(message)

                    if record is None:
                        continue

                    writer.writerow(record)

                    record_count += 1
                    vessel_ids.add(record["mmsi"])

                    if record_count % 100 == 0:

                        csv_file.flush()

                        print(
                            f"Records: {record_count:,} | "
                            f"Unique vessels: {len(vessel_ids):,}"
                        )

                except asyncio.TimeoutError:

                    if time.monotonic() < deadline:
                        print("Waiting for AIS messages...")

                except json.JSONDecodeError:

                    print("Invalid JSON message skipped.")

    print("\n" + "=" * 55)
    print("COLLECTION FINISHED")
    print("=" * 55)

    print(f"Total records: {record_count:,}")
    print(f"Unique vessels: {len(vessel_ids):,}")
    print(f"Output file: {OUTPUT_FILE}")

    if record_count == 0:
        print("Warning: No vessel records were collected.")


# ==========================================
# 5. Execute Collector
# ==========================================

if __name__ == "__main__":

    try:

        asyncio.run(collect_ais_data())

    except KeyboardInterrupt:

        print("\nCollection stopped by user.")

    except Exception as exc:

        print(f"Collector stopped: {type(exc).__name__}")
        print("Check API access and network connection.")
        raise SystemExit(1)