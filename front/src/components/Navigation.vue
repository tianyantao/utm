<template>
    <div>
            <a-menu v-model="current" mode="horizontal" @click="changeMenu" style="font-size: 16px;">
                <a-menu-item key="icons"><img  style="width: 130px;padding-left: 20px" src="icon.jpg"></a-menu-item>
                <a-menu-item key="main1" id="main1"><a href="#/">主 页</a></a-menu-item>
                <a-menu-item key="caselist" id="caselist"><a href="#/caselist">case列表</a></a-menu-item>
                <a-menu-item key="casesuite" id="casesuite"><a href="#/casesuite">suite列表</a></a-menu-item>
                <a-menu-item key="caseurls" id="caseurls"><a href="#/urls">urls列表</a></a-menu-item>
            </a-menu>
        </div>
</template>
<script>
    export default {
        name: 'navs',
        data() {
            return {
                current: ['main1']
            };
        },
        methods:{
            changeMenu(e){
                this.current = [e.key];
                this.$forceUpdate()
            }
        }

    };
</script>
