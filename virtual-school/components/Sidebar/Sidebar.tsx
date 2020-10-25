import Link from 'next/link';
import React, { ReactElement } from 'react';
import classes from './Sidebar.module.css'
const Sidebar = (): ReactElement => {
  return (
    <div className={classes.menu}>
      <ul className="list-group">
        <li className={`list-group-item list-group-item-action ${classes.menuItem}`}>
          <Link as={'/login'} href="/login">Login</Link>
        </li>
        <li className={`list-group-item list-group-item-action ${classes.menuItem}`}>
                    Schedules
        </li>
        <li className={`list-group-item list-group-item-action ${classes.menuItem}`}>
                    Assignments
        </li>
      </ul>
            
    </div>
  )
}

export default Sidebar