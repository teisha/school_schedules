/* eslint-disable @typescript-eslint/explicit-function-return-type */
/* eslint-disable indent */
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/globals.css'
import Page from '../containers/Page/Page'
import GlobalState from '../context/GlobalState'


function MyApp({ Component, pageProps }) {
  return (
    <>
      <GlobalState>
        <Page>
          <Component {...pageProps} />
        </Page>
      </GlobalState>
    </>
  )
}

export default MyApp
