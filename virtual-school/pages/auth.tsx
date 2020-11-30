import React, { useState, useEffect } from 'react'
import { useRouter } from 'next/router'
import { useContext } from 'react';
import { CognitoService } from '../services/CognitoService'
import ICognitoConfig from '../models/ICognitoConfig';
import AuthContext from '../context/auth-context';



const Auth: React.FC<{}> = ()  => {
    const cognito: CognitoService = new CognitoService();    
    const [isLoggedIn, setIsLoggedIn] = useState(false)
    const context = useContext(AuthContext)
    const router = useRouter()
    // eslint-disable-next-line @typescript-eslint/no-unused-vars
    
    useEffect( () => {
        console.log(window?.location )
        let [baseurl, ...rest] = window.location.href.split("#")
        const router_query = rest.join("#").split("&")
        const id_token = router_query[0].split("=")[1]
        // const { id_token, access_token, expires_in , token_type } = router.query
        console.log(`VALIDATE TOKEN: ${id_token}`)
        if (
            cognito.validateToken(id_token as string,
                process.env.config as unknown as ICognitoConfig) 
        ){
            cognito.setAuthToken(id_token as string)
            context.login(id_token);
            setIsLoggedIn(cognito.isUserSignedIn());
        } else {
            router.push('/login');
        }
    }, [])
       
    
    // http://localhost:4000/auth#id_token=eyJraWQiOiJSeGJkYjkyd0dFVTB4SFhVUFl4TVo3K3NtVVRJM1FvR2hYaWc1WkM4aEVFPSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiLXJ4REFQN0VDa0xQNURzd0c4dVJzZyIsInN1YiI6ImY5Y2RlZTdjLWE1OGUtNDllYy04MTE1LTY5ODA4Y2NlOWM1MSIsImF1ZCI6IjdwMWcyaG81ZXNsbTJ2ZWE3amY4bzhmMmFvIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImV2ZW50X2lkIjoiMjM3OWNiYTEtYzA1MS00MzA4LWJmZjQtZmQ0NTZjNDY0ZmVlIiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2MDY1MDc3NTAsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0xXzg5azA2bENTQSIsImNvZ25pdG86dXNlcm5hbWUiOiJsYWltYUIiLCJleHAiOjE2MDY1MTEzNTAsImlhdCI6MTYwNjUwNzc1MCwiZW1haWwiOiJhaHNpZXQ0QHlhaG9vLmNvbSJ9.smtwylDq3PHFvC7KtOHkZ8TnnKI8lkhcffuoB2lTIhks4GxtG0syk52vkw7WR7tLTyWTDmpNTHJrb113aXFauHE2yhZMUxTwNFlWHjCMW6_lguT6F10b84JL-SgI1cGXSJzLShdHgewFPSmsvbyeXnDK18xREfHL1geizBxQT_NJGmD4KUn2DXn83C1t0sdfjY27q5F0FFb_binbPHX73UUZ-_i6Btv6oLqNFFBBAm8xyw4eAD1uuEMXyav4aDO1Q5WlBR4c2ToG6fSo7OSKGJeCe96MxdrjAsvT2Rfv_wKAfldZcwUhF9WZGo-DNJaE-Hi5mYzAVJTM_-ph9OzGQg&access_token=eyJraWQiOiJlZWVicWR3RDJBUUlZK0VFYnJVZFg2MUdzZVlHXC91Smdwd1JEM001Rlc5az0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJmOWNkZWU3Yy1hNThlLTQ5ZWMtODExNS02OTgwOGNjZTljNTEiLCJldmVudF9pZCI6IjIzNzljYmExLWMwNTEtNDMwOC1iZmY0LWZkNDU2YzQ2NGZlZSIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE2MDY1MDc3NTAsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0xXzg5azA2bENTQSIsImV4cCI6MTYwNjUxMTM1MCwiaWF0IjoxNjA2NTA3NzUwLCJ2ZXJzaW9uIjoyLCJqdGkiOiJmOThlMGQxYy00MmIwLTRjNDItODhiNC05ZWY5YWI5ZmJhYmEiLCJjbGllbnRfaWQiOiI3cDFnMmhvNWVzbG0ydmVhN2pmOG84ZjJhbyIsInVzZXJuYW1lIjoibGFpbWFCIn0.GM-heLcwtOm4uYxfLY-cWQd94TMfmwoV-MLGk_pagfZbFMyJuC3DsInIkKv5Z949YAbht_RfRBbYBTJ5M5tQ8fb1KDnNZWPBmzp7jk5ZU17PaIzvP7BXgxqhkUGhkQEqG5jnC9hdpxI9zNS_c2JVGLtGtSmUblTjBzo4LT0ijfuay9ZVKkmXvGbXvRD4tpg7V7DtBv0zlnLvohhvTKJ1lrnythpNkZMU-l5_bPbuY4SEXFrkHduscdmAK4ZMFd1ur9LA8X8-Rgp0SUDuzF-zN5F55rk6xC_CpjYgVo95M2txrTLObdqFrqJ9Q0hoejbtUymyLbEucjjed8GlfMmelg&expires_in=3600&token_type=Bearer
    // access_token=eyJraWQiOiJlZWVicWR3RDJBUUlZK0VFYnJVZFg2MUdzZVlHXC91Smdwd1JEM001Rlc5az0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJmOWNkZWU3Yy1hNThlLTQ5ZWMtODExNS02OTgwOGNjZTljNTEiLCJldmVudF9pZCI6IjIzNzljYmExLWMwNTEtNDMwOC1iZmY0LWZkNDU2YzQ2NGZlZSIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE2MDY1MDc3NTAsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0xXzg5azA2bENTQSIsImV4cCI6MTYwNjUxMTM1MCwiaWF0IjoxNjA2NTA3NzUwLCJ2ZXJzaW9uIjoyLCJqdGkiOiJmOThlMGQxYy00MmIwLTRjNDItODhiNC05ZWY5YWI5ZmJhYmEiLCJjbGllbnRfaWQiOiI3cDFnMmhvNWVzbG0ydmVhN2pmOG84ZjJhbyIsInVzZXJuYW1lIjoibGFpbWFCIn0.GM-heLcwtOm4uYxfLY-cWQd94TMfmwoV-MLGk_pagfZbFMyJuC3DsInIkKv5Z949YAbht_RfRBbYBTJ5M5tQ8fb1KDnNZWPBmzp7jk5ZU17PaIzvP7BXgxqhkUGhkQEqG5jnC9hdpxI9zNS_c2JVGLtGtSmUblTjBzo4LT0ijfuay9ZVKkmXvGbXvRD4tpg7V7DtBv0zlnLvohhvTKJ1lrnythpNkZMU-l5_bPbuY4SEXFrkHduscdmAK4ZMFd1ur9LA8X8-Rgp0SUDuzF-zN5F55rk6xC_CpjYgVo95M2txrTLObdqFrqJ9Q0hoejbtUymyLbEucjjed8GlfMmelg&
    // expires_in=3600&
    // token_type=Bearer


    // Need higher order function to guard routes
    // save AuthToken on context (in hof?)
    // refresh token on expiration -> check expiration in hof

    return (
        <>
            {   !isLoggedIn  ?  
                <div className="text-center">
                    <div className="spinner-border" role="status">
                        <span className="sr-only">Loading...</span>
                    </div>
                </div>    :
                <> 
                    <h1> Hi {context.user.firstname || context.user.username} ! </h1>
                    <p> Thank you for loggin in.  You will be redirected shortly.  Please wait.</p>
                </>
            }
        </>
    )
}

export default Auth;