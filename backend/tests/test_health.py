from httpx import AsyncClient

from app.main import app


async def test_health_endpoint() -> None:
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.get("/healthz")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
