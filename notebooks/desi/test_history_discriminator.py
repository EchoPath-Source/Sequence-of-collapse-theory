import unittest
import numpy as np
from history_discriminator import exhaust_history, conditional_mu, trajectories, evaluate

class HistoryTests(unittest.TestCase):
    def test_static_limit(self):
        d=np.full((1,10),-.35)
        self.assertAlmostEqual(exhaust_history(d,np.linspace(0,100,11),1)[0],(1-.15*.65**1.5)/.85)
    def test_order_and_zero(self):
        t=np.linspace(0,8,81); a=np.full(80,.2); b=np.full(80,-.2)
        self.assertGreater(conditional_mu(exhaust_history(a,t,2)),conditional_mu(exhaust_history(b,t,2)))
        self.assertEqual(exhaust_history(np.zeros(80),t,2),1)
    def test_bounds(self):
        with self.assertRaises(ValueError):exhaust_history([.6],[0,1],1)
        with self.assertRaises(ValueError):exhaust_history([0],[1,0],1)
    def test_convergence(self):
        a=trajectories(64,steps=160);b=trajectories(64,steps=320)
        for tau in (1,5):
            g=[conditional_mu(exhaust_history(x[1],x[0],tau))-conditional_mu(exhaust_history(x[2],x[0],tau)) for x in (a,b)]
            self.assertLess(np.max(abs(g[0]-g[1])),2e-5)
        np.linalg.cholesky(a[-1])
    def test_projection(self):
        x=np.linspace(-1,1,20);X=np.column_stack([np.ones(20),x]);s=evaluate(x,X,np.eye(20),x)
        self.assertEqual(s['info'],0)
        s=evaluate(x*x,X,np.eye(20),x)
        self.assertGreater(s['info'],0);self.assertAlmostEqual(s['false_positive'],.05,places=6)

if __name__=='__main__':unittest.main()
