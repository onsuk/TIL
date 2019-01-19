const express = require('express')
const app = express()
const user = require('./api/user')
const morgan = require('morgan')

if (process.env.NODE_ENV !== 'test') {
    app.use(morgan('dev'))
}

app.use('/users', user)


module.exports = app