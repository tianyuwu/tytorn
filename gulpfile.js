/**
 * Created by tianyu on 16/6/19.
 * npm install gulp gulp-webpack vinyl-named --save-dev
 */
var gulp = require('gulp');
var webpack = require('gulp-webpack');
var named = require('vinyl-named');


var pageList = ['index'];

gulp.task('bundle', function() {
  return gulp.src(mapFiles(pageList, 'js'))
    .pipe(named())
    .pipe(webpack(getConfig()))
    .pipe(gulp.dest('static/'))
})

gulp.task('watch', function() {
  return gulp.src(mapFiles(pageList, 'js'))
    .pipe(named())
    .pipe(webpack(getConfig({watch: true})))
    .pipe(gulp.dest('static/'))
})



/**
 * @private
 */
function getConfig(opt) {
  var config = {
    module: {
      loaders: [
        { test: /\.vue$/, loader: 'vue'},

      ]
    },
    vue: {
     loaders: {
        js: 'babel'
     }
    }
  }
  if (!opt) {
    return config
  }
  for (var i in opt) {
    config[i] = opt[i]
  }
  return config
}

function mapFiles(list, extname) {
  return list.map(function (app) {return 'src/page/' + app + '.' + extname})
}