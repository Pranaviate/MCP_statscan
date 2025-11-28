import httpx

BASE_URL = "https://www150.statcan.gc.ca/t1/wds/rest"

async def get_cube_metadata(product_id: int) -> dict:
    """
    Get detailed metadata for a Statistics Canada dataset.

    Returns structure information including dimensions, members, and date ranges.

    :param product_id: The StatsCan product/cube ID (e.g., 18100004)
    :type product_id: int
    :return: Dictionary with cube metadata or error details
    :rtype: dict
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{BASE_URL}/getCubeMetadata", json=[{"productId": product_id}])
            data = response.json()

        return data
    except Exception as e:
        return {
            "error": str(e),
            "hint": "Failed to fetch cube metadata from StatsCan API"
        }
