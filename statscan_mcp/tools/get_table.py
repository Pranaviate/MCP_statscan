import httpx

BASE_URL = "https://www150.statcan.gc.ca/t1/wds/rest"

async def get_table(product_id: int, coordinate: str, latest_n: int) -> dict:
    """
    Get rectangular data slice from a Statistics Canada dataset.

    Fetches the latest N periods of data for specific dimension coordinates.

    :param product_id: The StatsCan product/cube ID (e.g., 35100003)
    :param coordinate: Dimension coordinate string (e.g., "1.12.0.0.0.0.0.0.0.0")
    :param latest_n: Number of latest periods to retrieve
    :return: Dictionary with table data or error details
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{BASE_URL}/getDataFromCubePidCoordAndLatestNPeriods", json=[{"productId": product_id, "coordinate": coordinate, "latestN": latest_n}])
            data = response.json()
        return data
    except Exception as e:
        return {
            "error": str(e),
            "hint": "Failed to fetch table data from StatsCan API"
        }