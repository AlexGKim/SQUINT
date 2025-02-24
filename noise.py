# implementation of the signal-to-noise equation in Eq 13 of Dalal et al.

import numpy
import astropy
import astropy.units as u
import argparse

def siginv_nu(A, F_nu, nu0, T_obs, sigma_t=5e-12):
	ans = A * F_nu / astropy.constants.h.to(u.erg*u.s) / nu0 * numpy.sqrt(T_obs/sigma_t) * (128*numpy.pi)**(-0.25)
	return ans.decompose()

def siginv_lam(A, F_lambda, lambda0, T_obs, sigma_t):
	A = A * u.m**2
	F_lambda = F_lambda * u.erg/u.s/(u.AA)/u.cm**2
	lambda0 = lambda0 * u.AA
	T_obs = T_obs * u.s
	sigma_t = sigma_t*1e-12 * u.s
	F_nu = F_lambda.to(u.erg / (u.s * u.cm**2 * u.Hz), u.spectral_density(lambda0))
	nu0 = lambda0.to(u.Hz, u.spectral())
	return siginv_nu(A, F_nu, nu0, T_obs, sigma_t)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple program with command-line arguments.")
    parser.add_argument("A", type=float, help="Telescope area times throughput [m^2]")    
    parser.add_argument("F_lambda", type=float, help="flux density [erg/s/cm^2/A]")
    parser.add_argument("lambda0", type=float, help="Wavelength [A]")
    parser.add_argument("T_obs", type=float, help="Exposure time [s]")
    parser.add_argument("sigma_t", type=float,  help="Detector jitter [ps]")

    args = parser.parse_args()

    print(siginv_lam(args.A, args.F_lambda, args.lambda0, args.T_obs, args.sigma_t))