# __$P$, $T$ and the Representation Labels__

## Introduction

The Poincaré algebra has two Casimirs: the momentum squared and the Pauli–Lubanski scalar. Their eigenvalues are the two labels of a one-particle representation, the mass and the spin, and the pair $(m,j)$ names the representation up to unitary equivalence. On the null cone one combination degenerates and the labels become $(0,h)$, the mass and the helicity.

The title names the two discrete operations that act on those labels. This article states both Casimirs, computes them on the two orbits, reads them as little-group labels, and then says what parity and time reversal do to the labelling and what they do not do.

The article assumes *Wigner's Classification: Two Casimirs, Three Orbits* for the orbit picture, *The Little Group of a Massive Particle: $\mathrm{SU}(2)$* and *The Little Group of a Null Momentum: $E(2)$* for the stabilisers, *The Two Casimirs of the Lorentz Algebra* for the Lorentz part, and *The Null Cone: The Massless Boundary* for the cone. The corpus's Pauli–Lubanski conventions, including the sign of the invariant, are those of *The Determination of the Possible Spins in Biquaternionic Form*, and this article follows them.

## The Poincaré Algebra

### What Is Added to the Lorentz Algebra

The Poincaré algebra is the Lorentz algebra together with four translation generators $\tilde P_\mu$:

$$
[\tilde M_{\mu\nu},\tilde P_\rho]=\text{(the Lorentz action on a vector)},
\qquad
[\tilde P_\mu,\tilde P_\nu]=0 .
$$

The translations commute, so the algebra is not simple, and its Casimirs are not the Casimirs of the Lorentz part alone. That is the whole structural difference, and it is what makes the labels physical: a Lorentz Casimir alone labels a representation of the homogeneous group, and a particle needs a momentum.

### The Casimirs

Two independent Casimir operators exist:

$$
C_1=\tilde P^{2}=\tilde P_\mu\tilde P^{\mu},
\qquad
C_2=\tilde W^{2}=-\tilde W_\mu\tilde W^{\mu},
$$

with $\tilde W_\mu$ the Pauli–Lubanski vector defined below. "Casimir" means commuting with all ten generators, so their eigenvalues are constant on an irreducible module.

### Why There Are Exactly Two

The Poincaré algebra has rank two after the translations are included: the momentum's length and one further invariant built from the Lorentz generators. The count is the same count that gives the Lorentz algebra's two Casimirs in *The Two Casimirs of the Lorentz Algebra*, with one of them promoted to the momentum and the other replaced by the Pauli–Lubanski scalar.

## The First Casimir: The Mass

### The Momentum Squared

$C_1=p^{2}$ is the invariant length of the four-momentum. Its sign separates the three orbits:

| $p^{2}$ | orbit | physical name |
|---|---|---|
| $>0$ | the hyperboloid | massive |
| $=0$ | the cone, minus the vertex | massless |
| $<0$ | the other hyperboloid | tachyonic |

The block treats the first two; the third is the same algebra with the sign of the invariant flipped and is not a physical orbit of a stable particle.

### The Two Sign Conventions of the Slices

The corpus writes the norm of a four-momentum in two ways because it works on two real slices.

- On the **Hermitian** slice, where the norm is the interval $q_t^{2}-\lvert\vec q\rvert^{2}$ of *The Null Cone: The Massless Boundary*, a timelike momentum has norm $+m^{2}c^{2}$. This is the convention this article uses for $C_1$ and $C_2$, and it is the one the other articles of the block use, so that the rest momentum is $\tilde P_{\mathrm{rest}}=mc\,e_t$ and $p^{2}=+m^{2}c^{2}$.
- On the **material** slice the four-momentum has $\langle\tilde P\rangle_{\natural}=-m^{2}c^{2}$, the convention of *The Determination of the Possible Spins in Biquaternionic Form*; the two readings differ by the sign of the norm.

Both are statements about $p^{2}$; the difference is the sign of the norm on the slice, and a formula transplanted from one slice to the other needs a sign. Nothing in the labelling depends on which is used, because the labels are the eigenvalues of Casimirs and not the norms themselves.

### The Shell

$C_1=m^{2}c^{2}$ defines the mass shell: a three-dimensional hyperboloid in momentum space for $m\neq0$, and the cone for $m=0$. The shell is the orbit, and the label $m$ is the orbit's name.

## The Pauli–Lubanski Vector

### The Definition

$$
\tilde W_\mu=\tfrac12\sum_{\nu,\rho,\sigma}\epsilon_{\mu\nu\rho\sigma}\tilde M^{\nu\rho}\tilde P^{\sigma}.
$$

It is the contraction of the Lorentz generators with the momentum, weighted by the alternating symbol; equivalently, it is the spin part of the angular momentum projected onto the momentum.

### The Three Properties

- $\tilde W_\mu\tilde P^{\mu}=0$: the vector is orthogonal to the momentum, identically, because the alternating symbol is antisymmetric in a pair and $P^{\sigma}P^{\mu}$ is symmetric.
- $[\tilde W_\mu,\tilde P_\nu]=0$: the Pauli–Lubanski vector is translation invariant, since it is built from $P$ bilinearly after the contraction.
- $[\tilde W_\mu,\tilde W_\nu]$ is proportional to $\epsilon_{\mu\nu\rho\sigma}\tilde W^{\rho}\tilde P^{\sigma}$, so the $\tilde W$'s close among themselves only on a fixed momentum shell.

The second property is what makes $C_2$ a Casimir: a quantity built from $P$ and $M$ that commutes with $P$ and whose square commutes with $M$ is central.

### The Scalar

$C_2=-\sum_\mu\tilde W_\mu\tilde W^{\mu}$ is the invariant content of the vector. On the rest frame of a massive particle,

$$
W_0=0,\qquad \vec W=\pm mc\vec S,
$$

with the sign fixed by the orientation convention of $\epsilon$, so

$$
C_2=m^{2}c^{2}\lvert\vec S\rvert^{2}=\hbar^{2}m^{2}c^{2}s(s+1).
$$

The computation is verified in the spin-$\tfrac12$ representation of the Lorentz algebra: with $\tilde P=(mc,0,0,0)$, the four Pauli–Lubanski generators come out as $W_0=0$ and $\vec W=mc\vec S$, with $\vec S$ the Hermitian spin operator so that $\vec S^{2}=+s(s+1)$, and $C_2=\tfrac34\hbar^{2}m^{2}c^{2}$, which is $s(s+1)$ at $s=\tfrac12$.

### Why $C_2$ Is the Spin

$\vec W/(mc)$ is the spin vector in the rest frame, so $C_2/(m^{2}c^{2})$ is the Casimir of the rest-frame rotation group. That is the content of the next section's little-group reading, and it is the reason the spin label is not an independent input: it is what $C_2$ measures.

## The Two Labels

### The Pair $(m,j)$

An irreducible unitary module of the Poincaré group of positive mass is labelled by

$$
(m,j),\qquad m>0,\quad j\in\{0,\tfrac12,1,\tfrac32,\dots\},
$$

and the module has dimension $2j+1$ times the dimension of the momentum space's orbit measure. The two numbers are the eigenvalues of the two Casimirs:

$$
C_1=m^{2}c^{2},\qquad C_2=\hbar^{2}m^{2}c^{2}j(j+1).
$$

### The Rest Frame

In the rest frame the momentum is $(mc,\vec 0)$ and the little group is the rotation group; the module restricts to the spin-$j$ representation of $SU(2)$, of dimension $2j+1$. So the label $j$ is the spin of the rest-frame state, and the momentum label is the orbit.

### The Counting

$$
\underbrace{2}_{\text{continuous labels}}=\underbrace{1}_{\text{mass}}+\underbrace{1}_{\text{spin}},
$$

and the spin's one parameter is discrete. The rest of the representation is the orbit: three momentum parameters, of which the mass fixes one combination and the little group acts on the rest.

## The Massless Case

### The Proportionality

On the cone, $\tilde W_\mu\tilde P^{\mu}=0$ and $\tilde W$ is orthogonal to a null vector, so $\tilde W$ is either proportional to $\tilde P$ or spacelike. The physical (finite-dimensional) case is the proportional one:

$$
\tilde W_\mu=h\,\tilde P_\mu ,
$$

with $h$ a constant on the module. Then $C_2=-\sum\tilde W_\mu\tilde W^{\mu}=h^{2}\cdot 0=0$, so the second Casimir *vanishes* on the massless orbit and the label $h$ is not read from it.

### The Helicity

$h$ is the **helicity**: the component of the spin along the momentum, in units of $\hbar$. It is invariant under the little group $E(2)$'s compact part and fixed by the requirement that the two null rotations act trivially. The massless labels are

$$
(0,h),\qquad h\in\{0,\pm\tfrac12,\pm1,\dots\},
$$

and parity, if it is a symmetry, requires both $h$ and $-h$ in the spectrum.

### The Fold

The label space folds along the cone: for $m>0$ the two Casimirs are independent, and for $m=0$ one of them is identically zero and the other carries a label that has no massive analogue. So the massless labelling is not the $m\to0$ limit of the massive one, and a reader who tries to take the limit term by term will find that the multiplicities diverge: the little group has grown from $SU(2)$ to $E(2)$.

### The Other Massless Case

The second possibility, $\tilde W$ spacelike, gives the "continuous spin" representations: infinitely many states per momentum, labelled by a continuous parameter. They are unitary and they are not realised in nature. The block names them and does not use them.

## PT and the Labels

### The Two Operations

Parity reverses the spatial momentum and leaves the energy; time reversal reverses both the momentum and the spin. Neither is in the connected Lorentz group, so neither is an element whose action the block's group theory supplies; both are discrete operations that act on the label set.

### What PT Does to the Labels

$PT$ leaves the momentum invariant, so it preserves $C_1$. It reverses the spin vector, so it preserves $C_2$ as well, since a Casimir is quadratic in the spin. On the labels,

$$
PT:(m,j)\longmapsto(m,j),\qquad (0,h)\longmapsto(0,-h).
$$

The second entry is the interesting one: on the massless orbit the second Casimir is zero and the label $h$ is a *linear* function of the spin, so the discrete operation that reverses the spin reverses the helicity, while on the massive orbit the label is quadratic and survives.

That is the precise sense in which PT "does nothing to the labels" and the precise sense in which it does something: the Casimir labels are untouchable, and the helicity is not a Casimir label.

### What It Does Not Do

$PT$ does not identify two inequivalent representations, and it does not make the labelling ambiguous. It maps a representation to another one, and the map happens to be the identity on the massive labels and the flip on the massless ones. A statement that PT "doubles the spectrum" is a statement about which representations are realised in a PT-symmetric theory, not about the labelling.

## The Little-Group Reading

### The Stabiliser

The little group of a momentum $\tilde P$ is

$$
G_{\tilde P}=\{\tilde U\in G:\mathrm{Cg}_{\tilde U}(\tilde P)=\tilde P\},
$$

the stabiliser under the congruence of *The Two Actions of One Group: Adjoint and Congruence*. For a timelike momentum it is isomorphic to $SU(2)$; for a null momentum it is the double cover of $E(2)$.

### The Labels as Little-Group Labels

A representation of the Poincaré group is a representation of the little group, induced to the whole group. So the labels are little-group labels:

| orbit | little group | label | what it names |
|---|---|---|---|
| timelike | $SU(2)$ | $j$ | the spin, dimension $2j+1$ |
| null | $E(2)$ | $h$ | the helicity, one state per sign |
| spacelike | $SU(1,1)$ | continuous | not physical |

### Why the Two Readings Agree

The Casimir reading says the labels are the eigenvalues of central operators. The little-group reading says they are the labels of the stabiliser's representations. They agree because a Casimir restricted to the stabiliser is a Casimir of the stabiliser: $C_2$ becomes $m^{2}c^{2}\vec S^{2}$ on the rest frame, which is the $SU(2)$ Casimir, and on the cone it collapses to zero while the helicity becomes the label of $E(2)$'s compact part.

### The Consistency of the Block

The two readings are used in different articles of the block for different purposes: the Casimir reading gives the value, the little-group reading gives the count of states. Neither is more fundamental, and the block's statements about "the two labels" always mean the pair $(m,j)$ or its massless substitute.

## Summary

The Poincaré algebra has two Casimirs, $C_1=p^{2}$ and $C_2=-\sum_\mu W_\mu W^{\mu}$ with $W_\mu$ the Pauli–Lubanski vector. Their eigenvalues label an irreducible module by $(m,j)$, with $C_1=m^{2}c^{2}$ and $C_2=\hbar^{2}m^{2}c^{2}j(j+1)$; in the rest frame $\vec W=\pm mc\vec S$, which is why $j$ is the spin. On the null cone $W_\mu=hP_\mu$, $C_2$ vanishes, and the labels become $(0,h)$ with $h$ the helicity, because the little group has grown from $SU(2)$ to $E(2)$. The two readings, by Casimirs and by little groups, agree on both orbits. $PT$ preserves the momentum and reverses the spin, so it fixes $(m,j)$ and flips $h$: the Casimir labels are untouchable and the helicity is not one.

## Summary of Notation

| symbol | meaning |
|---|---|
| $C_1=\tilde P^{2}$ | the momentum Casimir |
| $C_2=-\sum_\mu\tilde W_\mu\tilde W^{\mu}$ | the Pauli–Lubanski Casimir |
| $\mathcal{C}_{1,2}$ | the Casimirs of the Lorentz algebra, a different pair |
| $\tilde W_\mu$ | the Pauli–Lubanski vector |
| $(m,j)$ | the massive labels |
| $(0,h)$ | the massless labels |
| $G_{\tilde P}$ | the little group of the momentum |
| $h$ | helicity |

## Further Reading

- E. P. Wigner, "On unitary representations of the inhomogeneous Lorentz group", *Annals of Mathematics* 40 (1939) 149 — the two Casimirs and the orbit classification.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1, Cambridge University Press, 1995, §2.4–2.6 — the Pauli–Lubanski vector, the little groups and the helicity labels.
- Y. Ohnuki, *Unitary Representations of the Poincaré Group and Relativistic Wave Equations*, World Scientific, 1988 — the induced-representation construction with the Casimir eigenvalues computed explicitly.
- *The Determination of the Possible Spins in Biquaternionic Form* — the corpus's Pauli–Lubanski conventions and the sign of the invariant.
- *Wigner's Classification: Two Casimirs, Three Orbits* — the orbit picture in this block.
- *The Little Group of a Null Momentum: $E(2)$* — the stabiliser that produces the helicity label.
