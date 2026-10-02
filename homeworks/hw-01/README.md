# HW1 — Lyapunov-Based Adaptive Parameter Estimation

This homework implements adaptive estimators for a first-order scalar plant and a second-order state-space plant in Simulink. The original submission includes complete English and Persian reports, their LaTeX sources, model diagrams, and historical parameter-estimation plots. Both reports credit Ali Ramezanzadeh.

Files: [Simulink model](matlab/Adaptive.slx), [English report](reports/report.en.pdf), [Persian report](reports/report.fa.pdf), and [original figures](reports/FIGURES.md).

## Scalar estimator

The plant is

$$\dot{x}_p=-x_p+u.$$

The estimator uses a stable auxiliary coefficient $a_m=-2$:

$$\dot{\hat{x}}_p=a_m\hat{x}_p+(\hat{a}_p-a_m)x_p+\hat{k}_p u,$$

with estimation error $e=\hat{x}_p-x_p$ and update laws

$$\dot{\hat{a}}_p=-\gamma_1 e x_p,\qquad
\dot{\hat{k}}_p=-\gamma_2 e u.$$

The report varies the adaptation gains to improve the transient response and uses a sinusoidal excitation. The true parameter values are $a_p=-1$ and $k_p=1$. The supplied plot of $\hat{a}_p$ approaches the dashed $-1$ reference after an initial transient; the plots are original submission evidence rather than newly generated results.

## State-space estimator

The second plant is

$$\dot{X}_p=A_p X_p+B_p u,\qquad
A_p=\begin{bmatrix}0&1\\-2&-2\end{bmatrix},\quad
B_p=\begin{bmatrix}0\\1\end{bmatrix}.$$

The auxiliary matrix is $A_m=-2I$, and the estimator is

$$\dot{\hat{X}}_p=A_m\hat{X}_p+(\hat{A}_p-A_m)X_p+\hat{B}_p u.$$

For $e=\hat{X}_p-X_p$, the adaptation laws are

$$\dot{\hat{A}}_p=-\gamma_1 P e X_p^T,\qquad
\dot{\hat{B}}_p=-\gamma_2 P e u^T.$$

The report selects $Q=I$ in $P A_m+A_m^T P=-Q$, giving $P=0.25I$. A composite sinusoidal excitation is used for the six estimated entries of $A_p$ and $B_p$. The historical plots compare the estimates with each true matrix entry; the four $A_p$ traces approach $0$, $1$, $-2$, and $-2$.

## Experiments and interpretation

- Compare estimated parameters with the known plant parameters.
- Observe the initial transient and the effect of adaptation gains.
- Compare scalar and vector estimation structures.
- Examine the excitation used to support parameter identification.

The report describes one sinusoid for the scalar case and three sinusoidal components for the vector case. These are the chosen experiment inputs; the report does not provide a separate persistent-excitation proof, so the number of sinusoids should not be presented as a general sufficiency rule.

## Running and evidence

The submitted model is `Adaptive.slx`. Its saved blocks and configuration are the starting point for reproduction. Confirm the active excitation, gain values, initial conditions, solver, and stop time before trying to reproduce a particular figure. The report does not tabulate final numerical values for $\gamma_1$ and $\gamma_2$.

No MATLAB or Simulink simulation was rerun while preparing this repository. The preserved PDFs and images document the original experiments.
