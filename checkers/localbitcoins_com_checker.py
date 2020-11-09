import aiohttp

from checkers.base_checker import BaseChecker, CheckerResult


class LocalbitcoinsComChecker(BaseChecker):
    def __init__(self, timeout=None):
        super().__init__("https://www.localbitcoins.com/buy-bitcoins-online/.json", timeout=timeout)

    async def validate(self, response: aiohttp.ClientResponse, checker_result: CheckerResult):
        '''
        We have already done the request and it was successful,
        Google returned something(maybe good response, maybe captcha, we don't care)
        '''
        return True
