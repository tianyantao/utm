<template>
    <div>
        <navs></navs>
        <a-layout style="padding: 0 40px;height:100%;margin-top: 40px">
            <a-layout-sider width="200" style="border:none">
                <a-menu
                        mode="inline"
                        :default-selected-keys="[1]"
                        :default-open-keys="['sub1']"
                        style="height: 100%;border: none"
                        @click="handleClick"
                >
                    <a-menu-item v-for="item in suits" v-bind:key="item.suite_id"> {{item.suite_name}}</a-menu-item>
                </a-menu>
            </a-layout-sider>

            <a-layout-content>
                <a-row key="1" style="margin-bottom: 10px;margin-left: 10px">
                    <a-col span="3">
                        <a-button @click="deleteCases">批量删除({{selectedRowKeys.length}})</a-button>
                    </a-col>
                    <a-col span="4">
                        <a-input-search placeholder="关键字搜索" @change="onInputChange"
                                        style="width: 200px;"/>
                    </a-col>
                </a-row>
                <a-row key="2">
                    <a-table
                            :columns="columns"
                            :rowKey="record => record.case_id"
                            :dataSource="data"
                            :pagination="pagination"
                            :loading="loading"
                            @change="handleTableChange"
                            :scroll="{ y: 630 }"
                            :rowSelection="{selectedRowKeys: selectedRowKeys, onChange: onSelectChange}"
                            size="small"
                            width="400"

                    >
                        <template slot="name" slot-scope="name">
                            {{name.first}} {{name.last}}
                        </template>
                        <span slot="action" slot-scope="text, record">
                        <a-button @click="DeleteCasesFromSuite(suiteid,[record.case_id])">删除</a-button>
                    </span>
                    </a-table>
                </a-row>
            </a-layout-content>
        </a-layout>
    </div>
</template>
<script>
    import api from '~/service'
    import ALayoutSider from "ant-design-vue/es/layout/Sider";
    import ACol from "ant-design-vue/es/grid/Col";
    import AInputSearch from "ant-design-vue/es/input/Search";
    import ARow from "ant-design-vue/es/grid/Row";

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
            width: '25%',
        },
        {
            title: '用例标题',
            dataIndex: 'title',
            sorter: true,
            width: '25%',
        },
        {
            title: '作者',
            dataIndex: 'author',
            sorter: true,
            width: '8%',
            scopedSlots: {customRender: 'author'},
        },
        {
            title: '覆盖URL',
            dataIndex: 'url',
            sorter: true,
            width: '25%',
        },
        {
            title: '操作',
            dataIndex: 'action',
            scopedSlots: {customRender: 'action'},
            width: '8%',
        },
    ]

    export default {
        name: 'CaseSuit',
        components: {ARow, AInputSearch, ACol, ALayoutSider},
        mounted() {
            this.fetch();
        },
        data() {
            return {
                suits: [],
                data: [],
                loading: false,
                columns,
                pagination: {
                    total: 0,
                    pageSize: 100,
                    showTotal: total => `共有 ${total} 条数据`,
                },
                suiteid: 1,
                selectedRowKeys: [],
            };
        },
        methods: {
            fetch(params = {}) {
                document.getElementById('casesuite').click();
                this.loading = true;
                api.GetSuiteList({
                    ...params,
                }).then(data => {
                    this.loading = false
                    this.suits = data;
                    this.GetCaseListBySuiteId(this.suiteid);
                }).catch(e => {
                    console.error(e);
                })
            },

            handleClick(e) {
                this.GetCaseListBySuiteId(e.key);
                this.suiteid = e.key;
                this.selectedRowKeys = [];
            },

            GetCaseListBySuiteId(v) {
                this.loading = true;
                api.GetCaseListBySuiteId({
                    suiteid: v
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
            onInputChange(e) {
                const v = e.currentTarget.value;
                const newData = this.originData.filter(item => (String(item.title).indexOf(v) !== -1 || String(item.test_method_name).indexOf(v) !== -1 ||
                    String(item.url.toLocaleLowerCase()).indexOf(v.toLocaleLowerCase()) !== -1 || String(item.author).indexOf(v) !== -1));
                this.data = [...newData];
                const pagination = {...this.pagination};
                pagination.total = newData.length;
                pagination.current = 1;
                this.pagination = pagination;
            },
            DeleteCasesFromSuite(suiteid, caseids) {
                this.$message.loading('正在删除...', 0);
                api.DeleteCasesFromSuite({
                    suiteid: suiteid,
                    caseids: caseids
                }).then(data => {
                    this.$message.destroy()
                    if (data && data.code) {
                        this.$message.error(data.msg, 5)
                    } else {

                        this.originData = this.originData.filter(item => !caseids.includes(item.case_id));
                        this.data = this.originData;
                        const pagination = {...this.pagination};
                        pagination.total = this.data.length;
                        pagination.current = 1;
                        this.pagination = pagination;
                        var arr3 = this.selectedRowKeys.filter(el => !caseids.includes(el))
                        this.selectedRowKeys = arr3
                        this.$message.success('删除成功', 5);
                    }
                }).catch(e => {
                    console.error(e);
                })
            },
            handleTableChange(pagination) {
                const pager = {...this.pagination}
                pager.current = pagination.current
                this.pagination = pager
            },
            onSelectChange(selectedRowKeys) {
                this.selectedRowKeys = selectedRowKeys

            },
            deleteCases() {
                this.DeleteCasesFromSuite(this.suiteid, this.selectedRowKeys)
            }
        }

    };
</script>

<style scoped>

</style>