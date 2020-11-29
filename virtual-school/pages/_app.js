/* eslint-disable @typescript-eslint/explicit-function-return-type */
/* eslint-disable indent */
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/globals.css'
import GlobalState from '../context/GlobalState'


function MyApp({ Component, pageProps }) {
  return (
    <GlobalState>
      <Component {...pageProps} />
    </GlobalState>
  )
}

export default MyApp
