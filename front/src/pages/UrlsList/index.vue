<template>
    <div>
        <navs></navs>
        <div style="margin-left: 40px;margin-right: 40px">
            <a-row type="flex" align="bottom"  style="margin-bottom: 10px">
                <a-col :span="2">
                    <span> <a-button @click="addUrl">添加</a-button></span>
                </a-col>
                <a-col :span="5">
                    <a-input-search placeholder="关键字搜索" @change="onInputChange" style="width: 250px"/>
                </a-col>

                <a-col :span="4">
                    <span style="padding-left: 2%">是否覆盖:
                            <a-select style="width: 100px" @change="(v) => { selected(1,v) }"
                                      default-value="">
                                <a-select-option value="" style="padding-left: 30px">
                                    全部
                                </a-select-option>
                                <a-select-option value="已覆盖">
                                       已覆盖
                                </a-select-option>
                                <a-select-option value="未覆盖">
                                       未覆盖
                                </a-select-option>
                            </a-select>
                    </span>
                </a-col>
                <a-col span="8">
                    <span style="padding-left: 1%">从属业务线:
                           <a-select style="width: 100px" @change="(v) => { selected(2,v)}"
                                     default-value="">
                                <a-select-option value="" style="padding-left: 30px">
                                    全部
                                </a-select-option>
                                <a-select-option value="b">
                                       教师端
                                </a-select-option>
                                <a-select-option value="tiku">
                                       题库
                                </a-select-option>
                            </a-select>
                        </span>
                </a-col>
                <a-col :span="5" style="margin-top: 10px">
                    接口覆盖率:
                    <!--<br>-->
                    <a-progress :percent="percent" type="circle" :width="70"/>
                    <!--<a-progress :percent="percent"  type="circle" :width="70" :format="percent => `覆盖率${percent}%`"/>-->
                </a-col>
            </a-row>
            <a-row key="2">
                <a-table
                        :columns="columns"
                        :rowKey="record => record.case_id"
                        :dataSource="data"
                        :pagination="pagination"
                        :loading="loading"
                        size="small"
                        @change="handleTableChange"
                        :scroll="{ y: 630 }"

                >
                    <template slot="name" slot-scope="name">
                        {{name.first}} {{name.last}}
                    </template>
                    <span slot="action">
                        <a-button @click="showDeleteConfirm">删除</a-button>
                        <a-button @click="showConfirm">编辑</a-button>
                    </span>
                </a-table>
            </a-row>
        </div>
    </div>
</template>
<script>
    import api from '~/service'
    import ARow from "ant-design-vue/es/grid/Row";
    import ACol from "ant-design-vue/es/grid/Col";
    // import moment from 'moment'

    const columns = [
        {
            title: 'ID',
            dataIndex: 'id',
            sorter: true,
            width: '2%',
        },
        {
            title: 'url',
            dataIndex: 'url',
            sorter: true,
            width: '10%',
        },
        {
            title: '是否已覆盖',
            dataIndex: 'is_cover',
            sorter: true,
            width: '5%',
        },
        {
            title: '从属业务线',
            dataIndex: 'belong',
            sorter: true,
            width: '5%',
            customRender: (v) => {
                return v === null || v === "" ? '无' : v;
            }
        },
        {
            title: '操作',
            dataIndex: 'action',
            scopedSlots: {customRender: 'action'},
            width: '5%',
        },
        {
            title: '备注',
            dataIndex: 'remark',
            sorter: false,
            width: '10%',
            customRender: (v) => {
                return v === null || v === "" ? '无' : v;
            }
        },
    ]

    export default {
        name: 'UrlsList',
        components: {ACol, ARow},
        mounted() {
            this.fetch()
            // this.fetchEnv()
        },
        data() {
            return {
                data: [],
                pagination: {
                    total: 0,
                    pageSize: 100,
                    // showSizeChanger: true,
                    // showSizeChange: this.onShowSizeChange,
                    // pageSizeOptions: ['10', '20', '30', '40', '50', '100', '200', '500', '1000'],
                    showTotal: total => `共有 ${total} 条数据`,
                },
                loading: false,
                columns,
                selectedRowKeys: [],
                env: 'test',
                update: false,
                percent: 0
            };
        },
        computed: {
            hasSelected() {
                return this.selectedRowKeys.length > 0;
            },
        },
        methods: {
            onInputChange(e) {
                const v = e.currentTarget.value
                const newData = this.originData.filter(item => (String(item.url).toLocaleLowerCase().indexOf(v.toLocaleLowerCase()) !== -1 || String(item.remark).indexOf(v) !== -1));
                this.data = [...newData];
                const pagination = {...this.pagination};
                pagination.total = newData.length;
                pagination.current = 1;
                this.pagination = pagination;
            },
            selected(type, v) {
                if (type === 1) {
                    const newData = this.originData.filter(item => (String(item.is_cover).toLocaleLowerCase().indexOf(v.toLocaleLowerCase()) !== -1));
                    this.data = [...newData];
                    const pagination = {...this.pagination};
                    pagination.total = newData.length;
                    pagination.current = 1;
                    this.pagination = pagination;
                } else if (type === 2) {
                    const newData = this.originData.filter(item => (String(item.belong).toLocaleLowerCase().indexOf(v.toLocaleLowerCase()) !== -1));
                    this.data = [...newData];
                    const pagination = {...this.pagination};
                    pagination.total = newData.length;
                    pagination.current = 1;
                    this.pagination = pagination;
                }
            },
            onSearch(v) {
                const newData = this.originData.filter(item => (String(item.url).indexOf(v) !== -1 || String(item.remark).indexOf(v) !== -1));
                this.data = [...newData];

            },
            addUrl() {
                this.$confirm({
                    title: '未实现',
                    content: 'When clicked the OK button, this dialog will be closed after 1 second',
                    onOk() {
                        return new Promise((resolve, reject) => {
                            setTimeout(Math.random() > 0.5 ? resolve : reject, 1000);
                        }).catch(() => console.log('Oops errors!'));
                    },
                    onCancel() {
                    },
                });
            },
            showConfirm() {
                this.$confirm({
                    title: '未实现',
                    content: 'When clicked the OK button, this dialog will be closed after 1 second',
                    onOk() {
                        return new Promise((resolve, reject) => {
                            setTimeout(Math.random() > 0.5 ? resolve : reject, 1000);
                        }).catch(() => console.log('Oops errors!'));
                    },
                    onCancel() {
                    },
                });
            },
            showDeleteConfirm() {
                this.$confirm({
                    title: '确定弃用吗？',
                    content: '弃用后的url不会再进行自动化覆盖',
                    okText: 'Yes',
                    okType: 'danger',
                    cancelText: 'No',
                    onOk() {
                        console.log('OK');
                    },
                    onCancel() {
                        console.log('Cancel');
                    },
                });
            },
            start() {
                window.open(`#/runningResult?id=${this.selectedRowKeys.join('-')}`);
            },
            onSelectChange(selectedRowKeys) {
                this.selectedRowKeys = selectedRowKeys
            },
            onShowSizeChange(current, pageSize) {
                console.log(current, pageSize);
            },
            handleTableChange(pagination) {
                const pager = {...this.pagination}
                pager.current = pagination.current
                this.pagination = pager
                this.selectedRowKeys = [] // 分页更新，清除选中数据
                // this.fetch({
                //     results: pagination.pageSize,
                //     page: pagination.current,
                //     sortField: sorter.field,
                //     sortOrder: sorter.order,
                //     ...filters,
                // })
            },
            fetch(params = {}) {
                document.getElementById('caseurls').click()
                this.loading = true;
                api.fetchUrlsList({
                    ...params,
                }).then(data => {
                    const pagination = {...this.pagination};
                    const {
                        total,
                        url_list,
                        cover_rate,
                    } = data
                    pagination.total = total
                    this.loading = false
                    this.data = url_list
                    this.originData = url_list
                    this.percent = (cover_rate * 100).toFixed(1)
                    this.pagination = pagination
                })
            },
        },
    }
</script>


<style>

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