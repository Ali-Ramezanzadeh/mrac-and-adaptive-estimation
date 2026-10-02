# HW3 — Nonminimal Adaptive Observer Design

This homework develops an adaptive output observer for stable and unstable third-order plants. It discusses an observable canonical realization, a classical observer, a filtered nonminimal regressor structure, parameter adaptation, and Simulink experiments with different inputs.

The original report is Persian and credits Ali Ramezanzadeh, Amirkabir University of Technology, Department of Electrical Engineering, and course instructor Dr. Talebi. This overview is an English technical companion, with corrections to arithmetic clearly separated from the preserved original report.

Files: [Simulink model](matlab/HW3.slx), [original Persian report](reports/report.fa.pdf), and [original figures](reports/FIGURES.md).

## Plants

The stable plant is

$$G_s(s)=\frac{(s+1)(s+1.5)}{(s+2)(s+3)(s+4)}.$$

The unstable case replaces the pole at $-3$ with a pole at $+3$:

$$G_u(s)=\frac{(s+1)(s+1.5)}{(s+2)(s-3)(s+4)}.$$

The report gives observable canonical state-space matrices. For both plants, $B=[1.5,2.5,1]^T$ and $C=[0,0,1]$. The stable $A$ has final column $[-24,-26,-9]^T$; the unstable $A$ has final column $[24,10,-3]^T$, with the remaining nonzero entries $A_{21}=A_{32}=1$.

The classical observer is written as

$$\dot{\hat x}=A\hat x+Bu+L(y-\hat y),\qquad \hat y=C\hat x,$$

with observer gain $L$ selected by pole placement.

## Adaptive observer

The nonminimal structure uses filters driven by the input and the estimated output, an output-estimation error $e_1=\hat y_p-y_p$, and a six-entry regressor:

$$\hat\omega=[u,\hat\omega_1^T,y_p,\hat\omega_2^T]^T.$$

The report selects

$$\Lambda=\operatorname{diag}(-1,-2),\qquad l=[1,1]^T,\qquad\lambda=3,$$

and presents a Lyapunov-based parameter update law

$$\dot{\hat\theta}=-e_1\,\Beta\hat\omega.$$

The reported final diagonal adaptation matrix is

$$\Beta=\operatorname{diag}(0.4,100,300,100,5000,0.5).$$

The report also includes polynomial matching between the filtered observer and the plant. Its stable-case parameter trajectories are shown in the original figures.

## Historical experiments

- **Stable plant, step input:** output comparison, estimation error, and adaptive parameter trajectories.
- **Stable plant, band-limited white noise:** output, error, and parameter trajectories. The report estimates roughly 110 seconds for parameter settling with its tuned gains.
- **Unstable plant, step input:** a four-second simulation, shortened because of slow computation. The supplied error plot does not show convergence to zero and its envelope increases again toward the end of the interval. This short run does not establish long-term boundedness or stability.

## Arithmetic and notation caveats

The report's printed unstable denominator expansion and some listed observer coefficients disagree with its stated transfer functions. The original files are retained without modification.

The denominator implied by $(s+2)(s-3)(s+4)$ is

$$s^3+3s^2-10s-24,$$

consistent with the report's unstable state-space matrix. The printed $s^3+5s^2-2s-24$ is an arithmetic inconsistency.

For the particular polynomial formula printed in the report,

$$G_o(s)=\frac{c_0s^2+(c_1+c_2+3c_0)s+(2c_0+2c_1+c_2)}{s^3+(6-d_0)s^2+(11-d_1-d_2-3d_0)s+(6-2d_0-2d_1-d_2)},$$

matching the stable plant yields

$$[c_0,c_1,c_2,d_0,d_1,d_2]=[1,0,-0.5,-3,-6,0].$$

The stable report text lists the last two entries in the opposite order. Its `Parameters_final.png` figure approaches the vector $[-6,0]$; static inspection of the model's filter ordering supports that interpretation, indicating a likely transcription error in the text. Matching the unstable transfer function to the same printed formula gives $[1,0,-0.5,3,12,0]$; the original report's unstable coefficient list differs.

These are algebra checks of the stated formula. They are not a new simulation result or a replacement of the model's saved implementation. Filter-output conventions and regressor ordering must be checked in the Simulink model before applying coefficient changes.

## Running and evidence

The submitted model is `HW3.slx`. Select the appropriate plant and excitation, then confirm filter conventions, parameter ordering, gains, initial conditions, solver, and simulation duration. The four-second unstable experiment and long stable experiment require different configurations.

No MATLAB or Simulink simulation was rerun while preparing this repository. All displayed trajectories originate from the submitted coursework.
