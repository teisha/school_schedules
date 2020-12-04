/* eslint-disable @typescript-eslint/explicit-function-return-type */
import { NextPageContext } from 'next';
import  Router  from 'next/router';
import React, { Component, useContext, useEffect, useState } from 'react';
import authContext from '../context/auth-context';
import IAuthToken from '../models/IAuthToken';
import {CognitoService} from '../services/CognitoService'

const context = useContext(authContext);
const cognito = new CognitoService();

const withAuth = (WrappedComponent: any ) => {
    
    return props => {
        const [isLoggedIn, setIsLoggedIn] = useState(false)

        useEffect( () => {
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
                setIsLoggedIn( true)
            } else {
                setIsLoggedIn(  false )
            }
        }, [])

        const getInitialProps = async (ctx: NextPageContext) => {
            // Check if Page has a `getInitialProps`; if so, call it.
            if (WrappedComponent.getInitialProps){
                const pageProps =
                    WrappedComponent.getInitialProps &&
                    (await WrappedComponent.getInitialProps(ctx));
                // Return props.
                return { ...pageProps };
            }
        }

        return (
            <div>
                {isLoggedIn ? (
                    <div>LOADING....</div>
                ) : (
                    <WrappedComponent {...props} />
                )}
            </div>
        );
    }

}

export default withAuth;
