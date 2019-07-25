const path = require('path');
const webpack = require('webpack')
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const devMode = process.env.NODE_ENV !== 'production';

module.exports = {
  watch: true,
  mode : devMode ? 'development' : 'production',
  // devtool: 'source-map',
  context: path.resolve(__dirname, 'assets/js'),
  entry: {
    main: './main.js', 
    calendar: './calendar.js',
    dashboard: './dashboard.js',
    chart: './chart.js'
  },
  output: {
    filename: 'js/[name].js',
    path: path.resolve(__dirname, 'pugsley/static')
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: "css/[name].css",
      chunkFilename: "[id].css"
    }),
    new webpack.ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery'
    }),
    new webpack.ProvidePlugin({
      Chart: 'chart.js'
    })
  ],
  module: {
    rules: [
      {
        test: /\.s?[ac]ss$/,
        use: [
            { 
              loader: MiniCssExtractPlugin.loader,
              options: {
                outputPath: path.resolve(__dirname, 'pugsley/static/css'),
                publicPath: path.resolve(__dirname, 'pugsley/static/css')
              }
            },
            { loader: 'css-loader', options: { url: false, sourceMap: true } },
            { loader: 'sass-loader', options: { sourceMap: true } }
        ],
      },
      {
        test: /\.(png|gif|jpe|jpg|woff|woff2|eot|ttf|svg)(\?.*$|$)/,
        use: [
          {
            loader: 'url-loader',
            options: {
              outputPath: path.resolve(__dirname, 'pugsley/static/fonts'),
              publicPath: path.resolve(__dirname, 'pugsley/static/fonts')
            }
          }
        ]
      }
    ]
  }
};