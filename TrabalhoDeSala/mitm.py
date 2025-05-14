from mitmproxy import http
from mitmproxy import ctx

def request(flow: http.HTTPFlow):
    print(f"Interceptando requisição para: {flow.request.host}")
    flow.response = http.HTTPFlow.from_flow(flow)
    flow.response.headers['X-My-Header'] = 'Test'
    flow.response.content = b"HeHe"

def start_proxy():
    ctx.start_tcp_proxy("192.168.0.100", 12345)

start_proxy()