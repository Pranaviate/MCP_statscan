from statscan_mcp.providers.wds_client import WDSClient

client = WDSClient()


async def get_changed_vector_data(vector_id: int) -> dict:
    """
    Get changed/updated data for a specific Statistics Canada vector.

    Returns the latest changes for a vector if it was updated today.

    :param vector_id: The vector ID number (e.g., 32164132)
    :return: Dictionary with changed vector data or error details
    """
    return await client.post("getChangedSeriesDataFromVector", [{"vectorId": vector_id}])
