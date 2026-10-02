# HW4 - Output-feedback MRAC for a plant of relative degree two

This homework develops a model-reference adaptive controller for an unstable second-order plant. The original report is in Persian; this English companion summarizes its design and recorded results. The Simulink model and screenshots are historical project material. The simulations have not been rerun during repository preparation.

Open the [Simulink model](matlab/HW4.slx), the [original Persian report](reports/report.fa.pdf), or the [figure gallery](reports/FIGURES.md).

## Problem and model matching

The plant and reference model are

$$W_p(s)=\frac{2}{s^2-3s+2},\qquad W_m(s)=\frac{2}{s^2+3s+2}.$$

The report first argues that adding proper feedforward and feedback controllers cannot reduce the plant's relative degree. It then uses a polynomial model-matching identity with a first-order regressor filter, $\Lambda=-3$, $l=1$, and $\lambda(s)=s+3$.

With $C^*(s)=\theta_1^*$ and $D^*(s)=\theta_0^*(s+3)+\theta_2^*$, the final reported parameters are

$$k^*=1,\qquad \theta_0^*=-18,\qquad \theta_1^*=-6,\qquad \theta_2^*=60.$$

These values satisfy the minus-sign matching convention used in the report's final expansion:

$$((s+3)-\theta_1^*)(s^2-3s+2)-2[\theta_0^*(s+3)+\theta_2^*]=(s^2+3s+2)(s+3).$$

## Adaptive structure

The controller uses a parameter-derivative term to handle the plant's relative degree:

$$u=\theta^T\omega+\dot\theta^T\bar\omega,\qquad \bar\omega=\frac{1}{s+a}\omega.$$

The parameter vector is ordered as $\theta=[k,\theta_1,\theta_0,\theta_2]^T$, and the report gives

$$\dot\theta=-\Gamma\,\operatorname{sgn}(k_p)e_1\bar\omega,\qquad e_1=y_p-y_m.$$

The report states that its simulation uses integrators for the auxiliary filtered regressor, corresponding to $a=0$.

## Recorded experiments

Three input cases are documented:

- A sum of three sinusoidal signals, with plant/model outputs, tracking error, and adaptive parameters.
- A step-plus-sinusoid signal, with the same outputs and parameter trajectories.
- Band-limited white noise, with $\Gamma=\operatorname{diag}(2.5,16,18,30)$.

For the noise-driven case, the report describes parameter settling in approximately 150 seconds and convergence toward the algebraic matching values. This is a reported observation from the supplied plots, rather than a numerical result recalculated from simulation data.

The original figure assets are Sim.png, Plant.png, 3Sine.png, Error_3Sine.png, Parameters_3sine.png, Step_sine.png, Error_step_sine.png, Parameters_step_sine.png, final.png, error_final.png, and Parm_final.png.

## Interpretation and review notes

Output tracking and identification of the ideal parameter vector are different conclusions; successful tracking alone does not establish parameter convergence for an arbitrary reference input. The supplied plots are useful for comparing the effect of excitation, but no exported numerical trajectories or common error metrics were supplied.

The original algebra starts with a plus-sign Bezout identity and later changes to a minus sign. The final parameter values agree with the latter convention; use that convention when following the calculation.

The simulation choice $a=0$ makes the auxiliary filter an integrator. It is not a strictly stable first-order filter. Treat its reported convergence as an empirical result for the supplied examples, and revisit the assumptions before generalizing the stability argument.
