import typer
from bot.orders import place_order
from bot.validators import validate_input
from bot.logging_config import setup_logger
import logging

app = typer.Typer()
setup_logger()

@app.command()
def trade(
    symbol: str = typer.Option(...),
    side: str = typer.Option(...),
    order_type: str = typer.Option(...),
    quantity: float = typer.Option(...),
    price: float = typer.Option(None)
):
    try:
        validate_input(symbol, side, order_type, quantity, price)

        logging.info(f"Placing order: {symbol} {side} {order_type}")

        response = place_order(symbol, side, order_type, quantity, price)

        print("Order Response:", response)
        logging.info(f"Response: {response}")

    except Exception as e:
        print("Error:", e)
        logging.error(str(e))

if __name__ == "__main__":
    app()