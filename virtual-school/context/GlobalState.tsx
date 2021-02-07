import React, { PropsWithChildren, useState } from 'react'
import { useReducer } from 'react';
import IAuthToken from '../models/IAuthToken';
import { CognitoService } from '../services/CognitoService';
import AuthContext from './auth-context';
import { tokenReducer, LOGIN, CHECK_EXPIRED } from './token-reducer';
import IUser from '../models/IUser';


const GlobalState: React.FC<PropsWithChildren<any>> = (props: PropsWithChildren<any>) => {
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const [authTokenState, tokenDispatch] = useReducer(tokenReducer, {token: null} );
    const [user, setUser] = useState<IUser | null >(null)

    // eslint-disable-next-line @typescript-eslint/explicit-function-return-type
    const login = async (token: string) => {
        const cognito = new CognitoService();
        const authToken: IAuthToken = cognito.parseIdToken(token)
        
        console.log(`CONTEXT SET FROM TOKEN STRING ${JSON.stringify(authToken)}`)
        await tokenDispatch({ type: LOGIN, token: authToken });
        if (!authToken.is_expired) {
            setIsLoggedIn(true);
        }
        console.log(`TOKEN In Global State: ${JSON.stringify(authTokenState)}`)
    };
    
    const checkExpired = () : boolean => { 
        let isExpired = true;
        if (authTokenState.token != null) {
            isExpired = ( Date.now() / 1000) > authTokenState.expires
            tokenDispatch({type: CHECK_EXPIRED})
            setIsLoggedIn(!isExpired)
            return isExpired
        }
        if (isExpired) {
            setIsLoggedIn(false)
        }
        return isExpired
    };

    const logout = () => {
        console.log('Logout')
        tokenDispatch("LOGOUT")
        setUser(null)
        setIsLoggedIn(false)
    }

    return (
        <AuthContext.Provider
            value={{
                user: user,
                token: authTokenState.token,
                login: login,
                logout: logout,
                isLoggedIn: isLoggedIn,
                setUserContext: setUser,
                checkExpired: checkExpired
            }}
        >
            {props.children}
        </AuthContext.Provider>
    );
};

AuthContext.displayName = 'AuthContext';
export default GlobalState