import { shallow } from 'enzyme';
import React from 'react';
import App from '../pages/index';

describe('With Enzyme', () => {
  it('App shows "Virtual School" in a <title> tag', () => {
    const app = shallow(<App />);
    expect(app.find('title').text()).toEqual(' Virtual School ');
  });
});
