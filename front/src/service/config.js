import axios from 'axios';
import assign from 'object-assign';

// 创建axios实例
axios.defaults.headers['Content-Type'] = 'application/json; charset=UTF-8';
const service = axios.create();
// Axios request拦截器
service.interceptors.request.use((config) => {
  const { params, data, method } = config;
  switch (String(method).toUpperCase()) {
    case 'POST':
    case 'PUT':
    case 'PATCH':
      config.data = assign((data || {}));
      break;
    default:
      config.params = assign((params || {}));
  }

  return config;
}, (error) => {
  // Do something with request error
  console.error(error); // for debug
});


// Axios respone拦截器
service.interceptors.response.use((response) => {
  const res = response.data;
  const req = response.config;
  const { data, msg, code } = res;
  const { url } = req;
  // code 2xx: http request successfully;
  if (Number(res.code) === 200) {
    return data;
  }
  if (String(res.code).indexOf('2') === 0) {
    return res;
  }
  console.error(`
      XHR request error, the request url is ${url},
      code is ${code},
      msg is ${msg}`);
  return Promise.reject(res);
}, (error) => {
  Promise.reject(error);
});

export default service;
