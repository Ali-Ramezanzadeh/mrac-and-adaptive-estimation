# HW6 - Discrete-time parameter estimation with PA, OPA, and RLS

This homework studies online identification of a third-order discrete-time system. It compares error-projection and recursive least-squares estimators, then tests forgetting, weighting, covariance resetting, and covariance modification. The original English report contains parameter, predicted-output, and prediction-error plots. Those plots record the original work; the simulations have not been rerun during repository preparation.

Use the [original Live Script](matlab/HW6.mlx) or [readable MATLAB export](matlab/HW6_code_export.m) for the documented PA/OPA/RLS comparisons. The [Simulink model](matlab/HW6.slx) is a separate saved estimation prototype with the differences noted below. See the [English report](reports/report.en.pdf) and [figure gallery](reports/FIGURES.md).

Open the [Simulink model](matlab/HW6.slx), [MATLAB Live Script](matlab/HW6.mlx), [readable code export](matlab/HW6_code_export.m), [original English report](reports/report.en.pdf), or [figure gallery](reports/FIGURES.md).

## System and regressor

The plant uses observable companion form,

$$x(t+1)=\begin{bmatrix}-a_1&1&0\\-a_2&0&1\\-a_3&0&0\end{bmatrix}x(t)+\begin{bmatrix}b_1\\b_2\\b_3\end{bmatrix}u(t),\qquad y(t)=[1,0,0]x(t).$$

The constant-parameter experiment sets $a=[0,-0.01,0]^T$ and $b=[1,0,2]^T$. The report rewrites the input/output relation as

$$y(t)=\phi(t-1)^T\theta_{\mathrm{true}},\qquad \phi(t-1)=[y(t-1),y(t-2),y(t-3),u(t-3),u(t-2),u(t-1)]^T.$$

For this regressor order, $\theta_{\mathrm{true}}=[0,0.01,0,2,0,1]^T$: the output-history entries contain $-a_i$, and the input-history entries reverse the order of the state-space $b_i$.

The report uses white-noise excitation to compare the estimators. Its persistence-of-excitation statement describes the experimental intention; a numerical excitation-rank test is not supplied.

## Part I: Three baseline estimators

- Projection Algorithm (PA): updates the parameter vector by the instantaneous prediction error scaled by $\phi/(\phi^T\phi)$.
- Optimal Projection Algorithm (OPA): uses a covariance-weighted projection, with denominator $\phi^TP\phi$ and an accompanying covariance update.
- Recursive Least Squares (RLS): uses $K=P\phi/(1+\phi^TP\phi)$ and updates both $\hat\theta$ and $P$ recursively.

All methods are evaluated through estimated parameters, true/predicted outputs, and prediction error $e=y-\phi^T\hat\theta$. The report ranks OPA as fastest, PA next, and ordinary RLS slowest in this constant-parameter experiment. This is a comparison for the supplied tuning and input, rather than a universal ranking.

## Part II: Enhanced RLS

Three additional variants are documented:

- Selective data weighting: switches between large and small weights according to the regressor energy $\phi^TP\phi$ and a threshold.
- Exponential data weighting: uses a time-varying forgetting factor with $\alpha(t)=\alpha_0\alpha(t-1)+(1-\alpha_0)$ and covariance scaling by $1/\alpha$.
- Covariance resetting: periodically replaces the covariance matrix with a scaled identity matrix.

The report describes exponential weighting as the fastest of these three methods for its constant-parameter experiment. Selective weighting and resetting also give useful output estimation in the recorded cases.

## Part III: Changing parameters

The report changes the plant's $a$ vector at times 3, 6, and 9, using

$$a(t)=\begin{cases}[0,-0.1,0]^T,&0<t\leq3,\\[0.1,0,-0.2]^T,&3<t\leq6,\\[0,0.1,0]^T,&6<t\leq9,\\[0.1,0,-0.1]^T,&t>9.\end{cases}$$

The state-space input coefficients remain $b=[1,0,2]^T$, although the report's parameter-vector ordering writes them as $[b_3,b_2,b_1]^T=[2,0,1]^T$.

RLS, PA, OPA, and an RLS covariance-modification variant are compared. The modification adds an error-dependent term $\lambda_Q e(t)^2I$ to the covariance update to retain adaptation sensitivity. The report describes this modified estimator as best at following parameter changes in the recorded experiment. PA follows the changes more effectively than ordinary RLS; OPA's declining covariance reduces its ability to adapt later in the run.

## Interpretation and review notes

The original text alternates between “Optimal” and “Orthogonal” for OPA. This repository uses Optimal Projection Algorithm, matching the report's introductory definition and equation heading. The displayed PA update is an instantaneous error projection; it does not include explicit parameter bounds, despite that description in the original discussion.

Check denominators and initial covariance values before changing the excitation: PA and OPA equations can be singular when their regressor energy is zero. Compare methods using the same input realization, initialization, time grid, and stopping time before assigning a quantitative ranking.

The saved Simulink experiment uses a 0.01-second sample period and a 10-second stop time. The Live Script is a separate saved experiment with a 0.1-second sample period and a 40-second horizon. Static connection inspection also found an active output-regression coefficient of -0.01 in the model versus +0.01 in the script. The model's separate canonical-state chain and regression output require reconciliation before comparing the plant representations. Do not expect their transient plots to be numerically identical without aligning those definitions and settings.

The saved model's Product6 block multiplies the regressor, its energy $\phi^T\phi$, and the prediction error. This differs from the script's normalized PA increment, which divides by that energy. Treat the SLX as a prototype and review this block before describing it as the same normalized PA implementation. Original files are preserved; no repair or new simulation has been performed.

The original covariance-modification equations use inconsistent old/new time indices for $P$. The implementation is the relevant record for reproduction; the report alone is insufficient to reconstruct the update order unambiguously.
