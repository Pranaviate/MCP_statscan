from statscan_mcp.providers.wds_client import WDSClient

client = WDSClient()


async def get_changed_series_data(product_id: int, coordinate: str) -> dict:
    """
    Get changed/updated data for a specific series within a Statistics Canada dataset.

    Returns the latest changes for a series identified by cube ID and coordinates,
    if it was updated today.

    :param product_id: The StatsCan product/cube ID (e.g., 35100003)
    :param coordinate: Dimension coordinate string (e.g., "1.12.0.0.0.0.0.0.0.0")
    :return: Dictionary with changed series data or error details
    """
    return await client.post("getChangedSeriesDataFromCubePidCoord", [{"productId": product_id, "coordinate": coordinate}])
