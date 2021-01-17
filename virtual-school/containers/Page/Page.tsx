import styles from './Page.module.css'
import React from 'react'
import Sidebar from '../../components/Sidebar/Sidebar'
import Meta from '../../components/Meta'

const Page = (props) => {
    return (
        <>
        <Meta />
        <div className="container-fluid px-0 my-0 mx-0 h-100">
            <div className="row  mx-0 h-100">
                <div className="col col-2 px-0">
                    <Sidebar />
                </div>
                <main className={`col-10 col-md-4 pt-3 px-0 ${styles.main}`}>
                    {props.children}
                </main>
            </div>
        </div>
        <footer className={styles.footer}>
            <a
                href="http://laimab.x10host.com/wp/"
                target="_blank"
                rel="noopener noreferrer"
            >
        Powered by{' '}
                <img
                    src="/LaimaSoft-Logo-XD-300x239.png"
                    alt="Laimasoft Logo"
                    className={styles.Logo}
                />
            </a>
        </footer>
        </>
    )
}

export default Page