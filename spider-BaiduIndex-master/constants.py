# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 15:36
# @Author  : Conderfly
# @Email   : coderflying@163.com
# @File    : constants.py

js = '''function decrypt(t, e) {
            for (var n = t.split(""), i = e.split(""), a = {}, r = [], o = 0; o < n.length / 2; o++) a[n[o]] = n[n.length / 2 + o];
            for (var s = 0; s < e.length; s++) r.push(a[i[s]]);
            return r.join("")
        }'''

headers = {
    "Cookie": "BAIDUID=2120A077981BB396E943E18C37052575:FG=1; BIDUPSID=2120A077981BB396E943E18C37052575; PSTM=1574496401; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=7; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1578722705,1578727319; BDUSS=mJTcTVsYVpBZFUzV0w4aGN5TkpyZ35HT01PU1dRWXRYdGFCeElrd1RNfkJCRUZlRUFBQUFBJCQAAAAAAAAAAAEAAABaDIZ-Y3pjaHljaHkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMF3GV7BdxleU; CHKFORREG=0ddcb2d4a4873e804b42286ebb246b3d; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1578727363; H_PS_PSSID=1439_21122_30211_26350_22158",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}
data_url = 'https://index.baidu.com/api/SearchApi/index?word={}&area=0&days=30'
uniqid_url = 'https://index.baidu.com/Interface/ptbk?uniqid={}'
if __name__ == '__main__':
    pass
