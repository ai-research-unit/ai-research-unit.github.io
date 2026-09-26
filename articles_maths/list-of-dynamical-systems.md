
# __List of Dynamical Systems__

## Introduction

This article lists the dynamical systems the corpus introduces. A dynamical system is a space with a transformation or a flow that preserves a structure, and a row below names one system, records its entropy, its ergodicity and its mixing properties, and points to the article that introduces it. Every row points to an article; this article introduces nothing and proves nothing. The systems are grouped by the layer that introduces them: the rotations and translations, the expanding maps and the symbolic systems, the hyperbolic systems, the systems of geometry and mathematical physics, and the statistical invariants — entropy, Lyapunov exponent and Bowen–Ruelle measure — that the theory computes. The rows that record a failure — a rotation that is ergodic but not mixing, a toral automorphism that is not hyperbolic, an integrable system whose entropy vanishes — stand beside the systems as non-examples.

## Rotations, Translations and Equidistribution

| Object | Its entropy, ergodicity and mixing | Introduced in |
|---|---|---|
| the irrational rotation $x \mapsto x+\alpha$ | entropy $0$; ergodic, and not weakly mixing: the Koopman operator has the full circle of eigenvalues | *Ergodic Theory*; *Equidistribution* |
| the rational rotation $x \mapsto x+p/q$ | entropy $0$; not ergodic, its orbits being the cosets of $\frac1q\mathbb{Z}/\mathbb{Z}$ | *Ergodic Theory* |
| the rotation on a torus, and the Kronecker flow | entropy $0$; ergodic for independent irrational frequencies, and not mixing | *Ergodic Theory of Group Actions*; *Equidistribution* |
| the doubling map $x \mapsto 2x \bmod 1$ | entropy $\log2$; ergodic and mixing; the one-sided binary shift | *Ergodic Theory* |
| the Gauss map $x \mapsto 1/x \bmod 1$ | entropy $\pi^2/(6\log2)$; ergodic and mixing for the Gauss measure; the generator of the continued fraction | *Ergodic Theory*; *Diophantine Approximation and Continued Fractions* |
| a general expanding map of the circle and of an interval | entropy $\int\log\lvert T'\rvert\,d\mu$; ergodic and mixing for an absolutely continuous invariant measure | *Smooth Dynamical Systems* |

## Symbolic and Markov Systems

| Object | Its entropy, ergodicity and mixing | Introduced in |
|---|---|---|
| the full shift on $k$ symbols | topological entropy $\log k$; the Bernoulli shift with the uniform measure is ergodic and mixing | *Symbolic Dynamics* |
| the Bernoulli shift $(\sigma,\mu)$ | metric entropy $H(p) = \sum_ip_i\log(1/p_i)$; ergodic and mixing; classified by Ornstein's theorem | *Ergodic Theory*; *Symbolic Dynamics* |
| a subshift of finite type, and a topological Markov chain | topological entropy $\log\rho(A)$ with $\rho(A)$ the spectral radius of the transition matrix; the Markov measure is ergodic and mixing when the matrix is irreducible and aperiodic | *Symbolic Dynamics* |
| a sofic shift | topological entropy $\log\rho(A)$ of the underlying graph; the measure-theoretic properties as in the finite-type case | *Symbolic Dynamics*; *Dynamics and Number Theory* |
| a suspension flow over a symbolic system | entropy of the flow $h_\mu(T)/\int\tau\,d\mu$ with $\tau$ the roof function | *Hyperbolic Dynamics and Anosov Systems* |
| a Markov partition of a hyperbolic system | the symbolic model conjugate to the system off a measure-zero set | *Hyperbolic Dynamics and Anosov Systems* |

## Hyperbolic Systems

| Object | Its entropy, ergodicity and mixing | Introduced in |
|---|---|---|
| a hyperbolic toral automorphism $T_A$, $\lvert\operatorname{tr}A\rvert>2$ | entropy $\log\lvert\lambda\rvert$ for the larger eigenvalue; ergodic, mixing, and the prototype of hyperbolicity | *Ergodic Theory*; *Homogeneous Dynamics* |
| an Anosov diffeomorphism | topological entropy as the maximum and metric entropy given by Pesin's formula; ergodic and mixing in the volume case | *Hyperbolic Dynamics and Anosov Systems* |
| an Anosov flow | entropy from the Lyapunov exponent; the Bowen–Ruelle measure is the equilibrium state | *Hyperbolic Dynamics and Anosov Systems* |
| an Axiom A diffeomorphism and its spectral decomposition | the decomposition into finitely many topologically transitive basic sets, each with a Markov partition | *Hyperbolic Dynamics and Anosov Systems*; *Smooth Dynamical Systems* |
| the Smale horseshoe | topological entropy $\log2$ on the invariant Cantor set; the model of chaotic behaviour | *Chaos and Strange Attractors*; *Bifurcation Theory* |
| a hyperbolic set with the shadowing and specification properties | the pseudo-orbit is shadowed by a true orbit; specification gives the entropy and the periodic-point statistics | *Hyperbolic Dynamics and Anosov Systems* |

## The Systems of Geometry and Physics

| Object | Its entropy, ergodicity and mixing | Introduced in |
|---|---|---|
| the geodesic flow of a compact hyperbolic surface | entropy equal to the topological entropy of the surface, positive; ergodic and mixing for the Liouville measure | *The Geodesic Flow*; *Hyperbolic Dynamics and Anosov Systems* |
| a homogeneous flow and a unipotent flow | the Ratner classification of closures and equidistribution; equidistributed in the homogeneous space | *Homogeneous Dynamics*; *Ratner's Theorems* |
| a flow of an ergodic action of a Lie group | ergodic and mixing for the Haar measure under the Howe–Moore property | *Ergodic Theory of Group Actions* |
| a Hamiltonian system, and a Lagrangian system | entropy $0$ in the integrable case; the symplectic form and the Euler–Lagrange flow in general | *Lagrangian and Hamiltonian Systems* |
| an integrable system and the soliton equations | entropy $0$; the invariant tori of Liouville and the inverse-scattering solution | *Integrable Systems*; *Soliton Theory* |
| the Lorenz system | positive Lyapunov exponents and a strange attractor; the numerical prototype of chaos | *Chaos and Strange Attractors* |
| the Hénon map | a strange attractor of non-integer dimension; the Kaplan–Yorke formula | *Chaos and Strange Attractors* |
| the logistic family $x \mapsto \mu x(1-x)$ | period doubling, the Feigenbaum cascade and the chaotic window; the entropy grows with $\mu$ | *Bifurcation Theory*; *Chaos and Strange Attractors* |
| a random dynamical system | the multiplicative ergodic theorem gives the Lyapunov spectrum; the invariant measure is random | *Random Dynamical Systems* |
| a stochastic flow and its generator | the Markov semigroup and the Fokker–Planck equation; the invariant measure and its rate of convergence | *Stochastic Differential Equations* |

## The Statistical Invariants

| Object | What it measures | Introduced in |
|---|---|---|
| the Kolmogorov–Sinai entropy | the exponential rate of information, $h_\mu(T)$; an isomorphism invariant, computed by the Kolmogorov–Sinai theorem | *Ergodic Theory* |
| the topological entropy | the exponential growth of the number of distinguishable orbit segments; the maximum of the metric entropies | *Topological Dynamics*; *Symbolic Dynamics* |
| ergodicity | the absence of nontrivial invariant sets; the identity of time and space averages | *Ergodic Theory* |
| mixing, weak mixing and the K-property | the decay of correlations, and the hierarchy of mixing notions; the K-property implies mixing, which implies ergodicity | *Ergodic Theory* |
| the Lyapunov exponents | the exponential rates of separation of nearby orbits; the Oseledets theorem gives their existence | *Hyperbolic Dynamics and Anosov Systems* |
| Pesin's formula | the identity of the metric entropy with the total positive Lyapunov exponent | *Ergodic Theory*; *Hyperbolic Dynamics and Anosov Systems* |
| the Bowen–Ruelle measure | the invariant measure that is the equilibrium state for the geometric potential, the physical measure of an attractor | *Hyperbolic Dynamics and Anosov Systems*; *The Geodesic Flow* |
| the invariant measure and the ergodic decomposition | the measure preserved by the system, decomposed into ergodic components | *Ergodic Theory* |
| the Poincaré recurrence theorem | the almost-sure return of the orbit to a set of positive measure | *Ergodic Theory*; *Topological Dynamics* |

## Systems and Invariants That Fail a Property

| Object | The property that fails | Introduced in |
|---|---|---|
| the irrational rotation | is ergodic but not weakly mixing: the Koopman operator has eigenvalues of modulus one | *Ergodic Theory* |
| the rational rotation | is not ergodic; the invariant sets are the unions of cosets | *Ergodic Theory* |
| the identity map | has entropy $0$ and is not ergodic when the space is not a single atom | *Ergodic Theory* |
| an integrable Hamiltonian system | has zero entropy, so it is not chaotic; the KAM tori obstruct ergodicity | *Lagrangian and Hamiltonian Systems*; *Integrable Systems* |
| a non-hyperbolic toral automorphism, $\lvert\operatorname{tr}A\rvert \leq 2$ | has no hyperbolic splitting and entropy $0$; the elliptic and parabolic cases | *Ergodic Theory*; *Homogeneous Dynamics* |
| a system with a rigid factor | is ergodic but not mixing | *Ergodic Theory* |
| a measure-preserving transformation with an invariant set of intermediate measure | is not ergodic, however large the set | *Ergodic Theory* |
| two Bernoulli shifts of different entropy | are not isomorphic; Ornstein's theorem separates them | *Ergodic Theory* |
| a system whose only invariant measure is supported on a periodic orbit | has vanishing metric entropy and no chaotic statistics | *Chaos and Strange Attractors*; *Topological Dynamics* |

## Summary

This list gathers the dynamical systems of the corpus: the circle rotations and translations, the doubling and Gauss maps, the Bernoulli and Markov shifts, the hyperbolic toral automorphisms, Anosov and Axiom A systems and the horseshoe, the geodesic and homogeneous flows, the Hamiltonian, integrable, Lorenz, Hénon and logistic systems, the random and stochastic systems, and the invariants — Kolmogorov–Sinai and topological entropy, ergodicity, mixing, the Lyapunov exponents, the Bowen–Ruelle measure and the Poincaré recurrence theorem. The closing table records the systems and invariants that fail a property of the theory.

## Summary of Notation

The objects are named by their standard symbols; the tables use the following.

| Symbol | Meaning |
|---|---|
| $T$, $\sigma$ | a transformation, the shift |
| $\mu$, $h_\mu(T)$ | an invariant measure, the Kolmogorov–Sinai entropy |
| $T_A$ | the toral automorphism induced by $A \in SL_n(\mathbb Z)$ |
| $\lambda$, $\chi_i$ | an eigenvalue, a Lyapunov exponent |
| $H(p)$, $\rho(A)$ | the entropy of a probability vector, the spectral radius of a transition matrix |
| $h_{\mathrm{top}}$ | topological entropy |

## Further Reading

- Peter Walters, *An Introduction to Ergodic Theory* (Springer, 1982), for the entropy, ergodicity and mixing of the standard systems.
- Anatole Katok and Boris Hasselblatt, *Introduction to the Modern Theory of Dynamical Systems* (Cambridge University Press, 1995), for the catalogue of examples and the hyperbolic theory.
- Rufus Bowen, *Equilibrium States and the Ergodic Theory of Anosov Diffeomorphisms* (Springer, 1975), for the Bowen–Ruelle measure, Markov partitions and specification.
