import json
import requests
import datetime
import os
from google.oauth2 import service_account
from google.cloud import storage
from time import time


# --------------------------------------------------------------
# ---------------setting up shit---------------------------------
# --------------------------------------------------------------

# Setting up location id to be fetched (be wary to only limit adding individual values later in SQL, not in this functions)
# Properti di sekitar kabupaten cilacap (dan kabupaten2 lain)
location_ids = ["4000039"]
extraction_date = datetime.date.today().strftime("%Y-%m-%d")

# Setting up headers for the  requests
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0",
    "Accept": "*/*",
    "Accept-Encoding": "gzip,deflate,br",
    "Accept-Language": "en-US,en;q=0.5",
}

# setting up Google cloud credentials
service_account_file = os.environ.get("SERVICE_ACCOUNT_FILE")
credentials = service_account.Credentials.from_service_account_file(
    service_account_file
)

# --------------------------------------------------------------
# --------------------------------------------------------------

# setting up recursive function to extracting data from API
def extracting_data(url, header, extracted_property, extracted_metadata):
    property_data = requests.get(url, headers=header).json()
    api_version = property_data["version"]
    if not property_data["data"]:
        # new code
        # -----
        # old code
        extracted_metadata["api_version"] = property_data["version"]
        extracted_metadata["extraction_pipeline_metadata"][
            "extraction_date"
        ] = extraction_date
        extracted_property = "\n".join(extracted_property)
        print("end of data")
        return
    else:
        # current code
        current_extraction = [data for data in property_data["data"]]
        extracted_property.extend(current_extraction)
        print(extracted_property)
        next_url = property_data["metadata"]["next_page_url"]
        extracting_data(next_url, header, extracted_property, extracted_metadata)

        # # previous code
        # extracted_property["data"].extend(property_data["data"])
        # next_url = property_data["metadata"]["next_page_url"]
        # extracting_data(next_url, header, extracted_property)


# upload data to GCS
def upload_blob_to_gcs(bucket_name, contents, destination_blob_name):
    # Upload file to bucket"""

    # ID of GCS bucket
    # bucket_name =

    # the contents from memory to be uploaded to file
    # contents =

    # the ID of your GCS object
    # destination_blob_name =

    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_string(contents)


# Fetching the data from the API for every approximate location of location_ids. Duplicates is allowed, remember to remove them later in the SQL transforms script tho. No need to limit strictly by location.
# Also, later scripts need to partitionate the json by the time? (liat ntar)


# main function
for location_id in location_ids:
    # Set up empty list to store the individual property data
    t_start = time()
    extracted_property_object = []
    extracted_property_object_metadata = {
        "api_version": "api_version",
        "extraction_pipeline_metadata": {
            "extraction_date": extraction_date,
            "extraction_speed": "",
        },
    }

    # Do the fetching
    url = f"http://api.olx.co.id/relevance/v2/search?facet_limit=100&clientId=pwa&location_facet_limit=20&location={location_id}&page=0&category=88&clientVersion=10.12.0&user=183b5ebc936x2a092b41&platform=web-desktop"

    # Run the extraction!
    extracting_data(
        url, headers, extracted_property_object, extracted_property_object_metadata
    )
    t_end = time()
    extraction_speed = t_end - t_start
    extracted_property_object_metadata["extraction_pipeline_metadata"][
        "extraction_speed"
    ] = extraction_speed

    # Wrote extracted data to json bytes n cleaning trailing comma
    extracted_property_json = (
        json.dumps(extracted_property_object, indent=4)
        .replace(",]", "]")
        .replace(",}", "}")
    )
    extracted_property_metadata_json = json.dumps(
        extracted_property_object_metadata, indent=4
    )

    # upload to GCS??
    upload_blob_to_gcs(
        "olx-property-analytics-rafzul",
        extracted_property_json,
        f"test-{extraction_date}.json",
    )
    upload_blob_to_gcs(
        "olx-property-analytics-rafzul",
        extracted_property_metadata_json,
        f"test-{extraction_date}-metadata.json",
    )
    print("object uploaded")
