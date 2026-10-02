# HW5 - MRAC and augmented-error designs

This homework compares output-feedback model-reference adaptive control for plants of relative degree one, two, and three. The original report is already in English and includes algebra, Simulink diagrams, and recorded simulation plots. This companion provides a short technical map and identifies points to check when reproducing the work. No MATLAB/Simulink simulations were rerun during repository preparation.

Open the [Simulink model](matlab/HW5.slx), [original English report](reports/report.en.pdf), [assignment sheet](reports/assignment.fa.pdf), or [figure gallery](reports/FIGURES.md).

## Question 1: Relative-degree-one plant

$$W_p(s)=\frac{s+1}{(s-2)(s-1)},\qquad W_m(s)=\frac{1}{s+1}.$$

The reference model is expressed as $(s+1)/(s+1)^2$ for the polynomial calculation. With a regressor filter $1/(s+1)$, the report obtains $C^*(s)=0$ and $D^*(s)=-5s+1$. Its ideal parameters are

$$k^*=1,\qquad \theta_0^*=-5,\qquad \theta_1^*=0,\qquad \theta_2^*=6.$$

The report discusses a strictly positive real error model and the Meyer-Kalman-Yakubovich lemma. It tests step, sinusoidal ($\omega=1$), and white-noise excitation, using $\Gamma=\operatorname{diag}(0.6,0.7,5.4,11)$. It reports tracking-error settling below 10 seconds for the smooth inputs and more fluctuation for white noise. The parameter plot for white noise is reported to approach the algebraic values.

## Question 2: Relative-degree-two plant

$$W_p(s)=\frac{1}{s(s-1)},\qquad W_m(s)=\frac{1}{(s+1)^2}.$$

The minus-sign polynomial identity gives

$$k^*=1,\qquad \theta_0^*=-7,\qquad \theta_1^*=-3,\qquad \theta_2^*=6.$$

The control structure adds a parameter-derivative term,

$$u=\theta^T\omega+\dot\theta^T\bar\omega,$$

to accommodate the higher relative degree. The documented adaptation gains are $\Gamma=\operatorname{diag}(4,95,20,7)$. Step, sinusoidal, and white-noise cases include output, tracking-error, and parameter plots. The report describes fast tracking for smooth inputs and increased error fluctuation under white noise, while retaining convergence in its recorded experiments.

## Question 3: Relative-degree-three plant

$$W_p(s)=\frac{1}{(s+1)(s+2)(s+3)},\qquad W_m(s)=\frac{64}{(s+4)^3}.$$

The report uses an augmented-error structure labelled Error Model 4. It factors the model as

$$W_m(s)=W_1(s)W_2(s),\qquad W_1(s)=\frac{1}{(s+4)^2},\qquad W_2(s)=\frac{64}{s+4}.$$

It introduces filtered regressors, an auxiliary error $e_2$, and an augmented error $\epsilon_1=e_1+W_2(s)e_2$. Step and sinusoidal experiments show plant/model outputs and all three error signals. The recorded report describes convergence of those errors, with a slower sinusoidal transient.

The report lists $\Gamma_\phi=\operatorname{diag}(3,4,5,4,30,60)$ and $\Gamma_\psi=280$. Its reported ideal values are $k^*=64$, $\theta_0^*=7$, $\theta_1^*=[-8,1]^T$, and $\theta_2^*=[-57,34]^T$.

## Interpretation and review notes

These are historical examples, not a common benchmark with freshly measured settling times or error norms. The stability arguments in the original report should be read with their model, sign, filtering, and excitation assumptions. A finite plot does not establish a general global-stability theorem or parameter convergence for every input.

Question 1 prints a positive adaptation-law sign while defining $e_1=y_p-y_m$ and $\phi=\theta-\theta^*$. Reconcile that sign with the implemented summing junctions before reusing the displayed law.

Question 3 contains a filter-basis inconsistency. For its stated

$$\Lambda=\begin{bmatrix}0&1\\-1&-1\end{bmatrix},\qquad l=\begin{bmatrix}1\\2\end{bmatrix},$$

the numerator of $(sI-\Lambda)^{-1}l$ is $[s+3,2s-1]^T$, whereas the report writes $[s+1,2s+1]^T$. Static inspection confirms that the active Q3 model uses the stated matrices. The reported matching coefficients fit the latter written basis, so they should not be treated as the ideal values for the actual filter without recalculating the matching equations. The supplied original report and model remain available alongside this note.

Although the question text mentions Type-1 and Type-2 error augmentation, the report documents one Error Model 4 implementation rather than a separately measured comparison of both methods.
