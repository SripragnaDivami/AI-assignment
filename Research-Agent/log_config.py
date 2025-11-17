import logfire
import logging
import os
from dotenv import load_dotenv

def configure_logfire():
    """Initialize and configure Logfire with safe fallbacks."""
    load_dotenv()

    logfire_token = os.getenv("LOGFIRE_TOKEN")

    try:
        if logfire_token:
            # Use token from environment
            logfire.configure(token=logfire_token)
            logging.info("Logfire configured using LOGFIRE_TOKEN")
        else:
            # Try stored credentials (from `logfire auth`)
            logfire.configure()
            logging.info("Logfire configured using stored auth")
    except Exception as e:
        # Fallback to local-only logging
        logfire.configure(send_to_logfire=False)
        logging.warning(f"Logfire auth failed: {e}. Using local-only logging.")

    # Python logging config
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    logging.getLogger("pydantic_ai").setLevel(logging.DEBUG)
    logging.getLogger("httpx").setLevel(logging.INFO)
    logging.getLogger("httpcore").setLevel(logging.INFO)

    logging.info("Logfire initialization complete (no asyncio/httpx instrumentation required).")
