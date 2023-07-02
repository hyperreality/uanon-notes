pt = """----GEB-P NIS PGENGIEM DGASS---EH
--:hsaAHS 
215878
c86eadfe40735b822bc7633259a75aebe973923f1ba7f23742a8e0f2065a37db0146cce136fb4548d198c2768c036ab49c15417d2d7b3e73707b0bd9ad27d8d33888718748c9009852594c187b01fccba3bde93329a147a575b640f9d28abf2a31a5cf2420f71590b9e2f9325ae6d71e97646bd66080fb4fb805b2fffa5492b595e4dc706eed609663711b477d11d4181766803c03f9d06a6f873cb4ad76bf9288e0756324612d36390ad3d423511da435bb079b43d82356b4616a07ad55d884cc135aaa9db418073d807f11b61ce0105c18f54cac37f73a279794c8060683396c7d7814831a5c9106af0e92ce91d331a71cf473105366d6a60fa5e93ae81214b3130f75cd6996668996812a895862632596ad0d7dac6eaa690cd2f055163847d251eec811daaef6fad26cfd2eef45a99205dd6c74dbbb66f6ef6604d2008fe0db91217d9033abeddeb1db27c7da3a2bc41b59ca0784cb13d4f24c4e71edfd0d58d95554a4f14b98a46d0845a36486f8c5757c6b19872e2db09f465e34af07471a5e5e08695e1176cef174b224938f4fbd473ac693728295f69bef9b74d2c7770a6a543463b954f94e48c6ebf87ac3c9c6625f093b5d22ec0786088d6003accf8486c933a160a2968902efe7b03300902e517dd3ac843af93ca41a1a998829d9e1d9f16eb4a79d41b23713a99891ed3f2c191af5e29b034978c98e6b5ef1e08f82921f9e4777875afccdd163ab4dbd34f3f45b9b8ef2f5dd183e3d43ac168070d731638741ab8865409daeadf45248f12c759f69180e0aa852ebb559915ace761bfe0c7b60a04ce3d5e1477a4c6928f592324485beedcb63d0258af5d3688ee6102a2bfb2927fa4c5725cd674b03e46fa206a74b222f6c2e466837b1f9124d87b50223da36a9a384b21949e41d9a1f93b33fe474fc5e2704e62ee84089a5d1cb28dfe8dbbb2dbf4f912844e49e0f24c162501db3857501a679692bf7d5143007465efb300d8a269f059ddf2a2e9ff56f4c8f92b3897faf6315d776083bdd6395f7faa3545c4cecbdeeb23def125757b7d440dd4179a5bc440d035e03942787be158be57a93861aaf3e155e9a03f60fc2923196322b89497c7078982ac20fd8e82bf133d51623f5a1fc565097122b0ec8c2eb61cec8176dd5c3efd1daadc29227c2d926658c2b128a0d6b65d75d8b7dc77597c3efccc2964d0d697cf426cd6f55192f00818c690b29a175920130088e4bd40a3d4135459544d14d69c338ac4b70b97c8122be29ec1e48c69318d6fc6618e622c41c5de9ac5aa49097b366b3fd608ba59f38769bf72ad6dfb10c0e89b8980cc846dac8a28e2cd2fa9290976a761b60ad780e472c138053b89006ccb90842324ac06b986505f87ebaca266048��
9"""

with open("1_img.jpg", "rb") as f:
    bla = f.read()

# pt = "cfdef896"
pt = bla

out = bytearray()
for i, x in enumerate(pt):
    if i % 4 == 0:
        try:
            out.append(pt[i+3])
        except IndexError:
            pass
        try:
            out.append(pt[i+2])
        except IndexError:
            pass
        try:
            out.append(pt[i+1])
        except IndexError:
            pass
        try:
            out.append(pt[i])
        except IndexError:
            pass

print(out)

with open("out.jpg", "wb") as f:
    f.write(out)
