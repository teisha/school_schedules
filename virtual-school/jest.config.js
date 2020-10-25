/* eslint-disable indent */
module.exports = {
    verbose: true,
    preset: 'ts-jest',
    clearMocks: true,
    collectCoverage: true,
    moduleFileExtensions: [
        'ts',
        'tsx',
        'js'
    ],
    transform: {
        // eslint-disable-next-line quotes
        "^.+\\.(ts|tsx)$": "ts-jest"
    },
    testMatch: [
        '**/__tests__/*.(test|spec).(ts|tsx)'
    ],
    globals: {
        'ts-jest': {
            useBabelrc: true,
            tsConfig: '<rootDir>/tsconf.jest.json'
        }
    },
    coveragePathIgnorePatterns: [
        '/node_modules/',
        'enzyme.js'
    ],
    testPathIgnorePatterns: [
        './.next/',
        './node_modules/'
    ],
    setupFilesAfterEnv: ['<rootDir>/enzyme.js'],
    coverageReporters: [
        'json',
        'lcov',
        'text',
        'text-summary'
    ],
    moduleNameMapper: {
        '\\.(jpg|jpeg|png|gif|eot|otf|webp|svg|ttf|woff|woff2|mp4|webm|wav|mp3|m4a|aac|oga)$': '<rootDir>/__mocks__/mocks.js',
        '\\.(css|less|scss)$': '<rootDir>/__mocks__/styleMock.js'
    }
};