# __The Lie Structure of the Antisymmetric Quaternionic Product of the Quaternions__

## Introduction

The antisymmetrisation of the quaternionic product is
$$
\tilde q_1\wedge_{\natural}\tilde q_2=\tfrac12\bigl(\tilde q_1^{\natural}\tilde q_2-\tilde q_2^{\natural}\tilde q_1\bigr)=q_{1t}\vec q_2-q_{2t}\vec q_1-\vec q_1\times\vec q_2 .
$$
It is alternating and purely vector valued, and it is not a Lie bracket. On the vector subspace it agrees, up to sign, with the cross product and satisfies the Jacobi identity; on the whole algebra the identity fails, with a defect of dimension three carried by the scalar parts, in a way that is sharper than the complex case: here the defect is a pure quaternion and it sweeps all three vector directions.

The article is the real mirror of [The Lie Structure of the Antisymmetric Quaternionic Product](the-lie-structure-of-the-antisymmetric-quaternionic-product.html), with one point of difference, stated in the section of the failure: the biquaternion article attributes the failure to the scalar part, and over $\mathbb{R}$ the scalar parts are the coefficients of the defect and not its values.

The parent is [The General Quaternionic Bilinear Product of the Quaternions](the-general-quaternionic-bilinear-product-of-the-quaternions.html); the bracket as a multiplication is [Introduction to the Antisymmetric Quaternionic Algebra of the Quaternions](introduction-to-the-antisymmetric-quaternionic-algebra.html), cited and not restated. The other half is [The Jordan Structure of the Symmetric Quaternionic Product of the Quaternions](the-jordan-structure-of-the-symmetric-quaternionic-product-of-the-quaternions.html), and the bracket that works is [The Lie Structure of the Antisymmetric Plain Product of the Quaternions](the-lie-structure-of-the-antisymmetric-plain-product-of-the-quaternions.html).

## The Bracket

**Definition.** The **antisymmetric quaternionic product** is
$$
\tilde q_1\wedge_{\natural}\tilde q_2=\tfrac12\bigl(\tilde q_1^{\natural}\tilde q_2-\tilde q_2^{\natural}\tilde q_1\bigr).
$$

**Theorem (the closed form).** With $a=q_{1t}$, $b=q_{2t}$, $\vec u=\vec q_1$, $\vec v=\vec q_2$,
$$
\boxed{\;\tilde q_1\wedge_{\natural}\tilde q_2=a\vec v-b\vec u-\vec u\times\vec v\;}
$$
a pure quaternion.

*Proof.* In the quaternionic product the scalar row is symmetric and the vector part is antisymmetric; the half-difference removes the scalar row and keeps the vector part, which is $a\vec v-b\vec u-\vec u\times\vec v$. Equivalently, the transposed product $\tilde q_2^{\natural}\tilde q_1$ is the conjugate of $\tilde q_1^{\natural}\tilde q_2$, so the half-difference is the vector part of the product, and the scalar part is removed by the conjugation. Verified exactly on the sixteen pairs of the basis and on general elements.

**Remark (the bracket is not a commutator of an associative product).** The bracket of the plain product is half the commutator of the parent. This bracket is not of that form: if it were, the Jacobi identity would hold. It is the vector part of the quaternionic product, which is the object obtained by reflecting the first factor before multiplying; the reflection is what destroys the commutator structure.

## Purity and Alternation

**Proposition (alternation).** For every $\tilde q$ and all $\tilde q_1,\tilde q_2$,
$$
\tilde q\wedge_{\natural}\tilde q=0,\qquad
\tilde q_1\wedge_{\natural}\tilde q_2+\tilde q_2\wedge_{\natural}\tilde q_1=0,\qquad
\mathrm{Sc}\bigl(\tilde q_1\wedge_{\natural}\tilde q_2\bigr)=0 .
$$

*Proof.* In the closed form the first is $a\vec u-a\vec u-\vec u\times\vec u=0$; the second is the antisymmetry of the three terms; the third is the purity. Verified exactly on the basis.

**Corollary (the bracket is degenerate on the algebra).** Every square vanishes:
$$
\tilde q\wedge_{\natural}\tilde q=0\ \ \text{for every }\tilde q .
$$
In particular the algebra has no non-zero element whose bracket with itself is non-zero, and no element acts as a derivation of itself.

*Proof.* The first proposition. This is the sharpest formal difference from the bracket of the plain product, where the square is zero too, and it matters below: an alternating product has no powers, so no exponential series can be formed from it.

## The Jacobi Identity on the Vector Subspace

**Theorem (the pure part is a Lie algebra).** For $\tilde q_1,\tilde q_2,\tilde q_3$ pure,
$$
\tilde q_1\wedge_{\natural}\bigl(\tilde q_2\wedge_{\natural}\tilde q_3\bigr)+\tilde q_2\wedge_{\natural}\bigl(\tilde q_3\wedge_{\natural}\tilde q_1\bigr)+\tilde q_3\wedge_{\natural}\bigl(\tilde q_1\wedge_{\natural}\tilde q_2\bigr)=0 .
$$

*Proof.* For pure arguments the bracket is $-\vec u\times\vec v$, and the identity becomes the Jacobi identity of the cross product with the sign $(-1)^3=-1$ in front. Verified on all $64$ triples of the basis and on general pure triples with a residual of zero.

**Corollary (the isomorphism).** The map $\vec u\mapsto-\mathrm{ad}_{\vec u}$, where the adjoint is taken in the bracket $\wedge_{\natural}$, is an isomorphism of $(V,\wedge_{\natural})$ onto $\mathfrak{so}(3)$.

*Proof.* On $V$ the adjoint is $\vec v\mapsto-\vec u\times\vec v$, so the map is $\vec u\mapsto[\vec u]_\times$, which is the isomorphism of the plain case; and $[-\mathrm{ad}_{\vec u},-\mathrm{ad}_{\vec v}]=\mathrm{ad}_{\vec u\times\vec v}=-\mathrm{ad}_{-\vec u\times\vec v}$, which is the bracket of the two images. Verified by the matrices of the two adjoints.

**Remark (the sign and the orientation).** The bracket on $V$ is the negative of the cross product, so the isomorphism with $\mathfrak{so}(3)$ involves a sign and the orientations of the two sides are opposite. The sign is the trace of the reflection in the first slot, and it is the only trace of the parent that survives the restriction to the pure part.

## The Failure on the Whole Algebra

**Theorem (the defect in closed form).** For all $\tilde q_1,\tilde q_2,\tilde q_3$,
$$
\boxed{\;\mathrm{Jac}(\tilde q_1,\tilde q_2,\tilde q_3)=q_{1t}\,\vec q_2\times\vec q_3+q_{2t}\,\vec q_3\times\vec q_1+q_{3t}\,\vec q_1\times\vec q_2\;}
$$
a pure quaternion whose three vector coordinates are independent.

*Proof.* Each bracket in the sum is computed on the basis, where the identity is a check of $48$ triples with entries in $\{0,\pm1\}$; on general elements the identity is trilinear, so the check on the basis suffices, and it was repeated on random triples with a residual at the level of the arithmetic. The formula is the same as the complex one with the real scalar parts in the coefficients.

**Corollary (the defect has span three).** The values of the defect are
$$
\mathrm{Jac}(e_t,\vec e_x,\vec e_y)=\vec e_z,\qquad
\mathrm{Jac}(\vec e_x,e_t,\vec e_y)=-\vec e_z,\qquad
\mathrm{Jac}(\vec e_x,\vec e_y,e_t)=\vec e_z,\qquad
\mathrm{Jac}(\vec e_x,\vec e_y,\vec e_z)=0 ,
$$
and they span the whole vector subspace.

*Proof.* The three first triples give $\pm\vec e_z$; the cyclic permutations of $(\vec e_x,\vec e_y,\vec e_z)$ with $e_t$ in the three places give $\pm\vec e_x$ and $\pm\vec e_y$ by the same computation, so the span is three-dimensional. The last triple is pure, and the pure part is a Lie algebra. Computed exactly.

**Remark (the trap of the complex reading).** The biquaternion article attributes the failure of the Jacobi identity to the scalar part. Over $\mathbb{R}$ the failure has a different shape: the defect is a pure quaternion, its span is the three-dimensional vector subspace, and the scalar parts $q_{1t},q_{2t},q_{3t}$ are the coefficients that carry the failure and not the values it takes. **The defect lives in the vector directions and is carried by the scalar coefficients.** The difference is the difference between a defect that lies in a line and a defect that sweeps a three-space, and it is the same difference that separates a null direction from a null cone.

**Remark (the failure is not repairable).** No change of the bracket by adding a symmetric term can produce a Lie algebra on the whole space, because a Lie bracket on $\mathbb{H}$ whose restriction to $V$ is $-\times$ and which vanishes on $e_t$ in both slots is forced by bilinearity and alternation to be this one, and this one fails. The failure is therefore a property of the pairing and not of the presentation: within the batch of the two general products, the only antisymmetrisation that is a Lie bracket is the one of the plain product.

## The Left Multiplication by the Unit

**Proposition (the projection).** In the bracket $\wedge_{\natural}$,
$$
L_{e_t}\tilde q=e_t\wedge_{\natural}\tilde q=\vec q ,\qquad
\tilde q\wedge_{\natural}e_t=-\vec q ,
$$
so the left multiplication by the unit is the projection onto the vector subspace and the right multiplication is its negative.

*Proof.* The closed form with $a=1$, $\vec u=0$ gives $\vec q$; the antisymmetry gives the second. Verified in the coefficient basis.

**Corollary (the splitting is not a Lie splitting).** The map $L_{e_t}$ is idempotent, with eigenvalues $1,1,1,0$, and its kernel is the real line; but it is not a homomorphism of the bracket, since $L_{e_t}(\tilde q_1\wedge_{\natural}\tilde q_2)$ has no reason to vanish while $L_{e_t}\tilde q_1\wedge_{\natural}L_{e_t}\tilde q_2$ does not.

*Proof.* The eigenvalues are read in the basis. For the failure, at $\tilde q_1=e_t$ and $\tilde q_2=\vec e_x$: the left side is $L_{e_t}\vec e_x=\vec e_x$ and the right side is $0\wedge_{\natural}0=0$. Computed exactly.

## The Ideals and the Radical

**Proposition (the ideals).** The subspaces invariant under both adjoints are $0$, the vector subspace and the whole algebra.

*Proof.* A subspace $W$ is an ideal when $\mathrm{ad}_{\tilde q}W\subseteq W$ for all $\tilde q$. The adjoint of $e_t$ is the projection onto $V$, so an ideal containing a non-vector element contains $V$; and the adjoints of the vector units act on $V$ by $-\times$, which has no invariant line. Hence the three spaces. Verified by solving the invariance conditions on the coordinate subspaces of the basis.

**Proposition (the radical is zero).** The radical, the largest solvable ideal, is $\{0\}$.

*Proof.* The ideals are $0$, $V$ and $\mathbb{H}$. On $V$ the bracket is $-\times$, so $[V,V]=V$ and $V$ is perfect, hence not solvable; and $[\mathbb{H},\mathbb{H}]=V$, so the derived series of $\mathbb{H}$ is $\mathbb{H}\supset V\supset V\supset\cdots$ and never reaches zero. No non-zero ideal is solvable. Verified by computing the dimensions of the derived algebras on the basis.

**Remark (the formula that presupposes Jacobi).** In a Lie algebra the radical is the orthogonal complement of the derived algebra for the Killing form. Here that complement is $V^{\perp}=\mathbb{R}e_t$, and the real line is not an ideal, since $[e_t,\vec e_x]=\vec e_x$. The formula fails, and it fails because its proof uses the Jacobi identity. **The algebra has radical zero and a non-degenerate Killing form, and it is not a Lie algebra: both of the standard certificates are false witnesses when the identity fails.**

**Remark (the extension and its obstruction).** The algebra is an extension of the real line by the perfect algebra $V$,
$$
0\longrightarrow V\longrightarrow\mathbb{H}\longrightarrow\mathbb{R}\longrightarrow0 ,
$$
and the extension does not split as a direct sum of Lie algebras: the real line is not an ideal, as the remark above shows. **The Jacobi defect is the obstruction to the splitting, and the defect is three-dimensional because the vector subspace it would have to split off is three-dimensional.** In the plain case the extension is a direct sum, and the difference between the two columns is the Jacobi defect.

## The Killing Form

**Theorem (the Killing form).** With $\kappa(\tilde q_1,\tilde q_2)=\mathrm{tr}(\mathrm{ad}_{\tilde q_1}\mathrm{ad}_{\tilde q_2})$,
$$
\kappa(\tilde q_1,\tilde q_2)=3q_{1t}q_{2t}-2(\vec q_1,\vec q_2),
$$
of matrix $\mathrm{diag}(3,-2,-2,-2)$ in the basis, of signature $(1,3)$ and rank four.

*Proof.* $\mathrm{ad}_{e_t}$ is the projection onto $V$ and $\mathrm{ad}_{\vec u}$ is $\vec v\mapsto-\vec u\times\vec v$ plus a term in the real line; the products are computed in the coefficient basis, entry by entry. The trace of $\mathrm{ad}_{e_t}^2$ is the trace of the projection, which is $3$; the trace of $\mathrm{ad}_{\vec e_x}^2$ is $-2$, by the same computation as in the plain case. Verified in the basis and on random pairs.

**Corollary (the form is non-degenerate).** The radical of the Killing form is $\{0\}$; the form is indefinite of signature $(1,3)$, positive on the real line and negative on the vector subspace.

*Proof.* The displayed matrix has no kernel and its eigenvalues are $3,-2,-2,-2$. This is the sharpest contrast with the plain bracket, whose Killing form is degenerate on exactly the line that carries the positive direction here.

**Remark (the two forms of the same algebra).** The trace form of the bracket product vanishes, as it does for every alternating product, and the form that lives on the space is the Killing form. **The algebra therefore carries a non-degenerate invariant form of signature $(1,3)$ and is not a Lie algebra: a non-degenerate Killing form is not a certificate of the Jacobi identity, and here it is the form of a bracket that fails.** The form is the one of the four-dimensional Minkowski space, and it is the form that the article of the P norm studies under another name.

## The Absent Exponential

**Proposition (no exponential, for three reasons).** There is no exponential map attached to the bracket $\wedge_{\natural}$.

*Proof.* First, the bracket is not a Lie bracket, so no Lie group has it as its Lie algebra, by the theorem of Lie. Second, every square vanishes, so the formal series $\sum_n\tilde q^{\wedge_{\natural}n}/n!$ truncates at $e_t+\tilde q$ for every $\tilde q$, and the truncated map is not a group law: under the plain product, $(e_t+\tilde q_1)(e_t+\tilde q_2)$ carries the extra term $\tilde q_1\tilde q_2$. Third, the only flow that exists is the restriction to the vector subspace, where the bracket is $-\times$ and the flow is the rotation by $-t$ about $\vec u$.

**Remark (what survives).** What survives is the rotation on the pure part: for a unit $\vec u$ the map $\tilde q\mapsto$ the exponential of $t\,\mathrm{ad}_{\vec u}$ on $V$ is the rotation of angle $-t$, exactly as in the plain case with the opposite sign, and it fixes the real line. The rotor of the plain case has no counterpart here, because the versor product is not the exponential of this bracket. The whole of the group theory of the algebra belongs to the plain column, and the article [The Quaternion Versors and the Unitary Group](the-quaternion-versors-and-the-unitary-group.html) reads it there.

## The Four Brackets

Over $\mathbb{R}$ there are two general products, hence two antisymmetrisations, and the two transposed products give their negatives: the four brackets of the batch are $\pm\wedge$ and $\pm\wedge_{\natural}$.

| | $\wedge$ | $-\wedge$ | $\wedge_{\natural}$ | $-\wedge_{\natural}$ |
|---|---|---|---|---|
| alternating | yes | yes | yes | yes |
| Jacobi identity | yes | yes | no | no |
| image | $V$ | $V$ | $V$ | $V$ |
| kernel of $L_{e_t}$ | $\mathbb{H}$ | $\mathbb{H}$ | $\mathbb{R}e_t$ | $\mathbb{R}e_t$ |
| defect span | $0$ | $0$ | $3$ | $3$ |
| Killing signature | $(0,3)$ | $(0,3)$ | $(1,3)$ | $(1,3)$ |

**Remark (the sign never repairs).** The table is the exact statement that the antisymmetrisation is a property of the slot pairing and not of the order of the two slots. The sign of the bracket changes nothing: the defect of $-\wedge_{\natural}$ is the negative of the defect of $\wedge_{\natural}$, its span is the same, and the Killing form, being quadratic in the adjoint, is unchanged. **Two of the four brackets are Lie brackets and two are not, and the pair that is not is exactly the pair built from the quaternionic product.**

## Summary

The antisymmetric quaternionic product is
$$
\tilde q_1\wedge_{\natural}\tilde q_2=q_{1t}\vec q_2-q_{2t}\vec q_1-\vec q_1\times\vec q_2 ,
$$
alternating, purely vector valued, and not the commutator of an associative product.

On the vector subspace it is $-\vec u\times\vec v$, it satisfies the Jacobi identity there, and $(V,\wedge_{\natural})\cong\mathfrak{so}(3)$ with the opposite orientation. On the whole algebra the identity fails, with the defect $q_{1t}\vec q_2\times\vec q_3+q_{2t}\vec q_3\times\vec q_1+q_{3t}\vec q_1\times\vec q_2$, whose span is the whole vector subspace: the scalar parts are the coefficients of the defect and not its values, which is the point where the real case differs from the complex one.

The left multiplication by the unit is the projection onto the vector subspace, and the right multiplication is its negative. The ideals are $0$, $V$ and $\mathbb{H}$, and the radical is $V$, so the algebra is a non-split abelian extension of $\mathfrak{so}(3)$ by the real line.

The Killing form is $3q_{1t}q_{2t}-2(\vec q_1,\vec q_2)$, of signature $(1,3)$ and non-degenerate, and it certifies nothing about the Jacobi identity. The exponential is absent: the squares vanish, the series truncates, and only the rotation on the pure part survives.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | the quaternion algebra |
| $\tilde q=q_te_t+\vec q$ | the element, its scalar part and its vector part |
| $\tilde q_1\wedge_{\natural}\tilde q_2$ | the antisymmetric quaternionic product |
| $\mathrm{Jac}$ | the Jacobi defect, the sum of the three cyclic terms |
| $\mathrm{ad}_{\tilde q}$ | the bracket with $\tilde q$ |
| $\kappa$ | the Killing form |
| $L_{e_t}$ | the left multiplication by the unit |

## Further Reading

- [Introduction to the Antisymmetric Quaternionic Algebra of the Quaternions](introduction-to-the-antisymmetric-quaternionic-algebra.html), for the bracket as a multiplication.
- [The General Quaternionic Bilinear Product of the Quaternions](the-general-quaternionic-bilinear-product-of-the-quaternions.html), for the parent product.
- [The Lie Structure of the Antisymmetric Quaternionic Product](the-lie-structure-of-the-antisymmetric-quaternionic-product.html), for the biquaternion counterpart and its attribution of the failure.
- [The Lie Structure of the Antisymmetric Plain Product of the Quaternions](the-lie-structure-of-the-antisymmetric-plain-product-of-the-quaternions.html), for the bracket that is a Lie algebra.
- [The Jordan Structure of the Symmetric Quaternionic Product of the Quaternions](the-jordan-structure-of-the-symmetric-quaternionic-product-of-the-quaternions.html), for the other half, which fails the Jordan identity by one dimension.
