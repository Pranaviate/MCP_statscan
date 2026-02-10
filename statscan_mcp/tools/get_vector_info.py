from statscan_mcp.providers.wds_client import WDSClient

client = WDSClient()


async def get_vector_info(vector_id: int) -> dict:
    """
    Get metadata for a specific Statistics Canada vector.

    Returns information about the vector including its parent cube,
    coordinates, frequency, title, and other metadata (not the actual data).

    :param vector_id: The vector ID number (e.g., 41690973)
    :type vector_id: int
    :return: Dictionary with vector metadata or error details
    :rtype: dict
    """
    return await client.post("getSeriesInfoFromVector", [{"vectorId": vector_id}])
