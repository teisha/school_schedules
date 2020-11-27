import Link from 'next/link'
import React, { ReactElement } from 'react';

const Nav: React.FC<{}> = (): ReactElement => (
    <div>
        <Link href="/schedules">
            <a>Schedules</a>
        </Link>
        <Link href="/assignments">
            <a>Assignments</a>
        </Link>
    </div>
);

export default Nav