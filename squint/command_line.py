import squint.tools
import argparse

def noise_flam():
    parser = argparse.ArgumentParser(description="A simple program with command-line arguments.")
    parser.add_argument("A", type=float, help="Telescope area times throughput [m^2]")    
    parser.add_argument("F_lambda", type=float, help="flux density [erg/s/cm^2/A]")
    parser.add_argument("lambda0", type=float, help="Wavelength [A]")
    parser.add_argument("T_obs", type=float, help="Exposure time [s]")
    parser.add_argument("sigma_t", type=float,  help="Detector jitter [ps]")

    args = parser.parse_args()

    print(squint.tools.siginv_lam(args.A, args.F_lambda, args.lambda0, args.T_obs, args.sigma_t))


def diffraction_limit():
    parser = argparse.ArgumentParser(description="A simple program with command-line arguments.")
    parser.add_argument("D", type=float, help="Telescope baseline [m]")    
    parser.add_argument("lambda0", type=float, help="Wavelength [A]")

    args = parser.parse_args()

    print(squint.tools.diffraction_limit(args.lambda0, args.D ))