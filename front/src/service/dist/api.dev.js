"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports["default"] = void 0;

var _objectAssign = _interopRequireDefault(require("object-assign"));

var _config = _interopRequireDefault(require("./config"));

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { "default": obj }; }

var IS_MOCK = process.env.NODE_ENV === 'development';
var MOCK_PREFIX = 'http://yapi.235.mistong.com/mock/878';
var IS_SERVER = window.location.host.indexOf('qa.mistong.cn') !== -1;
var SERVER_MID_PATH = IS_SERVER ? '/pytest' : ''; // All http request url;

var URLS = {
  getCurrentEnv: {
    method: 'get',
    url: "".concat(SERVER_MID_PATH, "/getenv"),
    mockMethod: 'get',
    mockUrl: "".concat(MOCK_PREFIX, "/pytest/getenv")
  },
  setEnv: {
    method: 'get',
    url: "".concat(SERVER_MID_PATH, "/setenv"),
    mockMethod: 'get',
    mockUrl: "".concat(MOCK_PREFIX, "/pytest/setenv")
  },
  Status: {
    method: 'get',
    url: "".concat(SERVER_MID_PATH, "/status"),
    mockMethod: 'get',
    mockUrl: "".concat(MOCK_PREFIX, "/pytest/status")
  },
  Monitor: {
    method: 'get',
    url: "".concat(SERVER_MID_PATH, "/monitor/start"),
    mockMethod: 'get',
    mockUrl: 'http://yapi.235.mistong.com/mock/1133/pytest/monitor/start'
  },
  setMonitorlist: {
    method: 'get',
    url: "".concat(SERVER_MID_PATH, "/setmonitorlist"),
    mockMethod: 'get',
    mockUrl: "".concat(MOCK_PREFIX, "/pytest/setmonitorlist")
  },
  getCaseRunningStatus: {
    method: 'get',
    url: "".concat(SERVER_MID_PATH, "/status"),
    mockMethod: 'get',
    mockUrl: "".concat(MOCK_PREFIX, "/pytest/status")
  },
  runCases: {
    method: 'post',
    url: "".concat(SERVER_MID_PATH, "/run"),
    mockMethod: 'post',
    mockUrl: "".concat(MOCK_PREFIX, "/pytest/run")
  },
  fetchCaseList: {
    method: 'get',
    url: "".concat(SERVER_MID_PATH, "/caselist"),
    mockMethod: 'get',
    mockUrl: "".concat(MOCK_PREFIX, "/pytest/caselist")
  },
  fetchUrlsList: {
    method: 'get',
    url: "".concat(SERVER_MID_PATH, "/getallurls"),
    mockMethod: 'get',
    mockUrl: "".concat(MOCK_PREFIX, "/pytest/getallurls")
  },
  GetSuiteList: {
    method: 'get',
    url: "".concat(SERVER_MID_PATH, "/suite/list"),
    mockMethod: 'get',
    mockUrl: "http://yapi.235.mistong.com/mock/1133/suite/list"
  },
  CaseListBySuiteId: {
    method: 'get',
    url: "".concat(SERVER_MID_PATH, "/suite/case/list"),
    mockMethod: 'get',
    mockUrl: "http://yapi.235.mistong.com/mock/1133/suite/case/list"
  },
  DeleteCasesFromSuite: {
    method: 'post',
    url: "".concat(SERVER_MID_PATH, "/suite/case/delete"),
    mockMethod: 'post',
    mockUrl: "http://yapi.235.mistong.com/mock/1133/suite/case/delete"
  }
};

var parseOriginUrl = function parseOriginUrl(key) {
  var _URLS$key = URLS[key],
      method = _URLS$key.method,
      url = _URLS$key.url,
      mockUrl = _URLS$key.mockUrl,
      mockMethod = _URLS$key.mockMethod;
  return {
    method: IS_MOCK ? mockMethod || 'get' : method,
    url: IS_MOCK ? mockUrl : url
  };
};

var api = {};
Object.keys(URLS).forEach(function (item) {
  var localItem = parseOriginUrl(item);
  var method = localItem.method;

  switch (String(method).toUpperCase()) {
    case 'POST':
    case 'PUT':
    case 'PATCH':
      api[item] = function (params) {
        return (0, _config["default"])((0, _objectAssign["default"])({}, localItem, {
          data: params
        }));
      };

      break;

    default:
      api[item] = function (params) {
        return (0, _config["default"])((0, _objectAssign["default"])({}, localItem, {
          params: params
        }));
      };

  }
});

api.getApiUrl = function (key) {
  return parseOriginUrl(key).url;
};

var _default = api;
exports["default"] = _default;