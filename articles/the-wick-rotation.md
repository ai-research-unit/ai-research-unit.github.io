

# The Wick Rotation

## Introduction

The **Wick rotation** is a mathematical procedure used throughout quantum field theory, statistical mechanics, and condensed-matter physics. It consists of the analytic continuation of the time coordinate to imaginary values,

$$
t \to -i\tau,
$$

with $\tau$ real. Under this substitution, the Lorentzian structure of spacetime is replaced by a Euclidean one: the wave operator becomes the Laplacian, oscillating phases become decaying exponentials, and the Feynman path integral becomes a statistical-mechanical partition function.

The Wick rotation is one of the most useful tricks in theoretical physics. It is also one of the most mysterious. It works, spectacularly well, across a vast range of problems. But it is not a theorem of quantum field theory: it is a heuristic that requires the fields to extend analytically in the time coordinate, and the precise conditions under which it is justified are not always clear. In this sense, it is genuinely a **trick** — a clever manipulation that gives correct answers when it works, and whose justification is often deferred.

This article describes the Wick rotation as it is used in practice. It is confined to established physics. It presents the rotation as a trick, which is what it is, and lists the problems to which it is applied and the reasons it is useful. A companion article will extend the rotation to the biquaternion framework, where it acquires a structural interpretation.

The conventions are the standard ones of relativistic quantum field theory. The metric has signature $(-,+,+,+)$ in natural units $\hbar = c = 1$, so that

$$
ds^2 = -dt^2 + d\mathbf{x}^2.
$$

The d'Alembertian (wave operator) is

$$
\Box = -\frac{\partial^2}{\partial t^2} + \nabla^2.
$$

## The Problem

The central object of quantum field theory is the **path integral**,

$$
Z = \int \mathcal{D}\phi\; e^{iS[\phi]},
$$

where $S[\phi]$ is the action functional of the field $\phi$, and the integral is over all field configurations. The path integral provides a formal expression for transition amplitudes, correlation functions, and the partition function of the theory.

The integrand $e^{iS[\phi]}$ is a **complex phase of unit modulus**. It does not decay as the fields become large; it oscillates. The integral

$$
\int \mathcal{D}\phi\; e^{iS[\phi]}
$$

is therefore not absolutely convergent. It is an oscillatory integral over an infinite-dimensional space of fields. Making rigorous mathematical sense of such an integral is the central technical problem of constructive quantum field theory, and it is not solved in general.

The path integral is nevertheless used constantly in practice, because it gives correct perturbative results (via Feynman diagrams), correct anomaly computations, and correct non-perturbative results when supplemented by appropriate techniques (instantons, lattice gauge theory, etc.). The heuristic is powerful, and it is the foundation of modern theoretical physics.

But the oscillatory nature of the integrand is a genuine obstacle. It is the origin of the divergences of perturbation theory, of the difficulty of defining the measure, and of the analytic subtlety of the whole framework.

## The Wick Rotation

The Wick rotation is the substitution

$$
t \to -i\tau, \qquad \tau \in \mathbb{R},
$$

in the time coordinate. Under this substitution, derivatives transform as

$$
\frac{\partial}{\partial t} = i\frac{\partial}{\partial \tau}, \qquad \frac{\partial^2}{\partial t^2} = -\frac{\partial^2}{\partial \tau^2}.
$$

The consequences are as follows.

**The metric becomes Euclidean.** The invariant interval

$$
ds^2 = -dt^2 + d\mathbf{x}^2
$$

becomes

$$
ds^2 = d\tau^2 + d\mathbf{x}^2,
$$

which is the ordinary Euclidean metric on $\mathbb{R}^4$ with all four directions contributing with the same sign.

**The wave operator becomes the Laplacian.** The d'Alembertian

$$
\Box = -\frac{\partial^2}{\partial t^2} + \nabla^2
$$

becomes

$$
\Box_E = \frac{\partial^2}{\partial \tau^2} + \nabla^2,
$$

which is the four-dimensional Laplacian in the Euclidean coordinates $(\tau, x, y, z)$. The Lorentzian wave operator and the Euclidean Laplacian are related by the substitution $t \to -i\tau$: the Lorentzian operator acting on a function of $t$ becomes the Euclidean operator acting on the corresponding function of $\tau$.

**The action becomes imaginary.** The Lorentzian action $S$ becomes $i$ times a Euclidean action $S_E$:

$$
S \to i S_E.
$$

The precise relation depends on the normalization of the action, but the essential point is that the phase $e^{iS}$ becomes the real exponential

$$
e^{iS} \to e^{-S_E}.
$$

**The path integral becomes a partition function.** The Lorentzian path integral

$$
Z = \int \mathcal{D}\phi\; e^{iS[\phi]}
$$

becomes, after the Wick rotation,

$$
Z_E = \int \mathcal{D}\phi\; e^{-S_E[\phi]}.
$$

The integrand is now a **decaying** exponential: configurations with large Euclidean action are exponentially suppressed. The integral is manifestly convergent (at least formally), and it has the form of a **statistical-mechanical partition function** with $S_E$ playing the role of the energy functional.

## Why It Works

The justification for the Wick rotation is analytic continuation. Under suitable conditions, the integrand $e^{iS[\phi]}$ is an analytic function of the time coordinate $t$ in a domain of the complex plane that includes both the real axis and the negative imaginary axis. In this case, the integral along the real axis can be deformed to the imaginary axis without changing its value.

The deformation is the same as the standard trick for evaluating oscillatory Gaussian integrals. In one dimension,

$$
\int_{-\infty}^{+\infty} e^{iax^2}\,dx = \sqrt{\frac{i\pi}{a}},
$$

which can be obtained by rotating the contour from the real axis to the imaginary axis (times a sign). The Wick rotation is the field-theoretic analogue of this rotation: the contour in the complex time plane is rotated by $90°$, from the real axis to the imaginary axis.

For the deformation to be justified, the integrand must decay sufficiently fast at infinity in the complex time plane, so that the contributions from the arcs at infinity vanish. This condition is satisfied for many theories of interest — in particular for free fields and for asymptotically free theories — but it is **not automatic**. The Wick rotation is therefore not a theorem of quantum field theory: it is a trick that works when the analyticity conditions are met, and that can fail otherwise.

## Applications

The Wick rotation is applied in a wide range of problems. We list the principal ones.

**Euclidean quantum field theory.** The Euclidean path integral $Z_E = \int \mathcal{D}\phi\; e^{-S_E[\phi]}$ is the starting point of Euclidean field theory. In this framework, quantum field theory is treated as a statistical-mechanical system in four Euclidean dimensions, with correlation functions given by moments of the Euclidean measure. The Euclidean formulation is the basis of constructive quantum field theory, of the rigorous treatment of free fields, and of the renormalization group in the Wilsonian approach.

**Finite-temperature field theory.** At finite temperature $T$, quantum field theory is formulated on a Euclidean spacetime that is periodic in the imaginary time direction with period

$$
\beta = \frac{\hbar}{k_B T},
$$

where $k_B$ is Boltzmann's constant. The thermal partition function is

$$
Z(\beta) = \mathrm{Tr}\,e^{-\beta H} = \int \mathcal{D}\phi\; e^{-S_E[\phi]},
$$

with $\tau \in [0, \beta)$. The periodicity in imaginary time is the origin of the **Matsubara frequencies**: the Fourier modes of the fields in the compact $\tau$ direction are discrete, with frequencies $2\pi n/\beta$ for bosons and $(2n+1)\pi/\beta$ for fermions. Finite-temperature field theory is built entirely on this Euclidean formalism.

**Lattice gauge theory.** Non-perturbative computations in QCD and other gauge theories are performed on a Euclidean lattice of points in $\mathbb{R}^4$. The lattice discretization is introduced in the Euclidean setting, where the path integral is a convergent integral over the lattice fields. The continuum limit is taken by sending the lattice spacing to zero. This is the only known method for computing non-perturbative quantities in QCD from first principles, and it works entirely in the Euclidean setting. At finite temperature, the lattice has a finite extent in the Euclidean time direction, identified with $\beta$.

**Instantons and tunneling.** In quantum mechanics and quantum field theory, tunneling phenomena are described by **instantons**: classical solutions of the Euclidean equations of motion. In the Euclidean formulation, tunneling amplitudes are obtained from the Euclidean action of these solutions. This is the basis of the semiclassical treatment of the double-well potential, of the anomalous breaking of chiral symmetry in QCD, and of many other non-perturbative phenomena. The instanton calculus uses the Euclidean action as its fundamental object.

**Statistical mechanics.** The Euclidean path integral is formally identical to the partition function of a statistical-mechanical system, with the Euclidean action playing the role of the energy. This analogy is the basis of the deep connection between quantum field theory and statistical mechanics: a quantum field theory in $d$ spacetime dimensions is equivalent (in the Euclidean formulation) to a statistical-mechanical system in $d$ dimensions. Critical phenomena, the renormalization group, and the Wilsonian approach to effective field theory all use this correspondence.

**Stochastic quantization.** The Euclidean path integral is equivalent to a stochastic differential equation (the Langevin equation) with a noise term, whose stationary distribution is $e^{-S_E}$. This is the basis of stochastic quantization, an alternative formulation of quantum field theory in which the Euclidean field is obtained as the equilibrium distribution of a stochastic process in an auxiliary time parameter. It is used in numerical simulations and in certain analytic treatments.

**Spectral functions and real-time dynamics.** The Wick rotation is used to relate Euclidean correlation functions (which are computable by Monte Carlo methods) to Minkowski correlation functions (which describe real-time dynamics). The relation is the **spectral representation**, and its inversion (from Euclidean data to Minkowski spectral functions) is the subject of ongoing numerical work.

## What Is a Trick and What Is a Theorem

The Wick rotation is usually presented as a **trick**, and it is worth being precise about the sense in which this is true.

**What is a theorem.** Given a function that is analytic in a suitable domain and decays sufficiently fast at infinity, the contour integral along the real axis equals the contour integral along the imaginary axis. This is Cauchy's theorem, and it is a rigorous result of complex analysis.

**What is a trick.** The application of this theorem to the path integral of quantum field theory is not automatic. The path integral is not a well-defined mathematical object in general, and the analyticity conditions required for the Wick rotation are not always verified. The Wick rotation is therefore a heuristic that works for a large class of physically relevant theories, but that does not follow from a general mathematical theorem.

**What is remarkable.** Despite its lack of rigorous justification, the Wick rotation gives correct answers in an enormous range of applications, from perturbative QFT to lattice QCD to finite-temperature field theory. This is one of the empirical successes of the heuristic. It is the reason the Wick rotation is used universally, and it is the reason the Euclidean formulation of field theory is treated as fundamental by many practitioners.

## Limitations

The Wick rotation is not universally applicable. Its principal limitations are as follows.

**Analyticity.** The Wick rotation requires the fields and correlation functions to extend analytically in the time coordinate. In some theories — particularly those with massless particles, infrared divergences, or non-trivial asymptotic behavior — the analyticity conditions may fail.

**Curved spacetime.** In curved spacetime, the time coordinate is not globally defined, and the Wick rotation is more subtle. In spacetimes with a Killing vector that is timelike everywhere (stationary spacetimes), a Wick rotation can be defined locally, but the global structure is not always Euclidean. In more general spacetimes, the Wick rotation is not available.

**Real-time dynamics.** The Wick rotation gives access to Euclidean correlation functions, but real-time quantities — such as the response of a system to a time-dependent perturbation, or the real-time dynamics of a quantum quench — are not directly accessible. The analytic continuation back to real time is possible in principle, but numerically difficult, and it is one of the open problems of lattice field theory.

**Non-equilibrium systems.** The Euclidean formulation is well suited to equilibrium systems (thermal states), but non-equilibrium phenomena — transport, relaxation, decoherence — require real-time methods, for which the Wick rotation is not directly useful.

**Fermions.** The Wick rotation for fermion fields involves additional subtleties, because the spinor representation of the Lorentz group is not the same as the spinor representation of the Euclidean rotation group. The Euclidean formulation of fermionic field theory is possible, but it requires care.

**Gravity.** The Wick rotation is not straightforwardly defined for gravity, because the Euclidean gravitational action is unbounded below (the conformal factor problem). This is one of the obstacles to the Euclidean approach to quantum gravity.

These limitations are the reasons the Wick rotation is called a trick and not a theorem. It works for many problems and fails for others, and the reasons for success and failure are not always clear.

## Summary

The Wick rotation is the analytic continuation $t \to -i\tau$ of the time coordinate to imaginary values. It converts the Lorentzian structure of spacetime to a Euclidean one: the wave operator becomes the Laplacian, the oscillating phase $e^{iS}$ becomes the decaying exponential $e^{-S_E}$, and the Feynman path integral becomes a statistical-mechanical partition function.

The Wick rotation is used throughout quantum field theory, statistical mechanics, lattice gauge theory, and condensed-matter physics. Its principal applications are the Euclidean path integral, finite-temperature field theory, lattice QCD, instanton calculus, and the correspondence between quantum field theory and statistical mechanics.

The Wick rotation is a trick. It is justified by Cauchy's theorem when the appropriate analyticity conditions are satisfied, but the application to the path integral of quantum field theory is not automatic, and it is not a theorem of the theory. It works in a large class of physically relevant cases and fails in others.

The Euclidean formulation of field theory that results from the Wick rotation has become a fundamental tool of modern theoretical physics. The correspondence between Lorentzian and Euclidean formulations is one of the deepest structural features of quantum field theory, and it underlies much of the modern understanding of the subject.

## Further Reading

- G. C. Wick, "Properties of Bethe-Salpeter wave functions," *Physical Review* **96** (1954) 1124–1134, for the original introduction of the Wick rotation.
- J. Schwinger, "On the Euclidean structure of relativistic field theory," *Proceedings of the National Academy of Sciences* **44** (1958) 956–965, for the Euclidean formulation of field theory.
- J. Glimm and A. Jaffe, *Quantum Physics: A Functional Integral Point of View* (Springer, 1987), for the rigorous Euclidean approach to constructive quantum field theory.
- M. Le Bellac, *Thermal Field Theory* (Cambridge, 1996), for the finite-temperature imaginary-time formalism.
- J. Zinn-Justin, *Quantum Field Theory and Critical Phenomena* (Oxford, 2002), for the Euclidean path integral and its applications.
- M. Creutz, *Quarks, Gluons and Lattices* (Cambridge, 1983), for lattice gauge theory.
- H. Kleinert, *Path Integrals in Quantum Mechanics, Statistics, Polymer Physics, and Financial Markets* (World Scientific, 2009), for a comprehensive treatment of path integrals and their applications.
- A. M. Polyakov, *Gauge Fields and Strings* (Harwood, 1987), for instantons and non-perturbative effects in the Euclidean formulation.

