import httpx

BASE_URL = "https://www150.statcan.gc.ca/t1/wds/rest"


async def get_changed_cubes(date: str) -> dict:
    """
    Get list of Statistics Canada cubes/datasets changed on a specific date.

    Returns cubes that were updated or released on the specified date.

    :param date: Date to check for changes in YYYY-MM-DD format (e.g., "2024-01-15")
    :return: Dictionary with list of changed cubes or error details
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/getChangedCubeList/{date}")
            data = response.json()
        return data
    except Exception as e:
        return {
            "error": str(e),
            "hint": "Failed to fetch changed cubes from StatsCan API"
        }
