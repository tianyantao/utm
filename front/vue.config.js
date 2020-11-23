const path = require('path');
const resolve = dir => path.join(__dirname, dir);

module.exports = {
  configureWebpack: {
    resolve: {
      extensions: ['.js', '.jsx', '.json'],
      alias: {
        '~': resolve('src'),
      },
    },
  },
  publicPath: './',
}