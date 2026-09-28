
# __Split-Complex Null Quadric and Projective Geometry__

## Introduction

The norm $N(Z)=a^2-b^2$ of the split-complex algebra decides invertibility (*Split-Complex Norm and Invertibility*) and vanishes exactly on the zero divisors together with the origin (*Split-Complex Zero Divisors*). Both treatments are algebraic; this article treats the form geometrically. It polarises $N$ and reads $\mathbb{D}$ as a real quadratic space of signature $(1,1)$; describes the null cone as the pair of null lines; identifies the projective null quadric as two points of the real projective line; reads the two isotropic points as the **points at infinity** of the hyperbolic geometry of the plane; exhibits the hyperbolic one-parameter group $\{e^{jt}\}$ as the projectivity fixing them; and relates the picture to the projective quadric of the biquaternion algebra and to the hyperbolic geometry developed in *Hyperbolic Rotations*. It is the two-dimensional counterpart of *Biquaternion Null Quadric and Projective Geometry*, and the degeneration is complete: the smooth quadric surface of the biquaternion theory drops to two projective points.

The article owns the quadratic space $(\mathbb{D},N)$ read geometrically, the projective null quadric and the two points at infinity, the action of the hyperbolic group as a projectivity, and the cross-ratio description of the hyperbolic distance; the norm and its polarisation are defined and owned by *Split-Complex Norm and Invertibility*, and are used here as the geometric input. No physics is invoked and no new result is claimed.

**Conventions.** The algebra is $\mathbb{D}=\mathbb{R}[x]/(x^2-1)$, basis $1$, $j$ with $j^2=+1$; a general element is $Z=a+j b$ with $a,b\in\mathbb{R}$; idempotents $\Pi_\pm=\tfrac12(1\pm j)$; norm $N(Z)=a^2-b^2$, of signature $(1,1)$. The projective line of one-dimensional subspaces is written $\mathbb{P}(\mathbb{D})\cong\mathbb{RP}^1$, with homogeneous coordinates $[a:b]$ and affine coordinate $t=b/a$.

## The Quadratic Space

The norm $N(a,b)=a^2-b^2$ and its polarisation are defined and owned by *Split-Complex Norm and Invertibility*; the present article reads them geometrically. The form is homogeneous of degree two, and it polarises to the symmetric real-bilinear form

$$
B(Z,W)=a c-b d, \qquad Z=a+j b,\ W=c+j d,
$$

whose Gram matrix in the basis $\{1,j\}$ is $\mathbf{G}=\operatorname{diag}(1,-1)$. The pair $(\mathbb{D},N)$ is therefore a non-degenerate real quadratic space of dimension $2$ and signature $(1,1)$: the basis $\{1,j\}$ is orthogonal, with $N(1)=+1$ and $N(j)=-1$, and the Gram determinant is $\det\mathbf{G}=-1\neq0$. This is the geometry's input rather than its construction: the algebra owns the form, and the geometry reads it.

The form is **indefinite** and **split**: its discriminant is $\operatorname{disc}(N)=4>0$, a square in $\mathbb{R}$, and the form is isometric to the difference of two squares. The comparison with the definite case is the whole content of the geometry: the complex field carries the positive definite form $a^2+b^2$, whose projective null quadric is empty over $\mathbb{R}$, whereas the split-complex algebra carries $a^2-b^2$, whose projective null quadric is the pair of points computed below. The motions the form generates — its isometry group $O(1,1)$ and the hyperbolic rotations of its identity component — are the subject of *Hyperbolic Rotations*.

## The Isotropic Cone and the Null Lines

**Definition.** A vector $Z\neq0$ is **isotropic** or **null** if $N(Z)=0$, and the **isotropic cone** (the null cone) is $\mathcal{N}=\{Z:N(Z)=0\}$.

**Theorem.** The isotropic cone is the union of the two **null lines**

$$
\mathcal{N}=\{a=b\}\cup\{a=-b\}=\mathbb{R}(1+j)\ \cup\ \mathbb{R}(1-j)=\mathbb{R}\Pi_1\ \cup\ \mathbb{R}\Pi_2,
$$

each a maximal totally isotropic subspace of $(\mathbb{D},N)$; the two lines are the eigenspaces of the conjugation and are interchanged by it. There are no other isotropic vectors.

**Proof.** $N(Z)=a^2-b^2=(a-b)(a+b)$, so $N(Z)=0$ iff $a=b$ or $a=-b$, which are the two lines displayed. On either line the restricted form vanishes identically, so each is totally isotropic; a two-dimensional space of signature $(1,1)$ has totally isotropic subspaces only of dimension $1$, so each is maximal. The idempotents $\Pi_\pm=\tfrac12(1\pm j)$ span the two lines, and $\bar \Pi_1 = \Pi_2$.

So the null cone is a **degenerate quadric**: two lines meeting at the apex, rather than the nonsingular cone of a definite form. It contains the zero divisors of the algebra together with $0$, and the two lines are exactly the two isotropic directions of the Lorentzian plane.

## The Real Projective Line and the Two Points at Infinity

**Definition.** The **real projective line** of the algebra is the set of one-dimensional subspaces,

$$
\mathbb{P}(\mathbb{D})=(\mathbb{D}\setminus\{0\})/\mathbb{R}^\times \cong \mathbb{RP}^1\cong S^1,
$$

with a point written $[a:b]$ for the line spanned by $a+j b$; the affine coordinate is $t=b/a$ on the chart $a\neq0$, with the remaining point $[0:1]=[j]$ the point at infinity of the chart.

**Theorem (the projective null quadric).** The projectivised isotropic cone is the two-point set

$$
Q^0=\mathbb{P}(\mathcal{N})=\{[1:1],\ [1:-1]\}=\{[\mathbb{R}\Pi_1],\ [\mathbb{R}\Pi_2]\}\cong 2\ \text{points},
$$

the **two points at infinity** of the hyperbolic plane; in the affine coordinate they are $t=+1$ and $t=-1$.

**Proof.** The isotropic lines are the two spanned by $1+j$ and $1-j$, with homogeneous coordinates $[1:1]$ and $[1:-1]$, distinct because the lines are distinct. A one-dimensional subspace is isotropic iff it meets $\mathcal{N}\setminus\{0\}$, and $\mathcal{N}\setminus\{0\}$ is exactly the union of the two lines, so there are no others.

**The two arcs.** The two points at infinity divide the projective line into two open arcs:

$$
\mathbb{P}(\mathbb{D})\setminus Q^0=\{N>0\}\ \sqcup\ \{N<0\},
$$

the first the interval $-1<t<1$ through the real line $[1]=[1:0]$, the second the complementary arc through the split imaginary line $[j]$, corresponding to the directions of positive and negative norm. So the projective line is the circle, the isotropic points are two marked points, and the definite and indefinite directions occupy the two arcs they cut out.

**The quadratic form as a cross-ratio form.** The pair of isotropic points is the **absolute** of the geometry: the form $N$ is recovered from the two points, and every quantity of the geometry is a cross-ratio with respect to them. The **two points at infinity** are therefore not an accident of coordinates but the defining data of the Lorentzian structure.

## The Hyperbolic One-Parameter Group as a Projectivity

**Theorem (the hyperbolic group acts by projectivities).** The hyperbolic one-parameter group $\{e^{js}\}_{s\in\mathbb{R}}$, $e^{js}=\cosh s+j\sinh s$, preserves $N$ and therefore acts on the projective line, where its projectivity is

$$
s:\quad t\longmapsto t'=\frac{t+\tau}{1+\tau t}, \qquad \tau=\tanh s ,
$$

a Möbius transformation **fixing the two points at infinity** $t=\pm1$.

**Proof.** Multiplication by $e^{js}$ has matrix $\begin{pmatrix}\cosh s & \sinh s \\ \sinh s & \cosh s\end{pmatrix}$ on coordinates $(a,b)$, and preserves $N$ because $N(e^{js}Z)=N(e^{js})N(Z)=N(Z)$ with $N(e^{js})=\cosh^2 s-\sinh^2 s=1$. On the ratio $t=b/a$ it acts by $t'=\dfrac{a\sinh s+b\cosh s}{a\cosh s+b\sinh s}=\dfrac{t+\tanh s}{1+t\tanh s}$, the stated Möbius map. Its fixed points solve $t=(t+\tau)/(1+\tau t)$, that is $\tau t^2=\tau$, so $t=\pm1$ for $\tau\neq0$, which are the isotropic points.

**Corollary (the velocity-addition law).** The composition of two projectivities is the projectivity of the sum, $\tau\mapsto\tanh(s_1+s_2)=\dfrac{\tau_1+\tau_2}{1+\tau_1\tau_2}$; the parameter $\tau=\tanh s$ obeys the addition law of hyperbolic tangents, the two-dimensional analogue of the tangent-addition law of the complex circle.

**Remark (the full stabiliser).** The projectivities fixing each of the two points at infinity form the one-dimensional group

$$
\mathrm{Stab}\{Q^0\}\cong\mathbb{R}^\times,
$$

the projectivisation of the conformal group of the Lorentzian plane that preserves each null direction; the hyperbolic one-parameter group $\{e^{js}\}\cong(\mathbb{R},+)$ is its identity component, and the other component is obtained by composing with the projectivity $t\mapsto1/t$ induced by multiplication by $j$, which fixes both points and exchanges the two arcs. In the basis of idempotents the stabiliser is the group of diagonal matrices $\operatorname{diag}(\lambda,\lambda^{-1})$ modulo scalars, and the projectivity is the pair of reciprocal scalings of the two null directions.

## The Hyperbolic Line and Its Distance

**Definition.** The **hyperbolic line** is the arc of positive directions

$$
H=\{-1<t<1\}\subset\mathbb{P}(\mathbb{D}),
$$

between the two points at infinity, together with the hyperbolic distance

$$
d(t_1,t_2)=\lvert\operatorname{artanh} t_1-\operatorname{artanh} t_2\rvert .
$$

**Theorem (the distance is a cross-ratio).** With the two points at infinity as the absolute, the cross-ratio

$$
(t_1,t_2\,;\,-1,1)=\frac{(t_1+1)(t_2-1)}{(t_1-1)(t_2+1)}
$$

satisfies $d(t_1,t_2)=\tfrac12\lvert\ln(t_1,t_2\,;-1,1)\rvert$, so the hyperbolic distance is the logarithm of the cross-ratio to the two points at infinity, and the hyperbolic group $\{e^{js}\}$ acts on $H$ as the **one-parameter group of translations**, $s : t\mapsto t'$ with $\operatorname{artanh} t' = \operatorname{artanh} t + s$.

**Proof.** The substitution $\sigma=\operatorname{artanh} t$ conjugates the projectivity $t\mapsto(t+\tau)/(1+\tau t)$ to the translation $\sigma\mapsto\sigma+s$, since $\tanh(\sigma+s)=(\tanh\sigma+\tanh s)/(1+\tanh\sigma\tanh s)$; hence the group acts on $H$ by translations in the parameter $\sigma$, and the invariant distance is $\lvert\sigma_1-\sigma_2\rvert$. For the cross-ratio, $1+\tanh\sigma=e^{\sigma}/\cosh\sigma$ and $1-\tanh\sigma=e^{-\sigma}/\cosh\sigma$, so

$$
\Bigl\lvert\frac{(t_1+1)(t_2-1)}{(t_1-1)(t_2+1)}\Bigr\rvert=\frac{(1+t_1)(1-t_2)}{(1-t_1)(1+t_2)}=\exp\bigl(2(\sigma_1-\sigma_2)\bigr),
$$

and taking half the logarithm gives $\tfrac12\lvert\ln\rvert=\lvert\sigma_1-\sigma_2\rvert=d(t_1,t_2)$.

So the geometry attached to the split-complex plane is the one-dimensional **hyperbolic geometry**: the projective line with the two isotropic points as absolute, the interval between them as the hyperbolic line, and the hyperbolic group as its translations. This is the projective form of the rotations of *Hyperbolic Rotations*, and the same interval is the parameter domain of the spacelike branch of the unit hyperbola.

## Relation to the Biquaternion Quadric

The biquaternion null quadric in $\mathbb{P}^3(\mathbb{C})$ is the smooth Segre quadric $Q^2\cong\mathbb{P}^1\times\mathbb{P}^1$, a surface with two rulings; its projectivised null cone has real dimension $4$ and carries the two chiral spinor families as its two rulings. The split-complex quadric is the same construction in the lowest dimension, and the degeneration is a drop in rank and dimension.

| feature | $\mathbb{B}$ | $\mathbb{D}$ |
|---|---|---|
| quadratic space | $(\mathbb{C}^4, \sum_\mu Q_\mu^2)$, non-degenerate | $(\mathbb{R}^2, a^2-b^2)$, signature $(1,1)$ |
| null cone | nonsingular complex hypersurface, real dim $6$ | two real lines, real dim $1$ |
| projective null quadric | $Q^2\cong\mathbb{P}^1\times\mathbb{P}^1\subset\mathbb{P}^3$ | $Q^0$, two points of $\mathbb{RP}^1$ |
| rulings | two $\mathbb{P}^1$-families (the spinor lines) | two lines, each a single $1$-dimensional family |
| isometry group of the form | $O(1,3)$ on the real form | $O(1,1)$, real dim $1$, four components |
| identity component acting as projectivities | $PSO(1,3)^+$ | $\{e^{js}\}\cong(\mathbb{R},+)$ |

The pattern is that the null cone of $\mathbb{B}$ is a nonsingular quadric whose projectivisation is a surface with two rulings, while the null cone of $\mathbb{D}$ is a degenerate quadric whose projectivisation is two points; the two rulings survive only as the two null directions, and the spinor families of the biquaternion theory have no room to appear. The projective automorphism group descends from $PSO(1,3)^+$ to the hyperbolic translation group of the line.

## Summary

The split-complex norm $N(a,b)=a^2-b^2$ polarises to the Lorentzian inner product $B(Z,W)=a c-b d$ with Gram matrix $\operatorname{diag}(1,-1)$, making $(\mathbb{D},N)$ a non-degenerate real quadratic space of signature $(1,1)$. Its isotropic cone is the pair of null lines $\mathbb{R}(1+j)$ and $\mathbb{R}(1-j)$, each maximal totally isotropic and each spanned by an idempotent; the two lines are interchanged by the conjugation. The projective null quadric is the two-point set $Q^0=\{[1:1],[1:-1]\}\subset\mathbb{RP}^1$, whose points are the two points at infinity of the hyperbolic geometry: they are the absolute of the form, and they divide the projective line into the arc of positive directions and the arc of negative directions.

The hyperbolic one-parameter group $\{e^{js}\}$ acts on the projective line by the Möbius projectivity $t\mapsto(t+\tanh s)/(1+t\tanh s)$, fixing the two points at infinity; the full stabiliser of the pair is the one-dimensional group $\mathbb{R}^\times$, of which $\{e^{js}\}$ is the identity component. On the interval between the points at infinity the group acts as translations of the hyperbolic line, and the hyperbolic distance is the logarithm of the cross-ratio to the two points at infinity, $\tfrac12\lvert\ln(t_1,t_2\,;-1,1)\rvert$. The relation to the biquaternion quadric is a degeneration: the smooth Segre quadric surface $\mathbb{P}^1\times\mathbb{P}^1$ of $\mathbb{B}$ drops to two projective points, its two rulings to the two null directions, and its isometry group to the one-dimensional $O(1,1)$ whose identity component is the hyperbolic group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra |
| $Z = a + j b$ | General split complex number |
| $N(Z) = a^2 - b^2$ | Norm, signature $(1,1)$ |
| $B(Z,W) = a c - b d$ | Polar form, Lorentzian inner product |
| $\mathbf{G} = \operatorname{diag}(1,-1)$ | Gram matrix of $B$ |
| $\mathcal{N}$ | Isotropic cone; the two null lines $a = \pm b$ |
| $\Pi_\pm = \tfrac12(1\pm j)$ | Idempotents, spanning the null lines |
| $\mathbb{P}(\mathbb{D})\cong\mathbb{RP}^1$ | Real projective line; $[a:b]$, affine coordinate $t = b/a$ |
| $Q^0 = \{[1:1],[1:-1]\}$ | Projective null quadric; the two points at infinity |
| $t = \pm1$ | The two isotropic points in the affine coordinate |
| $e^{js} = \cosh s + j\sinh s$ | Hyperbolic one-parameter group |
| $t\mapsto\frac{t+\tanh s}{1+t\tanh s}$ | The projectivity induced on $\mathbb{P}(\mathbb{D})$ |
| $\mathrm{Stab}\{Q^0\}\cong\mathbb{R}^\times$ | Projectivities fixing each of the two points at infinity |
| $H = \{-1<t<1\}$ | The hyperbolic line, the arc of positive directions |
| $d(t_1,t_2) = \tfrac12\lvert\ln(t_1,t_2\,;-1,1)\rvert$ | Hyperbolic distance as a cross-ratio |
| $O(1,1)$ | Isometry group of the space, real dim $1$, four components |

## Further Reading

- O. Timothy O'Meara, *Introduction to Quadratic Forms* (Springer, Grundlehren der Mathematischen Wissenschaften 117, 1973), for quadratic spaces, signature, isotropy and totally isotropic subspaces.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, Graduate Studies in Mathematics 67, 2005), for the split form $x^2-y^2$, its discriminant and its isometry group.
- H. S. M. Coxeter, *The Real Projective Plane* (Springer, 3rd ed. 1993), for projectivities of the projective line, fixed points and cross-ratio.
- Jürgen Richter-Gebert, *Perspectives on Projective Geometry* (Springer, 2011), for the absolute, the Cayley–Klein model and hyperbolic distance as a cross-ratio.
- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the hyperbolic rotation group and the geometry of the split complex plane.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for $\mathrm{Cl}(1,1)$, its even part and the volume element.
