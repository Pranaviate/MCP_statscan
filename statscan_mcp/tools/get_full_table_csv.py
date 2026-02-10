from typing import Optional
from statscan_mcp.providers.wds_client import WDSClient

client = WDSClient()


async def get_full_table_csv(product_id: int, language: Optional[str] = "en") -> dict:
    """
    Get download URL for full Statistics Canada table in CSV format.

    Returns a URL to a downloadable ZIP file containing the complete table data.

    :param product_id: The StatsCan product/cube ID (e.g., 14100287)
    :param language: Language code - "en" for English or "fr" for French (default: "en")
    :return: Dictionary with download URL or error details
    """
    return await client.get(f"getFullTableDownloadCSV/{product_id}/{language}")
