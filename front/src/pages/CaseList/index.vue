<template>
    <div>
        <navs></navs>
        <div class="container case-list">
            <div style="margin-bottom: 16px;">
                <a-modal title="添加所选case到suite"
                         style="bottom: 50px;"
                         :visible="modal1Visible"
                         @ok="handleEditContentOk"
                         @cancel="() => setModal1Visible(false)"
                >
                    <a-radio-group @change="onChange" style="width:500px">
                        <a-row>
                            <a-col :span="10" v-for="item in options" v-bind:key="item.suite_id">
                                <a-radio :value="item.suite_id" style="padding-left: 5px">{{item.suite_name }}</a-radio>
                            </a-col>
                        </a-row>
                    </a-radio-group>
                </a-modal>&nbsp;

                <span style="padding-left: 10px"><a-input-search v-model="id_input" placeholder="关键字搜索" @change="onInputChange"
                                                          style="width: 200px;"/></span>
                <span style="padding-left: 1%">
                <a-select style="width: 150px" @change="(v) => { getCaselistBysuite(v) }" default-value="1000">
                <a-select-option value="1000">
                    根据suite筛选
                </a-select-option>
                <a-select-option v-for="item in options" v-bind:key="item.suite_id">
                     {{item.suite_name}}
                </a-select-option>
        </a-select></span>
            </div>
            <a-table
                    :columns="columns"
                    :rowKey="record => record.case_id"
                    :dataSource="data"
                    :pagination="pagination"
                    :loading="loading"
                    @change="handleTableChange2"
                    size="small"
                    :rowSelection="{selectedRowKeys: selectedRowKeys, onChange: onSelectChange}"
                    :scroll="{ y: 630 }"
            >
                <template slot="name" slot-scope="name">
                    {{name.first}} {{name.last}}
                </template>
                <span slot="suits" slot-scope="text, record">
                    <span v-if="searchSuiteId != 1000">
                        <span v-for="suite in options" v-bind:key="suite.suite_id">{{suite.suite_id == searchSuiteId ? suite.suite_name +" "  : ""}}</span>
                    </span>
                    <span v-else>
                        <span v-if="record.suite_ids === null">
                            <span>未设置</span>
                        </span>
                        <span v-else>
                            <span v-if="((record.suite_ids).indexOf(',') >= 1)">
                                <span>{{suite.suite_id == record.suite_ids ? suite.suite_name +" "  : ""}}</span>
                            </span>
                            <span v-else>
                                <span v-for="suite_id in (record.suite_ids).split(',')" v-bind:key="suite_id">
                                    <span v-for="suite in options" v-bind:key="suite.suite_id">{{suite.suite_id == suite_id ? suite.suite_name +" "  : ""}}</span>
                                </span>
                            </span>
                        </span>
                    </span>
                </span>
                <span slot="action2" slot-scope="text, record">
            <!--<a v-for="item in record.suite_ids" v-bind:key="item.suite_id" style="padding-left: 10px" >{{item.suite_name}}</a>-->
            <a-select style="width: 120px"
                      @change="(v) => { addCase(v, record.case_id) }" default-value="1000">
                <a-select-option value="1000">
                    请选择
                </a-select-option>
                <a-select-option v-for="item in options" v-bind:key="item.suite_id">
                     {{item.suite_name}}
                </a-select-option>
                <a-select-option value="0">
                    移除
                </a-select-option>
        </a-select>
        </span>
                <span slot="action" slot-scope="text, record">
                <a-button @click=run(record.case_id)>执行</a-button></span>
            </a-table>
            <a-modal title="确认运行环境"
                     style="top: 50px;"
                     :visible="modal1Visible2"
                     @ok="handleEditContentOk2"
                     @cancel="() => setModal1Visible2(false)"
            >
                <div style="margin-left: 10px; margin-right: 10px; padding: 40px;"><span
                        class="label">当前选择的是：<span style="font-weight: bolder">{{run_env}}</span></span>
                    <br>
                    <span style="padding-right: 10px;">是否切换运行环境</span>
                    <a-select defaultValue="run_env" :value="run_env" style="width: 120px" @change="handleEnvChange3">
                        <a-select-option value="test" disabled>test</a-select-option>
                        <a-select-option value="test1" disabled>test1</a-select-option>
                        <a-select-option value="pre">pre</a-select-option>
                        <a-select-option value="prod">prod</a-select-option>
                    </a-select>
                </div>
            </a-modal>
        </div>
        <a-drawer
                placement="bottom"
                :closable="false"
                :mask="false"
                height="70"
                :visible="true"
        >
            <div style="float: right;margin-right: 50%">
                <span style="font-size: 16px">已选择了 <span
                        style="color:red;">{{`${selectedRowKeys.length}`}}</span> 个用例</span>
                <span style="margin: 20px">
                     <a-button type="primary" @click="openSuite()" :disabled="!hasSelected" :loading="loading">
                         批量添加到suit
                     </a-button>
                </span>
                <a-button type="primary" @click="run(-1)" :disabled="!hasSelected" :loading="loading">
                    批量执行
                </a-button>
            </div>
        </a-drawer>
    </div>
</template>
<script>
    import api from '~/service'
    import AInputSearch from "ant-design-vue/es/input/Search";
    // import moment from 'moment'
    const columns = [
        {
            title: 'ID',
            dataIndex: 'case_id',
            sorter: true,
            width: '5%',
        },
        {
            title: '用例名称',
            dataIndex: 'test_method_name',
            sorter: true,
            width: '15%',
        },
        {
            title: '用例标题',
            dataIndex: 'title',
            sorter: true,
            width: '20%',
        },
        {
            title: '作者',
            dataIndex: 'author',
            sorter: true,
            width: '5%',
            scopedSlots: {customRender: 'author'},
        },
        {
            title: 'URL',
            dataIndex: 'url',
            sorter: true,
            width: '25%',
        },
        {
            title: '所在suite',
            dataIndex: '',
            sorter: true,
            scopedSlots: {customRender: 'suits'},
            width: '13%',
        },
        {
            title: '添加到suite',
            dataIndex: 'action2',
            scopedSlots: {customRender: 'action2'},
            width: '10%',
        },
        {
            title: '操作',
            dataIndex: 'action',
            scopedSlots: {customRender: 'action'},
            width: '5%',
        },
    ]
    export default {
        name: 'CaseList',
        components: {AInputSearch},
        mounted() {
            this.getsuitlist()
            this.fetch()
        },
        data() {
            return {
                checked: "", //已选中项
                options: [], //选项
                data: [],
                pagination: {
                    total: 0,
                    pageSize: 100,
                    showTotal: total => `共有 ${total} 条数据`,
                },
                loading: false,
                columns,
                selectedRowKeys: [],
                env: 'test',
                run_env: 'prod',
                statusMsg: '正在获取中',
                currentStatus: '正在获取中',
                modal1Visible2: false,//设置选择运行环境对话框默认不显示
                modal1Visible: false,//设置选择suite对话框默认不显示
                searchSuiteId: 1000,
                caseids: [],
                id_input: "",
            };
        },
        computed: {
            hasSelected() {
                return this.selectedRowKeys.length > 0;
            },
        },
        methods: {
            onInputChange(e) {
                const v = e.currentTarget.value;
                this.searchkey = v;
                const newData = this.originData.filter(item => (String(item.module).indexOf(v) !== -1 || String(item.title).indexOf(v) !== -1 || String(item.test_method_name).indexOf(v) !== -1 || String(item.url.toLocaleLowerCase()).indexOf(v.toLocaleLowerCase()) !== -1 || String(item.author).indexOf(v) !== -1));
                this.data = [...newData];
                const pagination = {...this.pagination};
                pagination.total = newData.length;
                pagination.current = 1;
                this.pagination = pagination;

            },
            addCase(selectValue, caseId) {
                if (selectValue == 1000) {
                    return
                }
                // this.suiteid = selectValue
                // this.caseid = caseId
                this.$message.loading('正在添加...', 0)
                api.AddCases2Suite({
                    suiteid: selectValue,
                    caseids: [caseId]
                }).then(data => {
                    this.$message.destroy()
                    if (data && data.code) {
                        this.$message.error(data.msg, 5)
                    } else {
                        this.$message.success("添加成功", 5)
                        this.fetch()
                    }
                }).catch(e => {
                    this.$message.destroy()
                    this.$message.error(e, 5)
                });
            },
            getsuitlist() {
                api.GetSuiteList({}).then(data => {
                    this.options = data;
                }).catch(e => {
                    console.error(e);
                })
                return this.options;
            },
            openSuite() {
                this.modal1Visible = true;
            },
            setModal1Visible(modal1Visible) {
                this.modal1Visible = modal1Visible;
            },
            setModal1Visible2(modal1Visible) {
                this.modal1Visible2 = modal1Visible;
            },
            handleEditContentOk() {
                if (this.checked != "") {
                    this.$message.loading('正在添加...', 0);
                    api.AddCases2Suite({
                        suiteid: this.checked,
                        caseids: this.selectedRowKeys
                    }).then(data => {
                        this.$message.destroy()
                        if (data && data.code) {
                            this.$message.error(data.msg, 5)
                        } else {
                            this.$message.success('添加成功', 5);
                            this.checked = "";
                            this.selectedRowKeys = [];
                            this.fetch();
                            console.log(this.data.msg);
                        }
                    }).catch(e => {
                        console.error(e);
                    })
                } else {
                    return
                }
                this.modal1Visible = false;
            },
            onChange(e) {
                this.checked = e.target.value;
            },
            run(v) {
                this.modal1Visible2 = true;
                if (v >= 0) {
                    this.caseids = [v];
                } else {
                    this.caseids = this.selectedRowKeys;
                }
            },
            start() {
                this.$message.loading('加入运行队列中...', 0)
                api.runCases({
                    caseids: this.caseids,
                    env: this.run_env
                }).then(data => {
                    this.$message.destroy();
                    this.$message.success('已加入队列。reportid:' + data, 5);
                    this.selectedRowKeys = [];
                    let routerJump = this.$router.resolve({name: 'runningResult', query: {reportid: data}});
                    window.open(routerJump.href, '_blank');
                }).catch(e => {
                    this.$message.destroy();
                    this.$message.error((e && e.msg) || '加入队列失败', 5);
                });
            },
            onSelectChange(selectedRowKeys){
                this.selectedRowKeys = selectedRowKeys
            },
            onShowSizeChange(current, pageSize) {
                console.log(current, pageSize);
            },
            getCaselistBysuite(v) {
                this.id_input = "";
                this.searchSuiteId = v;
                if (v == 1000) {
                    this.data = [];
                    this.fetch();
                    return
                }
                this.loading = true;
                api.GetCaseListBySuiteId({
                    suiteid: v
                }).then(data => {
                    const pagination = {...this.pagination};
                    const {
                        count,
                        caselist,
                    } = data;
                    pagination.total = count;
                    this.loading = false;
                    this.data = caselist;
                    this.originData = caselist
                    this.pagination = pagination
                })
            },
            handleTableChange2(pagination) {
                const pager = {...this.pagination}
                pager.current = pagination.current
                this.pagination = pager
                this.selectedRowKeys = [] // 分页更新，清除选中数据
            },
            handleEnvChange3(v) {
                this.run_env = v;
            },
            handleEditContentOk2() {
                this.modal1Visible2 = false;
                this.start();
            },
            fetch(params = {}) {
                document.getElementById('caselist').click();
                this.loading = true;
                api.fetchCaseList({
                    ...params,
                }).then(data => {
                    const pagination = {...this.pagination};
                    const {
                        count,
                        caselist,
                    } = data
                    pagination.total = count
                    this.loading = false
                    this.data = caselist
                    this.originData = caselist
                    this.pagination = pagination
                })
            },
        },
    }
</script>
<style>
    .container.case-list {
        margin: 30px;
    }

    .container .action-nav {
        padding: 0 0 20px;
        border-bottom: 1px solid #e5e5e5;
        margin-bottom: 30px;
    }

    .container .action-nav .label {
        margin-right: 5px;
        vertical-align: bottom;
    }

    .ant-table-body th, td {
        word-break: break-all;
    }
</style>