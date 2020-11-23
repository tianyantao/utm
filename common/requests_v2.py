# from common.log_upload import api_log
from requests import sessions
from requests.models import Request
import logging
import time
from common.helper import get_mac_address
from common.log_upload import api_log

logging.basicConfig(level='INFO')


class SessionV2(sessions.Session):
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def request(self, method, url,
                params=None, data=None, headers=None, cookies=None, files=None,
                auth=None, timeout=None, allow_redirects=True, proxies=None,
                hooks=None, stream=None, verify=False, cert=None, json=None):
        """Constructs a :class:`Request <Request>`, prepares it and sends it.
        Returns :class:`Response <Response>` object.

        :param method: method for the new :class:`Request` object.
        :param url: URL for the new :class:`Request` object.
        :param params: (optional) Dictionary or bytes to be sent in the query
            string for the :class:`Request`.
        :param data: (optional) Dictionary, bytes, or file-like object to send
            in the body of the :class:`Request`.
        :param json: (optional) json to send in the body of the
            :class:`Request`.
        :param headers: (optional) Dictionary of HTTP Headers to send with the
            :class:`Request`.
        :param cookies: (optional) Dict or CookieJar object to send with the
            :class:`Request`.
        :param files: (optional) Dictionary of ``'filename': file-like-objects``
            for multipart encoding upload.
        :param auth: (optional) Auth tuple or callable to enable
            Basic/Digest/Custom HTTP Auth.
        :param timeout: (optional) How long to wait for the server to send
            data before giving up, as a float, or a :ref:`(connect timeout,
            read timeout) <timeouts>` tuple.
        :type timeout: float or tuple
        :param allow_redirects: (optional) Set to True by default.
        :type allow_redirects: bool
        :param proxies: (optional) Dictionary mapping protocol or protocol and
            hostname to the URL of the proxy.
        :param stream: (optional) whether to immediately download the response
            content. Defaults to ``False``.
        :param verify: (optional) Either a boolean, in which case it controls whether we verify
            the server's TLS certificate, or a string, in which case it must be a path
            to a CA bundle to use. Defaults to ``True``.
        :param cert: (optional) if String, path to ssl client cert file (.pem).
            If Tuple, ('cert', 'key') pair.
        :rtype: requests.Response
        """
        # Create the Request.
        req = Request(
            method=method.upper(),
            url=url,
            headers=headers,
            files=files,
            data=data or {},
            json=json,
            params=params or {},
            auth=auth,
            cookies=cookies,
            hooks=hooks,
        )

        try:  # 预发环境自定义hosts
            from flask import current_app
            from config.config_hosts import HOSTS
            from urllib import parse
            if hasattr(current_app, 'pre'):
                host = parse.urlparse(req.url).netloc
                if host in HOSTS:
                    req.url = req.url.replace(host, HOSTS[host])
                    req.headers['Host'] = host
        except:
            logging.info('非预发环境，跳过hosts切换')

        prep = self.prepare_request(req)

        proxies = proxies or {}

        settings = self.merge_environment_settings(
            prep.url, proxies, stream, verify, cert
        )

        # Send the request.
        send_kwargs = {
            'timeout': timeout,
            'allow_redirects': allow_redirects,
        }
        send_kwargs.update(settings)





        resp = self.send(prep, **send_kwargs)
        try:
            req_body = prep.body
            req_body = req_body if not isinstance(req_body, bytes) else req_body.decode()
            req_body = "" if req_body is None else req_body
            logging.info("{0} {1} {2}".format(prep.method, prep.url, resp.status_code))

            api_log.add_api_records(req_method=prep.method, req_url=resp.url, req_data=req_body,
                                    req_headers=prep.headers, res_status=resp.status_code, res_content=resp.text,
                                    elapsed=resp.elapsed.total_seconds(),
                                    update_time=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),
                                    remark=get_mac_address(), res_headers=resp.headers)
        except Exception as e:
            logging.error("收集api调用日志发生错误！！！ {}".format(e))

        return resp

    def get(self, url, **kwargs):
        r"""Sends a GET request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """

        kwargs.setdefault('allow_redirects', True)
        return self.request('GET', url, **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        r"""Sends a POST request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, bytes, or file-like object to send in the body of the :class:`Request`.
        :param json: (optional) json to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """
        return self.request('POST', url, data=data, json=json, **kwargs)


def session():
    """
    Returns a :class:`Session` for context-management.

    :rtype: Session
    """

    return SessionV2()
