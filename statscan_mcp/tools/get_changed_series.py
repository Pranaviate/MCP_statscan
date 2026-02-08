import httpx

BASE_URL = "https://www150.statcan.gc.ca/t1/wds/rest"


async def get_changed_series() -> dict:
    """
    Get list of Statistics Canada series updated today.

    Returns all series that have been updated on the current day.
    This endpoint has no parameters - it always returns today's changes.

    :return: Dictionary with list of changed series or error details
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/getChangedSeriesList")
            data = response.json()
        return data
    except Exception as e:
        return {
            "error": str(e),
            "hint": "Failed to fetch changed series from StatsCan API"
        }
