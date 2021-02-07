import { useRouter } from 'next/router';
import React, { useContext, useState, useEffect } from 'react';
import { Button } from 'react-bootstrap';
import AuthContext from '../context/auth-context';
import ICognitoConfig from '../models/ICognitoConfig';
import IUser from '../models/IUser';
import { CognitoService } from '../services/CognitoService';
import  UserService  from '../services/UserService';


const Login = (props) => {
    console.log('Login through Cognito')
    const router = useRouter()
    const cognito = new CognitoService();    
    const context = useContext(AuthContext)

    // if not cognitoService .isloggeedIn, then call cognitoService.redirectToLogin

    // otherwise, user is logged in, so go to landing page
    // const initialValues: LoginInputs = { email: '', password: '', };

    const [error, setError] = useState('');
    const [userLoggedIn, setUserLoggedIn] = useState<IUser | null>(null)
    console.log(process.env.DYNAMODB)
    console.log(process.env.config)

    const handleSubmit = async (e: any) : Promise<void> => {
        e.preventDefault();
        try {
            await cognito.redirectToSignIn(process.env.config as unknown as ICognitoConfig);
        } catch (err){
            setError(err.message)
        }
    };

    const goHome = () => {
        console.log(`REDIRECT TO HOME PAGE: ${JSON.stringify(context.user)}`)
        router.push('/userhome', undefined, { shallow: true });
    }
    
    useEffect( () => {
        console.log(`Check token in localstorage: ${cognito.isUserSignedIn()}`);
        const authToken = cognito.getAuthToken()
        if ( authToken && typeof authToken !== 'undefined' && 
            authToken !== null) {

                const token = cognito.parseIdToken(authToken);
                console.log(`CALL LOGIN = SET CONTEXT ${JSON.stringify(token)}`);
                
                (async function() {
                    console.log("CALL CONTEXT - SET TOKEN TO GLOBALSTATE")
                    await context.login(cognito.getAuthToken());
                    console.log(`After context: ${JSON.stringify(context.token)}`)
                })()
                console.log(`Check login: ${JSON.stringify(token)}`)
        }
        
    }, [])

    useEffect( () => {
        (async function() {
            if (context.isLoggedIn) {
                const username = context.token.cognito_username

                console.log("TOKEN IS VALID; GETTING USER INFO FOR " + username)
                let user: IUser;
                try {
                    const userService: UserService = new UserService()
                    user = await userService.getUserData(username, context.token.rawtoken)
                    console.log(`SET CONTEXT USER: ${JSON.stringify(user)}`)
                    await context.setUserContext(user)
                    setUserLoggedIn( user );
                } catch (error) {
                    console.error("Could not set user");
                    console.error(error)
                }
            }
            console.log(`Check login state: ${JSON.stringify(context.token)}`)
        }) ()
    },
    [context.isLoggedIn])

    
    // need ability to create user:
    return (
        <>
            {error ? <p>Error: {error}</p> : null}

            <p> Am I logged in? </p>
            <p>{context.isLoggedIn 
                ? <Button variant="success" size="sm">Yes</Button> 
                : <Button variant="danger" size="sm">No</Button> 
            }</p>
            <p>
                { userLoggedIn 
                ? <span>Registered login to: {userLoggedIn.firstname}</span>
                : <span>No </span> }
            </p>            
          
            {/* Option for Signup - use AdminCreateUser or SignUp action from aws-sdk */}
            {/* Makes sure emails are lowercased */}
            {/* https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminCreateUser.html */}
            {/* https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SignUp.html
             */}
            {
                userLoggedIn
                ? <> 
                    <h1> {userLoggedIn.firstname || userLoggedIn.username} IS LOGGED IN </h1>
                    <Button variant="primary" onClick={goHome} >Home</Button>
                </>
                :
                <form className="container mx-auto max-w-sm" onSubmit={handleSubmit}>
                    <div>
                        <small>Click the button to go to Login Page</small>
                    </div>
                    <button type="submit">Go To Login</button>
                </form>
            }
        </>
    )    
}

export default Login;