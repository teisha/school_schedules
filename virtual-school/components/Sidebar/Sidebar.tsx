import Link from 'next/link';
import React, {FunctionComponent, ReactElement, useContext } from 'react';
import classes from './Sidebar.module.css'
import AuthContext from '../../context/auth-context'

type Props = {
  // posts: readonly RedditPost[];
  // subreddit: string;
};

// eslint-disable-next-line no-empty-pattern
const Sidebar: FunctionComponent<Props> = ({}): ReactElement => {
    const context = useContext(AuthContext)

    return (
        <div className={classes.menu}>
            <p className={`ml-1 ${classes.username}`}>
                    { context.user?.firstname }
            </p>
            <ul className="list-group">
                <li
                    className={`list-group-item list-group-item-action ${classes.menuItem}`}
                >
                    <Link as={'/login'} href="/login">
            Login
                    </Link>
                </li>
                <li
                    className={`list-group-item list-group-item-action ${classes.menuItem}`}
                >
          Student
                </li>

            </ul>
        </div>
    );
};

export default Sidebar