
# __Quaternion Operator Representation__

## Introduction

A quaternion can be read as an operator, rather than as a point, in three related ways: by left multiplication, by the adjoint action $x\mapsto qxq^{-1}$, and by the sandwich $x\mapsto qx\bar{\tilde q}$. The first is the operator of the regular representation; the second acts on the imaginary subspace as a rotation and is the source of the covering of the rotation group; the third agrees with the second on the unit sphere and carries the norm scale more generally. This article treats the three readings, their kernels and images, their action on the scalar and vector subspaces, and the double covers of $SO(3)$ and $SO(4)$ that the adjoint and the two-sided actions realise. It is the quaternion member of the family's operator-representation pair; its counterpart is the biquaternion operator representation, where the sandwich is taken with the Hermitian dagger and the operators are the similarity classes of $GL_2(\mathbb{C})$.

The article builds on *Quaternion Algebra* and *Quaternion Norm and Invertibility* for the algebra and the norm, on *The Scalar and Vector Subspaces of $\mathbb{H}$* for the decomposition on which the operators act, and on *Quaternion Rotations and Reflections* for the geometric interpretation of the adjoint action. The polar form of an element, which supplies the axis-angle reading of the operator, is from *Quaternion Polar Representation*.

The corpus's default base is a commutative ring with identity, and the operator statements over units require only that the element be invertible; the rotation, orthogonal and topological statements are over $\mathbb{R}$, and the double-cover statements are the statements of compact Lie groups.

Throughout, $\mathbb{H}$ is the quaternion algebra with basis $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$; a quaternion is $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ with conjugate $\bar{\tilde q} = q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3$ and norm form $N(\tilde q) = \tilde q\bar{\tilde q}$; the unit group is $\mathbb{H}^{\times} = \mathbb{H}\setminus\{0\}$ and the unit sphere is $Sp(1) = \{\tilde q : N(\tilde q) = 1\}\cong S^3$. The left multiplication operator is $L_q(x) = qx$, the right multiplication operator $R_q(x) = xq$, the adjoint action $\operatorname{Ad}_q(x) = qxq^{-1}$, and the sandwich $S_q(x) = qx\bar{\tilde q}$.

## The Element as an Operator

**Definition.** The **operator representation** of an element $\tilde q$ is the pair of endomorphisms $L_q$ and $R_q$ of the algebra given by left and right multiplication.

**Theorem.** For every $\tilde q$ the operators $L_q$ and $R_q$ are $F$-linear, they commute, and they satisfy

$$
L_pL_q = L_{pq}, \qquad R_pR_q = R_{qp}, \qquad L_pR_q = R_qL_p .
$$

An element $\tilde q$ is a unit exactly when $L_q$ (equivalently $R_q$) is invertible.

*Proof.* The multiplicativity identities are associativity, and the commuting identity is $L_pR_q(x) = pxq = R_qL_p(x)$. The kernel of $L_q$ is $\{x : qx = 0\}$, which is zero exactly when $\tilde q$ has no one-sided zero divisor, that is, when $\tilde q$ is a unit, by *Quaternion Norm and Invertibility*; the same argument applies to $R_q$. $\square$

**Proposition.** The operator $L_q$ is the sum of a scalar operator and a skew-adjoint operator on the Euclidean space $\mathbb{H}$: $L_q = q_0\,\mathrm{id} + L_{\mathbf{q}}$ with $L_{\mathbf{q}}$ skew-adjoint, and $L_q^{*} = L_{\bar{\tilde q}}$ for the Euclidean adjoint.

*Proof.* The scalar part $q_0$ acts as the scalar operator $q_0\,\mathrm{id}$; the pure part gives the skew part, since $\langle x, \mathbf{q}y\rangle = \langle \bar{\mathbf{q}}x, y\rangle = -\langle \mathbf{q}x, y\rangle$. The adjoint identity is $\langle x, qy\rangle = \operatorname{Sc}(x\,\overline{qy}) = \operatorname{Sc}(\bar{\tilde q} x\bar y) = \langle \bar{\tilde q} x, y\rangle$. $\square$

## The Adjoint Action

**Definition.** The **adjoint action** of a unit $\tilde q$ on $\mathbb{H}$ is

$$
\operatorname{Ad}_q(x) = qxq^{-1} = qx\bar{\tilde q} .
$$

**Theorem.** The adjoint action is an algebra automorphism for every unit $\tilde q$, it is the identity on the centre, and it preserves the norm form and the decomposition $\mathbb{H} = \mathbb{R}_{\mathbb{H}}\oplus\operatorname{Im}\mathbb{H}$.

*Proof.* For units $p,\tilde q$, $\operatorname{Ad}_p\operatorname{Ad}_q = \operatorname{Ad}_{pq}$ and $\operatorname{Ad}_q^{-1} = \operatorname{Ad}_{\tilde q^{-1}}$, so $\operatorname{Ad}_q$ is an automorphism; it fixes the centre because the centre is scalar and scalars commute. It preserves the norm form by $N(qxq^{-1}) = N(\tilde q)N(x)N(\tilde q)^{-1} = N(x)$; since it is an automorphism it fixes the scalar subspace pointwise and hence preserves the vector subspace. $\square$

**Theorem.** On the imaginary subspace the adjoint action is the orthogonal map

$$
\operatorname{Ad}_q(\mathbf{x}) = \frac{\bigl(q_0^2-|\mathbf{q}|^2\bigr)\mathbf{x} + 2\langle\mathbf{q},\mathbf{x}\rangle\mathbf{q} + 2q_0(\mathbf{q}\times\mathbf{x})}{N(\tilde q)},
$$

which for a unit quaternion reduces to the Euler–Rodrigues formula

$$
\operatorname{Ad}_u(\mathbf{x}) = \bigl(u_0^2-|\mathbf{u}|^2\bigr)\mathbf{x} + 2\langle\mathbf{u},\mathbf{x}\rangle\mathbf{u} + 2u_0(\mathbf{u}\times\mathbf{x}),
$$

the rotation by the axis $\mathbf{u}/|\mathbf{u}|$ and angle $2\arccos(u_0)$, with $u = u_0+\mathbf{u}$ a unit quaternion.

*Proof.* Expand $qxq^{-1} = qx\bar{\tilde q}/N(\tilde q)$ with $x = \mathbf{x}$ pure, using $\mathbf{a}\mathbf{x} = -\langle\mathbf{a},\mathbf{x}\rangle+\mathbf{a}\times\mathbf{x}$; collecting the scalar and vector terms and dividing by $N(\tilde q)$ gives the displayed expression. Writing the unit $u$ with $u_0 = \cos\theta$ and $\mathbf{u} = \mu\sin\theta$ exhibits it as the rotation of axis $\mu$ and angle $2\theta$. $\square$

**Proposition.** For a unit quaternion $u$ the adjoint action $\operatorname{Ad}_u$ is an orientation-preserving isometry of $\operatorname{Im}\mathbb{H}\cong\mathbb{R}^3$, the map $Sp(1)\to SO(3)$, $u\mapsto \operatorname{Ad}_u|_{\operatorname{Im}\mathbb{H}}$ is a surjective group homomorphism with kernel $\{\pm1\}$, and $\operatorname{Ad}_u = \operatorname{Ad}_{-u}$.

*Proof.* The restriction is orthogonal because it preserves the norm form on a three-dimensional space, and it is orientation-preserving; it is a homomorphism by the automorphism property, its kernel is the set of units centralising the imaginary subspace, namely $\{\pm1\}$, and the surjectivity and the two-to-one property are from *Quaternion Rotations and Reflections*. $\square$

## The Sandwich

**Definition.** The **sandwich** (or conjugation sandwich) of an element $\tilde q$ is

$$
S_q(x) = qx\bar{\tilde q} .
$$

**Theorem.** The sandwich is related to the adjoint action by

$$
S_q = N(\tilde q)\,\operatorname{Ad}_q,
$$

so that on the unit sphere $Sp(1)$ the sandwich and the adjoint action coincide; the sandwich scales the norm form by $N(\tilde q)^2$, its determinant on the four-dimensional space is $\det S_q = N(\tilde q)^4$, and it is invertible exactly when $\tilde q$ is.

*Proof.* Since $\bar{\tilde q} = N(\tilde q)\tilde q^{-1}$ for $\tilde q\neq0$, we have $qx\bar{\tilde q} = N(\tilde q)\,\tilde q x \tilde q^{-1} = N(\tilde q)\operatorname{Ad}_q(x)$. Hence the two agree when $N(\tilde q) = 1$. $\square$

**Theorem.** The sandwich preserves the norm form up to the square of $N(\tilde q)$: $N(S_q(x)) = N(\tilde q)^2N(x)$, and it maps the scalar subspace to itself and the vector subspace to itself.

*Proof.* $N(qx\bar{\tilde q}) = N(\tilde q)N(x)N(\bar{\tilde q}) = N(\tilde q)^2N(x)$. For a scalar $s$ the element $S_q(s) = qs\bar{\tilde q} = s\,q\bar{\tilde q} = sN(\tilde q)$ is scalar, so $S_q$ preserves the scalar subspace; being invertible and preserving the norm form, it preserves its orthogonal complement, the vector subspace. $\square$

**Proposition.** The unit-norm slice of the sandwich, $N(\tilde q) = 1$, is the adjoint action; on this slice the sandwich and the adjoint action are the same operator, and the scale $N(\tilde q)$ is the only difference away from it. The sandwich of a pure imaginary element $\mathbf{p}$ is $\mathbf{p}$ acting by $S_{\mathbf{p}}(x) = \mathbf{p}x\bar{\mathbf{p}} = N(\mathbf{p})\operatorname{Ad}_{\mathbf{p}}(x)$.

*Proof.* The first statement is the relation above; for pure $\mathbf{p}$ we have $\bar{\mathbf{p}} = -\mathbf{p}$, so $S_{\mathbf{p}}(x) = -\mathbf{p}x\mathbf{p}$, and the general relation applies. $\square$

## Kernel and Image

**Theorem.** For $\tilde q\neq0$ the operators $L_q$, $R_q$, $\operatorname{Ad}_q$ and $S_q$ are invertible, so each has kernel $0$ and image $\mathbb{H}$. For $\tilde q = 0$ all four are the zero operator.

*Proof.* Invertibility of $L_q$ and $R_q$ is the unit criterion; $\operatorname{Ad}_q$ is invertible for units with inverse $\operatorname{Ad}_{\tilde q^{-1}}$, and $S_q = N(\tilde q)\operatorname{Ad}_q$ is invertible whenever $N(\tilde q)\neq0$. For $\tilde q = 0$ every product vanishes. $\square$

**Proposition.** The fixed subspace of the adjoint action $\operatorname{Ad}_q$ is the centraliser of $\tilde q$ in $\mathbb{H}$: it is $\mathbb{H}$ when $\tilde q$ is central (that is, real), and the two-dimensional subalgebra $\{a+bq : a,b\in F\}\cong F[\tilde q]$ otherwise. On the imaginary subspace the fixed directions are the axis of the rotation, namely the line $\mathbb{R}\mathbf{q}$.

*Proof.* $qxq^{-1} = x$ iff $qx = xq$, so the fixed space is the centraliser. For real $\tilde q$ the centraliser is all of $\mathbb{H}$; for non-real $\tilde q$ it is the subalgebra generated by $\tilde q$ and $1$, of dimension two. On $\operatorname{Im}\mathbb{H}$ the fixed line is $\mathbb{R}\mathbf{q}$, the rotation axis, and the only nonzero fixed vectors of a rotation are along its axis. $\square$

## The Action on the Subspaces

**Definition.** The **action table** of the operator representation records, for each operator, its effect on the scalar subspace $\mathbb{R}_{\mathbb{H}}$ and on the vector subspace $\operatorname{Im}\mathbb{H}$.

| Operator | On $\mathbb{R}_{\mathbb{H}}$ | On $\operatorname{Im}\mathbb{H}$ |
|---|---|---|
| $L_q$, left multiplication | $s\mapsto qs$, lands in the span of $1,\mathbf{q}$ | $\mathbf{x}\mapsto -\langle\mathbf{q},\mathbf{x}\rangle+q_0\mathbf{x}+\mathbf{q}\times\mathbf{x}$ |
| $R_q$, right multiplication | $s\mapsto sq = qs$ | $\mathbf{x}\mapsto -\langle\mathbf{x},\mathbf{q}\rangle+q_0\mathbf{x}+\mathbf{x}\times\mathbf{q}$ |
| $\operatorname{Ad}_q$, adjoint | identity | rotation by the angle and axis of $\tilde q$ |
| $S_q$, sandwich | $N(\tilde q)\,\mathrm{id}$ | $N(\tilde q)$ times the rotation of $\operatorname{Ad}_q$ |

**Proposition.** Left and right multiplication do not preserve the two subspaces individually — each sends the scalar line into the plane spanned by $1$ and the acting element — while the adjoint action and the sandwich do preserve the decomposition, acting as the identity (respectively the scale $N(\tilde q)$) on the scalar line and as a rotation (scaled) on the vector subspace.

*Proof.* $L_q(s) = qs = sq$ lies in the span of $1$ and $\tilde q$, and $L_q(\mathbf{x})$ has the scalar part $-\langle\mathbf{q},\mathbf{x}\rangle$, so neither subspace is preserved in general. The adjoint action fixes every scalar and carries the vector subspace to itself by the theorem above, and the sandwich is $N(\tilde q)$ times it. $\square$

**Corollary.** The adjoint action of a unit is a rotation of the vector subspace, and it acts on the whole algebra as the direct sum of the identity on the scalar line and that rotation on the vector subspace; the two summands are the representations of dimensions one and three into which the four-dimensional operator decomposes.

*Proof.* The decomposition $\mathbb{H} = \mathbb{R}_{\mathbb{H}}\oplus\operatorname{Im}\mathbb{H}$ is preserved, the first summand is fixed, and the second carries the rotation; the dimensions are as stated. $\square$

## The Double Covers

**Theorem (double cover of $SO(3)$).** The adjoint action induces an exact sequence of Lie groups

$$
1\longrightarrow \{\pm1\}\longrightarrow Sp(1)\xrightarrow{\ \operatorname{Ad}\ } SO(3)\longrightarrow 1,
$$

so that $Sp(1)/\{\pm1\}\cong SO(3)$; the map is the universal double cover of the rotation group, and $Sp(1)\cong S^3$ is simply connected.

*Proof.* The map is a surjective homomorphism with kernel $\{\pm1\}$, as shown above; it is a covering map because it is a surjective homomorphism of Lie groups with discrete kernel (a standard fact quoted as standard), and the double cover is universal because $S^3$ is simply connected. $\square$

**Theorem (double cover of $SO(4)$).** The two-sided action induces an exact sequence

$$
1\longrightarrow \{(1,1),(-1,-1)\}\longrightarrow Sp(1)\times Sp(1)\xrightarrow{\ \rho\ } SO(4)\longrightarrow 1,
$$

where $\rho(u,v)(x) = ux\bar v$, so that $\bigl(Sp(1)\times Sp(1)\bigr)/\{\pm1\}\cong SO(4)$.

*Proof.* The map $(u,v)\mapsto \rho(u,v)$ is a homomorphism into the isometries of the Euclidean space $\mathbb{H}\cong\mathbb{R}^4$ because $N(ux\bar v) = N(x)$, and its image lies in the identity component $SO(4)$ since $Sp(1)\times Sp(1)$ is connected. Its kernel is $\{(u,v) : ux\bar v = x\ \forall x\}$, which forces $u = v$ up to the central element and gives exactly $\{\pm(1,1)\}$; a dimension count $\dim(Sp(1)\times Sp(1)) = 6 = \dim SO(4)$ and the connectedness of $Sp(1)\times Sp(1)$ then give surjectivity. $\square$

## Relation to the Polar Representation and to the Biquaternion Sandwich

**Theorem.** Every non-zero quaternion has the polar form $\tilde q = |\tilde q|u$ with $u\in Sp(1)$, and the adjoint action depends only on the unit factor: $\operatorname{Ad}_q = \operatorname{Ad}_u$, while the sandwich is $S_q = |\tilde q|^2\operatorname{Ad}_u$. The axis and angle of the rotation $\operatorname{Ad}_u$ are those of the polar form, $\mu = \mathbf{q}/|\mathbf{q}|$ and $\cos(\theta/2) = q_0/|\tilde q|$.

*Proof.* $\tilde q^{-1} = u^{-1}|\tilde q|^{-1}$ and $\tilde q = |\tilde q|u$ cancel the scale in $\operatorname{Ad}_q$; the sandwich scale is $N(\tilde q) = |\tilde q|^2$. The axis-angle identification is the polar form of *Quaternion Polar Representation*, where the half-angle is the angle of the unit factor. $\square$

The biquaternion operator representation takes the sandwich with the Hermitian dagger, $x\mapsto \tilde Qx\tilde Q^{\dagger}$, because the biquaternion algebra carries the conjugation $\dagger$ that the real quaternion algebra does not; here the sandwich is taken with quaternion conjugation $\bar{\cdot}$, which is the only antiautomorphism available, and it agrees with the adjoint action on the unit slice. The biquaternion account is in *Biquaternion Operator Representation*, where the sandwich acts on $M_2(\mathbb{C})$ by similarity and realises the Lorentz group rather than the rotation group; no such indefinite operator occurs here, because the quaternion norm form is definite.

## Summary

An element $\tilde q$ acts on the algebra by left and right multiplication $L_q$ and $R_q$, which commute and satisfy $L_pL_q = L_{pq}$ and $R_pR_q = R_{qp}$; $L_q = q_0\,\mathrm{id}+L_{\mathbf{q}}$ decomposes into a scalar and a skew-adjoint part. The adjoint action $\operatorname{Ad}_q(x) = qxq^{-1}$ is an algebra automorphism for every unit, it fixes the centre, preserves the norm form and the scalar–vector decomposition, and acts on the imaginary subspace as the rotation given by the Euler–Rodrigues formula; the sandwich $S_q(x) = qx\bar{\tilde q}$ equals $N(\tilde q)\operatorname{Ad}_q$, so it coincides with the adjoint action exactly on the unit slice $N(\tilde q) = 1$.

For $\tilde q\neq0$ all four readings are invertible with kernel $0$ and image $\mathbb{H}$; the fixed subspace of the adjoint action is the centraliser of $\tilde q$, all of $\mathbb{H}$ for real $\tilde q$ and the two-dimensional subalgebra $F[\tilde q]$ otherwise, with the axis line as the fixed direction on the imaginary subspace. The action table separates the operators that preserve the scalar–vector decomposition — the adjoint action and the sandwich, acting as the identity or the scale on the scalar line and as a rotation or a scaled rotation on the vector subspace — from left and right multiplication, which do not.

The adjoint action gives the double cover $Sp(1)\to SO(3)$ with kernel $\{\pm1\}$ and the two-sided action $Sp(1)\times Sp(1)\to SO(4)$ with kernel $\{\pm(1,1)\}$. The polar form separates the scale from the unit factor, and the adjoint action depends only on the latter while the sandwich carries the scale $|\tilde q|^2$; the biquaternion sandwich uses the Hermitian dagger and realises an indefinite group instead, a possibility closed here by the definiteness of the quaternion norm form.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | The quaternion algebra |
| $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ | Quaternion, conjugate $\bar{\tilde q}$, norm form $N(\tilde q) = \tilde q\bar{\tilde q}$ |
| $L_q(x) = qx$ | Left multiplication operator |
| $R_q(x) = xq$ | Right multiplication operator |
| $\operatorname{Ad}_q(x) = qxq^{-1} = qx\bar{\tilde q}$ | Adjoint action, an automorphism for a unit |
| $S_q(x) = qx\bar{\tilde q}$ | Sandwich $= N(\tilde q)\operatorname{Ad}_q$ |
| $Sp(1) = \{\tilde q : N(\tilde q) = 1\}\cong S^3$ | Unit quaternions |
| $\mathbb{R}_{\mathbb{H}}, \operatorname{Im}\mathbb{H}$ | Scalar line (fixed) and vector subspace (rotated) |
| $\operatorname{Ad}: Sp(1)\to SO(3)$ | Double cover with kernel $\{\pm1\}$ |
| $\rho(u,v)(x) = ux\bar v$ | Two-sided action, covering $SO(4)$ |
| $\mu = \mathbf{q}/\lvert\mathbf{q}\rvert$, $\theta$ | Rotation axis and angle from the polar form |
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra, sandwich with $\dagger$ |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the origin of the quaternion operator and the conjugation action.
- Peter Guthrie Tait, *An Elementary Treatise on Quaternions* (Cambridge University Press, 3rd ed. 1890), for the operator form of quaternion multiplication and rotation.
- Olinde Rodrigues, "Des lois géométriques qui régissent les déplacements d'un système solide", *Journal de Mathématiques Pures et Appliquées* **5** (1840) 380–440, for the Euler–Rodrigues rotation formula.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for the double covers $Sp(1)\to SO(3)$ and $Sp(1)\times Sp(1)\to SO(4)$.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the operator and spinor realisations of the quaternion algebra.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the conjugation action and the rotation groups.
