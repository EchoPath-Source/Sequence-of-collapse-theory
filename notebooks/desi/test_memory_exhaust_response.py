import unittest
import math
from scipy.integrate import solve_ivp
from memory_exhaust_response import q,rate,step,paired,toy_h,growing_mode

class ResponseTests(unittest.TestCase):
    def test_static(self):
        self.assertAlmostEqual(q(0),1)
        self.assertAlmostEqual(toy_h(step(0,q(-.35)-1,100,1)),69.31179362943229)
    def test_pair(self):
        for tau in (.1,1,5,10):
            for k in (0,.05,.2):
                a,b,d=paired(tau,ell=10,k=k)
                self.assertAlmostEqual(a-b,d,places=12)
                self.assertGreater(d,0)
    def test_ode(self):
        tau,ell,k=2,10,.05
        u=.02;s=-.07
        sol=solve_ivp(lambda t,y:[s/tau-rate(tau,ell,k)*y[0]],(0,3),[u],rtol=1e-11,atol=1e-13)
        self.assertAlmostEqual(sol.y[0,-1],step(u,s,3,tau,ell,k),places=10)
    def test_limits(self):
        self.assertLess(paired(.01)[2],1e-30)
        self.assertLess(paired(1e6)[2],1e-10)
        self.assertLess(paired(5,ell=30,k=.1)[2],paired(5)[2])
    def test_growing(self):
        self.assertTrue(0<growing_mode(1,10,.05)<growing_mode(1,0,.05)<1)
        self.assertGreater(growing_mode(10,0,0,initial='equilibrium'),growing_mode(10,0,0))
    def test_domain(self):
        for d in (-1,.6,float('nan')):
            with self.assertRaises(ValueError):q(d)
        with self.assertRaises(ValueError):rate(0,1,1)

if __name__=='__main__':unittest.main()
