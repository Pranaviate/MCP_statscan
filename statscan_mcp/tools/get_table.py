from statscan_mcp.providers.wds_client import WDSClient

client = WDSClient()


async def get_table(product_id: int, coordinate: str, latest_n: int) -> dict:
    """
    Get rectangular data slice from a Statistics Canada dataset.

    Fetches the latest N periods of data for specific dimension coordinates.

    :param product_id: The StatsCan product/cube ID (e.g., 35100003)
    :param coordinate: Dimension coordinate string (e.g., "1.12.0.0.0.0.0.0.0.0")
    :param latest_n: Number of latest periods to retrieve
    :return: Dictionary with table data or error details
    """
    return await client.post("getDataFromCubePidCoordAndLatestNPeriods", [{"productId": product_id, "coordinate": coordinate, "latestN": latest_n}])
