from flask_restful import Api
from flask_cors import *
from services.api_resource import *




CORS(app, supports_credentials=True)
api = Api(app)

api.add_resource(CaseList, '/caselist')
api.add_resource(GetEnv, '/env/get')
api.add_resource(SetEnv, '/env/set')
api.add_resource(RunMonitor, '/monitor')
api.add_resource(GetRunDetail, '/log/getrundetails')
api.add_resource(GetApiLogByRunId, '/log/getapilogs')
api.add_resource(Count, '/count')
api.add_resource(Run, '/run')
api.add_resource(GetReportById, '/getreport')
api.add_resource(AddCases2Suite, '/suite/case/add')
api.add_resource(DeleteCaseSuite, '/suite/case/delete')
api.add_resource(UrlsList, '/urls/list')
api.add_resource(Status, '/status')
api.add_resource(SuiteList, '/suite/list')
api.add_resource(CaseListBySuiteId, '/suite/case/list')
api.add_resource(HomeDetail, '/home/detail')


if __name__ == "__main__":
    app.run(debug=True, port=8876, host='0.0.0.0')