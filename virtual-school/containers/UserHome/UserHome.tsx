import React, { useState, useContext, useEffect } from 'react'
import { Button, Card } from 'react-bootstrap'
import { isPropertySignature } from 'typescript'
import AuthContext from '../../context/auth-context'
import withAuth from '../../hoc/withAuth'
import IUser from '../../models/IUser'


const UserHome = (props) => {
    const [user, setUser] = useState<IUser | null>(null)
    const context = useContext(AuthContext)

    useEffect( () => {
        console.log(`IsLoggedIn: ${props.isLoggedIn ? 'Y' : 'N'}`)
        console.log(`PROPS PASSED: ${JSON.stringify(props.user)}`)
        setUser(context.user)
        console.log(context)
        console.log('Home page for ' + context.user?.username)
    }, [])

    return (
        <>
            <p>{context.isLoggedIn 
                ? <Button variant="success" size="sm">Yes</Button> 
                : <Button variant="danger" size="sm">No</Button> 
            }</p>
            { props.isLoggedIn
            ? <>
                <Card>
                    <Card.Title><h1> Welcome {user?.firstname}</h1></Card.Title>
                    <Card.Body>
                        <ul>
                            { user?.students 
                                ? user.students.map( studentName => {
                                return (<li id={studentName}> {studentName} </li> )
                                })
                                : <p> Sign up students to view a schedule. </p>
                            }
                        </ul>
                    </Card.Body>
                </Card>
            </>
            : <>
                <h1> Wait for it ...</h1>
                <span> {JSON.stringify(context)} </span>
            </>
            }
        </>
    )


}

export default withAuth(UserHome);