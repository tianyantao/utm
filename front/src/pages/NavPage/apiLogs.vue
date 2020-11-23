<template>
    <div>
        <!--<navs></navs>-->
        <div style="margin-left: 50px;">
            <a style="font-size: 24px; font-weight: bolder; ">运行日志如下(Run_id:
                {{this.$route.query.run_id}})</a>
            <br>
            <span style="font-weight: bolder;font-size: 16px;">用例名称：</span> <span style="font-size: 16px;">{{this.$route.query.run_title }}</span>
            <br>
            <span style="font-weight: bolder;font-size: 16px;">开始时间：</span><span style="font-size: 16px;"> {{update_time}}</span>
            <br>
            <span style="font-weight: bolder;font-size: 16px;">运行结果：</span> <span
                :style="this.$route.query.run_result == 'P' ?  'color: green' : 'color: red;font-size: 16px;'">{{this.$route.query.run_result == "P" ? "通过": "失败" }}</span>
            <br>
        </div>
        <div class="center">
            <a-collapse v-model="activeKey" :bordered="false">
                <a-collapse-panel v-for="item in data" v-bind:key="item.status" v-bind:header="item.req_url"
                                  :style="item.http_status == '200' ?  'background: lightgreen;' : 'background: bisque;'">
                    <div style="background-color: #ffffff;padding: 10px;">
                        <p><span style="font-weight: bolder">运行用时：</span> {{item.elapsed}}</p>
                        <p><span style="font-weight: bolder">http状态：</span> {{item.http_status}}</p>
                        <p><span style="font-weight: bolder">开始时间：</span> {{item.update_time}}</p>
                        <p><span style="font-weight: bolder">接口路径：</span>
                            <a-tag color="blue">{{item.req_method}}</a-tag>
                            {{item.req_url}}
                        </p>
                        <p><span style="font-weight: bolder">请求body：</span> {{item.req_data}}</p>
                        <p><span style="font-weight: bolder">返回headers：</span> {{item.res_headers}}</p>
                        <p style="word-break:break-all;"><span style="font-weight: bolder">返回数据：</span>
                            {{item.res_content}}</p>
                    </div>
                </a-collapse-panel>
            </a-collapse>
        </div>
    </div>
</template>
<script>
    import api from '~/service'

    export default {
        name: 'ApiLogs',
        mounted() {
            this.fetch()
        },
        data() {
            return {
                data: [],
                loading: false,
                activeKey: [],
                update_time: "",
            };
        },
        methods: {
            fetch() {
                this.loading = true;
                api.GetApiLog({
                    run_id: this.$route.query.run_id
                }).then(data => {
                    this.loading = false;
                    this.data = data;
                    for (var i = 0; i < data.length; i++) {
                        this.data[i].status = 0;
                        if (this.data[i].http_status != '200') {
                            this.activeKey.push(i); //默认展开接口状态为非200的日志
                        }
                    }
                    this.update_time = data[0].update_time;
                    if (this.activeKey.length == 0) this.activeKey = [this.data.length - 1]; //所有接口都通过默认展开最后一个接口日志
                }).catch(e => {
                    console.error(e);
                    this.$message.error('数据未获取到哦~', 5)
                })
            },
        },
    };
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .center {
        margin-left: 50px;
        margin-top: 30px;
        margin-right: 50px;
        width: 95%;
    }
</style>