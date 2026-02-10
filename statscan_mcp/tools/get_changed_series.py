from statscan_mcp.providers.wds_client import WDSClient

client = WDSClient()

async def get_changed_series() -> dict:
    """
    Get list of Statistics Canada series updated today.

    Returns all series that have been updated on the current day.
    This endpoint has no parameters - it always returns today's changes.

    :return: Dictionary with list of changed series or error details
    """
    return await client.get(endpoint="getChangedSeriesList", params=None)
