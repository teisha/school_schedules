import Link from 'next/link';
import React, {FunctionComponent, ReactElement } from 'react';
import classes from './Sidebar.module.css'

type Props = {
  // posts: readonly RedditPost[];
  // subreddit: string;
};

// eslint-disable-next-line no-empty-pattern
const Sidebar: FunctionComponent<Props> = ({}): ReactElement => {
  return (
    <div className={classes.menu}>
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
          Schedules
        </li>
        <li
          className={`list-group-item list-group-item-action ${classes.menuItem}`}
        >
          Assignments
        </li>
      </ul>
    </div>
  );
};

export default Sidebar