import json

schema_reference = [
    "id",
    "score",
    "spell",
    "status",
    "category_id",
    "favorites",
    "vasTags",
    "has_phone_param",
    "description",
    "created_at",
    "inspection_info",
    "package_id",
    "title",
    "partner_id",
    "user_type",
    "price",
    "partner_code",
    "monetizationInfo",
    "images",
    "certified_car",
    "package",
    "is_kyc_verified_user",
    "locations_resolved",
    "deal_price",
    "business_platform",
    "main_info",
    "display_date",
    "isSpinViewAvailable",
    "user_id",
    "installment",
    "created_at_first",
    "locations",
    "parameters",
]

with open("/home/rafzul/projects/olx-property-analytics/staging_schema.json", "r") as f:
    schema_source = json.load(f)


# basic_search = []

# method 1
# def basicSearch(array_reference, array_source)
#     for i in enumerate(array_source)):
#         for name in array_reference:
#             if array_source[i]["name"] != name
#                 pass
#             else:
#                 basic_search.append(array_source)


# ------
# nyobain pake enumerate(array) vs range(len(array))

# schemas_destination = [(index, schema_reference[index]) for index in range(len(schema_reference))]

# schemas_destination = [datas["name"] for index, datas in enumerate(schemas_source)]

# -----

# method 2 pake dict get (kecepatan O(1))
def sortedUsingGet(array_reference, array_source):
    ordered_schema_reference = {
        value: index for index, value in enumerate(array_reference)
    }
    schemas_destination = sorted(
        array_source, key=lambda element: ordered_schema_reference.get(element["name"])
    )

    return schemas_destination


# method 3 pake index (kecepatan O(n))


schemas_destination = sortedUsingGet(schema_reference, schema_source)

with open(
    "/home/rafzul/projects/olx-property-analytics/sorted_staging_schema.json", "w"
) as f:
    json.dump(schemas_destination, f, indent=4)
