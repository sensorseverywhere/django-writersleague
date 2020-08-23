const path = require('path')

module.exports = {
  devServer: {
    host: '127.0.0.1',
    port: 8080,
    public: 'localhost:8080',
  },
  css: {
    loaderOptions: {
        scss: {
        additionalData: `
        @import "@/assets/scss/_variables.scss";
        @import "@/assets/scss/_mixins.scss";
        `
        }
        }
    }

}