import Link from 'next/link';

import classes from './Sidebar.module.css'
const Sidebar = (props) => {
    return (
        <div className={classes.menu}>
            <ul className="list-group">
                <li className="list-group-item list-group-item-action">
                    <Link as={'/login'} href="/login">Login</Link>
                </li>
                <li className="list-group-item list-group-item-action">
                    Schedules
                </li>
                <li className="list-group-item list-group-item-action">
                    Assignments
                </li>
            </ul>
            
        </div>
    )
}

export default Sidebar