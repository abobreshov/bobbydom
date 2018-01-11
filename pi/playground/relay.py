import logging
import argparse
import RPi.GPIO as GPIO

pin_constraint = {
    1, 2, 4, 6, 9, 14, 17, 20, 25, 30, 34, 39
}


def main(pin: int, level: bool):
    logging.info(f'Setting GPIO {pin} level: {int(level)}')
    try:
        if pin in pin_constraint:
            logging.error(f'pin {pin} is power or ground. Can\'t set value')
        else:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, level)
        input("Press Enter to continue...")
    except KeyboardInterrupt:
        # here you put any code you want to run before the program
        # exits when you press CTRL+C
        logging.warning("KeyboardInterrupt")
    except:
        # this catches ALL other exceptions including errors.
        # You won't get any error messages for debugging
        # so only use it once your code is working
        logging.error("UnknownError")
    finally:
        GPIO.cleanup()


if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    parser = argparse.ArgumentParser(description='Raspberry PI GPIO management')
    parser.add_argument('--pin', help='pin number not BCM')
    parser.add_argument('--val', help='HIGH or LOW')
    args = vars(parser.parse_args())
    p = int(args['pin'])
    v = bool(int(args['val']))
    main(p, v)
