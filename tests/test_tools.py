import pytest
from unittest.mock import AsyncMock, patch


# --- list_cubes tests ---

class TestListCubes:
    """Tests for the list_cubes tool (keyword filtering + limit logic)."""

    FAKE_CUBES = [
        {"cubeTitleEn": "Consumer Price Index", "productId": 18100004},
        {"cubeTitleEn": "Labour Force Survey", "productId": 14100287},
        {"cubeTitleEn": "Consumer Confidence", "productId": 99990001},
        {"cubeTitleEn": "GDP at basic prices", "productId": 36100434},
    ]

    @patch("statscan_mcp.tools.list_cubes.client")
    async def test_no_keyword_returns_all(self, mock_client):
        """Without keyword, returns all cubes up to default_limit."""
        mock_client.get = AsyncMock(return_value=self.FAKE_CUBES)
        from statscan_mcp.tools.list_cubes import list_cubes

        result = await list_cubes()

        assert result["total_count"] == 4
        assert result["returned_count"] == 4
        assert len(result["cubes"]) == 4

    @patch("statscan_mcp.tools.list_cubes.client")
    async def test_keyword_filters_results(self, mock_client):
        """Keyword filters cubes by English title (case-insensitive)."""
        mock_client.get = AsyncMock(return_value=self.FAKE_CUBES)
        from statscan_mcp.tools.list_cubes import list_cubes

        result = await list_cubes(keyword="consumer")

        assert result["total_count"] == 2
        titles = [c["cubeTitleEn"] for c in result["cubes"]]
        assert "Consumer Price Index" in titles
        assert "Consumer Confidence" in titles

    @patch("statscan_mcp.tools.list_cubes.client")
    async def test_default_limit_caps_results(self, mock_client):
        """default_limit caps the number of returned cubes."""
        mock_client.get = AsyncMock(return_value=self.FAKE_CUBES)
        from statscan_mcp.tools.list_cubes import list_cubes

        result = await list_cubes(default_limit=2)

        assert result["total_count"] == 4
        assert result["returned_count"] == 2
        assert len(result["cubes"]) == 2

    @patch("statscan_mcp.tools.list_cubes.client")
    async def test_error_passthrough(self, mock_client):
        """When client returns error, tool passes it through."""
        mock_client.get = AsyncMock(return_value={"error": "timeout", "hint": "try again"})
        from statscan_mcp.tools.list_cubes import list_cubes

        result = await list_cubes()

        assert result == {"error": "timeout", "hint": "try again"}

    @patch("statscan_mcp.tools.list_cubes.client")
    async def test_no_matches_returns_empty(self, mock_client):
        """Keyword that matches nothing returns empty list with zero counts."""
        mock_client.get = AsyncMock(return_value=self.FAKE_CUBES)
        from statscan_mcp.tools.list_cubes import list_cubes

        result = await list_cubes(keyword="nonexistent")

        assert result["total_count"] == 0
        assert result["returned_count"] == 0
        assert result["cubes"] == []

    @patch("statscan_mcp.tools.list_cubes.client")
    async def test_keyword_and_limit_combined(self, mock_client):
        """Keyword filters first, then limit caps the filtered results."""
        mock_client.get = AsyncMock(return_value=self.FAKE_CUBES)
        from statscan_mcp.tools.list_cubes import list_cubes

        result = await list_cubes(keyword="consumer", default_limit=1)

        assert result["total_count"] == 2   # 2 match "consumer"
        assert result["returned_count"] == 1  # but limit caps to 1
        assert len(result["cubes"]) == 1


# --- get_cube_metadata tests ---

class TestGetCubeMetadata:
    """Tests for get_cube_metadata (POST, array body)."""

    @patch("statscan_mcp.tools.get_cube_metadata.client")
    async def test_sends_correct_body(self, mock_client):
        """Sends POST with [{"productId": ...}] array body."""
        mock_client.post = AsyncMock(return_value={"status": "ok"})
        from statscan_mcp.tools.get_cube_metadata import get_cube_metadata

        await get_cube_metadata(product_id=18100004)

        mock_client.post.assert_called_once_with(
            "getCubeMetadata", [{"productId": 18100004}]
        )


# --- get_vector_data_by_range tests ---

class TestGetVectorDataByRange:
    """Tests for get_vector_data_by_range (GET, quoted vectorId)."""

    @patch("statscan_mcp.tools.get_vector_data_by_range.client")
    async def test_quotes_vector_id(self, mock_client):
        """vectorId is wrapped in quotes for the API."""
        mock_client.get = AsyncMock(return_value={"data": []})
        from statscan_mcp.tools.get_vector_data_by_range import get_vector_data_by_range

        await get_vector_data_by_range(
            vector_id=41690973, start_date="2020-01-01", end_date="2024-01-01"
        )

        mock_client.get.assert_called_once_with(
            "getDataFromVectorByReferencePeriodRange",
            params={
                "vectorIds": '"41690973"',
                "startRefPeriod": "2020-01-01",
                "endReferencePeriod": "2024-01-01",
            },
        )


# --- get_bulk_vectors tests ---

class TestGetBulkVectors:
    """Tests for get_bulk_vectors (POST, object body, string conversion)."""

    @patch("statscan_mcp.tools.get_bulk_vectors.client")
    async def test_converts_ids_to_strings(self, mock_client):
        """vector_ids are converted from int to str in the request body."""
        mock_client.post = AsyncMock(return_value={"data": []})
        from statscan_mcp.tools.get_bulk_vectors import get_bulk_vectors

        await get_bulk_vectors(
            vector_ids=[74804, 1],
            start_release_date="2020-01-01T08:30",
            end_release_date="2024-12-31T19:00",
        )

        mock_client.post.assert_called_once_with(
            "getBulkVectorDataByRange",
            {
                "vectorIds": ["74804", "1"],
                "startDataPointReleaseDate": "2020-01-01T08:30",
                "endDataPointReleaseDate": "2024-12-31T19:00",
            },
        )


# --- get_vectors_latest tests ---

class TestGetVectorsLatest:
    """Tests for get_vectors_latest (POST, list comprehension body)."""

    @patch("statscan_mcp.tools.get_vectors_latest.client")
    async def test_builds_body_per_vector(self, mock_client):
        """Builds one {vectorId, latestN} entry per vector ID."""
        mock_client.post = AsyncMock(return_value={"data": []})
        from statscan_mcp.tools.get_vectors_latest import get_vectors_latest

        await get_vectors_latest(vector_ids=[32164132, 41690973], latest_n=3)

        mock_client.post.assert_called_once_with(
            "getDataFromVectorsAndLatestNPeriods",
            [
                {"vectorId": 32164132, "latestN": 3},
                {"vectorId": 41690973, "latestN": 3},
            ],
        )


# --- get_changed_cubes tests ---

class TestGetChangedCubes:
    """Tests for get_changed_cubes (GET, date in URL path)."""

    @patch("statscan_mcp.tools.get_changed_cubes.client")
    async def test_date_appended_to_endpoint(self, mock_client):
        """Date is appended to endpoint path (not as query param)."""
        mock_client.get = AsyncMock(return_value=[])
        from statscan_mcp.tools.get_changed_cubes import get_changed_cubes

        await get_changed_cubes(date="2025-02-05")

        mock_client.get.assert_called_once_with("getChangedCubeList/2025-02-05")


# --- get_full_table_csv tests ---

class TestGetFullTableCsv:
    """Tests for get_full_table_csv (GET, productId + language in URL path)."""

    @patch("statscan_mcp.tools.get_full_table_csv.client")
    async def test_default_language_english(self, mock_client):
        """Default language is 'en', appended to URL path."""
        mock_client.get = AsyncMock(return_value={"status": "ok"})
        from statscan_mcp.tools.get_full_table_csv import get_full_table_csv

        await get_full_table_csv(product_id=14100287)

        mock_client.get.assert_called_once_with("getFullTableDownloadCSV/14100287/en")

    @patch("statscan_mcp.tools.get_full_table_csv.client")
    async def test_french_language(self, mock_client):
        """Can request French version."""
        mock_client.get = AsyncMock(return_value={"status": "ok"})
        from statscan_mcp.tools.get_full_table_csv import get_full_table_csv

        await get_full_table_csv(product_id=14100287, language="fr")

        mock_client.get.assert_called_once_with("getFullTableDownloadCSV/14100287/fr")
