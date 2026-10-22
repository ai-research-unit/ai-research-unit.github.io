
# __Split-Quaternion Exponential and Lie Group Structure__

## Introduction

The split-quaternion algebra $\mathbb{H}_{\mathrm{s}} \cong M_2(\mathbb{R})$ carries two group structures and one Lie algebra structure that interlock: the **group of units** $\mathbb{H}_{\mathrm{s}}^\times = GL_2(\mathbb{R})$, the **norm-one group** $U = \{N = 1\} \cong SL_2(\mathbb{R})$, and the Lie algebra $\mathrm{SL}_2(\mathbb{R})$ of traceless elements under the commutator. The link is the exponential map, which we compute in closed form and study for its group law, its kernel and its range. Because the split-quaternion norm is indefinite, the exponential splits into an elliptic part from the directions of square $-1$ and a hyperbolic part from the directions of square $+1$.

This article owns the exponential and the Lie group structure: the algebra as a Lie algebra, the closed form of the exponential, the group of units, the norm-one group and its identification with $SL_2(\mathbb{R})$, the elliptic and hyperbolic subgroups, and the polar and exponential parametrisation. It relies on *Split-Quaternion Rotations and the Lorentz Group* for the Lorentz action, on *Split-Quaternion Automorphisms and Derivations* for the derivations. No physics is invoked.

**Conventions.** A general element is $\tilde q = q_t + \vec v$ with $q_t = \operatorname{Sc}(\tilde q) \in \mathbb{R}$ and $\vec v = q_x\vec e_x + q_y\vec e_y + q_z\vec e_z \in V$. The split-quaternion norm is $\langle\tilde q\rangle_{\natural} = q_t^2 + \langle \vec v\rangle_{\natural}$ with $\langle \vec v\rangle_{\natural} = q_x^2 - q_y^2 - q_z^2$, and on a vector $\vec v^2 = -\langle \vec v\rangle_{\natural}$. Under the commutator $V$ is the Lie algebra $\mathrm{SL}_2(\mathbb{R})$.

## The Algebra as a Lie Algebra

**Definition.** The **commutator** $[\tilde q_1,\tilde q_2] = \tilde q_1 \tilde q_2 - \tilde q_2\tilde q_1$ makes $\mathbb{H}_{\mathrm{s}}$ into a real Lie algebra. Its centre is again the scalar line $S = \mathbb{R}\cdot1$, and the associated Lie algebra modulo the centre is

$$
\mathbb{H}_{\mathrm{s}}/S \;\cong\; V \;\cong\; \mathrm{SL}_2(\mathbb{R}),
$$

of dimension $3$.

**Proposition.** The commutator restricts to a Lie bracket on $V$, where it satisfies

$$
[\vec e_x,\vec e_y] = 2\vec e_z, \qquad [\vec e_y,\vec e_z] = -2\vec e_x, \qquad [\vec e_z,\vec e_x] = 2\vec e_y,
$$

so $V \cong \mathrm{SL}_2(\mathbb{R}) \cong \mathrm{SO}(2,1)$. The bracket vanishes on $S$ and on the split-complex planes: $[S, \mathbb{H}_{\mathrm{s}}] = 0$ and $[\mathbb{D}_k, \mathbb{D}_k] = 0$. The form $\langle\tilde q_1,\tilde q_2\rangle = \tfrac{1}{2}(\langle\tilde q_1+\tilde q_2\rangle_{\natural} - \langle\tilde q_1\rangle_{\natural} - \langle\tilde q_2\rangle_{\natural})$, restricted to $V$, is invariant under the adjoint action, and the **Killing form** of the Lie algebra $\mathrm{SL}_2(\mathbb{R})$ is a nonzero multiple of it; on $V$ it is the form of signature $(2,1)$.

**Proof.** The brackets are the multiplication table of the algebra. If $\tilde q_1, \tilde q_2 \in V$ then $\tilde q_1 \tilde q_2 + \tilde q_2\tilde q_1$ is scalar and equal to $-2\langle\tilde q_1,\tilde q_2\rangle$, so $[\tilde q_1,\tilde q_2] = \tilde q_1 \tilde q_2 - \tilde q_2\tilde q_1$ has zero trace and lies in $V$; the vanishing statements on $S$ and on each $\mathbb{D}_k$ are the commutativity of the scalar line and of the plane. Since $V$ is the adjoint module of $\mathrm{SL}_2(\mathbb{R})$ and is irreducible, the space of invariant symmetric bilinear forms on it is one-dimensional, so $\langle\cdot,\cdot\rangle|_V$ and the Killing form differ by a nonzero scalar. Invariance of $\langle\cdot,\cdot\rangle$ follows from the multiplicativity of $\langle\cdot\rangle_{\natural}$ along the one-parameter automorphism groups $\operatorname{Ad}_{\exp(tw)} = \exp(t\,\mathrm{ad}_w)$: differentiating $\langle\exp(t\,\mathrm{ad}_w)\tilde q_1, \exp(t\,\mathrm{ad}_w)\tilde q_2\rangle = \langle\tilde q_1,\tilde q_2\rangle$ at $t=0$ gives $\langle\mathrm{ad}_w \tilde q_1,\tilde q_2\rangle + \langle\tilde q_1,\mathrm{ad}_w \tilde q_2\rangle = 0$.

## The Group of Units

**Theorem.** The units of $\mathbb{H}_{\mathrm{s}}$ are the elements of nonzero norm,

$$
\mathbb{H}_{\mathrm{s}}^\times = \{\, \tilde q : \langle\tilde q\rangle_{\natural} \neq 0 \,\} \cong GL_2(\mathbb{R}),
$$

with inverse $\tilde q^{-1} = \tilde{q}^{\natural}/\langle\tilde q\rangle_{\natural}$. The group has exactly **two connected components**, $\{N > 0\}$ and $\{N < 0\}$, the sign of the split-quaternion norm separating them.

**Proof.** $\tilde q\tilde{q}^{\natural} = \langle\tilde q\rangle_{\natural}$ shows that $\langle\tilde q\rangle_{\natural}\neq0$ implies invertibility, and $\langle\tilde q_1 \tilde q_2\rangle_{\natural} = \langle\tilde q_1\rangle_{\natural}\langle\tilde q_2\rangle_{\natural}$ shows that the non-units are exactly the nonzero null elements. The continuous surjection $N : \mathbb{H}_{\mathrm{s}}^\times \to \mathbb{R}^\times$ maps onto the two components of $\mathbb{R}^\times$, and the level set $\{N>0\}$ is connected (it retracts onto $U$), as is $\{N<0\}$; so the group has two components.

The identity component $\{N>0\} \cong GL_2^+(\mathbb{R})$ is the part of the group acting by the orientation-preserving half of the Lorentz action; the component $\{N<0\}$ acts by Lorentz transformations reversing time orientation, as in *Split-Quaternion Rotations and the Lorentz Group*.

## The Exponential: Series and Closed Form

**Definition.** The **exponential** of $\tilde q \in \mathbb{H}_{\mathrm{s}}$ is

$$
\exp(\tilde q) = \sum_{k \geq 0} \frac{\tilde q^k}{k!},
$$

convergent for every $\tilde q$, because the algebra is finite-dimensional and a submultiplicative norm exists on it.

**Theorem (closed form).** Write $\tilde q = q_t + \vec v$ and put $\mu = \langle \vec v\rangle_{\natural} = q_x^2 - q_y^2 - q_z^2$. Then

$$
\exp(\tilde q) = \exp(q_t) \Bigl( \cosh\sqrt{-\mu} + \frac{\sinh\sqrt{-\mu}}{\sqrt{-\mu}}\,\vec v \Bigr), \qquad \mu < 0,
$$

$$
\exp(\tilde q) = \exp(q_t) \bigl( 1 + \vec v \bigr), \qquad \mu = 0,
$$

$$
\exp(\tilde q) = \exp(q_t) \Bigl( \cos\sqrt{\mu} + \frac{\sin\sqrt{\mu}}{\sqrt{\mu}}\,\vec v \Bigr), \qquad \mu > 0 .
$$

**Proof.** The scalar $q_t$ commutes with $\vec v$, so $\exp(\tilde q) = \exp(q_t) \exp(\vec v)$, and $\vec v^2 = -\langle \vec v\rangle_{\natural} = -\mu$ is scalar. Hence $\vec v^{2k} = (-1)^k \mu^k$ and $\vec v^{2k+1} = (-1)^k \mu^k \vec v$, and the series splits into the even and odd parts $\sum_k \frac{(-1)^k\mu^k}{(2k)!}$ and $\vec v \sum_k \frac{(-1)^k\mu^k}{(2k+1)!}$. These are the power series of $\cos$ and $\sin$ when $\mu > 0$, of $\cosh$ and $\sinh$ when $\mu < 0$ (after factoring $\sqrt{|\mu|}$), and terminate as $1$ and $\vec v$ when $\mu = 0$.

**Corollary.** The split-quaternion norm of the exponential is $\langle\exp(\tilde q)\rangle_{\natural} = \exp(2q_t)$, so the exponential lands in the component $\{N > 0\}$ of the group of units, and $\exp(S) = \mathbb{R}_{>0}$.

**Proof.** The multiplicativity $\langle ab\rangle_{\natural} = \langle a\rangle_{\natural}\langle b\rangle_{\natural}$ together with $\langle \exp(q_t)\rangle_{\natural} = \exp(2q_t)$ for a scalar reduce the claim to $\langle \exp(\vec v)\rangle_{\natural} = 1$ for $\vec v \in V$. The element $\vec v$ generates the commutative two-dimensional subalgebra $\operatorname{span}\{1, \vec v\}$ with $\vec v^2 = -\langle \vec v\rangle_{\natural}$; writing $\lambda = -\langle \vec v\rangle_{\natural}$, the exponential in this subalgebra is $\exp(\vec v) = \cosh\sqrt\lambda + \frac{\sinh\sqrt\lambda}{\sqrt\lambda}\,\vec v$ for $\lambda > 0$, $\exp(\vec v) = \cos\sqrt{-\lambda} + \frac{\sin\sqrt{-\lambda}}{\sqrt{-\lambda}}\,\vec v$ for $\lambda < 0$, and $\exp(\vec v) = 1 + \vec v$ for $\lambda = 0$; in each case $\langle \exp(\vec v)\rangle_{\natural} = 1$ by the identity $\langle a + b\vec v\rangle_{\natural} = a^2 - b^2\lambda$.

## The Group Law

The exponential is not a group homomorphism from the additive group of the algebra: $\exp(\tilde q_1)\exp(\tilde q_2) \neq \exp(\tilde q_1+\tilde q_2)$ whenever $[\tilde q_1,\tilde q_2] \neq 0$. The correct statement is the **Baker–Campbell–Hausdorff formula**, whose first terms are

$$
\log\bigl(\exp(\tilde q_1) \exp(\tilde q_2)\bigr) = \tilde q_1 + \tilde q_2 + \tfrac{1}{2}[\tilde q_1,\tilde q_2] + \tfrac{1}{12}\bigl([\tilde q_1,[\tilde q_1,\tilde q_2]] - [\tilde q_2,[\tilde q_2,\tilde q_1]]\bigr) + \cdots,
$$

a series in the free Lie algebra on $\tilde q_1,\tilde q_2$, convergent near the origin. Consequently the exponential is a local diffeomorphism from a neighbourhood of $0$ on the algebra to a neighbourhood of $1$ in the group of units, with local inverse the logarithm.

**Example.** For $\tilde q_1 = \vec e_x$ and $\tilde q_2 = \vec e_y$ one has $\exp(\vec e_x)\exp(\vec e_y) \neq \exp(\vec e_x+\vec e_y)$, because $[\vec e_x,\vec e_y] = 2\vec e_z \neq 0$; indeed $\log(\exp(\vec e_x)\exp(\vec e_y)) - (\vec e_x+\vec e_y)$ begins at second order with $\tfrac12[\vec e_x,\vec e_y] = \vec e_z$.

## Surjectivity of the Exponential

**Theorem.** The exponential is **not** surjective onto the group of units. A unit $\tilde u$ is an exponential if and only if it has a real logarithm, which holds exactly when each negative real root of the characteristic polynomial of $\tilde u$ occurs an even number of times; since that polynomial has degree two, a unit with a negative real root is an exponential precisely when the root is a double root.

**Proof.** This is the standard real-logarithm criterion for $2\times2$ matrices: $A = \exp(X)$ for real $X$ iff $A$ is invertible and each elementary divisor of $A$ belonging to a negative real eigenvalue occurs an even number of times.

**Example.** The element $-1$ is an exponential: $\exp(\pi \vec e_x) = \cos\pi + \sin\pi\,\vec e_x = -1$. The element $\tilde u = -\tfrac32 + \tfrac12 \vec e_y$, whose characteristic polynomial $\lambda^2 + 3\lambda + 2$ has the simple negative root $-1$, is not an exponential. The whole image of the exponential lies in the component $\{N>0\}$ by the corollary above, so no element of norm $\le 0$ is an exponential.

## The Kernel of the Exponential

**Theorem.** The kernel of the exponential on the algebra is

$$
\ker \exp = \{\, 2\pi k\,\vec\xi \;:\; k \in \mathbb{Z},\ \vec\xi \in V,\ \vec\xi^2 = -1 \,\} \cup \{0\},
$$

that is, $0$ together with the integer multiples of $2\pi$ on the "sphere" of roots of $-1$ in $V$.

**Proof.** $\exp(2\pi k\vec\xi) = \cos(2\pi k) + \sin(2\pi k)\vec\xi = 1$ for a root of $-1$ and $k\in\mathbb{Z}$, so these elements lie in the kernel. Conversely, if $\exp(\tilde q) = 1$ for real $\tilde q$, then $\tilde q$ is diagonalisable over $\mathbb{C}$ with eigenvalues in $2\pi i\mathbb{Z}$; reality forces the eigenvalue multiset to be $\{2\pi i k, -2\pi i k\}$, so $\tilde q$ is traceless with $\tilde q^2 = -(2\pi k)^2$, i.e. $\tilde q = 2\pi k\,\vec\xi$ with $\vec\xi$ a root of $-1$ (or $\tilde q = 0$).

Thus the exponential is a local homeomorphism everywhere and fails to be injective only along the discrete family of $2\pi$-multiples of the roots of $-1$; this is the source of the angle doubling of the Lorentz rotor of *Split-Quaternion Rotations and the Lorentz Group*.

## Polar and Exponential Parametrisation

**Theorem (polar form).** Every nonzero split-quaternion has a **polar decomposition**

$$
\tilde q = \rho\, \tilde u, \qquad \rho = \sqrt{|\langle\tilde q\rangle_{\natural}|} > 0, \qquad \tilde u = \tilde q/\rho, \qquad \langle \tilde u\rangle_{\natural} = \pm 1 .
$$

The positive scalar $\rho$ carries the scale, and the unit $\tilde u$ carries the direction; the unit $\tilde u$ is in $\mathrm{U}$ when $\langle\tilde q\rangle_{\natural}>0$ and in the component $\{N=-1\}$ when $\langle\tilde q\rangle_{\natural}<0$.

**Proof.** For $\langle\tilde q\rangle_{\natural}>0$, $\tilde q/\sqrt{\langle\tilde q\rangle_{\natural}}$ has norm $1$; for $\langle\tilde q\rangle_{\natural}<0$, $\tilde q/\sqrt{-\langle\tilde q\rangle_{\natural}}$ has norm $-1$. The polar decomposition is the multiplicative form of the decomposition of the group of units into its two components.

**Theorem (exponential parametrisation).** Every unit of the identity component $\{N>0\}$ that lies in the image of the exponential is $\exp(q_t + \vec v)$ with $q_t \in \mathbb{R}$ and $\vec v \in V$; the norm-one elements $\mathrm{U}$ that lie in the image are $\exp(\vec v)$ with $\vec v \in V$, and the elliptic and hyperbolic cases are selected by the sign of $\langle \vec v\rangle_{\natural}$: $\langle \vec v\rangle_{\natural} > 0$ gives the compact part and $\langle \vec v\rangle_{\natural} < 0$ the non-compact part.

**Proof.** Immediate from the closed form and the corollary $\langle\exp(\tilde q)\rangle_{\natural} = \exp(2q_t)$, which shows that $q_t$ is fixed by the split-quaternion norm: for $\mathrm{U}$ one needs $q_t = 0$. The sign of $\langle \vec v\rangle_{\natural}$ decides whether the orthogonal factor is trigonometric or hyperbolic in the closed form.

## The Norm-One Group and $SL_2(\mathbb{R})$

**Theorem.** The norm-one group

$$
U = \{\, \tilde q : \langle\tilde q\rangle_{\natural} = 1 \,\} = \mathrm{SL}_2(\mathbb{R})
$$

is a connected three-dimensional Lie group, a double cover of the identity component $\mathrm{SO}^{+}(2,1)$ of the Lorentz group by the adjoint action of *Split-Quaternion Rotations and the Lorentz Group*; its Lie algebra is $\mathrm{SL}_2(\mathbb{R}) = V$. The other component of the group of units is the coset $\{N = -1\} = \vec e_y U$ of $U$, so any negative-norm unit is a root of $-1$ times a norm-one unit.

**Proof.** The norm-one group is the kernel of the continuous norm homomorphism on the component $\{N>0\}$, and $\{N>0\}$ retracts onto $U$ by $\tilde q \mapsto \tilde q/\sqrt{\langle\tilde q\rangle_{\natural}}$; hence $U$ is connected. The identification with the double cover of $\mathrm{SO}^{+}(2,1)$, the Lie algebra $\mathrm{SL}_2(\mathbb{R}) = V$, and the coset statement $\{N=-1\} = \vec e_y U$ (since $\langle \vec e_y \tilde u\rangle_{\natural} = \langle \vec e_y\rangle_{\natural}\langle \tilde u\rangle_{\natural} = (-1)\cdot 1 = -1$) are as above.

## The Elliptic and Hyperbolic Subgroups

The one-parameter subgroups generated by the exponentials split by the sign of $\langle\cdot\rangle_{\natural}$ of the exponent.

**The elliptic subgroup.** For $\vec v = \theta \tilde u$ with $\tilde u$ a root of $-1$ ($\tilde u^2 = -1$, $\langle \tilde u\rangle_{\natural} = 1$), the closed form gives

$$
\exp(\theta \tilde u) = \cos\theta + \sin\theta\, \tilde u,
$$

a compact group isomorphic to $SO(2)$, the **elliptic** subgroup. The prototype is $\exp(\theta \vec e_x) = \cos\theta + \sin\theta\, \vec e_x$, whose adjoint action rotates $\operatorname{span}\{\vec e_y,\vec e_z\}$ by $2\theta$.

**The hyperbolic subgroups.** For $\vec v = \theta \tilde u$ with $\tilde u^2 = +1$ ($\langle \tilde u\rangle_{\natural} = -1$), for instance $\tilde u = \vec e_y$ or $\tilde u = \vec e_z$ or $\tilde u = (\vec e_y+\vec e_z)/\sqrt2$,

$$
\exp(\theta \tilde u) = \cosh\theta + \sinh\theta\, \tilde u,
$$

a non-compact group isomorphic to $\mathbb{R}$, the **hyperbolic** subgroup. The prototypes are $\exp(\theta \vec e_y)$ and $\exp(\theta \vec e_z)$, whose adjoint actions are boosts of the planes $\operatorname{span}\{\vec e_x,\vec e_z\}$ and $\operatorname{span}\{\vec e_x,\vec e_y\}$ of signature $(1,1)$.

**Terminology (hyperbolic versors).** The two families are Hamilton's versors and their indefinite counterparts: $\cos\theta + \xi\sin\theta$, built on a root of $-1$, is a **versor**, and $\cosh t + \eta\sinh t$, the same expression built on a unit of square $+1$, is a **hyperbolic versor**. Hyperbolic versors arise in any algebra of mixed signature; the earliest instance is in the tessarines of James Cockle (1848), the commutative algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$ that the corpus records as the tessarine or reduced biquaternion algebra in *List of Algebras by Dimension*; Homersham Cox used the element with quaternion multiplication (1882), and Alexander Macfarlane built the hyperbolic quaternions on it (1891), an algebra whose difficulties turned the subject toward the biquaternions. The parameter $t$ is the rapidity of the Lorentz boost that the one-parameter group represents, so the hyperbolic versor is the exponential form of a boost; Lie's one-parameter group is the notion that subsumes the versor and the hyperbolic versor alike.

**The parabolic directions.** For $\vec v$ null ($\vec v^2 = 0$, $\vec v \neq 0$), the closed form gives $\exp(\vec v) = 1 + \vec v$, a unipotent element; the exponentials of the null directions form the one-parameter unipotent subgroups conjugate to the translations of the affine line.

These are the elliptic, hyperbolic and parabolic one-parameter subgroups of the Lorentz group of *Split-Quaternion Rotations and the Lorentz Group*.

## The Lie Algebra and the Lorentz Group

The Lie algebra of the group of units is $\mathbb{H}_{\mathrm{s}} \cong \mathrm{GL}_2(\mathbb{R})$; the Lie algebra of $U = SL_2(\mathbb{R})$ is the traceless part $V \cong \mathrm{SL}_2(\mathbb{R})$; and the adjoint action on $V$ identifies these with the Lorentz Lie algebra:

$$
\operatorname{Lie}(U) = V \cong \mathrm{SL}_2(\mathbb{R}) \cong \mathrm{SO}(2,1),
$$

with the bracket of the proposition above. The exponential $\exp : V \to U$ is the exponential of the Lorentz Lie algebra composed with the double cover $SL_2(\mathbb{R}) \to SO^+(2,1)$; the elliptic, hyperbolic and parabolic one-parameter subgroups are the rotors, the boosts and the null transvections of the Lorentz group.

## Comparison with the Biquaternion Case

The biquaternion article *Biquaternion Lie Group and Exponential Structure* computes the same objects for $\mathbb{B} = M_2(\mathbb{C})$: the group of units $GL(2,\mathbb{C})$, the retraction onto $\mathrm{U}(2)$, the norm-one group $SL(2,\mathbb{C})$ retracting onto $SU(2)$, the closed form of the exponential, its kernel, and the elliptic and hyperbolic subgroups of the Lorentz group $SO(3,1)$. The split-quaternion case is the real, indefinite analogue. The group of units is $GL_2(\mathbb{R})$ rather than $GL(2,\mathbb{C})$, with **two** components instead of one; the norm-one group is $SL_2(\mathbb{R})$, which retracts onto the circle $SO(2)$ and has infinite cyclic fundamental group, in place of the simply connected sphere $SU(2)$; and the Lorentz group is the three-dimensional $\mathrm{SO}^{+}(2,1)$ in place of the six-dimensional $\mathrm{SO}^{+}(3,1)$. The closed form is the same series, with the sign of $\langle \vec v\rangle_{\natural}$ deciding between the trigonometric and the hyperbolic branch, the split signature producing both branches where the definite case produces only the elliptic one. Nothing biquaternion-specific — the central imaginary unit $i$, the unitary retraction, the complex parametrisation — is imported.

## Summary

The commutator makes $\mathbb{H}_{\mathrm{s}}$ a Lie algebra with centre $S$ and associated Lie algebra $V \cong \mathrm{SL}_2(\mathbb{R}) \cong \mathrm{SO}(2,1)$. The group of units is $\mathbb{H}_{\mathrm{s}}^\times = \{N \neq 0\} \cong GL_2(\mathbb{R})$, with two components $\{N>0\}$ and $\{N<0\}$; the norm-one group is $U = \{N=1\} \cong SL_2(\mathbb{R})$, a connected three-dimensional group that double-covers $\mathrm{SO}^{+}(2,1)$, with the other component the coset $\vec e_y U$.

The exponential has the closed form displayed above, with the sign of $\langle \vec v\rangle_{\natural}$ selecting the trigonometric branch ($\langle \vec v\rangle_{\natural}>0$), the hyperbolic branch ($\langle \vec v\rangle_{\natural}<0$) or the terminating branch ($\langle \vec v\rangle_{\natural}=0$); it satisfies $\langle\exp(\tilde q)\rangle_{\natural} = \exp(2q_t)$, so it lands in the identity component, it is a local diffeomorphism, and it obeys the Baker–Campbell–Hausdorff law rather than additivity. It is not surjective, its image being the invertible matrices with no negative real eigenvalue of odd multiplicity, and its kernel is $0$ together with the $2\pi$-multiples of the roots of $-1$. Every nonzero element has the polar form $\rho\tilde u$, and the norm-one elements in the image of the exponential are $\exp(\vec v)$ with $\vec v \in V$. The one-parameter subgroups are elliptic (compact, from roots of $-1$), hyperbolic (non-compact, from roots of $+1$ in $V$) and parabolic (unipotent, from the null directions). The comparison with $\mathbb{B}$ is the comparison of a real indefinite form with a complex definite one.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathbb{H}_{\mathrm{s}}$ | the split-quaternion algebra, $\cong M_2(\mathbb{R})$ | *Split-Quaternion Algebra* |
| $[\tilde q_1,\tilde q_2] = \tilde q_1 \tilde q_2 - \tilde q_2\tilde q_1$ | the commutator making the algebra a Lie algebra | this article |
| $V \cong \mathrm{SL}_2(\mathbb{R}) \cong \mathrm{SO}(2,1)$ | the traceless elements under the bracket | *Split-Quaternion Scalar and Vector Subspaces* |
| $\mathbb{H}_{\mathrm{s}}^\times = \{N \neq 0\}$ | the group of units, $\cong GL_2(\mathbb{R})$, two components | this article |
| $U = \{N=1\} = \mathrm{SL}_2(\mathbb{R})$ | the norm-one group | *Split-Quaternion Norm and Invertibility* |
| $\vec e_y U = \{N=-1\}$ | the other component of the group of units | this article |
| $\exp(\tilde q) = \sum \tilde q^k/k!$ | the exponential, with the closed form above | this article |
| $\tilde q = q_t + \vec v$, $\mu = \langle \vec v\rangle_{\natural}$ | the scalar–vector split and the sign parameter | this article |
| $\ker\exp$ | $\{2\pi k\vec\xi : k\in\mathbb{Z}, \vec\xi^2=-1\} \cup \{0\}$ | this article |
| $\langle\exp(\tilde q)\rangle_{\natural} = \exp(2q_t)$ | the split-quaternion norm of the exponential | this article |
| $\exp(\theta \tilde u) = \cos\theta + \sin\theta\,\tilde u$ | the elliptic subgroup ($\tilde u^2 = -1$) | this article |
| $\exp(\theta \tilde u) = \cosh\theta + \sinh\theta\,\tilde u$ | the hyperbolic subgroup ($\tilde u^2 = +1$ in $V$) | this article |
| $\rho\tilde u$ | the polar form of a nonzero element | *Split-Quaternion Polar Decomposition* |
| $\mathrm{SO}^{+}(2,1)$ | the identity component of the Lorentz group | *Split-Quaternion Rotations and the Lorentz Group* |

## Further Reading

- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed., Graduate Texts in Mathematics 222 (Springer, 2015), for the exponential map, the Baker–Campbell–Hausdorff formula and the matrix logarithm.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for the exponential of the classical matrix groups and the failure of surjectivity.
- Wulf Rossmann, *Lie Groups: An Introduction Through Linear Groups* (Oxford University Press, 2002), for the structure of $SL_2(\mathbb{R})$ and its one-parameter subgroups.
- Robert Gilmore, *Lie Groups, Lie Algebras, and Some of Their Applications* (Wiley, 1974), for $\mathrm{SL}_2(\mathbb{R}) \cong \mathrm{SO}(2,1)$ and the elliptic, hyperbolic and parabolic subgroups.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the exponential of the low-dimensional Clifford algebras and the rotor parametrisations.
