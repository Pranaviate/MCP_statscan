import httpx
from typing import Optional

BASE_URL = "https://www150.statcan.gc.ca/t1/wds/rest"

async def list_cubes(keyword: Optional[str] = None, default_limit: Optional[int] = 50) -> dict:
    """
    Search Statistics Canada datasets by keyword.

    Returns a list of cubes (datasets) from StatsCan. If a keyword is provided,
    filters results by searching in the English dataset titles. Results are limited
    to prevent overwhelming responses.

    :param keyword: Optional search term to filter datasets by title (case-insensitive)
    :type keyword: Optional[str]
    :param default_limit: Maximum number of results to return (default: 50)
    :type default_limit: Optional[int]
    :return: Dictionary with 'cubes' (list of datasets), 'total_count' (total matches),
             and 'returned_count' (number of items returned after limit)
    :rtype: dict
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/getAllCubesListLite")
            data = response.json()

        cubes = []

        if keyword:
            keyword_lower = keyword.lower()
            for cube in data:
                if keyword_lower in cube.get("cubeTitleEn", "").lower():
                    cubes.append(cube)
        else:
             cubes = data
        
        return {
        "cubes": cubes[:default_limit],
        "total_count": len(cubes),
        "returned_count": len(cubes[:default_limit])
        }
    except Exception as e:
            return {
                "error": str(e),
                "hint": "Failed to fetch cubes from StatsCan API"
            }