/* eslint-disable @typescript-eslint/explicit-function-return-type */
import  Router  from 'next/router';
import React from 'react';
import {CognitoService} from '../services/CognitoService'

const withAuth = ({ component: Component }) => {
    const cognito = new CognitoService();
    const isLoggedIn = (): boolean => {
        if  (cognito.isUserSignedIn() ) {
            // is AuthToken set in context
            // if not set in context
            // cognito.getAuthToken() 
            //  convert to AuthToken
            //  set in context
            // is expired token?

            // if expired, refresh token 
            console.log("SIGNED IN!")
            return true
        } else {
            return false
        }
    }
    return class Authenticated extends Component {
        static async getInitialProps(ctx) {
            // Check if Page has a `getInitialProps`; if so, call it.
            const pageProps =
                Component.getInitialProps &&
                (await Component.getInitialProps(ctx));
            // Return props.
            return { ...pageProps };
        }
        constructor(props) {
            super(props);
            this.state = {
                isLoading: true,
            };
        }
        componentDidMount() {
            if (!isLoggedIn() ) {
                Router.push('/login?redirected=true');
            }
            this.setState({ isLoading: false });
        }
        render() {
            return (
                <div>
                    {this.state.isLoading ? (
                        <div>LOADING....</div>
                    ) : (
                        <Component {...this.props} />
                    )}
                </div>
            );
        }
    };
}

export default withAuth;
