/* eslint-disable @typescript-eslint/explicit-function-return-type */
// Next.js API route support: https://nextjs.org/docs/api-routes/introduction

import { NextApiRequest, NextApiResponse } from 'next';

const login = async (req: NextApiRequest, res: NextApiResponse) => {
  const username: string = req.body.username;
  const password: string = req.body.pass;

  if (req.method === 'POST') {
    res.status(200).json({ sessionId: '1234567890' });
  } else {
    res.status(405).json({ message: 'We only support POST' });
  }
};

export default login;
