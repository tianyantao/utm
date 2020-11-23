<template>
    <div>
        <!--<navs></navs>-->
        <div class="running-result" style="text-align: center;">
            <!--<p class="result-text">{{ loading ? '任务调度中...' : ( result ? '任务调用成功' : '任务调用失败' ) }}</p>-->
            <a-divider>执行详情</a-divider>
            <div style="text-align: center;">

                <a-progress type="circle" :percent="percent" :format="percent => `执行进度${percent}%`"/>
            </div>


            <h2 v-if="report">
                <a-divider>执行结果</a-divider>
            </h2>
            <p v-if="report">用例执行总数：{{ detail.total }} 个</p>
            <p v-if="report">断言失败数量：{{ detail.assert_fail }} 个</p>
            <p v-if="report">执行报错数量：{{ detail.run_error }} 个</p>
            <p v-if="report">跳过用例数量：{{ detail.skiped }} 个</p>
            <p v-if="report">成功：{{ detail.success }} 个</p>
            <p v-if="report"><a :href="report" target="_blank">查看报告</a></p>
            <p v-else><a-divider>结果加载中，请稍后</a-divider></p>
            <a-divider dashed/>
        </div>
    </div>
</template>

<script>
    import api from '~/service'

    export default {
        name: 'RunningResult',
        props: {
            msg: String
        },
        data() {
            return {
                loading: false,
                result: false,
                detail: null,
                fetchInterval: null,
                percent: 0,
                report: false,
            }
        },
        mounted() {
            this.fetch(this.$route.query.reportid)
        },
        methods: {
            fetch(v) {
                const self = this;
                if (this.fetchInterval) {
                    return;
                }
                const IS_SERVER = window.location.host.indexOf('qa.mistong.cn') !== -1;
                const SERVER_MID_PATH = IS_SERVER ? '/pytest' : '';
                this.fetchInterval = setInterval(function () {
                    api.getCaseRunningStatus({reportid: v}).then(data => {
                        if (data.progress === 100 && data.report_url != null) {
                            self.detail = data
                            // self.report = `//${location.hostname}:8876${data.report_url}`
                            self.report = `//${location.host}${SERVER_MID_PATH}${data.report_url}`
                            self.percent = 100
                            clearInterval(self.fetchInterval)
                        } else {
                            self.detail = `执行进度${data.progress}`
                            self.percent = Number(String(data.progress).replace('%', ''))

                        }
                    }).catch(e => {
                        self.detail = e;
                    });
                }, 1000)
            }
        },
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .running-result {
        margin: 30px;
    }

    .running-result pre {
        background-color: #f2f4f5;
        padding: 8px 0;
    }
</style>