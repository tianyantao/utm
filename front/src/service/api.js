import assign from 'object-assign';
import axios from './config';
const IS_MOCK = process.env.NODE_ENV === 'development';
const MOCK_PREFIX = 'http://yapi.235.mistong.com/mock/878';
const IS_SERVER = window.location.host.indexOf('qa.mistong.cn') !== -1;
const SERVER_MID_PATH = IS_SERVER ? '/pytest' : '';
// All http request url;
const URLS = {
  getCurrentEnv: {
    method: 'get',
    url: `${SERVER_MID_PATH}/env/get`,
    mockMethod: 'get',
    mockUrl: `${MOCK_PREFIX}/pytest/env/get`,
  },
  setEnv: {
    method: 'get',
    url: `${SERVER_MID_PATH}/env/set`,
    mockMethod: 'get',
    mockUrl: `${MOCK_PREFIX}/pytest/env/set`,
  },
  Status: {
    method: 'get',
    url: `${SERVER_MID_PATH}/status`,
    mockMethod: 'get',
    mockUrl: `http://yapi.235.mistong.com/mock/878/pytest/status`,
  },
  Monitor: {
    method: 'get',
    url: `${SERVER_MID_PATH}/monitor`,
    mockMethod: 'get',
    mockUrl: 'http://yapi.235.mistong.com/mock/878/pytest/monitor',
  },
  getCaseRunningStatus: {
    method: 'get',
    url: `${SERVER_MID_PATH}/status`,
    mockMethod: 'get',
    mockUrl: `${MOCK_PREFIX}/pytest/status`,
  },
  runCases: {
    method: 'post',
    url: `${SERVER_MID_PATH}/run`,
    mockMethod: 'post',
    mockUrl: `${MOCK_PREFIX}/pytest/run`,
  },
  fetchCaseList: {
    method: 'get',
    url: `${SERVER_MID_PATH}/caselist`,
    mockMethod: 'get',
    mockUrl: `${MOCK_PREFIX}/pytest/caselist`,
  },
  GetCaseListBySuiteId: {
    method: 'get',
    url: `${SERVER_MID_PATH}/suite/case/list`,
    mockMethod: 'get',
    mockUrl: `${MOCK_PREFIX}/pytest/suite/case/list`,
  },
  fetchUrlsList: {
    method: 'get',
    url: `${SERVER_MID_PATH}/urls/list`,
    mockMethod: 'get',
    mockUrl: `${MOCK_PREFIX}/pytest/urls/list`,
  },
  GetSuiteList: {
    method: 'get',
    url: `${SERVER_MID_PATH}/suite/list`,
    mockMethod: 'get',
    mockUrl: `http://yapi.235.mistong.com/mock/1133/suite/list`,
  },
  DeleteCasesFromSuite: {
    method: 'post',
    url: `${SERVER_MID_PATH}/suite/case/delete`,
    mockMethod: 'post',
    mockUrl: `${MOCK_PREFIX}/pytest/suite/case/delete`,
  },
  GetRunDetails: {
    method: 'get',
    url: `${SERVER_MID_PATH}/log/getrundetails`,
    mockMethod: 'get',
    mockUrl: `http://yapi.235.mistong.com/mock/1133/log/getrundetails`,
  },
  GetApiLog: {
    method: 'get',
    url: `${SERVER_MID_PATH}/log/getapilogs`,
    mockMethod: 'get',
    mockUrl: `http://yapi.235.mistong.com/mock/1133/log/getapilogs`,
  },
  GetErrorApiLog: {
    method: 'get',
    url: `${SERVER_MID_PATH}/logs/geterrorapi`,
    mockMethod: 'get',
    mockUrl: `http://localhost:8876/logs/geterrorapi`,
  },
    AddCases2Suite: {
    method: 'post',
    url: `${SERVER_MID_PATH}/suite/case/add`,
    mockMethod: 'post',
    mockUrl: `http://yapi.235.mistong.com/mock/878/pytest/case/add`,
  },
};
const parseOriginUrl = (key) => {
  const {
    method, url, mockUrl, mockMethod,
  } = URLS[key];
  return {
    method: IS_MOCK ? mockMethod || 'get' : method,
    url: IS_MOCK ? mockUrl : url,
  };
};
const api = {};
Object.keys(URLS).forEach((item) => {
  const localItem = parseOriginUrl(item);
  const { method } = localItem;
  switch (String(method).toUpperCase()) {
    case 'POST':
    case 'PUT':
    case 'PATCH':
      api[item] = params => axios(assign({}, localItem, {
        data: params,
      }));
      break;
    default:
      api[item] = params => axios(assign({}, localItem, {
        params,
      }));
  }
});
api.getApiUrl = key => parseOriginUrl(key).url;
export default api;