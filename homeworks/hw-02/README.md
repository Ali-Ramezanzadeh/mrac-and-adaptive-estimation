# HW2 — Direct and Indirect Model Reference Adaptive Control

This homework compares direct and indirect MRAC for a scalar linear plant and implements a direct adaptive controller for a nonlinear plant. The original submission credits Ali Ramezanzadeh, Amirkabir University of Technology, Department of Electrical Engineering, and course instructor Dr. Talebi.

The Persian report contains the full figures and additional Lyapunov derivations. The supplied English report is a partial companion: its simulation section contains literal ellipses and a figure-placeholder sentence. This English repository overview therefore summarizes both sources and identifies equations that require review.

Files: [Simulink model](matlab/HW2.slx), [full Persian report](reports/report.fa.pdf), [original English draft](reports/report.en-draft.pdf), and [original figures](reports/FIGURES.md).

## Linear plant and reference model

The plant and reference model are

$$\dot{x}_p=3x_p+0.5u,\qquad
\dot{x}_m=-2x_m+2r.$$

The control law is $u=Kr+\theta x_p$. For these nominal parameters, the matching values calculated from the report's formulas are $K^*=4$ and $\theta^*=-10$.

In direct MRAC, the tracking error is $e=x_p-x_m$, and the report uses

$$\dot K=-\beta_1\operatorname{sgn}(k_p)e r,\qquad
\dot\theta=-\beta_2\operatorname{sgn}(k_p)e x_p.$$

The reported final adaptation gains are $\beta_1=4.5$ and $\beta_2=5$.

In indirect MRAC, the estimated plant coefficients $\hat a_p$ and $\hat k_p$ are used to calculate controller gains. The report defines the estimator error as $e=\hat x_p-x_p$ and updates $\hat a_p$ using $-\beta_2 e x_p$. A conditional update of $\hat k_p$ is intended to keep the estimated input gain away from zero. The report gives a lower bound of $0.1$, an example initial value of $0.2$, and final gains $\beta_1=1$, $\beta_2=8$.

## Nonlinear experiment

The stated plant is

$$\dot{x}_p=3x_p+2\sin^2(x_p)+x_p^3+u.$$

The report proposes $u=Kr+\theta_1 x_p+\theta_2 f(x_p)$ and corresponding error-times-regressor update laws for $K$, $\theta_1$, and $\theta_2$. Its selected gains are $(1,3,5.5)$, tuned for a reference with sinusoidal components at frequencies $1$, $2$, and $10$ as written in the report. These settings describe that experiment rather than a controller specification for arbitrary inputs.

## Historical results

The Persian report includes thirteen figures covering the three Simulink structures, adaptive parameter trajectories, reconstruction of plant coefficients, and error signals. It estimates an approximately seven-second parameter settling time for the illustrated direct linear and nonlinear cases.

Some displayed reconstructed coefficients initially become very large because they are calculated by division using small or zero adaptive gains. The report explicitly identifies these as display signals rather than signals used in the direct controller.

The report describes better tracking in its sinusoidal-input experiments and residual error in some indirect and step-input experiments. These observations concern the submitted configuration. They do not establish that every MRAC system fails to track a step, or that smooth reference signals alone guarantee parameter convergence.

## Original report issues to review

The submitted models and PDFs are preserved. Several expressions in the report need checking before treating its derivations as verified theory:

1. **Indirect estimator:** the report prints the correction term $(\hat a_p-a_p)x_p$ while its stated error equation assumes the auxiliary coefficient $a_m$ in that position. Static inspection of the model found the implemented correction $(\hat a_p-a_m)x_p$, consistent with the HW1 estimator structure.
2. **Input-gain boundary:** the prose and the final Persian piecewise rule give different signs for the condition at the lower bound. The embedded MATLAB Function allows the update when $eu<0$ or the estimate is above the bound, and otherwise sets the derivative to zero. The model therefore implements the intended lower-bound protection.
3. **Nonlinear matching:** the report sets $f(x_p)=\sin^2(x_p)+x_p^3$, but the stated plant has coefficients $2$ and $1$ on those two nonlinear terms. The actual model uses $f(x_p)=x_p^3+2\sin^2(x_p)$, preserving the factor omitted from that printed regressor.
4. **Lyapunov derivations:** some displayed steps omit reference factors or gain scaling that appear in the controller laws. The report is coursework evidence, not a complete independently checked stability proof.

## Running and evidence

The submitted model is `HW2.slx`. Reproduction requires selecting the intended direct, indirect, or nonlinear subsystem and checking reference signals, adaptation gains, initial conditions, solver settings, and stop time. One saved model state should not be assumed to reproduce every historical figure automatically.

No MATLAB or Simulink simulation was rerun while preparing this repository. The original reports and figures remain the evidence for the reported experiments.
