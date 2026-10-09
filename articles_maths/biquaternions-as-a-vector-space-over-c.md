# __Biquaternions as a Vector Space over $\mathbb{C}$__

## Introduction

This article treats the biquaternions as a **complex vector space**: the set of elements, its addition, the scalar action of $\mathbb{C}$ it carries, its coordinates, and the conjugations as complex-linear and complex-antilinear maps. The same set read over the real scalars, the complex structure that reading needs and the real forms it produces, is *Biquaternions as a Vector Space over $\mathbb{R}$*; that reading is the restriction of scalars of this one and adds no element. The two readings whose base is a ring of operators rather than a field of scalars — the bimodule over $\mathbb{H}$ and the module over $\mathbb{B}$ itself — are separate articles, *Biquaternions as a Bimodule over $\mathbb{H}$* and *Modules over the General Plain Algebra of Biquaternions*. The goal is to lay out the complex linear structure precisely and to name the **six** distinguished real subspaces that arise from the conjugations: four of dimension four, together with the two-dimensional centre and the six-dimensional vector subspace. The six are not developed here: they are defined one to a section in *Introduction to the Six Subspaces*, and the three decompositions into pairs of them are *Decompositions Along the Six Subspaces*.

$\mathbb{B}$ carries its product as well, and the product makes it an algebra. That reading, with the product taken as the multiplication, is *Introduction to the General Plain Algebra of Biquaternions*; here the product is used only to say that the scalar action is compatible with it. The four conjugations and the group they generate are *The Group of Involutions*.

The treatment is elementary and self-contained: every claim is either proved or stated as a definition, and no physics is invoked. The anti-Hermitian subspace is defined algebraically. No form appears in this article; the Hermitian form and the inner product are *Biquaternion Norm and Invertibility*. The product of the algebra — its definition, its two scalar–vector parts, and the dot and cross products they are built from — is *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, and it is used here as given.

The quaternion algebra $\mathbb{H}$ is assumed from the article on quaternion algebra, together with its basis, its multiplication and its conjugation. No facts about $\mathbb{H}$ are restated here.

## The Complex Vector Space

### Definition

The **biquaternion algebra** is the complexification of the quaternion algebra:

$$
\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H},
$$

read here as a $\mathbb{C}$-vector space: an additive group with a scalar multiplication by the complex numbers. It is therefore **four-dimensional** over $\mathbb{C}$, with complex basis $\{e_0, e_1, e_2, e_3\}$. It also carries its product, the one defined and studied in *The Four General Products of the Biquaternion $\mathbb{C}$ Space*; the product is $\mathbb{C}$-bilinear, so the scalars may be moved through it, and it makes $\mathbb{B}$ an algebra over $\mathbb{C}$, a reading developed in *Introduction to the General Plain Algebra of Biquaternions*. Its centre is the scalar line $\mathbb{C}e_0$, spanned over $\mathbb{R}$ by $e_0$ and $ie_0$, and it is one of the six distinguished real subspaces of the group.

### Developed Form

A general biquaternion is written in developed form as

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3, \qquad Q_\mu \in \mathbb{C},
$$

or, more compactly, as

$$
\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu, \qquad Q_\mu \in \mathbb{C}.
$$

We write

$$
\tilde{Q} = Q_0 + \mathbf{Q}, \qquad \mathbf{Q} = \sum_{k=1}^{3} Q_k e_k,
$$

where $Q_0$ is the **complex scalar part** and $\mathbf{Q}$ is the **complex vector part**. The tilde signals that $\tilde{Q}$ is an element of the algebra $\mathbb{B}$, not a four-vector.

Each complex coefficient is written in terms of its real and imaginary parts:

$$
Q_0 = q_0 + i q'_0, \qquad Q_k = q_k + i q'_k, \qquad q_\mu, q'_\mu \in \mathbb{R}.
$$

The scalar imaginary $i$ satisfies $i^2 = -1$ and commutes with all quaternion units: $i e_k = e_k i$. Multiplication by it is a real-linear map $J$ of $\mathbb{B}$ with $J^2 = -\mathrm{id}$, the complex structure of the real reading; the operator and the reading it builds are *Biquaternions as a Vector Space over $\mathbb{R}$*.

In the complex coordinates, $\tilde{Q}$ is the four-tuple $(Q_0, Q_1, Q_2, Q_3)$.

### The Coordinate Systems

The same element is written in three coordinate systems, and all three are used below.

**Real coordinates.** Splitting each complex coefficient as $Q_\mu = q_\mu + iq'_\mu$ with $q_\mu, q'_\mu \in \mathbb{R}$ gives a list of eight real numbers on the real basis:

$$
\tilde{Q} = q_0e_0 + q_1e_1 + q_2e_2 + q_3e_3 + q'_0(ie_0) + q'_1(ie_1) + q'_2(ie_2) + q'_3(ie_3).
$$

**Complex coordinates.** Collecting the eight real numbers into four complex ones gives the developed form, four complex coordinates $(Q_0, Q_1, Q_2, Q_3)$ on the complex basis $\{e_0, e_1, e_2, e_3\}$.

**Quaternionic coordinates.** Collecting them by the scalar imaginary instead gives

$$
\tilde{Q} = h_1 + ih_2, \qquad h_1 = \sum_{\mu=0}^{3} q_\mu e_\mu \in \mathbb{H}, \qquad h_2 = \sum_{\mu=0}^{3} q'_\mu e_\mu \in \mathbb{H},
$$

a real quaternion plus $i$ times another real quaternion. The decomposition is unique, so in this view an element is a **pair of quaternions**.

| coordinates | basis | count | scalars |
|---|---|---|---|
| real | $e_0, e_1, e_2, e_3, ie_0, ie_1, ie_2, ie_3$ | $8$ | $\mathbb{R}$ |
| complex | $e_0, e_1, e_2, e_3$ | $4$ | $\mathbb{C}$ |
| quaternionic | $e_0, ie_0$ | $2$ | $\mathbb{H}$ |

The three rows count the same element against three scalar systems, and all three are used below. The first row is the coordinate list of the real reading of *Biquaternions as a Vector Space over $\mathbb{R}$*; the eight real coordinates and the four complex ones differ only in how the eight real numbers are gathered.

### Conjugations

There are **four** natural conjugations on $\mathbb{B}$. The first three are obtained from the quaternion conjugation ${}^{\natural}$ and the complex conjugation $\bar{\cdot}$; the fourth is defined as the negative of Hermitian conjugation:

**Quaternion conjugation** $\tilde{Q}^{\natural}$:

$$
\tilde{Q}^{\natural} = Q_0 e_0 - Q_1 e_1 - Q_2 e_2 - Q_3 e_3.
$$

**Complex conjugation** $\bar{\tilde{Q}}$:

$$
\bar{\tilde{Q}} = \bar{Q_0} e_0 + \bar{Q_1} e_1 + \bar{Q_2} e_2 + \bar{Q_3} e_3.
$$

**Hermitian conjugation** $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$:

$$
\tilde{Q}^{*} = \bar{Q_0} e_0 - \bar{Q_1} e_1 - \bar{Q_2} e_2 - \bar{Q_3} e_3.
$$

**Anti-Hermitian conjugation** $\tilde{Q}^\flat = -\tilde{Q}^{*}$:

$$
\tilde{Q}^\flat = -\bar{Q_0} e_0 + \bar{Q_1} e_1 + \bar{Q_2} e_2 + \bar{Q_3} e_3.
$$

Each conjugation is an involution: applying it twice returns the original biquaternion. Each therefore splits $\mathbb{B}$ into a fixed space and an anti-fixed space, and each of the two is a real vector subspace of $\mathbb{B}$. The first three have distinct eigenspaces, six in all; the reversal $\flat = -{}^{*}$ reproduces the two eigenspaces of ${}^{*}$ with the signs exchanged and adds no new one. The six are the **six distinguished subspaces** of $\mathbb{B}$, defined one to a section in *Introduction to the Six Subspaces* and tabulated in *Comparison of the Six Subspaces*.

The two anti-automorphisms ${}^{\natural}$ and ${}^{*}$, the Klein four-group they generate with the identity and their composite $\bar{\cdot}$, the place of the reversal $\flat = -{}^{*}$ outside it and the composition table that includes the reversal are *The Group of Involutions*; the lattice of the fixed spaces is *Comparison of the Six Subspaces*. Neither the group nor the six subspaces are repeated here: this article keeps the four formulas above, and the three decompositions the conjugations cut out are *Decompositions Along the Six Subspaces*.

## Summary

The biquaternion algebra read over the complex scalars is the set $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$, a complex vector space of dimension four on the basis $e_0 = 1, e_1, e_2, e_3$, with $e_k^2 = -e_0$. The central element $i$ satisfies $i^2 = -1$ and commutes with the quaternion units, and its multiples form the scalar line $\mathbb{C}e_0$, the centre, one of the six distinguished real subspaces.

The same element is written in three coordinate systems: eight real coordinates on the real basis $e_0, e_1, e_2, e_3, ie_0, ie_1, ie_2, ie_3$, four complex coordinates on the complex basis, and two quaternionic coordinates as a pair of real quaternions. The complex action is the linear structure of this article; the same set with the scalars cut down to $\mathbb{R}$, of dimension eight, and the complex structure $J$ that returns one reading from the other, are *Biquaternions as a Vector Space over $\mathbb{R}$*.

It carries four natural conjugations, ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}$ and $\flat = -{}^{*}$, of which the first three are commuting involutions; the group they form is *The Group of Involutions*. They define the six distinguished real subspaces of $\mathbb{B}$, defined one to a section in *Introduction to the Six Subspaces*, and the three direct-sum decompositions they cut out are *Decompositions Along the Six Subspaces*; the coordinate blocks, the intersections, the sums and the action of the conjugations upon the six are *Comparison of the Six Subspaces*.

Beyond the scalar fields the same set carries two structures whose base is a ring and not a field: the $\mathbb{H}$-bimodule, developed in *Biquaternions as a Bimodule over $\mathbb{H}$*, and the module over $\mathbb{B}$ itself, developed in *Modules over the General Plain Algebra of Biquaternions*.

The product read as the multiplication of an algebra is *Introduction to the General Plain Algebra of Biquaternions*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | Quaternion algebra |
| $\mathbb{B}$ | Biquaternion algebra, $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ |
| $e_0 = 1$ | Identity |
| $e_1, e_2, e_3$ | Quaternion units, $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, $i^2 = -1$, commutes with $e_k$ |
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ | General biquaternion |
| $Q_\mu = q_\mu + i q'_\mu$ | Complex coefficient, with $q_\mu, q'_\mu \in \mathbb{R}$ |
| $Q_0$ | Complex scalar part |
| $\mathbf{Q}$ | Complex vector part |
| $J : \tilde{Q} \mapsto i\tilde{Q}$ | the real-linear complex structure, $J^2 = -\mathrm{id}$ |
| $\tilde{Q}^{\natural} = Q_0 e_0 - \mathbf{Q}$ | Quaternion conjugate |
| $\bar{\tilde{Q}} = \bar{Q_0} e_0 + \mathbf{Q}^*$ | Complex conjugate |
| $\tilde{Q}^{*} = \bar{Q_0} e_0 - \mathbf{Q}^*$ | Hermitian conjugate |
| $\tilde{Q}^\flat = -\overline{\tilde{Q}^{\natural}} = -\tilde{Q}^{*}$ | Anti-Hermitian conjugate |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original formulation.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic treatment of biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the Clifford-algebra reading of the biquaternions.
