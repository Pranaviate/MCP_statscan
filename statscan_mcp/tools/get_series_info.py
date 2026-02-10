from statscan_mcp.providers.wds_client import WDSClient

client = WDSClient()


async def get_series_info(product_id: int, coordinate: str) -> dict:
    """
    Get metadata for a specific series within a Statistics Canada dataset.

    Returns series information based on cube product ID and dimension coordinates.

    :param product_id: The StatsCan product/cube ID (e.g., 35100003)
    :param coordinate: Dimension coordinate string (e.g., "1.12.0.0.0.0.0.0.0.0")
    :return: Dictionary with series metadata or error details
    """
    return await client.post("getSeriesInfoFromCubePidCoord", [{"productId": product_id, "coordinate": coordinate}])
