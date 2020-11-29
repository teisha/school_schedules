/* eslint-disable @typescript-eslint/no-unused-vars */
import { Context, createContext } from 'react';
import IAuthToken from '../models/IAuthToken';
import IUser from '../models/IUser';

export default createContext<{
    user: IUser | null;
    token: IAuthToken | null;
    login: (_token: string) => void;
    logout: (_token: string) => void;
        }>({
            user: null,
            token: null,
            login: (_token: string): void => {},
            logout: (_token: string): void => {},
        });
        
// <{
//     user: IUser | null;
//     token: IAuthToken | null;
//     login: (_token: string) => void;
//     logout: (_token: string) => void;
//         }>

// export function AuthProvider({ children }: any) {
//   const [user, setUser] = useState<IUser | null>(null);

//   useEffect( () => {
//     //get from api backend and populate user
//   }, [user])
//   // handle auth logic here...

//   return (
//     < AuthContext.Provider value={{ user }}> {children} </AuthContext.Provider>
//   );
// }
