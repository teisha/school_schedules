/* eslint-disable indent */
module.exports = {
    verbose: true,
    preset: 'ts-jest',
    clearMocks: true,
    collectCoverage: true,
    transform: {
        // eslint-disable-next-line quotes
        "^.+\\.(ts|tsx)$": "ts-jest"
    },
    'testRegex': '(/__tests__/.*|(\\.|/)(test|spec))\\.tsx?$',
    // testMatch: [
    //     '**\\*.(test|spec).(ts|tsx)'
    // ],
    globals: {
        'ts-jest': {
            tsConfig: '<rootDir>/tsconf.jest.json'
        }
    },
    coveragePathIgnorePatterns: [
        '/node_modules/',
        'enzyme.js'
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
    },
    'testEnvironment': 'node',
    // 'roots': [
    //     '<rootDir>/components'
    // ],
    'moduleFileExtensions': [
        'ts',
        'tsx',
        'js',
        'jsx',
        'json',
        'node'
    ],
    'testPathIgnorePatterns': ['<rootDir>/.next/', '<rootDir>/node_modules/'],
    'snapshotSerializers': ['enzyme-to-json/serializer'],
};