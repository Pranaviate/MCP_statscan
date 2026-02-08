import httpx

BASE_URL = "https://www150.statcan.gc.ca/t1/wds/rest"


async def get_full_table_sdmx(product_id: int) -> dict:
    """
    Get download URL for full Statistics Canada table in SDMX format.

    Returns a URL to a downloadable ZIP file containing the complete table data
    in SDMX (Statistical Data and Metadata eXchange) format. This is a bilingual
    XML format used for international statistical data exchange.

    :param product_id: The StatsCan product/cube ID (e.g., 14100287)
    :return: Dictionary with download URL or error details
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{BASE_URL}/getFullTableDownloadSDMX/{product_id}"
            )
            data = response.json()
        return data
    except Exception as e:
        return {
            "error": str(e),
            "hint": "Failed to get SDMX download URL from StatsCan API"
        }
