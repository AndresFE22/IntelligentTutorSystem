const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  publicPath: process.env.NODE_ENV === "production" 
  ? "/diccionariokogui/" 
  : "/",
  devServer: {
    proxy: {
      '^/api': {
        target: 'http://127.0.0.1:5000',
        changeOrigin: true,
        pathRewrite: {
          '^/api': '' 
        }
      }
    },
  }
})
