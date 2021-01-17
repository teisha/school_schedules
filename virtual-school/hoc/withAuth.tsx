/* eslint-disable @typescript-eslint/explicit-function-return-type */
import { NextPageContext } from 'next';
import   { useRouter }  from 'next/router';
import React, {  useContext, useEffect, useState } from 'react';
import authContext from '../context/auth-context';


const withAuth = (WrappedComponent: any ) => {
    return props => {
        const router = useRouter()
        const context = useContext(authContext);
        const [isLoggedIn, setIsLoggedIn] = useState<boolean>(context.isLoggedIn)
    
        useEffect( () => {
            console.log("withAUTH - CHECK EXPIRED");
            (async function() {
                const currentPage = router.pathname
                const isExpired = await context.checkExpired()
                console.log(context);
                if ( isExpired ) {
                    router.push({
                        pathname: '/auth',
                        query: { redirectTo: currentPage },
                    })
                } else {
                    console.log("SET LOGIN TO TRUE")
                    setIsLoggedIn(true)
                }
            }) ()
        }, []) 

        useEffect( () => {
            setIsLoggedIn(context.isLoggedIn)
        }, [context])
        
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
            <WrappedComponent user={context.user} isLoggedIn={isLoggedIn} {...props} />
        );
    }

}

export default withAuth;
