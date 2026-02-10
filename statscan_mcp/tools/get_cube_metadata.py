from statscan_mcp.providers.wds_client import WDSClient

client = WDSClient()


async def get_cube_metadata(product_id: int) -> dict:
    """
    Get detailed metadata for a Statistics Canada dataset.

    Returns structure information including dimensions, members, and date ranges.

    :param product_id: The StatsCan product/cube ID (e.g., 18100004)
    :type product_id: int
    :return: Dictionary with cube metadata or error details
    :rtype: dict
    """
    return await client.post("getCubeMetadata", [{"productId": product_id}])
