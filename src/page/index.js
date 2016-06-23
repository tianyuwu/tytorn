/**
 * Created by tianyu on 16/6/19.
 */
var Vue = require('vue');
Vue.config.delimiters = ['${', '}'];
var App = require('../components/app.vue');
new Vue({
    el:'body',
    // data:{username:"wutianyu"}
    components: { "app": App }
});