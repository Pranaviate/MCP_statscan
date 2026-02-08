import httpx

BASE_URL = "https://www150.statcan.gc.ca/t1/wds/rest"


async def get_changed_vector_data(vector_id: int) -> dict:
    """
    Get changed/updated data for a specific Statistics Canada vector.

    Returns the latest changes for a vector if it was updated today.

    :param vector_id: The vector ID number (e.g., 32164132)
    :return: Dictionary with changed vector data or error details
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{BASE_URL}/getChangedSeriesDataFromVector",
                json=[{"vectorId": vector_id}]
            )
            data = response.json()
        return data
    except Exception as e:
        return {
            "error": str(e),
            "hint": "Failed to fetch changed vector data from StatsCan API"
        }
