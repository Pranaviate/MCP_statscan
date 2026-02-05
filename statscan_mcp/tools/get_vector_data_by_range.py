import httpx

BASE_URL = "https://www150.statcan.gc.ca/t1/wds/rest"

async def get_vector_data_by_range(
        vector_id: int,
        start_date: str,
        end_date: str
) -> dict:
    """
    Fetch time series data for a specific Statistics Canada vector.

    Returns actual data values over time for the specified vector.

    :param vector_id: The vector ID number (e.g., 41690973)
    :type vector_id: int
    :param start_date: Start date in YYYY-MM-DD format (e.g., 2020-01-01)
    :type start_date: str
    :param end_date: End date in YYYY-MM-DD format (e.g., 2024-01-01)
    :type end_date: str
    :return: Dictionary with time series data or error details
    :rtype: dict
    """

    try:
        params = {
            "vectorIds": f'"{vector_id}"',
            "startRefPeriod": start_date,
            "endReferencePeriod": end_date
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{BASE_URL}/getDataFromVectorByReferencePeriodRange",
                params=params
            )
            data = response.json()

        return data
    except Exception as e:
        return {
            "error": str(e),
            "hint": "Failed to fetch vector data from StatsCan API"
        }
