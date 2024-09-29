# log_config.py
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log message format
    handlers=[
        logging.FileHandler('app.log'),  # Log messages will be written to this file
        logging.StreamHandler()  # Log messages will also be printed to console
    ]
)

def example_function():
    """Example function to demonstrate logging."""
    try:
        logging.info("Function execution started.")
        # Your processing logic here
        result = 1 / 0  # This will raise a ZeroDivisionError
        logging.info("Function executed successfully.")
    except ZeroDivisionError as e:
        logging.error(f"An error occurred: {e}")
    finally:
        logging.info("Function execution finished.")

if __name__ == "__main__":
    logging.info("Application started.")
    example_function()
    logging.info("Application finished.")
