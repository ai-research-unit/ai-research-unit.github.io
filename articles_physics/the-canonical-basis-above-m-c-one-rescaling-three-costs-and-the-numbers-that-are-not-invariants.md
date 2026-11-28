# __The Canonical Basis Above $M_C$: One Rescaling, Three Costs and the Numbers That Are Not Invariants__

## Introduction

[The census](the-census-above-m-c-nineteen-structures-eighteen-admissible-eleven-written.html) quotes eleven structures with fifteen coefficients. This article states the coordinates they are quoted in.

One shift of the trace mode,

$$
\Xi\ \longrightarrow\ \Xi+b\,(\operatorname{tr}\Xi)\,\mathbb 1,
$$

leaves the traceless part fixed and rescales the trace by $1+4b$. Three things move: the scalar kinetic term, the potential, and one of the two Yukawa matrices. Canonical normalisation fixes $b$ and so fixes all three.

## The Shift

Every Hermitian matrix splits once.

$$
\Xi=\Xi_{0}+\frac{1}{4}\bigl(\operatorname{tr}\Xi\bigr)\mathbb 1,
\qquad
\operatorname{tr}\Xi_{0}=0 .
$$

Under the shift, $\Xi_{0}$ is unchanged and

$$
\operatorname{tr}\Xi\ \longrightarrow\ (1+4b)\operatorname{tr}\Xi .
$$

The redefinition is invertible for $1+4b\neq0$ and changes no path integral. Anything that moves under it was never physical; only its count survives.

## The First Cost: The Kinetic Term

$$
\operatorname{tr}(D_{\imath}\Xi)^{\dagger}(D_{\imath}\Xi)=\operatorname{tr}(D_{\imath}\Xi_{0})^{\dagger}(D_{\imath}\Xi_{0})+\tfrac14\bigl(\partial_{\imath}\operatorname{tr}\Xi\bigr)^{2},
$$

with no cross term, because $\operatorname{tr}(D\Xi_{0})^{\dagger}=0$. A general kinetic term adds $c\,(\partial\operatorname{tr}\Xi)^{2}$, and the total coefficient $\tfrac14+c$ scales as

$$
\tfrac14+c\ \longrightarrow\ (1+4b)^{2}\bigl(\tfrac14+c\bigr).
$$

So $c$ is removable, and canonical normalisation sets $1+4b=(1+4c)^{-1/2}$.

## The Second Cost: The Potential

$$
\operatorname{tr}\Xi^{2}=\operatorname{tr}\Xi_{0}^{2}+\tfrac14 s^{2},
\qquad s\equiv\operatorname{tr}\Xi .
$$

$\mu_{\Phi}^{2}$ is fixed as the coefficient of $\operatorname{tr}\Xi_{0}^{2}$; the trace mass $\mu_{\Phi}^{2}+4\mu_{2}^{2}$ is not.

The quartic expands with four different powers of $s$.

$$
\operatorname{tr}\Xi^{4}=\operatorname{tr}\Xi_{0}^{4}+s\operatorname{tr}\Xi_{0}^{3}+\tfrac{3}{8}s^{2}\operatorname{tr}\Xi_{0}^{2}+\tfrac{1}{64}s^{4},
$$

so the four pieces scale as $(1+4b)^{0,1,2,4}$. One shift moves four couplings; their number stays four because one parameter cannot collapse four directions.

## The Third Cost: The Yukawa Matrices

$$
\bar\xi^{\alpha}\Xi\,\xi^{\beta}=\bar\xi^{\alpha}\Xi_{0}\,\xi^{\beta}+\tfrac14\bigl(\operatorname{tr}\Xi\bigr)\bar\xi^{\alpha}\xi^{\beta},
$$

so

$$
y\ \longrightarrow\ y,
\qquad
y'\ \longrightarrow\ \frac{y'}{1+4b},
\qquad
\frac{y'}{y}\ \longrightarrow\ \frac{1}{1+4b}\,\frac{y'}{y}.
$$

The ratio moves. The pair's eight numbers stay eight, and $y$'s spectrum alone is invariant.

## What Moves

| object | under the shift |
|---|---|
| the eleven rows | unchanged |
| $\Xi_{0}$, $\operatorname{tr}\Xi_{0}^{2}$ | fixed |
| $\operatorname{tr}\Xi$ | $\times(1+4b)$ |
| kinetic coefficient | $\times(1+4b)^{2}$ |
| trace mass $\mu_{\Phi}^{2}+4\mu_{2}^{2}$ | moves |
| the four $\lambda$'s | move, each differently |
| $y$ | fixed |
| $y'$ | $\times(1+4b)^{-1}$ |

Anything built on $\Xi_{0}$ is invariant; anything touching the trace is not. The count never moves, because a coordinate change cannot change how many invariant monomials the group admits.

## The Zeros Are Basis Statements

$$
\operatorname{tr}\Xi^{3}=\operatorname{tr}\Xi_{0}^{3}+\tfrac34 s\operatorname{tr}\Xi_{0}^{2}+\tfrac{1}{16}s^{3}.
$$

A basis with no cubic is not a basis with no cubic after a trace shift. So "declared zero" means zero in the canonical basis, and the census says so. A reader who shifts and finds a cubic has changed coordinates, not found an error.

## Checks

1. $\Xi_{0}$ fixed, $\operatorname{tr}\Xi\to(1+4b)\operatorname{tr}\Xi$.
2. The kinetic split has no cross term.
3. $\tfrac14+c\to(1+4b)^{2}(\tfrac14+c)$.
4. The quartic powers are $0,1,2,4$.
5. $y$ fixed, $y'\to y'/(1+4b)$.
6. Eleven rows in every basis.
7. $\operatorname{tr}\Xi^{3}$ contains $\tfrac34s\operatorname{tr}\Xi_{0}^{2}$.

## Summary

One rescaling of the trace mode costs the kinetic coefficient a factor $(1+4b)^{2}$, costs the potential four couplings moving with different powers, and divides $y'$ by $1+4b$ while $y$ stays put. The count of structures is unmoved, since a coordinate change is not a change in the invariant ring. The declared zeros hold in the canonical basis only: a trace shift turns on a cubic and turns $(\partial\operatorname{tr}\Xi)^{2}$ into a second kinetic term.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\Xi_{0}$ | traceless part |
| $s$ | $\operatorname{tr}\Xi$ |
| $b$ | shift parameter |
| $c$ | coefficient of $(\partial\operatorname{tr}\Xi)^{2}$ |
| canonical basis | $c=0$, $b=0$ |

## Further Reading

- [The Census Above $M_C$](the-census-above-m-c-nineteen-structures-eighteen-admissible-eleven-written.html)
- [The Coefficients Above $M_C$](the-coefficients-above-m-c-fifteen-constants-one-gauge-parameter-and-one-angle-without-a-row.html)
- [The Primordial Potential](the-primordial-potential-one-symmetric-minimum-above-m-c.html)
- [The Lagrangian and the Scalar Matrix](the-lagrangian-and-the-scalar-matrix-one-field-one-commutator-four-quartics.html)
