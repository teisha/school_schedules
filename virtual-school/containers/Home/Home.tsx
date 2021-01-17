
import styles from './Home.module.css'
import React, { ReactElement } from 'react';
import { Card } from 'react-bootstrap';

const Home = (): ReactElement => {
    return (
        <>
            <h1 className={styles.title}>
                <span className={styles.modern}> Virtual </span>
                <span className={styles.classic}> School </span>
            </h1>
            <p className={styles.description}>
    Figure out a student's day with an automated calendar.
            </p>

            <section className={`col col-12 mx-auto  ${styles.Grid}`}>
                <Card className={`card mx-auto ${styles.Card}`}>
                    <Card.Body>
                        <Card.Text>
                        <span className="card-text text-center">
        To sign up,{' '}
                            <a href="mailto:bunnyballoon467-laimasoft@yahoo.com?Subject=VirtualSchool">
                                {' '}
            send a request{' '}
                            </a>
                        </span>
                        </Card.Text>
                    </Card.Body>
                    <Card.Img className={`card-img-top ${styles.CardImage}`} variant="bottom" src="/computer calendar.svg" alt="virtual school schedule" />
                </Card>

                {/* <article className={`card mx-auto ${styles.Card}`}>
                    <img
                        className={`card-img-top ${styles.CardImage}`}
                        
                        alt="virtual school schedule"
                    />
                    <div className="card-body">

                    </div>
                </article> */}
            </section>

        </>
    );
};

export default Home


/*
    <>
        < div className="container-fluid px-0 my-0 mx-0" >
            <div className={`row ${styles.row}`} >
                <div className="col col-2">
                    <Sidebar   />
                </div>
                <main className={`col-10 col-md-4 px-0 ${styles.main}`} >
                    <h1 className={styles.title }>
                        <span className={styles.modern }> Virtual < /span>
                        <span className={styles.classic } > School < /span>
                    < /h1>

                    <p className={styles.description } >
                        Figure out a student's day with an automated calendar.
                    < /p>

                    <section className={styles.Grid } >
                        <article className="card">
                            <img className={styles.image }
                                src = "/computer calendar.svg"
                                alt = "virtual school schedule" />
                            < p >
                                To sign up, <a href="mailto:bunnyballoon467-laimasoft@yahoo.com?Subject=VirtualSchool" > send a request < /a>
                            < /p>
                        < /article>
                    < /section>
                </main>
            </div>
        </div>
        < footer className={styles.footer } >
            <a href="http://laimab.x10host.com/wp/"
                target = "_blank"
                rel = "noopener noreferrer"
            >
                Powered by{ ' ' }
            <img src="/LaimaSoft-Logo-XD-300x239.png" alt="Laimasoft Logo" className={styles.Logo } />
            </a>
        < /footer>
    < />
*/