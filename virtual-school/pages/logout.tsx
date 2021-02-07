import React, { useContext, useEffect, useState } from 'react'
import { Button } from 'react-bootstrap'
import AuthContext from '../context/auth-context'
import ICognitoConfig from '../models/ICognitoConfig'
import { CognitoService } from '../services/CognitoService'



const Logout: React.FC<{}> = ()  => {
    const context = useContext(AuthContext)
    const cognito = new CognitoService()
    const [error, setError] = useState(null)
    useEffect(() => {
        try {
            context.logout()
            cognito.logout(process.env.config as unknown as ICognitoConfig);
        } catch (err){
            setError(err.message)
        }

    })

    return  (
        <>
            <p> Am I logged in? </p>
            <p>{context.isLoggedIn 
                ? <Button variant="success" size="sm">Yes</Button> 
                : <Button variant="danger" size="sm">No</Button> 
            }</p>
        </>
    )
}

export default Logout;
