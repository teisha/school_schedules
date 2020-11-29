import React, { PropsWithChildren } from 'react'
import { useReducer } from 'react';
import AuthContext from './auth-context';
import { tokenReducer, LOGIN } from './token-reducer';
import { userReducer } from './user-reducer';



const GlobalState: React.FC<PropsWithChildren<any>> = (props: PropsWithChildren<any>) => {

    const [authTokenState, tokenDispatch] = useReducer(tokenReducer, null);
    const [authUserState, userDispatch] = useReducer(userReducer, null);

    // eslint-disable-next-line @typescript-eslint/explicit-function-return-type
    const login = (token: string) => {
        tokenDispatch({ type: LOGIN, token: token });
        userDispatch({ type: LOGIN, username: authTokenState.token?.cognito_username });
    };
    const logout = () => {
        console.log('Logout')
    }

    return (
        <AuthContext.Provider
            value={{
                user: authUserState.user,
                token: authTokenState.token,
                login: login,
                logout: logout,
            }}
        >
            {props.children}
        </AuthContext.Provider>
    );
};

export default GlobalState