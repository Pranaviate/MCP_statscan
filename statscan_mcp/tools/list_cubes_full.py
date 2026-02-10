from typing import Optional
from statscan_mcp.providers.wds_client import WDSClient

client = WDSClient()


async def list_cubes_full(keyword: Optional[str] = None, default_limit: Optional[int] = 50) -> dict:
    """
    Search Statistics Canada datasets by keyword (full metadata).

    Returns a list of cubes with complete metadata including dimensions,
    frequencies, and survey information. Use list_cubes for a lightweight
    version with minimal fields.

    :param keyword: Optional search term to filter datasets by title (case-insensitive)
    :type keyword: Optional[str]
    :param default_limit: Maximum number of results to return (default: 50)
    :type default_limit: Optional[int]
    :return: Dictionary with 'cubes' (list of datasets), 'total_count' (total matches),
             and 'returned_count' (number of items returned after limit)
    :rtype: dict
    """
    data = await client.get("getAllCubesList")

    if "error" in data:
        return data

    if keyword:
        keyword_lower = keyword.lower()
        cubes = [cube for cube in data if keyword_lower in cube.get("cubeTitleEn", "").lower()]
    else:
        cubes = data

    return {
        "cubes": cubes[:default_limit],
        "total_count": len(cubes),
        "returned_count": len(cubes[:default_limit])
    }
