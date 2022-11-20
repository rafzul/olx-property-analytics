import json
import requests


# Setting up location id to be fetched (be wary to only limit adding individual values later in SQL, not in this functions)
# Properti di sekitar kabupaten cilacap (dan kabupaten2 lain)
location_ids = ["4000039"]

# Setting up headers for the  requests
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0",
    "Accept": "*/*",
    "Accept-Encoding": "gzip,deflate,br",
    "Accept-Language": "en-US,en;q=0.5",
}


def extracting_data(url, header, extracted_property):
    property_data = requests.get(url, headers=header).json()
    print("-----------------------")
    print(property_data)
    if not property_data["data"]:
        extracted_property["version"] = property_data["version"]
        extracted_property["metadata"] = property_data["metadata"]
        extracted_property["empty"] = not property_data["empty"]
        extracted_property["not_empty"] = not property_data["not_empty"]
        extracted_property["suggested_data"] = property_data["suggested_data"]
        extracted_property["similarads_data"] = property_data["similarads_data"]
        print("----------")
        print("end of data")
        return
    else:
        extracted_property["data"].extend(property_data["data"])
        next_url = property_data["metadata"]["next_page_url"]
        extracting_data(next_url, header, extracted_property)


# Fetching the data from the API for every approximate location of location_ids. Duplicates is allowed, remember to remove them later in the subsequent transforms script tho. No need to limit strictly by location.
# Also, later scripts need to partitionate the json by the time? (liat ntar     )
for location_id in location_ids:
    # Set up empty list to store the individual property data

    extracted_property_object = {
        "version": "",
        "data": [],
        "metadata": {},
        "empty": "",
        "not_empty": "",
        "suggested_data": [],
        "similarads_data": [],
    }

    # Do the fetching
    url = f"http://api.olx.co.id/relevance/v2/search?facet_limit=100&clientId=pwa&location_facet_limit=20&location={location_id}&page=0&category=88&clientVersion=10.12.0&user=183b5ebc936x2a092b41&platform=web-desktop"

    extracting_data(url, headers, extracted_property_object)

    # wrote extracted data to json file
    with open("test_extraction_api3.json", "w") as jsonfile:
        json.dump(extracted_property_object, jsonfile, indent=4)
    # print(extracted_property_object)
