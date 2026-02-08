import httpx
from typing import Optional

BASE_URL = "https://www150.statcan.gc.ca/t1/wds/rest"


async def get_full_table_csv(product_id: int, language: Optional[str] = "en") -> dict:
    """
    Get download URL for full Statistics Canada table in CSV format.

    Returns a URL to a downloadable ZIP file containing the complete table data.

    :param product_id: The StatsCan product/cube ID (e.g., 14100287)
    :param language: Language code - "en" for English or "fr" for French (default: "en")
    :return: Dictionary with download URL or error details
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{BASE_URL}/getFullTableDownloadCSV/{product_id}/{language}"
            )
            data = response.json()
        return data
    except Exception as e:
        return {
            "error": str(e),
            "hint": "Failed to get CSV download URL from StatsCan API"
        }
