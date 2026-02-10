from statscan_mcp.providers.wds_client import WDSClient

client = WDSClient()


async def get_changed_cubes(date: str) -> dict:
    """
    Get list of Statistics Canada cubes/datasets changed on a specific date.

    Returns cubes that were updated or released on the specified date.

    :param date: Date to check for changes in YYYY-MM-DD format (e.g., "2024-01-15")
    :return: Dictionary with list of changed cubes or error details
    """
    return await client.get(f"getChangedCubeList/{date}")
