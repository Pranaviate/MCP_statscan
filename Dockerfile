FROM ghcr.io/astral-sh/uv:python3.11-alpine

WORKDIR /app

# Install dependencies first (layer cache)
COPY pyproject.toml uv.lock ./
RUN uv sync --no-dev --frozen

# Copy source code
COPY statscan_mcp/ statscan_mcp/

ENV TRANSPORT=http
ENV PORT=8080
EXPOSE 8080

CMD ["uv", "run", "python", "-m", "statscan_mcp"]
