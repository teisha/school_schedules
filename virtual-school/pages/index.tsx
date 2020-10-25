import Head from 'next/head'
import Home from '../containers/Home/Home'

// eslint-disable-next-line @typescript-eslint/explicit-function-return-type
function Index() {
  return (
    <>
      <Head>
        <title> Virtual School </title>
        <link rel="icon" href="/favicon.ico" />
        <meta name="viewport" content="initial-scale=1.0, width=device-width" />
      </Head>
      <Home />
    </>
  )
}

export default Index


/*
  5 |         <Head>
  6 |             <title>Virtual School < /title>
  7 |             <link rel="icon" href="/favicon.ico" />
*/