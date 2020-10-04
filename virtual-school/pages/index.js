import Head from 'next/head'
import styles from '../styles/Home.module.css'

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>Virtual School</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>
          <span className={styles.modern}> Virtual</span>
          <span className={styles.classic}> School</span>
        </h1>

        <p className={styles.description}>
          Figure out a student's day with an automated calendar.
        </p>

        <section className={styles.grid}>
          <article className={styles.card}>
            <img className={styles.image} src="/computer calendar.svg" alt="virtual school schedule"></img>
            <p>
              To sign up, <a href="mailto:bunnyballoon467-laimasoft@yahoo.com?Subject=VirtualSchool">send a reqest</a>
            </p>
          </article>
        </section>
      </main>

      <footer className={styles.footer}>
        <a
          href="http://laimab.x10host.com/wp/"
          target="_blank"
          rel="noopener noreferrer"
        >
          Powered by{' '}
          <img src="/LaimaSoft-Logo-XD-300x239.png" alt="Laimasoft Logo" className={styles.logo} />
        </a>
      </footer>
    </div>
  )
}
