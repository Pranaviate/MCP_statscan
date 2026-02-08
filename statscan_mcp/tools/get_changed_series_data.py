import httpx

BASE_URL = "https://www150.statcan.gc.ca/t1/wds/rest"


async def get_changed_series_data(product_id: int, coordinate: str) -> dict:
    """
    Get changed/updated data for a specific series within a Statistics Canada dataset.

    Returns the latest changes for a series identified by cube ID and coordinates,
    if it was updated today.

    :param product_id: The StatsCan product/cube ID (e.g., 35100003)
    :param coordinate: Dimension coordinate string (e.g., "1.12.0.0.0.0.0.0.0.0")
    :return: Dictionary with changed series data or error details
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{BASE_URL}/getChangedSeriesDataFromCubePidCoord",
                json=[{"productId": product_id, "coordinate": coordinate}]
            )
            data = response.json()
        return data
    except Exception as e:
        return {
            "error": str(e),
            "hint": "Failed to fetch changed series data from StatsCan API"
        }
