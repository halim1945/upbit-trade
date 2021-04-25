import pyupbit

access = "9CjrtmUNJTSae14W2odPwRMLlr0YXFwJQhKvazKL"          # 본인 값으로 변경
secret = "NKMEeUqBEDIRFgfpYAoZj5qKOiGpikkleOrNjyud"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-DOGE"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회