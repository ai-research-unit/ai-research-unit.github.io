# __The Jordan Structure of the Symmetric Plain Sesquilinear Product__

## Introduction

The symmetrisation of $\tilde Q_1\tilde Q_2^{*}$ is $\tilde Q_1\bullet_{*}\tilde Q_2=H(\tilde Q_1,\tilde Q_2)e_t$, the second of the two central products of the batch and the only one whose defining form is positive definite. It is conjugate-commutative, it has no unit, and it fails the Jordan identity by a defect of one dimension. Its cone of squares is a ray, and the ray is the whole of what the algebra can see: the squares of all elements, not only of the Hermitian ones, lie on it, and no element of the algebra has a square that leaves it.

This article reads the Jordan structure of the algebra: the symmetrisation, the identity and its failure, the defect in closed form, the cone of squares, the Peirce theory, the operators, and the row of the algebra in the comparison of the four symmetrisations.

The setting is [The General Plain Sesquilinear Product](the-general-plain-sesquilinear-product.html), whose second half is this product. The companion articles are [The Jordan Structure of the Symmetric Quaternionic Product](the-jordan-structure-of-the-symmetric-quaternionic-product.html), which is the indefinite central case, and [The Jordan Structure of the Symmetric Plain Product](the-jordan-structure-of-the-symmetric-plain-product.html), which is the unital case. The forms are [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), and the positive cone is [Hermitian Squares and the Algebraic Positive Cone](hermitian-squares-and-the-algebraic-positive-cone.html).

## The Symmetrisation

**Definition.** The **symmetric plain sesquilinear product** is
$$
\tilde Q_1\bullet_{*}\tilde Q_2=\tfrac12\bigl(\tilde Q_1\tilde Q_2^{*}+\overline{\tilde Q_2\tilde Q_1^{*}}\bigr).
$$

**Theorem (the product is a Hermitian form).** For all $\tilde Q_1,\tilde Q_2$,
$$
\boxed{\;\tilde Q_1\bullet_{*}\tilde Q_2=\bigl(Q_{1t}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})\bigr)e_t=H(\tilde Q_1,\tilde Q_2)e_t\;}
$$

*Proof.* In the general plain sesquilinear product the scalar row is $Q_{1t}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})$, which is Hermitian in the pair, and the vector part is $Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2}$, which changes sign under the exchange with conjugation. The scalar row survives and the vector part cancels. Verified exactly on the basis and on general elements.

**Corollary (the elementary properties).** The product is conjugate-commutative, $\tilde Q_1\bullet_{*}\tilde Q_2=\overline{\tilde Q_2\bullet_{*}\tilde Q_1}$; its image is the centre, of complex dimension $1$; it has no unit; and every square is a nonnegative multiple of $e_t$.

*Proof.* The first three items as in the quaternionic case, with $H$ in place of $\langle\cdot,\cdot\rangle_{\natural}$. For the square, $\tilde Q\bullet_{*}\tilde Q=H(\tilde Q,\tilde Q)e_t$ and $H(\tilde Q,\tilde Q)=\lvert Q_t\rvert^2+\lvert\vec Q\rvert^2\geq0$, with equality only at $\tilde Q=0$.

**Remark (the two central products are one product and a bar).** The two central symmetrisations are related by
$$
\tilde Q_1\bullet_{*}\tilde Q_2=\tilde Q_1\bullet_{\natural}\overline{\tilde Q_2},
$$
verified exactly on the basis. The whole Jordan theory of this article is therefore the theory of the quaternionic central product with the second argument barred, and the bar is what makes the difference: it turns the indefinite symmetric form $\langle\cdot,\cdot\rangle_{\natural}$ into the definite Hermitian form $H$, the isotropic cone into a point, and the improper cone of squares into a ray.

**Remark (the conjugation is not commutativity).** The product is not commutative: with $\tilde Q_1=e_t$ and $\tilde Q_2=i e_t$ the value is $-ie_t$ and the value at the reversed order is $+ie_t$. What holds is the conjugate-commutativity, and it is the correct symmetry for a product whose values are Hermitian forms: the pair is ordered up to conjugation.

## The Jordan Identity

**Theorem (the identity fails).** There are $\tilde Q_1,\tilde Q_2$ with
$$
\tilde Q_1^2\bullet_{*}\bigl(\tilde Q_2\bullet_{*}\tilde Q_1\bigr)\neq\bigl(\tilde Q_1^2\bullet_{*}\tilde Q_2\bigr)\bullet_{*}\tilde Q_1 .
$$

*Proof.* Take $\tilde Q_1=\tilde Q_2=\vec e_x$. Then $\tilde Q_1^2=H(\vec e_x,\vec e_x)e_t=e_t$, and the left side is $e_t\bullet_{*}e_t=e_t$; the right side is $(e_t\bullet_{*}\vec e_x)\bullet_{*}\vec e_x=0\bullet_{*}\vec e_x=0$. Computed exactly.

**Proposition (the two cases of vanishing).** The defect vanishes when the vector parts are orthogonal for $H$ and the scalar part of the first argument is real, and it does not vanish otherwise.

*Proof.* The defect is computed in the next section; the formula is $\lVert\tilde Q_1\rVert^{2}\bigl((\vec Q_1,\overline{\vec Q_2})+2i\operatorname{Im}(Q_{1t})\overline{Q_{2t}}\bigr)e_t$, which vanishes exactly on those two conditions together. Verified on general elements.

**Remark (the bar in the identity).** The Jordan identity is written with the product in the same order on both sides. For a conjugate-commutative product the two sides differ by the conjugation of one factor, and that difference is the source of the failure: the identity is a statement about a commutative product, and a conjugate-commutative product satisfies it only when its values are fixed by the conjugation, which for a central product means that the second factor is real.

## The Defect

**Theorem (the defect in closed form).** For all $\tilde Q_1,\tilde Q_2$,
$$
\boxed{\;D(\tilde Q_1,\tilde Q_2)=\tilde Q_1^2\bullet_{*}\bigl(\tilde Q_2\bullet_{*}\tilde Q_1\bigr)-\bigl(\tilde Q_1^2\bullet_{*}\tilde Q_2\bigr)\bullet_{*}\tilde Q_1=\lVert\tilde Q_1\rVert^{2}\Bigl((\vec Q_1,\overline{\vec Q_2})+2i\operatorname{Im}(Q_{1t})\overline{Q_{2t}}\Bigr)e_t\;}
$$

*Proof.* Write $c=\lVert\tilde Q_1\rVert^{2}=H(\tilde Q_1,\tilde Q_1)$, a nonnegative real number, so that $\tilde Q_1^2=ce_t$. Then $\tilde Q_2\bullet_{*}\tilde Q_1=\overline{H(\tilde Q_1,\tilde Q_2)}e_t$, and $e_t\bullet_{*}\beta e_t=\overline{\beta}e_t$, so the left term is $cH(\tilde Q_1,\tilde Q_2)e_t$. On the right, $\tilde Q_1^2\bullet_{*}\tilde Q_2=c\overline{Q_{2t}}e_t$, and its product with $\tilde Q_1$ is $c\overline{Q_{2t}}\overline{Q_{1t}}e_t$. The difference is $c\bigl(H(\tilde Q_1,\tilde Q_2)-\overline{Q_{1t}}\,\overline{Q_{2t}}\bigr)e_t$, and $H(\tilde Q_1,\tilde Q_2)=Q_{1t}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})$, so the bracket is $(\vec Q_1,\overline{\vec Q_2})+(\overline{Q_{1t}}-Q_{1t})\overline{Q_{2t}}$, which is the display. Verified on general elements, deviation at the level of the arithmetic.

**Corollary (the defect is one-dimensional).** The image of $D$ is the centre, spanned by $e_t$.

*Proof.* Every value is a multiple of $e_t$, and the value at $\tilde Q_1=\tilde Q_2=\vec e_x$ is $e_t$.

**Remark (the second term).** The defect has two terms and they are of different natures. The first, $(\vec Q_1,\overline{\vec Q_2})e_t$, is the one that survives on the real subspace, and it is the analogue of the defect of the quaternionic central product. The second, $2i\operatorname{Im}(Q_{1t})\overline{Q_{2t}}e_t$, is pure imaginary and needs a genuinely complex scalar part in the first argument; it has no analogue in the quaternionic case, where the scalar part enters only through $Q_{1t}Q_{2t}$ and the failure is $\langle\vec Q_1,\vec Q_2\rangle Q_{1t}$ with no imaginary part. The comparison of the two formulas is the exact content of the bar.

**Remark (the reason the defect is small).** The defect is one-dimensional for the same structural reason as in the quaternionic case: the product is central, its Peirce spaces multiply into the centre, and the identity can fail only in the centre. The three nonzero defects of the batch are $1$, $1$ and $4$, and the two ones belong to the two central products.

## The Cone of Squares

**Proposition (the squares of all elements).** For every $\tilde Q$,
$$
\tilde Q\bullet_{*}\tilde Q=\lVert\tilde Q\rVert^{2}e_t,\qquad \lVert\tilde Q\rVert^{2}=\lvert Q_t\rvert^2+\lvert\vec Q\rvert^2\geq0,
$$
with equality only at $\tilde Q=0$. The cone of squares is the ray $\mathbb{R}_{\geq0}e_t$.

*Proof.* The norm is positive definite by the display, so the diagonal map takes $\mathbb{B}$ onto the ray and $0$ only onto $0$. The cone generated by the values is the ray.

**Remark (a proper cone, and the smallest one).** The ray is closed, pointed, proper, and it has empty interior in $\mathbb{B}$; in the Hermitian subspace it is the ray of the positive multiples of $e_t$, which is the intersection of that subspace with the ray. The algebra is the only one of the four whose cone of squares is a ray, and it is also the only one whose norm is definite: the two facts are the same fact.

**Remark (no isotropic elements).** The algebra has no element with a square equal to zero, and therefore no absolute zero divisor. The statement is stronger than the vanishing of the isotropic cone of $H$: it says that the diagonal map is injective on the ray, and it is the algebraic form of the definiteness of the form. The nilpotents of the algebra, which exist, are all of index three or more; they are read in [The Square Roots of Zero and the Nilpotents of the Biquaternion Algebra](the-square-roots-of-zero-and-the-nilpotents-of-the-biquaternion-algebra.html).

**Remark (the comparison of the four cones).** The four cones of squares are the Lorentz cone for the symmetric plain product, the ray for this product, and the whole line for the two remaining ones. The two proper cones are therefore of different kinds: one is full-dimensional in the Hermitian subspace and the other is a ray, and the difference is the difference between a form of inertia $(3,1)$ and a definite form.

## The Peirce Theory

**Proposition (the idempotents).** The idempotents are $0$ and $e_t$.

*Proof.* The equation reads $\lVert\tilde\Pi_{\mathrm{id}}\rVert^{2}e_t=\tilde\Pi_{\mathrm{id}}$, so $\tilde\Pi_{\mathrm{id}}=\lambda e_t$ with $\lvert\lambda\rvert^2=\lambda$, that is $\lambda\in\{0,1\}$. Verified by solving the conditions in the coefficient basis.

**Theorem (the Peirce decomposition).** At $e_t$ the multiplication operator has the eigenvalues $1,0,0,0$, with
$$
\mathbb{B}_{1}=\mathbb{C}e_t,\qquad \mathbb{B}_{0}=\mathbb{B}_{V}=\mathbb{C}\vec e_x\oplus\mathbb{C}\vec e_y\oplus\mathbb{C}\vec e_z .
$$

*Proof.* $L(e_t)\tilde Q=H(e_t,\tilde Q)e_t=\overline{Q_t}e_t$, whose matrix has rank one and the spectrum displayed. The kernel is the set of elements with zero scalar part, that is the vector subspace. Computed exactly.

**Proposition (the Peirce rules, one of which fails).** With the two spaces as above,
$$
\mathbb{B}_{1}\bullet_{*}\mathbb{B}_{1}\subset\mathbb{B}_{1},\qquad
\mathbb{B}_{1}\bullet_{*}\mathbb{B}_{0}=0,\qquad
\mathbb{B}_{0}\bullet_{*}\mathbb{B}_{0}\subset\mathbb{B}_{1}.
$$

*Proof.* $e_t\bullet_{*}e_t=e_t$; $e_t\bullet_{*}\vec e_x=H(e_t,\vec e_x)e_t=0$; $\vec e_x\bullet_{*}\vec e_y=\delta_{xy}e_t$. Verified on the basis of the two spaces.

**Remark (the two three-dimensional subspaces).** The Peirce space $\mathbb{B}_0$ is the vector subspace, the set of elements with zero scalar part. It is not the anti-Hermitian subspace $\mathbb{B}_{\Phi}$, which is the set of the elements $i\vec s$ with $\vec s$ real. The first is a complex subspace of complex dimension three; the second is a real subspace of real dimension three, contained in the first, and it is not a complex subspace at all. The Peirce theory of a central product selects the first, and the quadratic theory of the forms selects the second. The distinction matters for every statement about cones, because the cone of squares lives in $\mathbb{B}_{\Psi}$ and the Peirce spaces live in $\mathbb{B}$.

**Remark (the same failure as the identity's).** The third inclusion violates the classical rule and is exactly the failure of the Jordan identity. The two central products have the same Peirce pattern, the same spectrum at the unit, the same failed rule and the same defect dimension; they differ in the sign inside the defect and in the definiteness of the form. The Peirce theory of the algebra as a whole is [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html).

## The Operators

**Definition.** $L(\tilde Q_1)\tilde Q_2=\tilde Q_1\bullet_{*}\tilde Q_2$ and $U(\tilde Q_1)=2L(\tilde Q_1)^2-L(\tilde Q_1^2)$.

**Proposition (rank one).** For $\tilde Q_1\neq0$, $L(\tilde Q_1)$ has rank one, image $\mathbb{C}e_t$ and kernel the $H$-orthogonal hyperplane of $\tilde Q_1$.

*Proof.* The values are $H(\tilde Q_1,\tilde Q_2)e_t$, and the kernel is the set where the form vanishes. Verified by the singular values in the coefficient basis.

**Theorem (the quadratic representation).** For all $\tilde Q_1,\tilde Q_2$,
$$
U(\tilde Q_1)\tilde Q_2=\Bigl(2Q_{1t}\overline{H(\tilde Q_1,\tilde Q_2)}-\lVert\tilde Q_1\rVert^{2}\overline{Q_{2t}}\Bigr)e_t .
$$

*Proof.* $L(\tilde Q_1)^2\tilde Q_2=H\bigl(\tilde Q_1,H(\tilde Q_1,\tilde Q_2)e_t\bigr)e_t=Q_{1t}\overline{H(\tilde Q_1,\tilde Q_2)}e_t$, and $L(\tilde Q_1^2)\tilde Q_2=\lVert\tilde Q_1\rVert^{2}\overline{Q_{2t}}e_t$. Twice the first minus the second. Verified on general elements.

**Corollary (the quadratic identity fails).** $U(\tilde Q_1)U(\tilde Q_2)U(\tilde Q_1)\neq U(U(\tilde Q_1)\tilde Q_2)$ in general.

*Proof.* The two sides are computed from the closed form; the left is of degree five in the coordinates and the right of degree three, so they cannot agree on an open set. The deviation on random pairs is of order $10^2$.

**Remark (the operator norm).** The form $H$ is positive definite, so the multiplication operators have a norm, and the norm of $L(\tilde Q_1)$ is $\lVert\tilde Q_1\rVert$, attained at $\tilde Q_2=\tilde Q_1$. The inequality is Cauchy–Schwarz applied to $\lvert H(\tilde Q_1,\tilde Q_2)\rvert$, and the equality is $\lVert L(\tilde Q_1)\tilde Q_1\rVert=\lVert\tilde Q_1\rVert^{3}=\lVert\tilde Q_1\rVert\cdot\lVert\tilde Q_1\rVert$. Verified numerically, with the supremum approached from below and reached at the diagonal.

**Remark (no Euclidean structure).** The algebra is not a Euclidean Jordan algebra: it has no unit, and the multiplication operators are not self-adjoint for any positive definite form that makes the product a Jordan product, since $L(\tilde Q_1)$ has rank one and its adjoint would have to have rank one as well while the product is not symmetric. What it has instead is a definite form, a proper cone and a rank-one multiplication everywhere, which is the pair of properties of a Euclidean Jordan algebra that survive without a unit.

## The Place among the Four

| | this algebra | $\bullet$ | $\bullet_{\natural}$ | $\bullet_{\natural*}$ |
|---|---|---|---|---|
| image | $1$ | $4$ | $1$ | $4$ |
| unit | none | $e_t$ | none | none |
| symmetry | conjugate-commutative | commutative | commutative | conjugate-commutative |
| Jordan identity | no | yes | no | no |
| defect | $1$ | $0$ | $1$ | $4$ |
| cone of squares | $\mathbb{R}_{\geq0}e_t$ | $t\geq\lvert\vec s\rvert$ | $\mathbb{R}e_t$ | $\mathbb{R}e_t$ |
| index-$2$ nilpotents | none | none | the isotropes of $N$ | the isotropes of $K$ |
| spectrum of $L(e_t)$ | $1,0,0,0$ | $1,1,1,1$ | $1,0,0,0$ | $1,-1,-1,-1$ |

**Remark (the column with a definite form).** This is the only column of the batch whose defining form is definite, and the definiteness shows in three places at once: the cone of squares is a ray and not a line, there are no isotropic elements, and the defect has no term that grows with the imaginary part of the scalar part alone. The algebra fails the Jordan identity, and the failure is one-dimensional; the column therefore does not repair the loss of the identity, it only removes the indefiniteness. The column that carries a norm, an order and a cone is the plain one, which is the Jordan algebra $H_2(\mathbb{C})\cong JSpin_3$ of [The Biquaternion Algebra as a JB-Algebra](the-biquaternion-algebra-as-a-jb-algebra.html); the definiteness recorded here is a property of a form and it is not the positivity of an order, and the two are distinguished there.

## Summary

The symmetric plain sesquilinear product is $\tilde Q_1\bullet_{*}\tilde Q_2=H(\tilde Q_1,\tilde Q_2)e_t=[Q_{1t}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})]e_t$. It is conjugate-commutative and not commutative, its image is the centre, and it has no unit. It is the quaternionic central product with the second argument barred.

It fails the Jordan identity with the defect $D(\tilde Q_1,\tilde Q_2)=\lVert\tilde Q_1\rVert^{2}\bigl((\vec Q_1,\overline{\vec Q_2})+2i\operatorname{Im}(Q_{1t})\overline{Q_{2t}}\bigr)e_t$, of image the centre and dimension one. The two terms of the defect separate the real and the imaginary contributions, and the second has no analogue in the quaternionic case.

The squares are $\lVert\tilde Q\rVert^{2}e_t$ with the norm positive definite, so the cone of squares is the ray $\mathbb{R}_{\geq0}e_t$ and the algebra has no absolute zero divisor. The idempotents are $0$ and $e_t$, the Peirce spaces are the centre and the vector subspace, and the third Peirce rule fails, as in the quaternionic case.

The multiplication operators have rank one and the quadratic representation is $U(\tilde Q_1)\tilde Q_2=\bigl(2Q_{1t}\overline{H(\tilde Q_1,\tilde Q_2)}-\lVert\tilde Q_1\rVert^{2}\overline{Q_{2t}}\bigr)e_t$, and the quadratic identity fails.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra |
| $\tilde Q=Q_te_t+\vec Q$ | the element, its scalar part and its vector part |
| $\tilde Q_1\bullet_{*}\tilde Q_2$ | the symmetric plain sesquilinear product |
| $H(\tilde Q_1,\tilde Q_2)=Q_{1t}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})$ | the positive definite Hermitian form |
| $\lVert\tilde Q\rVert^{2}=H(\tilde Q,\tilde Q)$ | the norm of the form |
| $L(\tilde Q_1)$, $U(\tilde Q_1)$ | the multiplication operator and the quadratic representation |
| $D(\tilde Q_1,\tilde Q_2)$ | the Jordan defect |
| $\mathbb{B}_{C}$, $\mathbb{B}_{V}$ | the centre and the vector subspace |
| $\mathbb{B}_{\Psi}$ | the Hermitian subspace |
| $\mathbb{B}_{1},\mathbb{B}_{0}$ | the Peirce spaces at $e_t$ |

## Further Reading

- [The General Plain Sesquilinear Product](the-general-plain-sesquilinear-product.html), for the product of which this is the symmetrisation.
- [The Jordan Structure of the Symmetric Quaternionic Product](the-jordan-structure-of-the-symmetric-quaternionic-product.html), for the companion central product.
- [The Jordan Structure of the Symmetric Plain Product](the-jordan-structure-of-the-symmetric-plain-product.html), for the symmetrisation that satisfies the identity.
- [The Lie Structure of the Antisymmetric Plain Sesquilinear Product](the-lie-structure-of-the-antisymmetric-plain-sesquilinear-product.html), for the other half of the same product.
- [Hermitian Squares and the Algebraic Positive Cone](hermitian-squares-and-the-algebraic-positive-cone.html), for the cone of squares and its definiteness.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for $H$ and its companions.
