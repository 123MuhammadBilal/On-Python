from TiktokApi import TiktokApi

verifyfp = "verify_84bdbed22e113e20e58887a31558a80a"

api = TiktokApi.get_instance(custom_verifyfp=verifyfp, use_test_endpoints=True)

tiktoks = api.trending()

for tiktok in tiktoks:
    print(tiktok["author"]["uniqueId"])
