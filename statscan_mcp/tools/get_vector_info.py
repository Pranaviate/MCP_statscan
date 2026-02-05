import httpx

BASE_URL = "https://www150.statcan.gc.ca/t1/wds/rest"

async def get_vector_info(
        vector_id: int,
) -> dict:
    """
    Get metadata for a specific Statistics Canada vector.

    Returns information about the vector including its parent cube,
    coordinates, frequency, title, and other metadata (not the actual data).

    :param vector_id: The vector ID number (e.g., 41690973)
    :type vector_id: int
    :return: Dictionary with vector metadata or error details
    :rtype: dict
    """

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{BASE_URL}/getSeriesInfoFromVector",
                json=[{"vectorId": vector_id}]
            )
            data = response.json()

        return data
    except Exception as e:
        return {
            "error": str(e),
            "hint": "Failed to fetch vector data from StatsCan API"
        }