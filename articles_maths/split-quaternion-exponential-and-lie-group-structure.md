
# __Split-Quaternion Exponential and Lie Group Structure__

## Introduction

The split-quaternion algebra $\mathbb{H}_{\mathrm{s}} \cong M_2(\mathbb{R})$ carries two group structures and one Lie algebra structure that interlock: the **group of units** $\mathbb{H}_{\mathrm{s}}^\times = GL_2(\mathbb{R})$, the **norm-one group** $U = \{N = 1\} \cong SL_2(\mathbb{R})$, and the Lie algebra $\mathfrak{sl}_2(\mathbb{R})$ of traceless elements under the commutator. The link is the exponential map, which we compute in closed form and study for its group law, its kernel and its range. Because the norm form is indefinite, the exponential splits into an elliptic part from the directions of square $+1$ and a hyperbolic part from the directions of square $-1$.

This article owns the exponential and the Lie group structure: the algebra as a Lie algebra, the closed form of the exponential, the group of units, the norm-one group and its identification with $SL_2(\mathbb{R})$, the elliptic and hyperbolic subgroups, and the polar and exponential parametrisation. It relies on *Split-Quaternion Rotations and the Lorentz Group* for the Lorentz action, on *Split-Quaternion Automorphisms and Derivations* for the derivations. No physics is invoked.

**Conventions.** A general element is $\tilde q = q_0 + \mathbf v$ with $q_0 = \operatorname{Sc}(\tilde q) \in \mathbb{R}$ and $\mathbf v = q_1e_1 + q_2e_2 + q_3e_3 \in V$. The norm form is $N(\tilde q) = q_0^2 + N(\mathbf v)$ with $N(\mathbf v) = q_1^2 - q_2^2 - q_3^2$, and on a vector $\mathbf v^2 = -N(\mathbf v)$. Under the commutator $V$ is the Lie algebra $\mathfrak{sl}_2(\mathbb{R})$.

## The Algebra as a Lie Algebra

**Definition.** The **commutator** $[\tilde q,y] = \tilde q y - y\tilde q$ makes $\mathbb{H}_{\mathrm{s}}$ into a real Lie algebra. Its centre is again the scalar line $S = \mathbb{R}\cdot1$, and the associated Lie algebra modulo the centre is

$$
\mathbb{H}_{\mathrm{s}}/S \;\cong\; V \;\cong\; \mathfrak{sl}_2(\mathbb{R}),
$$

of dimension $3$.

**Proposition.** The commutator restricts to a Lie bracket on $V$, where it satisfies

$$
[e_1,e_2] = 2e_3, \qquad [e_2,e_3] = -2e_1, \qquad [e_3,e_1] = 2e_2,
$$

so $V \cong \mathfrak{sl}_2(\mathbb{R}) \cong \mathfrak{so}(2,1)$. The bracket vanishes on $S$ and on the split-complex planes: $[S, \mathbb{H}_{\mathrm{s}}] = 0$ and $[\mathbb{D}_k, \mathbb{D}_k] = 0$. The form $B(\tilde q,y) = \tfrac{1}{2}(N(\tilde q+y) - N(\tilde q) - N(y))$, restricted to $V$, is invariant under the adjoint action, and the **Killing form** of the Lie algebra $\mathfrak{sl}_2(\mathbb{R})$ is a nonzero multiple of it; on $V$ it is the form of signature $(2,1)$.

**Proof.** The brackets are the multiplication table of the algebra. If $\tilde q, y \in V$ then $\tilde q y + y\tilde q$ is scalar and equal to $-2B(\tilde q,y)$, so $[\tilde q,y] = \tilde q y - y\tilde q$ has zero trace and lies in $V$; the vanishing statements on $S$ and on each $\mathbb{D}_k$ are the commutativity of the scalar line and of the plane. Since $V$ is the adjoint module of $\mathfrak{sl}_2(\mathbb{R})$ and is irreducible, the space of invariant symmetric bilinear forms on it is one-dimensional, so $B|_V$ and the Killing form differ by a nonzero scalar. Invariance of $B$ follows from the multiplicativity of $N$ along the one-parameter automorphism groups $\operatorname{Ad}_{e^{tw}} = e^{t\,\mathrm{ad}_w}$: differentiating $N\bigl(e^{t\,\mathrm{ad}_w} y\bigr) = N(y)$ at $t=0$ gives $B(\mathrm{ad}_w \tilde q, y) + B(\tilde q, \mathrm{ad}_w y) = 0$. $\square$

## The Group of Units

**Theorem.** The units of $\mathbb{H}_{\mathrm{s}}$ are the elements of nonzero norm,

$$
\mathbb{H}_{\mathrm{s}}^\times = \{\, \tilde q : N(\tilde q) \neq 0 \,\} \cong GL_2(\mathbb{R}),
$$

with inverse $\tilde q^{-1} = \bar{\tilde q}/N(\tilde q)$. The group has exactly **two connected components**, $\{N > 0\}$ and $\{N < 0\}$, the sign of the norm separating them.

**Proof.** $\tilde q\bar{\tilde q} = N(\tilde q)$ shows that $N(\tilde q)\neq0$ implies invertibility, and $N(\tilde q y) = N(\tilde q)N(y)$ shows that the non-units are exactly the nonzero null elements. The continuous surjection $N : \mathbb{H}_{\mathrm{s}}^\times \to \mathbb{R}^\times$ maps onto the two components of $\mathbb{R}^\times$, and the level set $\{N>0\}$ is connected (it retracts onto $U$), as is $\{N<0\}$; so the group has two components. $\square$

The identity component $\{N>0\} \cong GL_2^+(\mathbb{R})$ is the part of the group acting by the orientation-preserving half of the Lorentz action; the component $\{N<0\}$ acts by Lorentz transformations reversing time orientation, as in *Split-Quaternion Rotations and the Lorentz Group*.

## The Exponential: Series and Closed Form

**Definition.** The **exponential** of $\tilde q \in \mathbb{H}_{\mathrm{s}}$ is

$$
\exp(\tilde q) = e^{\tilde q} = \sum_{k \geq 0} \frac{\tilde q^k}{k!},
$$

convergent for every $\tilde q$, because the algebra is finite-dimensional and a submultiplicative norm exists on it.

**Theorem (closed form).** Write $\tilde q = q_0 + \mathbf v$ and put $\mu = N(\mathbf v) = q_1^2 - q_2^2 - q_3^2$. Then

$$
\exp(\tilde q) = e^{q_0} \Bigl( \cosh\sqrt{-\mu} + \frac{\sinh\sqrt{-\mu}}{\sqrt{-\mu}}\,\mathbf v \Bigr), \qquad \mu < 0,
$$

$$
\exp(\tilde q) = e^{q_0} \bigl( 1 + \mathbf v \bigr), \qquad \mu = 0,
$$

$$
\exp(\tilde q) = e^{q_0} \Bigl( \cos\sqrt{\mu} + \frac{\sin\sqrt{\mu}}{\sqrt{\mu}}\,\mathbf v \Bigr), \qquad \mu > 0 .
$$

**Proof.** The scalar $q_0$ commutes with $\mathbf v$, so $e^{\tilde q} = e^{q_0} e^{\mathbf v}$, and $\mathbf v^2 = -N(\mathbf v) = -\mu$ is scalar. Hence $\mathbf v^{2k} = (-1)^k \mu^k$ and $\mathbf v^{2k+1} = (-1)^k \mu^k \mathbf v$, and the series splits into the even and odd parts $\sum_k \frac{(-1)^k\mu^k}{(2k)!}$ and $\mathbf v \sum_k \frac{(-1)^k\mu^k}{(2k+1)!}$. These are the power series of $\cos$ and $\sin$ when $\mu > 0$, of $\cosh$ and $\sinh$ when $\mu < 0$ (after factoring $\sqrt{|\mu|}$), and terminate as $1$ and $\mathbf v$ when $\mu = 0$. $\square$

**Corollary.** The norm of the exponential is $N(e^{\tilde q}) = e^{2q_0}$, so the exponential lands in the component $\{N > 0\}$ of the group of units, and $\exp(S) = \mathbb{R}_{>0}$.

**Proof.** The multiplicativity $N(ab) = N(a)N(b)$ together with $N(e^{q_0}) = e^{2q_0}$ for a scalar reduce the claim to $N(e^{\mathbf v}) = 1$ for $\mathbf v \in V$. The element $\mathbf v$ generates the commutative two-dimensional subalgebra $\operatorname{span}\{1, \mathbf v\}$ with $\mathbf v^2 = -N(\mathbf v)$; writing $\lambda = -N(\mathbf v)$, the exponential in this subalgebra is $e^{\mathbf v} = \cosh\sqrt\lambda + \frac{\sinh\sqrt\lambda}{\sqrt\lambda}\,\mathbf v$ for $\lambda > 0$, $e^{\mathbf v} = \cos\sqrt{-\lambda} + \frac{\sin\sqrt{-\lambda}}{\sqrt{-\lambda}}\,\mathbf v$ for $\lambda < 0$, and $e^{\mathbf v} = 1 + \mathbf v$ for $\lambda = 0$; in each case $N(e^{\mathbf v}) = 1$ by the identity $N(a + b\mathbf v) = a^2 - b^2\lambda$. $\square$

## The Group Law

The exponential is not a group homomorphism from the additive group of the algebra: $\exp(\tilde q)\exp(y) \neq \exp(\tilde q+y)$ whenever $[\tilde q,y] \neq 0$. The correct statement is the **Baker–Campbell–Hausdorff formula**, whose first terms are

$$
\log\bigl(e^{\tilde q} e^y\bigr) = \tilde q + y + \tfrac{1}{2}[\tilde q,y] + \tfrac{1}{12}\bigl([\tilde q,[\tilde q,y]] - [y,[y,\tilde q]]\bigr) + \cdots,
$$

a series in the free Lie algebra on $\tilde q,y$, convergent near the origin. Consequently the exponential is a local diffeomorphism from a neighbourhood of $0$ on the algebra to a neighbourhood of $1$ in the group of units, with local inverse the logarithm.

**Example.** For $\tilde q = e_1$ and $y = e_2$ one has $e^{e_1}e^{e_2} \neq e^{e_1+e_2}$, because $[e_1,e_2] = 2e_3 \neq 0$; indeed $\log(e^{e_1}e^{e_2}) - (e_1+e_2)$ begins at second order with $\tfrac12[e_1,e_2] = e_3$.

## Surjectivity of the Exponential

**Theorem.** The exponential is **not** surjective onto the group of units. A unit $\tilde a$ is an exponential if and only if it has a real logarithm, which holds exactly when each negative real root of the characteristic polynomial of $\tilde a$ occurs an even number of times; since that polynomial has degree two, a unit with a negative real root is an exponential precisely when the root is a double root.

**Proof.** This is the standard real-logarithm criterion for $2\times2$ matrices: $A = e^X$ for real $X$ iff $A$ is invertible and each elementary divisor of $A$ belonging to a negative real eigenvalue occurs an even number of times. $\square$

**Example.** The element $-1$ is an exponential: $\exp(\pi e_1) = \cos\pi + \sin\pi\,e_1 = -1$. The element $\tilde a = -\tfrac32 + \tfrac12 e_2$, whose characteristic polynomial $\lambda^2 + 3\lambda + 2$ has the simple negative root $-1$, is not an exponential. The whole image of the exponential lies in the component $\{N>0\}$ by the corollary above, so no element of norm $\le 0$ is an exponential.

## The Kernel of the Exponential

**Theorem.** The kernel of the exponential on the algebra is

$$
\ker \exp = \{\, 2\pi k\,\mathbf u \;:\; k \in \mathbb{Z},\ \mathbf u \in V,\ \mathbf u^2 = -1 \,\} \cup \{0\},
$$

that is, $0$ together with the integer multiples of $2\pi$ on the "sphere" of roots of $-1$ in $V$.

**Proof.** $e^{2\pi k\mathbf u} = \cos(2\pi k) + \sin(2\pi k)\mathbf u = 1$ for a root of $-1$ and $k\in\mathbb{Z}$, so these elements lie in the kernel. Conversely, if $e^{y} = 1$ for real $y$, then $y$ is diagonalisable over $\mathbb{C}$ with eigenvalues in $2\pi i\mathbb{Z}$; reality forces the eigenvalue multiset to be $\{2\pi i k, -2\pi i k\}$, so $y$ is traceless with $y^2 = -(2\pi k)^2$, i.e. $y = 2\pi k\,\mathbf u$ with $\mathbf u$ a root of $-1$ (or $y = 0$). $\square$

Thus the exponential is a local homeomorphism everywhere and fails to be injective only along the discrete family of $2\pi$-multiples of the roots of $-1$; this is the source of the angle doubling of the Lorentz rotor of *Split-Quaternion Rotations and the Lorentz Group*.

## Polar and Exponential Parametrisation

**Theorem (polar form).** Every nonzero split-quaternion has a **polar representation**

$$
\tilde q = \rho\, u, \qquad \rho = \sqrt{|N(\tilde q)|} > 0, \qquad u = \tilde q/\rho, \qquad N(u) = \pm 1 .
$$

The positive scalar $\rho$ carries the scale, and the unit $u$ carries the direction; the unit $u$ is in $U$ when $N(\tilde q)>0$ and in the component $\{N=-1\}$ when $N(\tilde q)<0$.

**Proof.** For $N(\tilde q)>0$, $\tilde q/\sqrt{N(\tilde q)}$ has norm $1$; for $N(\tilde q)<0$, $\tilde q/\sqrt{-N(\tilde q)}$ has norm $-1$. The polar representation is the multiplicative form of the decomposition of the group of units into its two components. $\square$

**Theorem (exponential parametrisation).** Every unit of the identity component $\{N>0\}$ that lies in the image of the exponential is $\exp(q_0 + \mathbf v)$ with $q_0 \in \mathbb{R}$ and $\mathbf v \in V$; the norm-one elements $U$ that lie in the image are $\exp(\mathbf v)$ with $\mathbf v \in V$, and the elliptic and hyperbolic cases are selected by the sign of $N(\mathbf v)$: $N(\mathbf v) > 0$ gives the compact part and $N(\mathbf v) < 0$ the non-compact part.

**Proof.** Immediate from the closed form and the corollary $N(e^{\tilde q}) = e^{2q_0}$, which shows that $q_0$ is fixed by the norm: for $U$ one needs $q_0 = 0$. The sign of $N(\mathbf v)$ decides whether the orthogonal factor is trigonometric or hyperbolic in the closed form. $\square$

## The Norm-One Group and $SL_2(\mathbb{R})$

**Theorem.** The norm-one group

$$
U = \{\, \tilde q : N(\tilde q) = 1 \,\} = \mathrm{SL}_2(\mathbb{R})
$$

is a connected three-dimensional Lie group, a double cover of the identity component $\mathrm{SO}^{+}(2,1)$ of the Lorentz group by the adjoint action of *Split-Quaternion Rotations and the Lorentz Group*; its Lie algebra is $\mathfrak{sl}_2(\mathbb{R}) = V$. The other component of the group of units is the coset $\{N = -1\} = e_2 U$ of $U$, so any negative-norm unit is a root of $-1$ times a norm-one unit.

**Proof.** The norm-one group is the kernel of the continuous norm homomorphism on the component $\{N>0\}$, and $\{N>0\}$ retracts onto $U$ by $\tilde q \mapsto \tilde q/\sqrt{N(\tilde q)}$; hence $U$ is connected. The identification with the double cover of $\mathrm{SO}^{+}(2,1)$, the Lie algebra $\mathfrak{sl}_2(\mathbb{R}) = V$, and the coset statement $\{N=-1\} = e_2 U$ (since $N(e_2 u) = N(e_2)N(u) = (-1)\cdot 1 = -1$) are as above. $\square$

## The Elliptic and Hyperbolic Subgroups

The one-parameter subgroups generated by the exponentials split by the sign of $N$ of the exponent.

**The elliptic subgroup.** For $\mathbf v = \theta u$ with $u$ a root of $-1$ ($u^2 = -1$, $N(u) = 1$), the closed form gives

$$
\exp(\theta u) = \cos\theta + \sin\theta\, u,
$$

a compact group isomorphic to $SO(2)$, the **elliptic** subgroup. The prototype is $\exp(\theta e_1) = \cos\theta + \sin\theta\, e_1$, whose adjoint action rotates $\operatorname{span}\{e_2,e_3\}$ by $2\theta$.

**The hyperbolic subgroups.** For $\mathbf v = \theta u$ with $u^2 = +1$ ($N(u) = -1$), for instance $u = e_2$ or $u = e_3$ or $u = (e_2+e_3)/\sqrt2$,

$$
\exp(\theta u) = \cosh\theta + \sinh\theta\, u,
$$

a non-compact group isomorphic to $\mathbb{R}$, the **hyperbolic** subgroup. The prototypes are $\exp(\theta e_2)$ and $\exp(\theta e_3)$, whose adjoint actions are boosts of the planes $\operatorname{span}\{e_1,e_3\}$ and $\operatorname{span}\{e_1,e_2\}$ of signature $(1,1)$.

**The parabolic directions.** For $\mathbf v$ null ($\mathbf v^2 = 0$, $\mathbf v \neq 0$), the closed form gives $\exp(\mathbf v) = 1 + \mathbf v$, a unipotent element; the exponentials of the null directions form the one-parameter unipotent subgroups conjugate to the translations of the affine line.

These are the elliptic, hyperbolic and parabolic one-parameter subgroups of the Lorentz group of *Split-Quaternion Rotations and the Lorentz Group*.

## The Lie Algebra and the Lorentz Group

The Lie algebra of the group of units is $\mathbb{H}_{\mathrm{s}} \cong \mathfrak{gl}_2(\mathbb{R})$; the Lie algebra of $U = SL_2(\mathbb{R})$ is the traceless part $V \cong \mathfrak{sl}_2(\mathbb{R})$; and the adjoint action on $V$ identifies these with the Lorentz Lie algebra:

$$
\operatorname{Lie}(U) = V \cong \mathfrak{sl}_2(\mathbb{R}) \cong \mathfrak{so}(2,1),
$$

with the bracket of the proposition above. The exponential $\exp : V \to U$ is the exponential of the Lorentz Lie algebra composed with the double cover $SL_2(\mathbb{R}) \to SO^+(2,1)$; the elliptic, hyperbolic and parabolic one-parameter subgroups are the rotors, the boosts and the null transvections of the Lorentz group.

## Comparison with the Biquaternion Case

The biquaternion article *Biquaternion Lie Algebra and Lie Group Structure* computes the same objects for $\mathbb{B} = M_2(\mathbb{C})$: the group of units $GL(2,\mathbb{C})$, the retraction onto $U(2)$, the norm-one group $SL(2,\mathbb{C})$ retracting onto $SU(2)$, the closed form of the exponential, its kernel, and the elliptic and hyperbolic subgroups of the Lorentz group $SO(3,1)$. The split-quaternion case is the real, indefinite analogue. The group of units is $GL_2(\mathbb{R})$ rather than $GL(2,\mathbb{C})$, with **two** components instead of one; the norm-one group is $SL_2(\mathbb{R})$, which retracts onto the circle $SO(2)$ and has infinite cyclic fundamental group, in place of the simply connected sphere $SU(2)$; and the Lorentz group is the three-dimensional $\mathrm{SO}^{+}(2,1)$ in place of the six-dimensional $\mathrm{SO}^{+}(3,1)$. The closed form is the same series, with the sign of $N(\mathbf v)$ deciding between the trigonometric and the hyperbolic branch, the split signature producing both branches where the definite case produces only the elliptic one. Nothing biquaternion-specific — the central imaginary unit $i$, the unitary retraction, the complex parametrisation — is imported.

## Summary

The commutator makes $\mathbb{H}_{\mathrm{s}}$ a Lie algebra with centre $S$ and associated Lie algebra $V \cong \mathfrak{sl}_2(\mathbb{R}) \cong \mathfrak{so}(2,1)$. The group of units is $\mathbb{H}_{\mathrm{s}}^\times = \{N \neq 0\} \cong GL_2(\mathbb{R})$, with two components $\{N>0\}$ and $\{N<0\}$; the norm-one group is $U = \{N=1\} \cong SL_2(\mathbb{R})$, a connected three-dimensional group that double-covers $\mathrm{SO}^{+}(2,1)$, with the other component the coset $e_2 U$.

The exponential has the closed form displayed above, with the sign of $N(\mathbf v)$ selecting the trigonometric branch ($N(\mathbf v)>0$), the hyperbolic branch ($N(\mathbf v)<0$) or the terminating branch ($N(\mathbf v)=0$); it satisfies $N(e^{\tilde q}) = e^{2q_0}$, so it lands in the identity component, it is a local diffeomorphism, and it obeys the Baker–Campbell–Hausdorff law rather than additivity. It is not surjective, its image being the invertible matrices with no negative real eigenvalue of odd multiplicity, and its kernel is $0$ together with the $2\pi$-multiples of the roots of $-1$. Every nonzero element has the polar form $\rho u$, and the norm-one elements in the image of the exponential are $\exp(\mathbf v)$ with $\mathbf v \in V$. The one-parameter subgroups are elliptic (compact, from roots of $-1$), hyperbolic (non-compact, from roots of $+1$ in $V$) and parabolic (unipotent, from the null directions). The comparison with $\mathbb{B}$ is the comparison of a real indefinite form with a complex definite one.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathbb{H}_{\mathrm{s}}$ | the split-quaternion algebra, $\cong M_2(\mathbb{R})$ | *Split-Quaternion Algebra* |
| $[\tilde q,y] = \tilde q y - y\tilde q$ | the commutator making the algebra a Lie algebra | this article |
| $V \cong \mathfrak{sl}_2(\mathbb{R}) \cong \mathfrak{so}(2,1)$ | the traceless elements under the bracket | *Split-Quaternion Scalar and Vector Subspaces* |
| $\mathbb{H}_{\mathrm{s}}^\times = \{N \neq 0\}$ | the group of units, $\cong GL_2(\mathbb{R})$, two components | this article |
| $U = \{N=1\} = \mathrm{SL}_2(\mathbb{R})$ | the norm-one group | *Split-Quaternion Norm and Invertibility* |
| $e_2 U = \{N=-1\}$ | the other component of the group of units | this article |
| $\exp(\tilde q) = \sum \tilde q^k/k!$ | the exponential, with the closed form above | this article |
| $\tilde q = q_0 + \mathbf v$, $\mu = N(\mathbf v)$ | the scalar–vector split and the sign parameter | this article |
| $\ker\exp$ | $\{2\pi k\mathbf u : k\in\mathbb{Z}, \mathbf u^2=-1\} \cup \{0\}$ | this article |
| $N(e^{\tilde q}) = e^{2q_0}$ | the norm of the exponential | this article |
| $\exp(\theta u) = \cos\theta + \sin\theta\,u$ | the elliptic subgroup ($u^2 = -1$) | this article |
| $\exp(\theta u) = \cosh\theta + \sinh\theta\,u$ | the hyperbolic subgroup ($u^2 = +1$ in $V$) | this article |
| $\rho u$ | the polar form of a nonzero element | *Split-Quaternion Polar Representation* |
| $\mathrm{SO}^{+}(2,1)$ | the identity component of the Lorentz group | *Split-Quaternion Rotations and the Lorentz Group* |

## Further Reading

- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed., Graduate Texts in Mathematics 222 (Springer, 2015), for the exponential map, the Baker–Campbell–Hausdorff formula and the matrix logarithm.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for the exponential of the classical matrix groups and the failure of surjectivity.
- Wulf Rossmann, *Lie Groups: An Introduction Through Linear Groups* (Oxford University Press, 2002), for the structure of $SL_2(\mathbb{R})$ and its one-parameter subgroups.
- Robert Gilmore, *Lie Groups, Lie Algebras, and Some of Their Applications* (Wiley, 1974), for $\mathfrak{sl}_2(\mathbb{R}) \cong \mathfrak{so}(2,1)$ and the elliptic, hyperbolic and parabolic subgroups.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the exponential of the low-dimensional Clifford algebras and the rotor parametrisations.
