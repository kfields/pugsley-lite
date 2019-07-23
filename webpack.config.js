const path = require('path');
const webpack = require('webpack')
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const devMode = process.env.NODE_ENV !== 'production';

module.exports = {
  mode : devMode ? 'development' : 'production',
  // devtool: 'source-map',
  context: path.resolve(__dirname, 'src'),
  entry: {
    main: './main.js', 
    calendar: './calendar.js',
    dashboard: './dashboard.js',
    chart: './chart.js'
  },
  output: {
    filename: '[name].js',
    path: path.resolve(__dirname, 'pugsley/static/dist')
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: "[name].css",
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
            MiniCssExtractPlugin.loader,
            { loader: 'css-loader', options: { url: false, sourceMap: true } },
            { loader: 'sass-loader', options: { sourceMap: true } }
        ],
      },
      {
        test: /\.(woff|woff2|eot|ttf|otf)$/,
        use: [
          {
            loader: 'file-loader',
            options: {
              name: '[name].[ext]',
              outputPath: path.resolve(__dirname, 'pugsley/static/fonts/')
            }
          }
        ]
      }
    ]
  }
};