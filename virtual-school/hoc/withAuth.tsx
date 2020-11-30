/* eslint-disable @typescript-eslint/explicit-function-return-type */
import  Router  from 'next/router';
import React, { useContext } from 'react';
import authContext from '../context/auth-context';
import IAuthToken from '../models/IAuthToken';
import {CognitoService} from '../services/CognitoService'

const withAuth = ({ component: Component }) => {
    const context = useContext(authContext);
    const cognito = new CognitoService();
    const isLoggedIn = (): boolean => {
        let token: IAuthToken = context.token;
        // if the token was lost in the session, but is
        // in localstorage, load it into the session state
        if (!token && cognito.isUserSignedIn()) {
            context.login(cognito.getAuthToken())
            token = context.token;
        }

        context.checkExpired();

        if (token && !token.is_expired) {
            // TODO: 
            // if expired, refresh token 
            console.log('SIGNED IN!')
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
