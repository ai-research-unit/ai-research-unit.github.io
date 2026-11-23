# __The Quaternion Versors and the Unitary Group__

## Introduction

The versors are the quaternions of norm one. They form the unit sphere $S^3$, a compact Lie group of dimension three, and the group is at once Hamilton's group of the versors, the symplectic group $\mathrm{Sp}(1)$ and the special unitary group $SU(2)$. It is the compact group of the algebra: the group of invertibles is a positive scale times it, and its two-sided action on the algebra gives the double covers of $SO(3)$ and of $SO(4)$.

The article proves the group structure and the identification with $SU(2)$, computes the Lie algebra and the exponential, states the two double covers with their kernels, and then reads the unitary group of the algebra from the two forms: the definite form has the versors for its $\mathbb{H}$-linear isometry group, and the indefinite form has none beyond the two signs, so the indefinite unitary group is large as a real group and trivial as a group of the algebra. The article ends with the matrix model, where the versors are the intersection of the algebra with $\mathrm{U}(2)$, and with the maximal torus and the Weyl group.

The group of invertibles and the topology of the sphere are [The Quaternion Group of Invertibles as a Topological Group](the-quaternion-group-of-invertibles-as-a-topological-group.html) and [Quaternion Topology](quaternion-topology.html); the rotation action is [Quaternion Rotations and Reflections](quaternion-rotations-and-reflections.html), cited and not restated.

## The Versors and the Unit Sphere

**Definition.** A **versor** is a quaternion of norm one, $\tilde u\tilde u^{\natural}=e_t$; the set of the versors is the unit sphere $S^3=\{N=1\}$.

**Theorem (the versors form a group).** $S^3$ is closed under the product and the inverse, and it is a subgroup of $\mathbb{H}^{\times}$; it is the kernel of the homomorphism $N\colon\mathbb{H}^{\times}\to\mathbb{R}_{>0}$.

*Proof.* $N(\tilde u\tilde v)=N(\tilde u)N(\tilde v)=1$ and $N(\tilde u^{-1})=1$; the inverse of a versor is its conjugate, which is a versor. The multiplicativity of $N$ is the statement that the map is a homomorphism, and the kernel is the sphere. Verified on products of random versors.

**Corollary (the group of invertibles).** $\mathbb{H}^{\times}=\mathbb{R}_{>0}\times S^3$, the scale and the versor being unique, and $S^3$ is a deformation retract of the group of invertibles.

*Proof.* Every non-zero $\tilde q$ is $r\tilde u$ with $r=\lvert\tilde q\rvert>0$ and $\tilde u=\tilde q/r$; the retraction is the normalisation, and the homotopy is the linear interpolation of the scale. Verified by computing the two factors.

**Remark (the sphere is the whole compact part).** The versors are the only elements of norm one, and they are all of them: the sphere is the level set of the norm and the compact subgroup of the group of invertibles. **The algebra has exactly one compact group of positive dimension, and it is the group of its versors.**

## The Lie Group Structure

**Theorem (the Lie algebra).** $S^3$ is a Lie group of dimension three, and its Lie algebra is the vector subspace $\operatorname{Vect}(\mathbb{H})$ with the bracket
$$
[\vec u,\vec v]=\vec u\vec v-\vec v\vec u=2\,\vec u\times\vec v ,
$$
isomorphic to $\mathfrak{so}(3)$.

*Proof.* The sphere is a smooth submanifold of $\mathbb{H}$ as the preimage of the regular value $1$ of $N$; the group operations are the restrictions of the bilinear product and of the linear conjugation, hence smooth. The tangent space at $e_t$ is the kernel of the differential of $N$, that is the hyperplane $e_t^{\perp}=\operatorname{Vect}(\mathbb{H})$. The bracket of two left-invariant fields at the identity is the commutator, and for pure quaternions $\vec u\vec v-\vec v\vec u=2\vec u\times\vec v$. The identification with $\mathfrak{so}(3)$ is the cross product algebra of [The Lie Structure of the Antisymmetric Plain Product of the Quaternions](the-lie-structure-of-the-antisymmetric-plain-product-of-the-quaternions.html). Verified on the basis.

**Theorem (the exponential).** The exponential of the group is the quaternion exponential restricted to the vector subspace,
$$
\exp(\vec v)=\cos\lvert\vec v\rvert+\frac{\vec v}{\lvert\vec v\rvert}\sin\lvert\vec v\rvert ,
$$
it is surjective onto $S^3$, its kernel is the union of the spheres $2\pi kS^2$, and it is a local diffeomorphism exactly where $\lvert\vec v\rvert\notin2\pi\mathbb{Z}\setminus\{0\}$.

*Proof.* The exponential series of a pure quaternion is the cosine plus the sine times the unit direction, by $\vec m^2=-e_t$. Every versor is $\cos\theta+\sin\theta\,\vec m$ with $\theta\in[0,\pi]$ and $\vec m$ unit, so the map is onto; the vanishing of the sine gives the kernel; the differential has the rank of $\sin\lvert\vec v\rvert/\lvert\vec v\rvert$ times the identity on the complement of the radial direction. Verified numerically on the four axes. The exponential is read in [Quaternion Exponential and Lie Group Structure](quaternion-exponential-and-lie-group-structure.html).

**Remark (the group is not a product of circles).** $\pi_1(S^3)=0$, so the group is simple modulo its centre, and it is not a torus: its rank is one and its maximal torus is a circle, but the circle does not fill it. **The versor group is the compact simply connected group of rank one, and this is the whole of its structure as a group.**

## The Identity with $SU(2)$ and $\mathrm{Sp}(1)$

**Theorem (the three names).** The versor group is $SU(2)$ through the standard matrix model, and it is $\mathrm{Sp}(1)$ as the group of the quaternionic unitary $1\times1$ matrices.

*Proof.* In the model of [The M2C-H Standard Representation](m2c-h-pauli-representation.html), the image of a versor is a matrix $A$ with $A^*A=I$ and $\det A=N(\tilde u)=1$, so $SU(2)$ contains the image; conversely a matrix of $U(2)$ in the image of the algebra is determined by its first row of length one, which is the image of a versor. The identification with $\mathrm{Sp}(1)$ is the case $n=1$ of the definition of the quaternionic unitary group. Verified by multiplying the matrices of random versors.

**Corollary (the centre and the quotient).** The centre of the versor group is $\{\pm e_t\}$, and the quotient is $SO(3)$.

*Proof.* A versor commutes with every versor only if it is real, by the centraliser theorem, and the real versors are $\pm e_t$; the quotient by the centre is the rotation group of the adjoint action. Verified on the two central elements.

**Remark (why three names for one group).** The three names record three structures: the quaternionic structure (the algebra acting on itself), the complex structure (the matrix model) and the symplectic structure (the hermitian form). **The versor group is the same group in the three languages, and the identifications are the identifications of the three descriptions of the algebra.**

## The Two-Sided Action and the Double Covers

**Theorem (the covers).** The adjoint action $\tilde q\mapsto\tilde u\tilde q\tilde u^{-1}$ gives a surjective homomorphism $S^3\to SO(3)$ with kernel $\{\pm e_t\}$; the two-sided action $(\tilde u,\tilde p)\cdot\tilde q=\tilde u\tilde q\tilde p^{-1}$ gives a surjective homomorphism $S^3\times S^3\to SO(4)$ with kernel $\{(\pm e_t,\pm e_t)\}$ of order two.

*Proof.* Both actions are by algebra automorphisms and preserve $N$, hence are orthogonal; the adjoint action fixes $e_t$ and acts on the vector subspace by rotations, with determinant one; the two-sided action has determinant one on $\mathbb{H}=\mathbb{R}^4$ and every orientation-preserving isometry is of this form, by counting the dimensions and using the simplicity of the two factors. The kernels are computed by the centraliser theorem. Verified on the matrices of the actions. The covers and the rotation formulas are in [Quaternion Rotations and Reflections](quaternion-rotations-and-reflections.html) and [Four-Dimensional Rotations](four-dimensional-rotations.html).

**Corollary (the spin groups).** $S^3=\mathrm{Spin}(3)$ and $S^3\times S^3=\mathrm{Spin}(4)$, and the two covers are the universal covers of the two rotation groups.

*Proof.* The two groups are simply connected and the covers have kernel of order two; a connected two-fold cover of a Lie group by a simply connected group is its universal cover. Verified by the fundamental groups.

**Remark (the two-sided action and the two commuting spheres).** The left and the right factors of $S^3\times S^3$ commute elementwise and meet in $\{\pm e_t\}$, and the two spheres generate $SO(4)$. **The double cover of the four-dimensional rotation group is the product of two copies of the versor group, and the product is the algebraic form of the decomposition of a rotation into two isoclinic rotations.**

## The Unitary Group of the Two Forms

**Definition.** For a quadratic form $Q$ on $\mathbb{H}$ the **$\mathbb{H}$-linear unitary group** is $U_{\mathbb{H}}(Q)=\{f\in GL_{\mathbb{H}}(\mathbb{H}):\ Q\circ f=Q\}$, the isometries that commute with the left action of the algebra.

**Theorem (the definite form).** $U_{\mathbb{H}}(N)=S^3$: the $\mathbb{H}$-linear isometries of the quaternion norm are the right multiplications by the versors, and the group is compact of dimension three.

*Proof.* An $\mathbb{H}$-linear $f$ is the right multiplication by $\tilde g=f(e_t)$; the condition $N(\tilde q\tilde g)=N(\tilde q)$ for all $\tilde q$ is $N(\tilde g)=1$, since $N$ is multiplicative. So the group is the versor group, acting on the right. Verified on random versors.

**Theorem (the indefinite form).** $U_{\mathbb{H}}(P)=\{\pm e_t\}$: the only $\mathbb{H}$-linear isometries of the plain form are the two signs, so the indefinite form has no continuous group of the algebra.

*Proof.* With $f$ the right multiplication by $\tilde g$, the condition is $P(\tilde q\tilde g)=P(\tilde q)$ for all $\tilde q$. At $\tilde q=e_t$ it gives $P(\tilde g)=1$, that is $g_t^2-\lvert\vec g\rvert^2=1$. At a pure unit $\tilde q=\vec n$ it gives $P(\vec n\tilde g)=P(\vec n)=-1$, and the scalar part of $(\vec n\tilde g)^2$ is $2\langle\vec g,\vec n\rangle^2-g_t^2-\lvert\vec g\rvert^2$, so the condition reads $\langle\vec g,\vec n\rangle^2=\lvert\vec g\rvert^2$ for every invertible $\vec n$, which forces $\vec g=0$ and then $g_t=\pm1$. Verified numerically: the two signs satisfy the condition and no other candidate does.

**Remark (the two readings of the contrast).** The real isometry group of $P$ is the large non-compact $O(1,3)$ of [The P Isometry Group and Its Cartan Decomposition](the-p-isometry-group-and-its-cartan-decomposition.html), and almost none of it commutes with the algebra; the real isometry group of $N$ is the compact $O(4)$, and its $\mathbb{H}$-linear part is the versor group. **The definite form has a unitary group of the algebra and it is the versors; the indefinite form has none, and the contrast is the sharpest measure of what the definite form does for the algebra.**

## The 2×2 Matrix Model and $\mathrm{U}(2)$

**Theorem (the intersection with $\mathrm{U}(2)$).** In the model $\mathbb{H}\subset M_2(\mathbb{C})$, the versor group is $\mathbb{H}\cap U(2)=SU(2)$, and $U(2)$ is the central product of $SU(2)$ with the circle of the scalar phases, a circle that leaves the algebra.

*Proof.* The image of a versor is unitary with determinant one; conversely a unitary matrix in the image has determinant of modulus one and equal to $N(\tilde u)=1$. A matrix of $U(2)$ has determinant of modulus one, and the scalar matrices $e^{i\theta}I$ are not in the image of $\mathbb{H}$ unless $\theta\in\pi\mathbb{Z}$, since their entries are complex and not of the quaternionic form. Verified on the two families.

**Remark (the phase the quaternion does not have).** $U(2)$ is the unitary group of the complexified algebra, and the quaternion algebra meets it in $SU(2)$: the missing circle is the central phase that the biquaternion block has and the real algebra does not. **The unitary group of the algebra is the special unitary group of its matrix model, and the specialness is the reality condition of the coefficients.**

## The Maximal Torus and the Weyl Group

**Theorem (the maximal torus).** For a unit axis $\nu$, the circle $T_\nu=\{e^{\theta\nu}:\theta\in\mathbb{R}\}$ is a maximal torus of the versor group, and every maximal torus is of this form for exactly one axis line.

*Proof.* The circle is a compact connected abelian subgroup, and a compact abelian subgroup of $S^3$ lies in a plane $\mathbb{C}_\nu$, by the centraliser theorem applied to one of its non-real elements; the plane meets the sphere in the circle. The axis and its negative give the same circle. Verified on the four coordinate axes.

**Theorem (the Weyl group).** The normaliser of $T_\nu$ is $T_\nu\cup\{\tilde u:\tilde u\nu\tilde u^{-1}=-\nu\}$, and the Weyl group is $\mathbb{Z}/2$, acting on the circle by $\theta\mapsto-\theta$.

*Proof.* A versor normalises the circle exactly when it sends the axis line to itself, that is when it fixes or reverses $\nu$; the reversers exist, for instance the versors of the angle $\pi$ about an axis perpendicular to $\nu$, and they act by conjugation on the circle with the inversion. Verified on the two classes.

**Remark (the two circles).** The circle of the versors of the axis $\nu$ is the intersection of the group with the plane $\mathbb{C}_\nu$, and the planes of the different axes give the different maximal tori, two axes giving the same torus exactly when they are the same line. **The projective plane of the axes is the space of the maximal tori of the versor group.**

**Remark (rank one).** The versor group has rank one: one circle of the maximal torus and one reflection in the Weyl group. **Its maximal torus is the circle of the versors of a named axis, which is the group of the axis pairing of [The Axis Pairing of the Polar Decomposition of a Quaternion](the-axis-pairing-of-the-polar-decomposition-of-a-quaternion.html), and its Weyl group is the exchange of the two signs of the axis.**

## The Place Among the Groups

| group | dimension | compact | simply connected | relation to the algebra |
|---|---|---|---|---|
| $S^3\cong\mathrm{Sp}(1)\cong SU(2)$ | $3$ | yes | yes | the versors |
| $SO(3)$ | $3$ | yes | no | the adjoint quotient |
| $SO(4)$ | $6$ | yes | no | the two-sided quotient |
| $\mathrm{Spin}(4)$ | $6$ | yes | yes | $S^3\times S^3$ |
| $\mathbb{H}^{\times}$ | $4$ | no | no | the invertibles |
| $O(4)$ | $6$ | yes | no | the isometries of $N$ |
| $O(1,3)$ | $6$ | no | no | the isometries of $P$ |
| $U(2)$ | $4$ | yes | no | the unitary group of the matrix model |

**Remark (the reading of the table).** The versor group is the only compact group of the algebra itself; the rotation groups are its quotients, the spin groups its products, the groups of invertibles its cone, and the isometry groups of the two forms are the two ways of enlarging it, one compact and one not. **The compact column contains the versors and their quotients; the non-compact column contains the invertibles and the isometries of the indefinite form; and the unitary group of the algebra is the single group of the first column.**

## Summary

The versors are the quaternions of norm one; they form the sphere $S^3$, a compact connected simply connected Lie group of dimension three, which is the kernel of the norm and the compact part of the group of invertibles.

Its Lie algebra is the vector subspace with the bracket $2\vec u\times\vec v$, isomorphic to $\mathfrak{so}(3)$; its exponential is the quaternion exponential of a pure element, surjective with kernel the spheres $2\pi kS^2$.

It is $\mathrm{Sp}(1)$, $SU(2)$ and $\mathrm{Spin}(3)$, its centre is $\{\pm e_t\}$, and its two-sided action gives the double covers of $SO(3)$ and $SO(4)$, the second with kernel of order two, so that $\mathrm{Spin}(4)=S^3\times S^3$.

The $\mathbb{H}$-linear isometry group of the definite form is the versor group; that of the indefinite form is the two signs, so the indefinite form has no continuous unitary group of the algebra.

In the matrix model the versors are $\mathbb{H}\cap U(2)=SU(2)$, and the missing circle is the central phase of the biquaternion block.

The maximal torus is the circle of the versors of a named axis, and the Weyl group is $\mathbb{Z}/2$ acting by inversion.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S^3$ | the versor group, the unit sphere |
| $N$ | the quaternion norm |
| $T_\nu$ | the circle of the versors of the axis $\nu$ |
| $U_{\mathbb{H}}(Q)$ | the $\mathbb{H}$-linear isometries of the form $Q$ |
| $\mathrm{Spin}(n)$ | the universal cover of $SO(n)$ |
| $\mathrm{Sp}(1)$ | the quaternionic unitary group of order one |

## Further Reading

- [The Quaternion Group of Invertibles as a Topological Group](the-quaternion-group-of-invertibles-as-a-topological-group.html) for the group of invertibles and its topology.
- [Quaternion Rotations and Reflections](quaternion-rotations-and-reflections.html) and [Four-Dimensional Rotations](four-dimensional-rotations.html) for the two double covers.
- [The M2C-H Standard Representation](m2c-h-pauli-representation.html) for the matrix model and the identification with $SU(2)$.
- [The P Isometry Group and Its Cartan Decomposition](the-p-isometry-group-and-its-cartan-decomposition.html) for the indefinite isometry group.
- [The Unitary Group of the Biquaternion Algebra](the-unitary-group-of-the-biquaternion-algebra.html) for the complex counterpart.
