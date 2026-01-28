# MCP Trading Platform

A multi-agent AI trading platform that enables autonomous trading agents to make investment decisions, execute trades, and manage portfolios using the Model Context Protocol (MCP).

## Overview

This system implements a sophisticated trading simulation where multiple AI agents with distinct personas and strategies autonomously research opportunities, analyze market conditions, and execute trades. The platform features a modular architecture using MCP for service communication, real-time market data integration, and a web-based dashboard for monitoring trader performance.

## Features

- 🤖 **Multi-Agent System**: Multiple autonomous trading agents with unique personas (Warren Patience, George Bold, Ray Systematic, Cathie Crypto)
- 📊 **Real-Time Market Data**: Integration with Polygon.io API for stock price data (supports free, paid, and realtime tiers)
- 💼 **Portfolio Management**: Complete account system with balance tracking, holdings, and transaction history
- 🔍 **Research Capabilities**: Web search and research tools powered by Brave Search API
- 📈 **Live Dashboard**: Gradio-based web interface with real-time portfolio visualization and activity logs
- 🧠 **Multiple LLM Support**: Compatible with OpenAI, DeepSeek, Google Gemini, and Grok models
- 💾 **Persistent Storage**: SQLite database for accounts, transactions, logs, and market data caching
- 🔔 **Notifications**: Push notification support via Pushover integration
- 📝 **Comprehensive Logging**: Detailed activity tracing and logging system

## Architecture

The system follows a modular design with the following components:

```
┌─────────────────┐
│  Scheduler      │
│ (trading_floor) │
└────────┬────────┘
         │
         ├─── Creates Traders
         │
         ▼
┌─────────────────┐
│  Trader Agent   │
│  (traders.py)   │
└────────┬────────┘
         │
         ├─── Connects to MCP Servers
         │
         ▼
┌─────────────────────────────────────┐
│         MCP Servers                  │
│  ┌──────────────┐  ┌──────────────┐ │
│  │ Accounts     │  │ Market Data  │ │
│  │ Server       │  │ Server       │ │
│  └──────────────┘  └──────────────┘ │
│  ┌──────────────┐  ┌──────────────┐ │
│  │ Push         │  │ Researcher   │ │
│  │ Notifications│  │ (Web Search) │ │
│  └──────────────┘  └──────────────┘ │
└─────────────────────────────────────┘
         │
         ├─── Executes Trades
         │
         ▼
┌─────────────────┐
│   Database      │
│  (accounts.db)  │
└────────┬────────┘
         │
         ├─── Stores State
         │
         ▼
┌─────────────────┐
│  Web Dashboard  │
│    (app.py)     │
└─────────────────┘
```

## Prerequisites

- Python 3.12 or higher
- `uv` package manager (recommended) or `pip`
- Node.js and npm (for MCP servers that require them)
- API keys for:
  - Polygon.io (for market data)
  - LLM provider (OpenAI)
  - Brave Search API (for research)
  - Pushover (for notifications)

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Mcp_trading
   ```

2. **Install dependencies using uv** (recommended):
   ```bash
   uv sync
   ```

   Or using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root with the following variables:

   ```env
   # Market Data
   POLYGON_API_KEY=your_polygon_api_key
   POLYGON_PLAN=free  # Options: free, paid, realtime

   # LLM Providers (at least one required)
   OPENAI_API_KEY=your_openai_key

   # Research 
   BRAVE_API_KEY=your_brave_api_key

   # Notifications 
   PUSHOVER_USER=your_pushover_user
   PUSHOVER_TOKEN=your_pushover_token

   # Trading Configuration
   RUN_EVERY_N_MINUTES=60
   RUN_EVEN_WHEN_MARKET_IS_CLOSED=false
   USE_MANY_MODELS=false
   ```

4. **Initialize the database**:
   The database will be created automatically on first run, or you can use the setup notebooks:
   ```bash
   jupyter notebook set_up_accouts.ipynb
   ```

## Usage

### Starting the Trading Floor

Run the scheduler to start the trading agents:

```bash
uv run trading_floor.py
```

Or with Python:
```bash
python trading_floor.py
```

The scheduler will:
- Create trader instances with assigned personas
- Execute trades at the configured interval (default: every 60 minutes)
- Log all activities to the database

### Launching the Web Dashboard

In a separate terminal, start the Gradio dashboard:

```bash
uv run app.py
```

Or:
```bash
python app.py
```

The dashboard will open in your browser, showing:
- Real-time portfolio values for each trader
- Portfolio value time series charts
- Current holdings and recent transactions
- Live activity logs

### Configuration Options

Environment variables control system behavior:

- `RUN_EVERY_N_MINUTES`: Trading execution interval (default: 60)
- `RUN_EVEN_WHEN_MARKET_IS_CLOSED`: Allow trading outside market hours (default: false)
- `USE_MANY_MODELS`: Use diverse LLM models vs. single model (default: false)

## Project Structure

```
Mcp_trading/
├── accounts.py              # Account management and portfolio operations
├── accounts_client.py       # MCP client for account operations
├── accounts_server.py       # MCP server exposing account tools
├── app.py                   # Gradio web dashboard
├── database.py              # SQLite database operations
├── market.py                # Market data integration (Polygon.io)
├── market_server.py         # MCP server for market data
├── mcp_params.py            # MCP server configuration
├── push_server.py           # Push notification MCP server
├── templates.py             # Agent instructions and prompts
├── traders.py               # Trader agent implementation
├── trading_floor.py         # Scheduler and orchestration
├── tracers.py               # Logging and tracing system
├── util.py                  # Utility functions
├── accounts.db              # SQLite database
├── memory/                   # Trader-specific memory databases
│   ├── Warren.db
│   ├── George.db
│   ├── Ray.db
│   └── Cathie.db
├── Notebooks/               # Setup and analysis notebooks
│   ├── setup_gpt.ipynb
│   ├── setup_polygon.ipynb
│   └── set_up_accouts.ipynb
├── pyproject.toml           # Project dependencies
├── requirements.txt         # Python dependencies
└── SYSTEM_IMPLEMENTATION.md # Detailed system documentation
```

## Core Components

### Trading Agents (`traders.py`)
Autonomous AI agents that:
- Connect to MCP servers for tools and resources
- Research opportunities using web search
- Analyze market conditions
- Execute buy/sell trades
- Maintain investment strategies

### Account Management (`accounts.py`)
Portfolio management system with:
- Cash balance tracking
- Stock holdings management
- Transaction history
- Portfolio valuation
- Profit/loss calculation

### Market Data (`market.py`)
Stock price data integration:
- Polygon.io API integration
- Market hours detection
- Price caching
- Fallback to random prices for testing

### Web Dashboard (`app.py`)
Real-time monitoring interface:
- Portfolio value visualization
- Holdings and transactions display
- Activity log viewer
- Auto-refreshing updates

## Trading Agents

The system includes four pre-configured trading agents:

1. **Warren Patience**: Long-term, value-focused investment strategy
2. **George Bold**: Aggressive, risk-taking approach
3. **Ray Systematic**: Quantitative, systematic trading
4. **Cathie Crypto**: Cryptocurrency-focused strategy

Each agent maintains its own account, strategy, and decision-making process.

## MCP Servers

The system uses Model Context Protocol (MCP) for modular service communication:

**Trader MCP Servers**:
- `accounts_server.py`: Portfolio operations (buy/sell, balance, holdings)
- `push_server.py`: Notification system
- `market_server.py`: Stock price lookups

**Researcher MCP Servers**:
- `mcp-server-fetch`: Web page retrieval
- `@modelcontextprotocol/server-brave-search`: Web search
- `mcp-memory-libsql`: Persistent knowledge graph

## Database Schema

The SQLite database (`accounts.db`) contains:

- **accounts**: Account state (name, JSON account data)
- **logs**: Activity logs (timestamp, type, message)
- **market**: Cached market data by date

## Development

### Adding New Traders

Edit `trading_floor.py` to add new traders:

```python
names = ["Warren", "George", "Ray", "Cathie", "YourTrader"]
lastnames = ["Patience", "Bold", "Systematic", "Crypto", "YourPersona"]
```

### Adding New MCP Servers

Configure in `mcp_params.py`:

```python
trader_mcp_server_params = [
    {"command": "uv", "args": ["run", "your_server.py"]},
    # ... existing servers
]
```

### Customizing Agent Instructions

Modify prompts in `templates.py` to change agent behavior and strategies.

## Limitations

- **Simulation Environment**: Paper trading only, not connected to real brokerage
- **Market Data**: Free tier provides end-of-day prices only
- **Single Instance**: SQLite limits to single-machine deployment
- **LLM Dependency**: Trading decisions depend on LLM reasoning quality

## Troubleshooting

### Market Data Issues
- Verify `POLYGON_API_KEY` is set correctly
- Check API rate limits and subscription tier
- System falls back to random prices if API unavailable

### MCP Server Errors
- Ensure Node.js is installed for servers requiring `npx`
- Check that all required environment variables are set
- Review server logs for connection issues

### Database Errors
- Ensure write permissions in project directory
- Check disk space availability
- Database is created automatically on first run

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Add your license here]

## Acknowledgments

- Built with [AutoGen AgentChat](https://github.com/microsoft/autogen)
- Uses [Model Context Protocol](https://modelcontextprotocol.io/)
- Market data provided by [Polygon.io](https://polygon.io/)

## Documentation

For detailed system implementation details, see [SYSTEM_IMPLEMENTATION.md](SYSTEM_IMPLEMENTATION.md).

