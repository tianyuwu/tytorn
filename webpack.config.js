/**
 * Created by tianyu on 16/5/30.
 */
module.exports = {
    entry: "./src/page/index.js", //入口文件
    output: {
        path:"./static", //输出目录
        filename:"index.js"  //输出文件夹
    },
    module:{
        loaders:[
            {test:/\.js/,loader:"babel-loader"}  //用什么loader来编译
        ]
    }
};