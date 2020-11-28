import React, { useState } from 'react';
import ICognitoConfig from '../models/ICognitoConfig';
import { CognitoService } from '../services/CognitoService'


export type LoginInputs = {
  email: string
  password: string
}

const Login: React.FC<{}> = ()  => {
    const cognito = new CognitoService();    


    // if not cognitoService .isloggeedIn, then call cognitoService.redirectToLogin

    // otherwise, user is logged in, so go to landing page
    // const initialValues: LoginInputs = { email: '', password: '', };

    const [error, setError] = useState('');
    console.log(process.env.DYNAMODB)
    console.log(process.env.config)
    console.log('Login through Cognito')

    const handleSubmit = async (e: any) : Promise<void> => {
        e.preventDefault();
        try {
            await cognito.redirectToSignIn(process.env.config as unknown as ICognitoConfig);
        } catch (err){
            setError(err.message)
        }
    };

    //   const handleInputChange = (e: React.ChangeEvent<any>) => {
    //     e.persist();
    //     setInputs({
    //       ...inputs,
    //       [e.target.name]: e.target.value,
    //     });
    //   };

    return (
        <>
            {error ? <p>Error: {error}</p> : null}

            {/* Option for Signup - use AdminCreateUser or SignUp action from aws-sdk */}
            {/* Makes sure emails are lowercased */}
            {/* https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminCreateUser.html */}
            {/* https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SignUp.html
             */}
            {
                cognito.isUserSignedIn() 
                    ? <h1> USER IS LOGGED IN </h1>
                    :
                    <form className="container mx-auto max-w-sm" onSubmit={handleSubmit}>

                        <div>
                            <small><strong>user:</strong> rickety_cricket@example.com</small>
                            <small><strong>password:</strong> {process.env.NODE_ENV} </small>
                        </div>
                        <button type="submit">Go To Login</button>
                    </form>
            }
        </>
    )
}

export default Login;