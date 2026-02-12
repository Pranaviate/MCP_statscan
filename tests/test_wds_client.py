import pytest
from unittest.mock import AsyncMock, patch, MagicMock
from statscan_mcp.providers.wds_client import WDSClient

@pytest.fixture
def client():
    return WDSClient()

async def test_get_request(client):
    # Step 2: tell the fake what to return
    fake_response = MagicMock()
    fake_response.json.return_value = [{"cubeTitleEn": "Test"}]
    with patch.object(client.client, "request", new_callable=AsyncMock, return_value=fake_response): 
        result = await client.get("getAllCubesListLite")
    assert result == [{"cubeTitleEn": "Test"}]


async def test_post_request(client):
    # Step 2: tell the fake what to return
    fake_response = MagicMock()
    fake_response.json.return_value = {"status": "ok"}
    with patch.object(client.client, "request", new_callable=AsyncMock, return_value=fake_response) as mock_request:
        result = await client.post("getCubeMetadata", [{"productId": 18100004}])
    
        mock_request.assert_called_once_with(
            "POST",
            f"{WDSClient.BASE_URL}/getCubeMetadata",
            params=None,
            json=[{"productId": 18100004}],
        )


async def test_exception_request(client):
    with patch.object(client.client, "request", new_callable=AsyncMock, side_effect=Exception("Connection refused")):
        result = await client.get("getAllCubesListLite")
    assert "error" in result
    assert "Connection refused" in result["error"]



