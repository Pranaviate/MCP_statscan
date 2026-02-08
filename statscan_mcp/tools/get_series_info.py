import httpx

BASE_URL = "https://www150.statcan.gc.ca/t1/wds/rest"


async def get_series_info(product_id: int, coordinate: str) -> dict:
    """
    Get metadata for a specific series within a Statistics Canada dataset.

    Returns series information based on cube product ID and dimension coordinates.

    :param product_id: The StatsCan product/cube ID (e.g., 35100003)
    :param coordinate: Dimension coordinate string (e.g., "1.12.0.0.0.0.0.0.0.0")
    :return: Dictionary with series metadata or error details
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{BASE_URL}/getSeriesInfoFromCubePidCoord",
                json=[{"productId": product_id, "coordinate": coordinate}]
            )
            data = response.json()
        return data
    except Exception as e:
        return {
            "error": str(e),
            "hint": "Failed to fetch series info from StatsCan API"
        }
