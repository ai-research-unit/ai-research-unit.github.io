
# __Quaternion Exponential and Lie Group Structure__

## Introduction

The quaternion algebra is at once an associative algebra, a Lie algebra under the commutator bracket, and the tangent space at the identity of its group of units; the unit sphere is a compact Lie group, and the exponential map connects the three descriptions. This article develops that structure: the Lie algebra of $\mathbb{H}$ and its decomposition into a centre and an orthogonal part, the exponential map and its closed form, the surjectivity of the exponential onto the group of units, the polar split of the units into a positive scale and the unit sphere, the compact subgroup $Sp(1)$ and its parametrisation, and the relation to the rotations and reflections of the geometry slot. It is the quaternion member of the family's exponential-and-Lie-group pair; its counterpart is the biquaternion case, where the unit group is $GL_2(\mathbb{C})$ and the exponential is complex.

The article uses *Quaternion Algebra* and *Quaternion Norm and Invertibility* for the algebra and the units, *The Scalar and Vector Subspaces of $\mathbb{H}$* for the decomposition, *Quaternion Rotations and Reflections* for the orthogonal actions, and *Quaternion Automorphisms and Derivations* for the derivation algebra, which is the Lie algebra computed here independently. The special functions are in *Quaternion Special Functions*.

The corpus's default base is a commutative ring with identity, but the exponential series, the closed form and the Lie group statements require a complete ordered field, so everything below is stated over $\mathbb{R}$; the algebraic identities remain meaningful for complex coefficients and are used in the comparison.

Throughout, $\mathbb{H}$ is the quaternion algebra over $\mathbb{R}$ with basis $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$; a quaternion is $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ with conjugate $\bar{\tilde q}$, norm $N(\tilde q) = \tilde q\bar{\tilde q}$ and modulus $|\tilde q| = \sqrt{N(\tilde q)}$; the unit group is $\mathbb{H}^{\times} = \mathbb{H}\setminus\{0\}$ and the unit sphere is $Sp(1) = \{\tilde q : N(\tilde q) = 1\}\cong S^3$.

## The Lie Algebra Structure

**Definition.** The **commutator bracket** on $\mathbb{H}$ is $[x,y] = xy-yx$; the algebra $\mathbb{H}$ with this bracket is the **Lie algebra of the quaternion algebra**.

**Proposition.** The bracket is bilinear, alternating and satisfies the Jacobi identity, so $\mathbb{H}$ is a Lie algebra; the centre of the algebra is the centre of the Lie algebra, and the derived subalgebra is the vector subspace,

$$
[\mathbb{H},\mathbb{H}] = \operatorname{Im}\mathbb{H}, \qquad Z(\mathbb{H}) = \mathbb{R}_{\mathbb{H}} .
$$

*Proof.* The bracket of an associative algebra is a Lie bracket, the Jacobi identity being the associativity of multiplication. The commutator of any two quaternions is pure, since $\mathrm{Sc}([x,y]) = \mathrm{Sc}(xy)-\mathrm{Sc}(yx) = 0$, and the pure quaternions are all obtained as commutators, for instance $e_1 = \tfrac12[e_2,e_3]$; hence $[\mathbb{H},\mathbb{H}] = \operatorname{Im}\mathbb{H}$. The centre of the bracket is the set of elements commuting with every quaternion, namely $\mathbb{R}_{\mathbb{H}}$.

**Theorem.** As a Lie algebra the quaternion algebra splits as the direct sum of its centre and a simple ideal,

$$
\mathbb{H} = \mathbb{R}_{\mathbb{H}}\oplus\operatorname{Im}\mathbb{H}\cong\mathbb{R}\oplus\mathrm{SO}(3),
$$

and $\operatorname{Im}\mathbb{H}$ is isomorphic to the cross-product Lie algebra $\mathrm{SO}(3)\cong\mathrm{SU}(2)$, with $[\mathbf{p},\mathbf{q}] = 2(\mathbf{p}\times\mathbf{q})$.

*Proof.* The centre is an abelian ideal, and it commutes with the vector subspace, so the sum is direct; $\operatorname{Im}\mathbb{H}$ is a subalgebra and an ideal because its bracket lands in itself and the centre commutes with it. The bracket on the vector subspace is $[\mathbf{p},\mathbf{q}] = \mathbf{p}\mathbf{q}-\mathbf{q}\mathbf{p} = 2(\mathbf{p}\times\mathbf{q})$, which is the cross-product Lie algebra, isomorphic to $\mathrm{SO}(3)$ and to $\mathrm{SU}(2)$.

**Corollary.** The Lie algebra $\mathbb{H}$ is reductive but not semisimple: its centre is one-dimensional, and its derived algebra $\operatorname{Im}\mathbb{H}\cong\mathrm{SO}(3)$ is simple. The Killing form is negative definite on the derived ideal and zero on the centre.

*Proof.* $\mathrm{SO}(3)$ is simple, being the Lie algebra of the simple compact group $SO(3)$; the centre contributes a one-dimensional abelian factor, so the sum is reductive and not semisimple. The Killing form of a compact simple Lie algebra is negative definite, and it vanishes on the centre, which is abelian.

## The Exponential Map

**Definition.** The **exponential** of a quaternion is the sum of the series

$$
\exp(\tilde q) = \sum_{n=0}^{\infty}\frac{\tilde q^n}{n!},
$$

which converges for every $\tilde q$ because the quaternion norm is multiplicative and $\mathbb{H}$ is complete as a finite-dimensional real space.

**Proposition.** For every $\tilde q$ the exponential satisfies $N(\exp(\tilde q)) = e^{2q_0}$, so $\exp(\tilde q)$ is a unit with $|\exp(\tilde q)| = e^{q_0}$; the exponential maps the pure imaginary subspace into the unit sphere.

*Proof.* By continuity of $\exp$ relative to the rational exponential and the identity $N(\exp(\tilde q)) = \exp(2\mathrm{Sc}\tilde q)$, which holds for rational multiples and extends by continuity; for pure $\tilde q$, $q_0 = 0$ and the quaternion norm is one.

### Closed Form

**Theorem (closed form).** For $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ with $\mathbf{q}\neq0$,

$$
\exp(\tilde q) = e^{q_0}\Bigl(\cos|\mathbf{q}| + \frac{\mathbf{q}}{|\mathbf{q}|}\sin|\mathbf{q}|\Bigr),
$$

and for $\mathbf{q} = 0$ it reduces to the real exponential $\exp(q_0) = e^{q_0}$.

*Proof.* Write $\mathbf{q} = \mu\rho$ with $\mu$ a pure unit and $\rho = |\mathbf{q}|\geq0$, so $\mu^2 = -1$. Then $(q_0+\mu\rho)^n$ may be expanded, and separating the terms by the parity of $n$ and summing the real exponential gives the displayed expression, exactly as for the complex exponential.

**Corollary.** The exponential commutes with neither addition nor multiplication of quaternions; it satisfies $N(\exp \tilde q) = e^{2\mathrm{Sc}(\tilde q)}$ and maps the imaginary subspace onto the unit sphere, where it is the parametrisation $\exp(\mu\theta) = \cos\theta+\mu\sin\theta$ for a pure unit $\mu$.

*Proof.* The failure of additivity and multiplicativity is the non-commutativity of the algebra; the quaternion norm identity is the previous proposition; the pure case is the closed form with $q_0 = 0$.

### Surjectivity

**Theorem.** The exponential is surjective onto the group of units,

$$
\exp(\mathbb{H}) = \mathbb{H}^{\times} = \mathbb{H}\setminus\{0\},
$$

and it is surjective onto the unit sphere when restricted to the imaginary subspace.

*Proof.* Every non-zero quaternion has the polar form $\tilde q = |\tilde q|u$ with $|\tilde q| > 0$ and $u$ a unit quaternion; writing $u = \cos\theta+\mu\sin\theta$ with $\mu$ a pure unit and $\theta = \arccos(u_0)\in[0,\pi]$ gives $u = \exp(\mu\theta)$ by the closed form, and $|\tilde q| = e^{\ln|\tilde q|}$. Hence $\tilde q = \exp(\ln|\tilde q|+\mu\theta)$. The unit-sphere statement is the case $\ln|\tilde q| = 0$.

**Proposition.** The exponential is not injective; its kernel is the union of the spheres of pure quaternions of radius $2\pi k$ together with the origin,

$$
\exp^{-1}(1) = \{0\}\cup\bigcup_{k\geq1}\bigl\{x\in\operatorname{Im}\mathbb{H} : |x| = 2\pi k\bigr\},
$$

and its restriction to the open set $\{\tilde q : |\mathbf{q}| < \pi\}$ is a diffeomorphism onto $\mathbb{H}^{\times}\setminus(-\mathbb{R}_{>0})$.

*Proof.* $\exp(\tilde q) = 1$ forces $e^{q_0} = 1$ and $\sin|\mathbf{q}| = 0$ with $\cos|\mathbf{q}| = 1$, so $q_0 = 0$ and $|\mathbf{q}| = 2\pi k$ for an integer $k\geq0$, the case $k = 0$ giving the origin; conversely any such pure quaternion gives $\exp = 1$ by the closed form. The restriction statement is the classical property of the complex exponential applied to each axis direction $\mu$.

## The Group of Units

**Theorem.** The group of units is the direct product of the positive scalars and the unit sphere,

$$
\mathbb{H}^{\times}\cong\mathbb{R}_{>0}\times Sp(1), \qquad \tilde q = |\tilde q|\,u, \quad u = \frac{\tilde q}{|\tilde q|},
$$

and the two factors commute and are the image under the exponential of the centre and of the imaginary subspace respectively.

*Proof.* The polar split is *Quaternion Norm and Invertibility*; the scale factor is $\exp(q_0)$ with $q_0$ real and the unit factor is $\exp(\mathbf{q})$ up to the periodicity of the pure component, so the two exponential images are the two factors.

**Theorem.** The polar form and the exponential form are the same decomposition: every unit has the parametrisation

$$
u = \exp(\mu\theta) = \cos\theta+\mu\sin\theta, \qquad \mu\in\operatorname{Im}\mathbb{H},\quad N(\mu) = 1,\quad \theta\in[0,\pi],
$$

and the map $(\mu,\theta)\mapsto\exp(\mu\theta)$ is a diffeomorphism of the open set $\theta\in(0,\pi)$ onto the unit sphere with the two poles removed.

*Proof.* The parametrisation is the closed form on the pure subspace, and the failure of injectivity occurs exactly at the poles $u = \pm1$, where the axis $\mu$ is undetermined; away from them the axis and the angle are unique.

## The Compact Subgroup

**Theorem.** The unit sphere $Sp(1)$ is a compact connected Lie group of dimension three, diffeomorphic to $S^3$ and isomorphic to $SU(2)$; it is the maximal compact subgroup of $\mathbb{H}^{\times}$, and the group of units is the product of it with the non-compact factor $\mathbb{R}_{>0}$.

*Proof.* The unit sphere is the set $N(\tilde q) = 1$, a closed bounded subset of $\mathbb{R}^4$, hence compact; multiplication is smooth and the inverse is smooth, so it is a Lie group of dimension three, and its identification with $SU(2)$ is standard. It is the maximal compact subgroup of the product $\mathbb{R}_{>0}\times Sp(1)$ because the line has no non-trivial compact subgroup.

**Corollary.** The exponential image of the imaginary subspace is the whole of $Sp(1)$, so $Sp(1)$ is generated by its one-parameter subgroups $\exp(\mathbb{R}\mu)$, one for each pure unit $\mu$; the one-parameter subgroups are the great circles through the identity.

*Proof.* Surjectivity onto the unit sphere is the theorem above; a one-parameter subgroup is the image of $\mathbb{R}\mu$ under the exponential, which is the circle $t\mapsto\cos t+\mu\sin t$; the geodesic reading of these circles is in *Quaternion Rotations and Reflections*.

**Remark (versors, hyperbolic versors, and one-parameter groups).** The unit quaternions are Hamilton's versors, and the subgroup $\exp(\mathbb{R}\mu)$ generated by a unit pure $\mu$ is the family of versors of the fixed axis $\mu$; the naming and the arc picture are in *Quaternion Rotations and Reflections*. A **hyperbolic versor** is the same expression $\exp(tr) = \cosh t + r\sinh t$ with $r^2 = +1$ in place of $r^2 = -1$. It cannot be formed in $\mathbb{H}$, whose only elements of square $+1$ are the scalars $\pm1$, and it requires an algebra of split signature, the split-complex numbers or the split-quaternions of *Split-Complex Exponential and Lie Group Structure* and *Split-Quaternion Exponential and Lie Group Structure*. Lie's one-parameter group is the notion that subsumes both: for each $r$ with $r^2 = \pm1$ the map $t\mapsto\exp(tr)$ is a one-parameter subgroup, elliptic for $r^2 = -1$ and hyperbolic for $r^2 = +1$. In the definite case the generator directions $r$ and $-r$ trace the same circle in opposite directions, which is the reversal of direction of the corresponding rotation, while in the indefinite case they give the two branches $e^{tr}$ and $e^{-tr}$ of a hyperbola, and the exponential is injective along each line.

## The Exponential Parametrisation

**Theorem.** Every non-zero quaternion can be written uniquely as

$$
\tilde q = e^{\alpha}\exp(\mu\theta), \qquad \alpha\in\mathbb{R}, \quad \mu\in\operatorname{Im}\mathbb{H},\ N(\mu) = 1, \quad \theta\in[0,\pi],
$$

with the further identification $(\mu,\pi)\sim(-\mu,\pi)$ at the negative real axis.

*Proof.* Take $\alpha = \ln|\tilde q|$ and $\mu\theta$ the axis-angle form of the unit factor; the closed form gives the product, and the uniqueness away from the poles is that of the polar form and of the axis-angle pair.

**Proposition.** In this parametrisation the quaternion norm is $N(\tilde q) = e^{2\alpha}$, the modulus is $|\tilde q| = e^{\alpha}$, and the argument is $\theta$ along the direction $\mu$; the logarithm

$$
\log(\tilde q) = \ln|\tilde q| + \mu\theta
$$

is a right inverse of the exponential, defined on the complement of the negative real axis, and is multivalued on the whole of $\mathbb{H}^{\times}$.

*Proof.* The quaternion norm identity is the closed form; the logarithm inverts $\exp$ on the stated set by the surjectivity proof, and the ambiguity is the period $2\pi$ in the pure direction.

## The Adjoint Action of the Exponential

**Theorem.** The adjoint action of the exponential is the conjugation by its value,

$$
\exp(t\,\operatorname{ad}_{\mu})(x) = e^{t\mu}\,x\,e^{-t\mu} = \operatorname{Ad}_{e^{t\mu}}(x),
$$

for every $x\in\mathbb{H}$ and every $\mu\in\operatorname{Im}\mathbb{H}$; equivalently the adjoint representation of the Lie algebra and the adjoint action of the group of units agree under the exponential.

*Proof.* The identity $\exp(\operatorname{ad}_a) = \operatorname{Ad}_{\exp a}$ is the standard Lie-theoretic identity for an inner derivation, here computed from the series.

The identification of the adjoint action with the rotations of $\operatorname{Im}\mathbb{H}$, the half-angle rule, and the completion of the rotation group to the full orthogonal group by the orientation-reversing maps are the subject of *Quaternion Rotations and Reflections*; this article supplies the exponential and the adjoint identity that the geometry slot uses.

## Comparison with the Biquaternion Case

The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has the same underlying multiplication but complex coefficients, so its Lie algebra is the complexification $\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}$, and its group of units is $GL_2(\mathbb{C})$.

| Feature | $\mathbb{H}$ | $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
|---|---|---|
| Lie algebra | $\mathbb{R}\oplus\mathrm{SO}(3)$, real dimension $4$ | $\mathrm{GL}_2(\mathbb{C})$, complex dimension $4$ |
| Exponential | surjective onto $\mathbb{H}^{\times}$ | surjective onto $GL_2(\mathbb{C})$ |
| Closed form | $e^{q_0}(\cos\lvert\mathbf{q}\rvert+\mu\sin\lvert\mathbf{q}\rvert)$ | the same with complex $q_0,\mathbf{q}$ |
| Group of units | $\mathbb{R}_{>0}\times S^3$, compact factor $S^3$ | $GL_2(\mathbb{C})$, non-compact, connected |
| Maximal compact subgroup | $Sp(1)\cong SU(2)$ | $U(2)$ |
| Rotation group from the adjoint action | $SO(3)$ | $PSL(2,\mathbb{C})$, the projective Lorentz group |

The quaternion exponential is real and its unit group is the product of a line and a compact three-sphere; the biquaternion exponential is complex, its unit group is the non-compact $GL_2(\mathbb{C})$, and the adjoint action generates the projective Lorentz group rather than the rotation group. The reason is the same throughout: the quaternion norm is definite, so the unit sphere is compact and the one-parameter groups are circles, while the complex norm is indefinite, so the unit group is non-compact and the one-parameter groups include hyperbolic rotations. The biquaternion account is in *Biquaternion Lie Group and Exponential Structure*.

## Summary

The quaternion algebra is a Lie algebra under the commutator bracket, with derived subalgebra the imaginary subspace and centre the real line, splitting as $\mathbb{R}_{\mathbb{H}}\oplus\operatorname{Im}\mathbb{H}\cong\mathbb{R}\oplus\mathrm{SO}(3)$; it is reductive and not semisimple. The exponential has the closed form $\exp(q_0+\mathbf{q}) = e^{q_0}(\cos|\mathbf{q}|+\frac{\mathbf{q}}{|\mathbf{q}|}\sin|\mathbf{q}|)$, it satisfies $N(\exp \tilde q) = e^{2q_0}$, and it is surjective onto the group of units but not injective, with kernel the spheres of pure quaternions of radius $2\pi k$.

The group of units splits as $\mathbb{H}^{\times}\cong\mathbb{R}_{>0}\times Sp(1)$, and the unit sphere is the compact connected three-dimensional Lie group $Sp(1)\cong S^3\cong SU(2)$, the maximal compact subgroup; the polar and exponential forms of an element are the same decomposition, $\tilde q = e^{\alpha}\exp(\mu\theta)$ with $\mu$ a pure unit and $\theta\in[0,\pi]$, and the logarithm $\log \tilde q = \ln|\tilde q|+\mu\theta$ inverts the exponential off the negative real axis. The adjoint action of the exponential is the conjugation by its value, $\exp(t\operatorname{ad}_\mu) = \operatorname{Ad}_{e^{t\mu}}$, and the reading of this adjoint action as the rotations of the imaginary subspace is in *Quaternion Rotations and Reflections*.

The biquaternion case replaces the definite norm by the indefinite complex one: the unit group becomes $GL_2(\mathbb{C})$, the maximal compact subgroup becomes $U(2)$, and the adjoint action generates the projective Lorentz group. The compactness of $Sp(1)$ and the circularity of its one-parameter subgroups are exactly what the definite quaternion norm buys.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | The quaternion algebra, as algebra and as Lie algebra |
| $[x,y] = xy-yx$ | Commutator bracket |
| $\mathbb{R}_{\mathbb{H}}, \operatorname{Im}\mathbb{H}$ | Centre and derived subalgebra |
| $\mathbb{H}\cong\mathbb{R}\oplus\mathrm{SO}(3)$ | Lie algebra decomposition |
| $\exp(\tilde q) = \sum_n \tilde q^n/n!$ | Exponential map |
| $\exp(q_0+\mathbf{q}) = e^{q_0}(\cos\lvert\mathbf{q}\rvert+\frac{\mathbf{q}}{\lvert\mathbf{q}\rvert}\sin\lvert\mathbf{q}\rvert)$ | Closed form |
| $\exp(\mu\theta) = \cos\theta+\mu\sin\theta$ | Unit-sphere parametrisation, $\mu$ a pure unit |
| $\exp^{-1}(1) = \{2\pi k\mu\}$ | Kernel of the exponential |
| $\mathbb{H}^{\times}\cong\mathbb{R}_{>0}\times Sp(1)$ | Polar split of the units |
| $Sp(1)\cong S^3\cong SU(2)$ | Compact subgroup, maximal compact |
| $\log \tilde q = \ln\lvert \tilde q\rvert+\mu\theta$ | Logarithm, inverse off the negative axis |
| $\operatorname{Ad}_u(x) = uxu^{-1}$ | Adjoint action; $\exp(\operatorname{ad}_a) = \operatorname{Ad}_{\exp a}$ |
| $O(3)$ | Orthogonal group of $\operatorname{Im}\mathbb{H}$, from *Quaternion Rotations and Reflections*, where $O(3) = \{\pm\operatorname{Ad}_u : u\in Sp(1)\}$ |
| $GL_2(\mathbb{C}), U(2), PSL(2,\mathbb{C})$ | Biquaternion unit group, maximal compact, adjoint group |

## Further Reading

- John Stillwell, *Naive Lie Theory* (Springer, 2008), for the exponential map, the unit quaternions and the rotation group.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2nd ed. 2015), for the exponential of a matrix Lie algebra and the Lie correspondence.
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for $SU(2)$, its Lie algebra and the covering of $SO(3)$.
- John Voight, *Quaternion Algebras* (Springer, 2021), for the quaternion exponential and the unit group.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the exponential of a multivector and the spin parametrisation.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge University Press, 2003), for the rotor exponential and the composition of rotations.
