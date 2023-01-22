import babel from 'gulp-babel';
import dartSass from 'sass';
import gulpSass from 'gulp-sass';

import gulp from 'gulp';
const sass = gulpSass(dartSass);

import postcss from 'gulp-postcss';
import autoprefixer from 'autoprefixer';
import cssnano from 'cssnano';
import sourcemaps from 'gulp-sourcemaps';
import rename from 'gulp-rename';


// let babel = require('gulp-babel')
// let dartSass = require('sass')
// let gulp = require('gulp')
// let postcss = require('postcss')
// let autoprefixer = require('autoprefixer')
// let cssnano = require('cssnano')
// // let sourcemaps = require('sourcemaps')

// // const sass = gulpSass(dartSass);
// const sass = require('gulp-sass');



const paths = {
    // scripts: {
    //     src: 'riders/src/scripts/*.js',
    //     dest: 'riders/static/riders/scripts'
    // },
    styles: {
        src: 'assets/src/scss/*.scss',
        desta: 'assets/dist/css',
        destb: 'static/css'
    },
    url: {
        dev: 'localhost:8000',
    }
};

function style() {
    return (
        gulp
            .src(paths.styles.src)
            .pipe(sourcemaps.init())
            .pipe(sass())
            .on("error", sass.logError)
            .pipe(postcss([autoprefixer(), cssnano()]))
            .pipe(sourcemaps.write('/maps'))
            .pipe(rename(function(path) {
                if (!path.extname.endsWith('.map')) {
                    path.basename += '.min';
                    //gulp-rename with function only concats 'dirname + basename + extname'
                }
            }))
            .pipe(gulp.dest(paths.styles.desta))
            .pipe(gulp.dest(paths.styles.destb))
    );
}


function watch() {
    gulp.watch(paths.styles.src, style);
}


export const dev = gulp.series(style, watch);