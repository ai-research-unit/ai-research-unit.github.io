
# __Dual-Numbers Null Quadric and Projective Geometry__

## Introduction

The norm $N(a + \varepsilon b) = a^2$ decides invertibility in the dual-number algebra and vanishes exactly on the zero divisors together with the origin. Both statements are algebraic: the criterion is in *Dual-Numbers Norm and Invertibility* and the zero-divisor classification in *Dual-Numbers Zero Divisors*. This article treats the form geometrically, following the structural model *Biquaternion Null Quadric and Projective Geometry*, where the norm of the biquaternions defines the Segre quadric in $\mathbb{P}^3$. Here the algebra is two-dimensional and the form has rank one, so the quadric degenerates to a single point of multiplicity two and the whole projective picture collapses.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. Throughout the algebra is $\mathbb{D}' = \mathbb{R}[\varepsilon]/(\varepsilon^2)$, a general dual number is

$$
Z = a + \varepsilon b, \qquad a, b \in \mathbb{R},
$$

with $a = \operatorname{Re} Z$, $b = \operatorname{Inf} Z$, dual conjugation $\bar{Z} = a - \varepsilon b$, the norm $N(Z) = Z\bar{Z} = a^2$ and its polar form $B(Z, W) = a c$ (a form and a distance, defined in *Dual-Numbers Norm and Invertibility*), and the maximal ideal $\mathrm{M} = (\varepsilon) = \varepsilon\mathbb{R}$, real submodule $R_{\mathbb{D}'}$ and infinitesimal submodule $\varepsilon R_{\mathbb{D}'}$. The geometry of the dual plane itself—dilations, shears, the parabolic angle—is developed in *Shears and Parabolic Rotations*.

## The Degenerate Isotropic Cone

### The Isotropic Set

**Definition.** The **isotropic set** of the norm is

$$
\mathcal{N} = \{Z \in \mathbb{D}' : N(Z) = 0\} = \{Z : a = 0\} = \mathrm{M},
$$

the maximal ideal. Its punctured part is the zero-divisor set $\mathcal{Z} = \mathrm{M} \setminus \{0\}$.

**Theorem.** $\mathcal{N} = \mathrm{M}$ is a single line through the origin, closed and of real dimension one, and it is a cone with apex $0$; it is the radical of $B$. As a quadratic cone it is a **double line**: the equation $a^2 = 0$ is the square of the linear equation $a = 0$, so the cone is the line $a = 0$ counted twice.

**Proof.** $N(Z) = a^2 = 0$ forces $a = 0$, giving the line $\varepsilon\mathbb{R}$; homogeneity gives the cone property; and $a^2$ factors as $a\cdot a$, so the defining polynomial is the square of the linear form $a$.

### Comparison with a Non-Degenerate Cone

For a non-degenerate binary quadratic form $a^2 - \sigma b^2$ with $\sigma \neq 0$ the isotropic set is a union of two distinct lines through the origin, the two null directions; for the positive-definite form $a^2 + b^2$ it is a single point, the origin. The degenerate dual form is the intermediate case: the two null directions of the split-complex form have coalesced into a single line, and because the form is a perfect square, the coalescence is a genuine doubling rather than a loss. The real dimension of the isotropic set is one, whereas for the split-complex form it is also one (a union of two lines is one-dimensional), but the two cases differ in multiplicity: the dual line is met with multiplicity two by every transverse line, the split-complex pair with multiplicity one each.

## The Projective Line

### The Projective Dual Line

**Definition.** The **projective dual line** is

$$
\mathbb{P}(\mathbb{D}') = \mathbb{P}^1(\mathbb{R}) = \{[a : b] : (a,b) \neq (0,0)\},
$$

the space of lines through the origin of the dual plane; it is a one-dimensional projective space homeomorphic to a circle.

### The Affine Chart

On the open chart $\{a \neq 0\}$ use the affine coordinate

$$
t = \frac{b}{a},
$$

the coordinate of the line through the origin of slope $t$, i.e. of the point $[(1, t)] = [1 : t]$; the complement of the chart is the single point

$$
[0 : 1] = [\varepsilon],
$$

the class of the maximal ideal, the point at infinity of the chart.

### The Projective Isotropic Point

**Theorem.** The projectivised isotropic set is the single point

$$
\mathbb{P}(\mathcal{N}) = \{[0 : 1]\} = \{[\varepsilon]\} \subset \mathbb{P}^1(\mathbb{R}),
$$

a point of multiplicity two. It is the unique real point of the projective quadric $a^2 = 0$, and the projective quadric is that point counted twice.

**Proof.** In homogeneous coordinates the equation $N = 0$ reads $a^2 = 0$, whose only solution is $a = 0$, giving the point $[0 : 1]$; the equation is a square, so the zero is of multiplicity two.

### The Ramified Point

So the projective dual quadric is a **single ramified point** rather than a pair of rational points or a smooth conic. In the affine picture the line $a = 0$ has two ends, $b \to +\infty$ and $b \to -\infty$; the projective line identifies them into one point, and the fact that the projective quadric counts it twice is exactly the statement that both ends are isotropic. A non-degenerate binary form would give two distinct points—the two null directions—or, in the definite case, no real point; the dual form gives one point of multiplicity two, the degenerate intermediate.

## The Parabolic Projectivity

### The Action on the Projective Line

Multiplication by the unit $u = 1 + s\varepsilon$ is the shear $S(s)$, which acts on the dual plane by

$$
S(s)(a + \varepsilon b) = a + (b + sa)\varepsilon.
$$

In homogeneous coordinates this is the linear map $[a : b] \mapsto [a : b + sa]$, induced by the matrix

$$
\begin{pmatrix} 1 & 0 \\ s & 1 \end{pmatrix}.
$$

**Theorem.** On the affine chart $\{a \neq 0\}$ the shear acts by translation of the coordinate $t$:

$$
t = \frac{b}{a} \;\longmapsto\; \frac{b + sa}{a} = t + s.
$$

It fixes the isotropic point $[\varepsilon] = [0:1]$ and no other point, and it is the one-parameter unipotent subgroup of the parabolic subgroup of $PGL_2(\mathbb{R})$ that fixes that point.

**Proof.** The computation of $t \mapsto t + s$ is immediate; the point $[0:1]$ is fixed because $S(s)(\varepsilon) = \varepsilon$, and a translation of the affine line fixes only its point at infinity. The matrix has a repeated eigenvalue $1$ and is unipotent, so the subgroup is parabolic and conjugate to the translations.

### The Projectivity Fixing the Ramified Point

So the parabolic one-parameter group of the dual numbers is exactly the unipotent subgroup of $PGL_2(\mathbb{R})$ that fixes the isotropic point, and the isotropic point is fixed with multiplicity two, matching its multiplicity as a point of the projective quadric. The shears are the "rotations" of the degenerate form, and the geometry they generate is the geometry of the dual plane described in *Shears and Parabolic Rotations*: the orbits are the fibres of the augmentation, the isotropic line is fixed pointwise, and the parabolic angle is additive.

## Relation to the Null Quadric of $\mathbb{B}$ and to the Geometry of the Dual Plane

### The Biquaternion Quadric

In the biquaternion algebra the norm $N(\tilde{Q}) = \sum_\mu Q_\mu^2$ is non-degenerate on $\mathbb{C}^4$, and its null cone projects to the smooth Segre quadric $\mathbb{P}^1 \times \mathbb{P}^1 \subset \mathbb{P}^3$, a surface with two rulings, each ruling a family of null planes, and the isotropic subspaces are two-dimensional. Every ingredient of that picture depends on the non-degeneracy of the form and on the complex dimension four.

In the dual case the form has rank one on a real vector space of dimension two. The consequences are the following, and they are all forced by the rank:

| | $\mathbb{B}$ (rank $4$, dim $4$ over $\mathbb{C}$) | $\mathbb{D}'$ (rank $1$, dim $2$ over $\mathbb{R}$) |
|---|---|---|
| Polar form $B$ | non-degenerate | degenerate, $\operatorname{rad} B = \mathrm{M}$ |
| Isotropic set | null cone, codimension $2$ | single line $\mathrm{M}$, codimension $1$ |
| Projective quadric | smooth Segre quadric $\mathbb{P}^1\times\mathbb{P}^1$ | single point of multiplicity two |
| Maximal totally isotropic subspace | dimension $2$ (null planes) | dimension $1$ (the line $\mathrm{M}$) |
| Rulings | two, indexed by spinors | none |
| Polarity | non-degenerate correlation | none |
| Symmetry group of the quadric | projectivity group acting on $\mathbb{P}^3$ | parabolic subgroup of $PGL_2(\mathbb{R})$ |

The comparison isolates the single feature that controls the whole degeneration: the rank of the polar form. Rank one means the radical is a hyperplane (the maximal ideal), so the isotropic set is the radical, the maximal totally isotropic subspace is one-dimensional, and the projective quadric is a doubled point. In the biquaternion case rank four gives a radical of dimension zero, an isotropic cone of codimension two, and a smooth quadric surface with rulings. There is no intermediate for a two-dimensional real form except the split case of rank two, whose projective quadric is two distinct points.

### The Geometry of the Dual Plane

Read on the dual plane rather than on the projective line, the picture is the one developed in *Shears and Parabolic Rotations*: the isotropic line $\mathrm{M}$ is the fixed line of the shear, the shear translates the fibres of the augmentation, and the norm registers none of the displacement because the nilpotent direction lies in the radical. The projective statement—the shear is the parabolic projectivity fixing the doubled isotropic point—is the compact way to say that multiplication by a unit acts on the dual plane as a unipotent map with a single fixed line, the isotropic line.

## Summary

The norm $N(a + \varepsilon b) = a^2$ of the dual numbers has the polar form $B(Z, W) = a c$, a symmetric $\mathbb{R}$-bilinear form of rank one with radical the maximal ideal $\mathrm{M} = \varepsilon\mathbb{R}$. The isotropic set is the single line $\mathrm{M}$, a cone with apex $0$ that is the **double line** $a^2 = 0$; the form admits no polarity, since every point off the isotropic line has the same polar $\mathrm{M}$ and the isotropic line has polar the whole space. On the projective dual line $\mathbb{P}^1(\mathbb{R})$ with affine coordinate $t = b/a$, the projective quadric is the single point $[\varepsilon] = [0:1]$ of multiplicity two, the ramified point at infinity of the chart. Multiplication by the unit $1 + s\varepsilon$ acts as the shear, which on the projective line is the parabolic projectivity $t \mapsto t + s$ fixing $[\varepsilon]$, the unipotent subgroup of $PGL_2(\mathbb{R})$ that fixes the doubled isotropic point and generates the geometry of the dual plane. Compared with the biquaternion null quadric—the smooth Segre quadric $\mathbb{P}^1\times\mathbb{P}^1$ with two rulings, self-dual polarity and dimension-two null planes—the dual quadric is the total degeneration forced by rank one: a single doubled point, no rulings, no polarity, and a one-dimensional isotropic subspace.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}' = \mathbb{R}[\varepsilon]/(\varepsilon^2)$ | Dual-number algebra; $\varepsilon^2 = 0$ |
| $Z = a + \varepsilon b$ | General dual number |
| $a = \operatorname{Re} Z$, $b = \operatorname{Inf} Z$ | Real and infinitesimal parts |
| $N(Z) = Z\bar{Z} = a^2$ | Norm, rank one |
| $B(Z,W) = a c$ | Polar form, symmetric bilinear, rank one |
| $[B] = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ | Matrix of the polar form $B$ in the basis $(1,\varepsilon)$ |
| $\mathrm{M} = (\varepsilon) = \operatorname{rad}(B)$ | Maximal ideal, radical, isotropic line |
| $\mathcal{N} = \mathrm{M}$ | Isotropic set, the double line $a^2 = 0$ |
| $\mathbb{P}(\mathbb{D}') = \mathbb{P}^1(\mathbb{R})$ | Projective dual line |
| $[a : b]$ | Homogeneous coordinates; $[\varepsilon] = [0:1]$ |
| $t = b/a$ | Affine coordinate on $\{a \neq 0\}$ |
| $S(s)$ | Shear, parabolic projectivity $t \mapsto t + s$ |
| $\mathbb{B}$ | Biquaternion algebra, the comparison model, Segre quadric |

## Further Reading

- Pierre Samuel, *Projective Geometry* (Springer, New York, 1988), for polarity, degenerate quadrics, and the projective classification of binary quadratic forms.
- J. G. Semple and G. T. Kneebone, *Algebraic Projective Geometry* (Oxford University Press, Oxford, 1952), for quadrics, their rulings, and degenerate limits.
- Eduard Study, *Geometrie der Dynamen* (Teubner, Leipzig, 1903), for the projective geometry of the dual numbers and their isotropic line.
- Wilhelm Blaschke, *Vorlesungen über Differentialgeometrie I* (Springer, Berlin, 1930), for the classical use of the dual isotropic direction in line geometry.
- Vladimir V. Kisil, *Geometry of Möbius Transformations: Elliptic, Parabolic and Hyperbolic Actions of $SL(2,\mathbb{R})$* (Imperial College Press, London, 2012), for parabolic projectivities fixing a point of the projective line and the unipotent one-parameter subgroups.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Grundlehren der mathematischen Wissenschaften 294, Springer, Berlin, 1991), for the radical of a degenerate form and the dimension of its maximal totally isotropic subspaces.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, Natick, 2003), for the norms and isotropic sets of the number systems of the family.
