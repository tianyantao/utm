<template>

    <div>
        <navs></navs>
        <!--<div class="runstatus">-->
        <!--<a style="font-size: 20px; padding-right: 130px;font-weight: bolder;">自动化平台当前状态</a>-->
        <!--<br><br>-->
        <!--<div style="width: 600px; text-align: left;margin: 0 auto">-->
        <!--<div class="left">-->
        <!--<a-progress type="circle" :percent="status.progress"/>-->
        <!--</div>-->
        <!--<div class="right">-->
        <!--<span style="font-size: 18px;">{{status.msg}}</span>-->
        <!--<p style="font-size: 16px;">total:{{status.total}}</p>-->
        <!--<p style="font-size: 16px;">success:{{status.success}} <span style="padding-left: 18px;">fail:{{status.assert_fail}}</span><br>-->
        <!--<span>skipped:{{status.skiped}}</span> <span style="padding-left: 10px;">error:{{status.run_error}}</span></p>-->
        <!--<p><a v-bind:href="status.report_url">点击查看报告</a></p>-->
        <!--</div>-->
        <!--</div>-->
        <!--</div>-->
        <div class="runstatus">
            <div>
             <div style="padding-bottom: 10px;  width: 100%;">
                 <span class="t"><a-switch checked-children="查看全部日志" un-checked-children="查看错误日志" default-checked @change="errorlog" /></span>
                    <a-button type="primary" @click="start('all')" :loading="loading">
                        全量执行
                    </a-button>&nbsp;
                    <a-button type="primary" @click="start('b')" :loading="loading">
                        全量执行B端用例
                    </a-button>&nbsp;
                    <a-button type="primary" @click="start('tiku')" :loading="loading">
                        全量执行tiku用例
                    </a-button>
                    <a-modal title="确认运行环境"
                     style="top: 50px;"
                     :visible="modal1Visible"
                     @ok="handleEditContentOk"
                     @cancel="() => setModal1Visible(false)"
            >
                      <div style="margin-left: 10px; margin-right: 10px; padding: 40px;"><span
                              class="label">当前选择的是：<span style="font-weight: bolder">{{run_env}}</span></span>
                          <br>
                          <span style="padding-right: 10px;">是否切换运行环境</span>
                            <a-select defaultValue="run_env" :value="run_env" style="width: 120px" @change="handleEnvChange2">
                                <a-select-option value="test" disabled>test</a-select-option>
                                <a-select-option value="test1" disabled>test1</a-select-option>
                                <a-select-option value="pre">pre</a-select-option>
                                <a-select-option value="prod">prod</a-select-option>
                            </a-select>
                        </div>
            </a-modal>
                    <div style="float: right; margin-left: 10px;">
                        <div style="float: right; margin-left: 10px; margin-right: 10px; padding-left: 40px;">        <div >
            <span style="font-size: 18px; font-weight: bolder;">当前平台：</span>
            <span v-if = "status.status === 0" style="font-size: 18px;color: green">空闲</span>
            <span v-if = "status.status === 1" style="font-size: 18px;"><span v-if="status.run_type === 0" style="color: red">监控正在运行</span><span v-else style="color: #fa8c16"> 非监控的运行</span> </span>
            <span v-if = "status.status === 2" style="font-size: 18px;color: blue">排队中</span>
                        </div></div>
                        <a-button :disabled="currentStatusBtn"
                                  style="float: right;" type="primary"
                                  :loading="loading"
                                  @click="ChangeStatus">{{currentStatus}}
                        </a-button>
                    </div>
                </div>
            </div>
            <div>
                <a-table
                        :columns="columns"
                        :rowKey="record => record.id"
                        :pagination=false
                        :dataSource="data"
                        :loading="loading"
                        :scroll="{ y: 630 }"
                        size="small"
                        id="record => record.id"
                >
                <span slot="status" slot-scope="text, record" style="padding-left: 15px;">
                    <a-tag :key="record.status"
                         :color="record.status == 'P' ?  'green' : 'red'">
                       {{ record.status == 'P' ?  'Pass' : 'Fail' }}
                     </a-tag></span>
                <span slot="is_monitor" slot-scope="text, record" style="padding-left: 15px;">
                    <a-tag :key="record.is_monitor"
                         :color="record.is_monitor == '1' ?  'cyan' : 'orange'">
                       {{ record.is_monitor == '1' ?  '是' : '否' }}
                     </a-tag></span>
                 <span slot="action" slot-scope="text, record">
                          <a @click="toApilogs(record.id, record.status, record.title)"> 查看详情</a>
                 </span>
                </a-table>
            </div>
        </div>
    </div>
</template>
<script>
    import api from '~/service'
    const columns = [
        {
            title: 'ID',
            dataIndex: 'id',
            width: '5%',
        },
        {
            title: '用例名称',
            dataIndex: 'test_method_name',
            width: '10%',
        },
        {
            title: '用例标题',
            dataIndex: 'title',
            width: '10%',
        },
        {
            title: 'url',
            dataIndex: 'url',
            width: '15%',
        },
        {
            title: '作者',
            dataIndex: 'author',
            width: '5%',
        },
        {
            title: '执行结果',
            dataIndex: 'status',
            scopedSlots: {customRender: 'status'},
            width: '5%',
        },
        {
            title: '用时',
            dataIndex: 'elapsed',
            width: '3%',
        },
        {
            title: '执行时间',
            dataIndex: 'update_time',
            width: '7%',
        },
        {
            title: '是否监控',
            dataIndex: 'is_monitor',
            scopedSlots: {customRender: 'is_monitor'},
            width: '5%',
        },
        {
            title: '操作',
            dataIndex: 'action',
            scopedSlots: {customRender: 'action'},
            width: '5%',
        },
    ]
    export default {
        name: 'NavPage',
        mounted() {
            this.getStatus(); //监控状态
            this.fetchEnv();
            this.getRunDetails(0,20);
            this.getReportid(0);
            // setInterval(() => {
            //     this.getdetails();
            // }, 5000);
        },
        data() {
            return {
                data: [],
                loading: false,
                child_loading: false,
                apidata: [],
                errordata: [],
                status: [],
                columns,
                currentStatus: '正在获取中',
                env: 'test', //全局环境
                currentStatusBtn: false,
                suite: "all",
                run_env: 'test', //手动执行时选择环境
                modal1Visible: false ,//设置运行环境对话框隐藏
                reportids:["j.0"],
            };
        },
        methods: {
            getReportid(reportid){  //运行日志&状态
                 api.Status({reportid:reportid}).then(data => {
                     this.status = data;
                }).catch(e => {
                    console.error(e);
                });
            },
            getStatus() {
                api.Status({reportid:0}).then(data => {
                    this.currentStatus = true;
                    if(data.status === 1 && data.run_type === 0){
                        this.currentStatus = "停止监控";
                    }else{
                        this.currentStatus = "开启监控";
                    }
                }).catch(e => {
                    console.error(e);
                });
            },
            ChangeStatus() {
                const startValue = {}
                if (this.currentStatus === "开启监控") {
                    startValue.start = 1;
                }else{
                    startValue.start = 0;
                }
                api.Monitor(startValue).then(data => {
                    this.$message.destroy();
                    if(data && data.code != 200){
                        this.$message.info(`失败，请重试`, 1);
                        this.currentStatus = startValue.start === 0 ? "停止监控" : "开启监控";
                    }else{
                        this.$message.success(`成功`, 1);
                        this.currentStatus = startValue.start === 1 ? "停止监控" : "开启监控";
                    }
                }).catch(e => {
                    this.$message.destroy()
                    this.$message.error(e.msg, 2)
                });
            },
            fetchEnv() {
                const self = this;
                api.getCurrentEnv().then(function (data) {
                    self.env = data;
                    self.run_env = data;
                });
            },

            handleEnvChange2(v) {
                this.run_env = v;
            },
            start(suite) {
                this.modal1Visible = true;
                this.suite = suite;
            },
            setModal1Visible(modal1Visible) {
                this.modal1Visible = modal1Visible;
            },
            handleEditContentOk(){
                this.modal1Visible = false;
                this.$message.loading('加入运行队列中...', 0)
                api.runCases({
                    suite: this.suite,
                    env: this.run_env
                }).then(data =>{
                    this.$message.destroy();
                    // this.reportids.push(this.suite + "." + data);
                    this.$message.success('已加入队列。reportid:'+data, 5)
                    let routerJump = this.$router.resolve({name:'runningResult', query:{reportid: data}});
                    window.open(routerJump.href, '_blank')
                }).catch(e => {
                    this.$message.destroy();
                    this.$message.error((e && e.msg) || '加入队列失败', 5)
                });
            },
            errorlog(checked){ //切换全部运行日志 与 仅查看错误日志
                if (checked == 0){
                    this.getRunDetails(1, 20);
                }else{
                    this.getRunDetails(0, 20);
                }
            },
            getRunDetails(s, limit) {
                this.loading = true;
                api.GetRunDetails({
                    status: s,
                    limit: limit
                }).then(data => {
                    this.loading = false
                    this.data = data
                })
            },
            toApilogs(run_id, run_result, run_title){
                let routerJump = this.$router.resolve({ name: 'apiLogs', query: { run_id: run_id , run_result: run_result, run_title: run_title}});
                window.open(routerJump.href, '_blank');
            },
        },
    };
</script>
<style>
    .runstatus {
        background-color: #f9f0ff;
        padding-top: 20px;
        margin-left: 50px;
        margin-top: 30px;
        margin-right: 50px;
        text-align: center;
        height: 250px;
    }
    .t{
        float: left;
    }
    .left {
        float: left;
        width: 400px;
        padding-bottom: 10px;
    }
    .right {
        margin-left: 200px;
        padding-bottom: 10px;
        text-align: left;
        /*background-color: #8cc8ff;*/
    }
    div#rundetails {
        /*margin: 100px;*/
        width: 1000px;
        padding: 60px;
        height: 800px;
    }
    div#apilogs {
        width: 1000px;
        padding: 60px;
        height: 800px;
        position: absolute;
        right: 0px;
    }
    .column {
        float: left;
        width: 50%;
    }
    /*ul {*/
    /*    font-style: oblique;*/
    /*}*/
</style>