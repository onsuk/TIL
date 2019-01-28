const utils = require('./utils')
const assert = require('assert')
const should = require('should')

describe('utils.js 모듈 테스트', () => { it('문자열의 첫번째 문자를 대문자로~', () => {
        const result = utils.capitialize('hello')
        result.should.be.equal('Hello')
    })
})