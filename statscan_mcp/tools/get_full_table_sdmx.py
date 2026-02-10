from statscan_mcp.providers.wds_client import WDSClient

client = WDSClient()


async def get_full_table_sdmx(product_id: int) -> dict:
    """
    Get download URL for full Statistics Canada table in SDMX format.

    Returns a URL to a downloadable ZIP file containing the complete table data
    in SDMX (Statistical Data and Metadata eXchange) format. This is a bilingual
    XML format used for international statistical data exchange.

    :param product_id: The StatsCan product/cube ID (e.g., 14100287)
    :return: Dictionary with download URL or error details
    """
    return await client.get(f"getFullTableDownloadSDMX/{product_id}")
