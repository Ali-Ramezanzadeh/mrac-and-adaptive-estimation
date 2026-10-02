# MRAC and Adaptive Estimation in MATLAB/Simulink

Six Adaptive Control homework projects by **Ali Ramezanzadeh**, covering model reference adaptive control (MRAC), adaptive observers, and online parameter estimation. The repository combines mathematical design, Simulink implementations, and the original simulation reports.

| Homework | Focus | Main methods |
|---|---|---|
| [HW1](homeworks/hw-01/README.md) | Adaptive system identification | Scalar and state-space estimators; Lyapunov-based update laws |
| [HW2](homeworks/hw-02/README.md) | Linear and nonlinear MRAC | Direct/indirect adaptation; input-gain boundary protection |
| [HW3](homeworks/hw-03/README.md) | Adaptive output observation | Nonminimal filters; stable/unstable plant experiments |
| [HW4](homeworks/hw-04/README.md) | Output-feedback MRAC | Relative-degree-two design; filtered regressors |
| [HW5](homeworks/hw-05/README.md) | Higher-relative-degree MRAC | Polynomial matching; derivative and augmented-error structures |
| [HW6](homeworks/hw-06/README.md) | Discrete-time parameter estimation | PA, OPA, RLS; weighting, resetting, and covariance modification |

![Original HW5 MRAC implementation](homeworks/hw-05/reports/figures/Q1Main.png)

## Included files

- Six original `.slx` models, preserved unchanged.
- The original HW6 `.mlx` Live Script and a readable `.m` export of its twelve code sections.
- English guides for every homework, original English/Persian PDFs, and 99 supplied figure assets.
- Original report LaTeX sources, figures, and report variants in [archive/](archive/README.md).
- [Simulation instructions](docs/SIMULATION.md), [report index](docs/REPORTS.md), and [verification record](docs/VERIFICATION.md).

## Open a model

In MATLAB, make this repository your current folder:

```matlab
addpath('scripts');
open_homework(1);
```

Select the relevant subsystem/input and use Run in Simulink. Models were saved in **R2022b**. Their saved stop times range from 10 to 1500 seconds; the configuration table and HW6 script differences are in [SIMULATION.md](docs/SIMULATION.md).

## Evidence and scope

The PDFs and figures document the original coursework experiments. Repository preparation checks file integrity, model archive structure, saved settings, and Live Script code preservation. **MATLAB/Simulink simulations were not rerun here.** Reported settling behavior is labeled historical, and formula/notation issues are identified in the homework guides.

Tracking error approaching zero and parameter estimates reaching their true values are separate observations; the supplied examples should be interpreted with their excitation, tuning, and plant assumptions.

HW6's Live Script contains the documented PA/OPA/RLS comparisons. Its SLX is retained as a separate estimation prototype with update/configuration differences explained in the homework guide.

## Credits

The supplied reports credit Ali Ramezanzadeh and identify Amirkabir University of Technology, Department of Electrical Engineering, and Dr. Talebi. This repository presents coursework as coursework. See [credits and provenance](docs/CREDITS.md).

No source-code license has been selected.
