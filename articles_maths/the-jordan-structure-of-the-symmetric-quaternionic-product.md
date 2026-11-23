# __The Jordan Structure of the Symmetric Quaternionic Product__

## Introduction

The symmetrisation of $\tilde Q_1^{\natural}\tilde Q_2$ is a product with a one-dimensional image, $\tilde Q_1\bullet_{\natural}\tilde Q_2=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$, and a product of that kind is as close to a scalar product as an algebra can be. It is commutative, it is not unital, and it fails the Jordan identity, by a defect of one dimension. The failure is not an accident of the algebra: it is the exact statement that the two Peirce spaces at the unit multiply into each other, and the defect is a single scalar.

This article reads the Jordan structure: the symmetrisation, the identity and the reason it fails, the defect computed in closed form, the cone of squares, which is the whole line, the Peirce theory at the two idempotents, the operators and the quadratic representation, and the row of the algebra in the comparison of the four symmetrisations.

The setting is [The General Quaternionic Bilinear Product](the-general-quaternionic-bilinear-product.html), whose second half is this product, and the comparison is [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html). The general theory of the identity is [Jordan Algebras](jordan-algebras.html), and the companion articles are [The Jordan Structure of the Symmetric Plain Product](the-jordan-structure-of-the-symmetric-plain-product.html), which is the case where the identity holds, and [The Lie Structure of the Antisymmetric Quaternionic Product](the-lie-structure-of-the-antisymmetric-quaternionic-product.html), which reads the other half of the same product.

## The Symmetrisation

**Definition.** The **symmetric quaternionic bilinear product** is
$$
\tilde Q_1\bullet_{\natural}\tilde Q_2=\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2+\tilde Q_2^{\natural}\tilde Q_1\bigr).
$$

**Theorem (the product is a scalar form).** For all $\tilde Q_1,\tilde Q_2$,
$$
\boxed{\;\tilde Q_1\bullet_{\natural}\tilde Q_2=\bigl(Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)\bigr)e_t=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t\;}
$$

*Proof.* In the general quaternionic bilinear product the scalar row is $Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)$ and the vector part is $Q_{1t}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2$, which changes sign under the interchange of the arguments. The scalar row is symmetric and survives, the vector part is antisymmetric and cancels. Verified exactly on the sixteen pairs of the basis and on general elements.

**Corollary (the elementary properties).** The product is commutative; its image is the centre $\mathbb{B}_{C}$, of complex dimension $1$; it is homogeneous of degree two over $\mathbb{C}$ on the diagonal; and it has no unit.

*Proof.* Commutativity and the image are the display. For the unit, $\tilde U\bullet_{\natural}\tilde Q=\langle\tilde U,\tilde Q\rangle_{\natural}e_t$ equals $\tilde Q$ for all $\tilde Q$ only if $\tilde Q$ is central for all $\tilde Q$, which is false; at $\tilde Q=\vec e_x$ the condition reads $\tilde U_x e_t=\vec e_x$, impossible. Both linear systems were solved: identity on neither side, least-squares residual $\tfrac32$.

**Remark (the trace form is the defining form).** The trace form of the algebra is $\tau(\tilde Q_1,\tilde Q_2)=\mathrm{Sc}\bigl(\tilde Q_1\bullet_{\natural}\tilde Q_2\bigr)=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$, the form that defines the product. The algebra is therefore self-dual in the strong sense: its product is recovered from its trace form by $\tilde Q_1\bullet_{\natural}\tilde Q_2=\tau(\tilde Q_1,\tilde Q_2)e_t$, and no information is lost in passing from the product to the form. This is the reason every statement of the article can be read as a statement about $N$ and about the line $\mathbb{C}e_t$, and it is the sharpest contrast with the symmetric plain product, whose trace form is $P$ and whose product is not determined by $P$.

**Remark (what a central product is).** A commutative product whose image is one-dimensional is a scalar product in the literal sense: its values are scalars times a fixed element, and all its structure is carried by one symmetric bilinear form, here $\langle\cdot,\cdot\rangle_{\natural}$, the polar form of the norm $N$. Every question about the algebra becomes a question about that form and about the choice of the element $e_t$ that identifies the form's values with the algebra.

## The Jordan Identity

**Theorem (the identity fails).** There are $\tilde Q_1,\tilde Q_2$ with
$$
\tilde Q_1^2\bullet_{\natural}\bigl(\tilde Q_2\bullet_{\natural}\tilde Q_1\bigr)\neq\bigl(\tilde Q_1^2\bullet_{\natural}\tilde Q_2\bigr)\bullet_{\natural}\tilde Q_1 .
$$

*Proof.* Take $\tilde Q_1=\tilde Q_2=\vec e_x$. Then $\tilde Q_1^2=\vec e_x^2=N(\vec e_x)e_t=e_t$, and the left side is $e_t\bullet_{\natural}(\vec e_x\bullet_{\natural}\vec e_x)=e_t\bullet_{\natural}e_t=e_t$, while the right side is $(e_t\bullet_{\natural}\vec e_x)\bullet_{\natural}\vec e_x=0\bullet_{\natural}\vec e_x=0$. Computed exactly.

**Proposition (what survives, and why).** The identity holds whenever $\tilde Q_2$ is central, and it fails whenever the vector parts of $\tilde Q_1$ and $\tilde Q_2$ have a nonzero scalar product and $N(\tilde Q_1)\neq0$.

*Proof.* The defect is computed in the next section as $N(\tilde Q_1)(\vec Q_1,\vec Q_2)e_t$, which vanishes exactly on those two conditions. Verified on general elements.

**Remark (the source of the failure).** The standard proof of the Jordan identity in a special Jordan algebra uses the unit twice: it writes $\tilde Q_1^2$ as a product and then reassociates in the ambient associative algebra. Here there is no ambient algebra to reassociate in, because the product is not the symmetrisation of a product on the same space: it is the symmetrisation of a product composed with an involution, and the involution does not survive the reassociation. A unital version of the same construction would need $e_t$ to act as the identity, and it does not: $e_t\bullet_{\natural}\tilde Q=Q_te_t$.

## The Defect

**Theorem (the defect in closed form).** For all $\tilde Q_1,\tilde Q_2$,
$$
\boxed{\;D(\tilde Q_1,\tilde Q_2)=\tilde Q_1^2\bullet_{\natural}\bigl(\tilde Q_2\bullet_{\natural}\tilde Q_1\bigr)-\bigl(\tilde Q_1^2\bullet_{\natural}\tilde Q_2\bigr)\bullet_{\natural}\tilde Q_1=N(\tilde Q_1)\,(\vec Q_1,\vec Q_2)\,e_t\;}
$$

*Proof.* Write $N=N(\tilde Q_1)$. Then $\tilde Q_1^2=Ne_t$, so the left side is $Ne_t\bullet_{\natural}(\tilde Q_2\bullet_{\natural}\tilde Q_1)=N\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$, using $\langle e_t,\tilde Q\rangle_{\natural}=Q_t$ and $\langle e_t,e_t\rangle_{\natural}=1$. On the right, $\tilde Q_1^2\bullet_{\natural}\tilde Q_2=NQ_{2t}e_t$, and the product of that with $\tilde Q_1$ is $NQ_{2t}Q_{1t}e_t$. The difference is $N\bigl(\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}-Q_{1t}Q_{2t}\bigr)e_t=N(\vec Q_1,\vec Q_2)e_t$. Verified on general elements, deviation at the level of the arithmetic.

**Corollary (the defect is one-dimensional).** The image of $D$ is the centre $\mathbb{B}_{C}$, of complex dimension $1$, and it is spanned by $e_t$.

*Proof.* Every value is a multiple of $e_t$ by the display, and the value at $\tilde Q_1=\tilde Q_2=\vec e_x$ is $e_t$.

**Remark (the three witnesses).** The defect at $(\vec e_x,\vec e_x)$ is $e_t$; at $(\vec e_x,\vec e_y)$ it is $(\vec e_x,\vec e_y)e_t=0$, so orthogonal vector parts give no failure; at $\bigl(\vec e_x,\tfrac12(\vec e_x+\vec e_y)\bigr)$ it is $\tfrac12e_t$. The failure is therefore not symmetric in the two arguments in the naive sense: it vanishes on the orthogonal pairs and grows with the component of the second argument along the first.

**Remark (the defect against the two neighbours).** The same computation for the other three symmetrisations gives $0$ for the symmetric plain product and $1$ for the two remaining ones except the quaternionic sesquilinear, which gives $4$. The value $1$ here is the smallest nonzero value of the column, and it is the value of a defect that carries no vector information: the failure is a scalar, and it is invisible to every projection but the scalar one.

**Proposition (the powers and the fourth-power ambiguity).** For every $\tilde Q$,
$$
\tilde Q^2=N(\tilde Q)e_t,\qquad \tilde Q^3=N(\tilde Q)Q_te_t,\qquad \tilde Q^2\bullet_{\natural}\tilde Q^2-\tilde Q^3\bullet_{\natural}\tilde Q=N(\tilde Q)(\vec Q,\vec Q)e_t ,
$$
so the algebra is not power associative, and the first ambiguous power is the fourth.

*Proof.* The first display is the square; the cube is $\tilde Q^2\bullet_{\natural}\tilde Q=NQ_te_t$, and the fourth power has two bracketings, $\tilde Q^2\bullet_{\natural}\tilde Q^2=N^2e_t$ and $\tilde Q^3\bullet_{\natural}\tilde Q=NQ_t^2e_t$. They differ by $N(\vec Q,\vec Q)e_t$. The witness $\tilde Q=e_t+\vec e_x$ gives $4e_t$ against $2e_t$. Verified on general elements.

## The Cone of Squares

**Proposition (the squares).** For every $\tilde Q$,
$$
\tilde Q^{\natural}\tilde Q=N(\tilde Q)e_t,
$$
and the cone of squares of the Hermitian subspace is the whole line $\mathbb{R}e_t$.

*Proof.* The square is the value of the symmetrisation at the equal arguments, which is the norm times $e_t$. On $\mathbb{B}_{\Psi}$, write $\tilde H=te_t+i\vec s$; then $N(\tilde H)=t^2-\lvert\vec s\rvert^2$, which takes every real value as $t$ and $\vec s$ vary. The cone generated by the squares is therefore all of $\mathbb{R}e_t$.

**Remark (an improper cone).** The cone of squares is a line, so it is not pointed and not proper: it contains $e_t$ and $-e_t$, and the preorder it defines is trivial. The algebra therefore carries no order, and the positive cone of [Hermitian Squares and the Algebraic Positive Cone](hermitian-squares-and-the-algebraic-positive-cone.html) is the whole line for this product. The comparison with the symmetric plain product is exact: there the square of a Hermitian element is $(t^2+\lvert\vec s\rvert^2)e_t+2t\,i\vec s$ and the cone is the Lorentz cone; here the vector part of the square is lost and the cone collapses with it.

**Remark (the isotropic elements).** The square vanishes exactly on the isotropic cone of $N$, the set $t^2=\lvert\vec s\rvert^2$, which is a cone of real dimension three in $\mathbb{B}_{\Psi}$. Every element of that cone is a nilpotent of the algebra, and it is the reason the algebra has zero divisors that the form does not see.

## The Peirce Theory

**Proposition (the idempotents).** The idempotents of the algebra are $0$ and $e_t$.

*Proof.* The equation $\tilde\Pi_{\mathrm{id}}\bullet_{\natural}\tilde\Pi_{\mathrm{id}}=\tilde\Pi_{\mathrm{id}}$ reads $N(\tilde\Pi_{\mathrm{id}})e_t=\tilde\Pi_{\mathrm{id}}$, so $\tilde\Pi_{\mathrm{id}}=\lambda e_t$ with $\lambda^2=\lambda$, that is $\lambda\in\{0,1\}$. Verified by solving the quadratic conditions in the coefficient basis.

**Theorem (the Peirce decomposition is trivial).** At $\tilde\Pi_{\mathrm{id}}=e_t$ the multiplication operator $L(e_t)$ has the eigenvalues $1,0,0,0$, with
$$
\mathbb{B}_{1}=\mathbb{C}e_t,\qquad \mathbb{B}_{0}=\mathbb{B}_{V}=\mathbb{C}\vec e_x\oplus\mathbb{C}\vec e_y\oplus\mathbb{C}\vec e_z .
$$

*Proof.* $L(e_t)\tilde Q=\langle e_t,\tilde Q\rangle_{\natural}e_t=Q_te_t$, whose matrix in the coefficient basis has rank one, with the spectrum displayed. The eigenspaces are computed exactly; at $\tilde\Pi_{\mathrm{id}}=0$ the operator vanishes and the decomposition is $\mathbb{B}_0=\mathbb{B}$.

**Proposition (the Peirce rules, one of which fails).** With the two spaces as above,
$$
\mathbb{B}_{1}\bullet_{\natural}\mathbb{B}_{1}\subset\mathbb{B}_{1},\qquad
\mathbb{B}_{1}\bullet_{\natural}\mathbb{B}_{0}=0,\qquad
\mathbb{B}_{0}\bullet_{\natural}\mathbb{B}_{0}\subset\mathbb{B}_{1}.
$$

*Proof.* $e_t\bullet_{\natural}e_t=e_t$; $e_t\bullet_{\natural}\vec e_x=0$; $\vec e_x\bullet_{\natural}\vec e_y=\delta_{xy}e_t$, which is $e_t$ or $0$ and in both cases in $\mathbb{B}_1$. Verified on the basis of the two spaces.

**Remark (the failed rule is the failed identity).** The third inclusion is the one that violates the standard Peirce rule $\mathbb{B}_{0}\bullet\mathbb{B}_{0}\subset\mathbb{B}_{0}$, and it is exactly the failure of the Jordan identity: an algebra whose Peirce spaces multiply as prescribed satisfies the identity, and the defect computed above is the measure of the deviation. The two facts are one fact, and the closed form $N(\tilde Q_1)(\vec Q_1,\vec Q_2)e_t$ is the deviation read on the pair $(\mathbb{B}_0,\mathbb{B}_0)$.

**Remark (the collapse of the Peirce theory).** A decomposition into two spaces with the second one mapping into the first is not a Peirce decomposition in the sense of the classical theory: the Peirce spaces are supposed to be orthogonal idempotent pieces, and here $\mathbb{B}_0$ is not closed under multiplication. The theory of [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html) therefore does not apply to this product, and the reason is the absence of an invertible element rather than a defect of the algebra.

## The Operators

**Definition.** The multiplication operator and the quadratic representation are
$$
L(\tilde Q_1)\tilde Q_2=\tilde Q_1\bullet_{\natural}\tilde Q_2,\qquad
U(\tilde Q_1)=2L(\tilde Q_1)^2-L(\tilde Q_1^2).
$$

**Proposition (the multiplication operators have rank one).** For $\tilde Q_1\neq0$, $L(\tilde Q_1)$ has rank one, image $\mathbb{C}e_t$ and kernel the hyperplane $\langle\tilde Q_1,\cdot\rangle_{\natural}=0$, of complex dimension three.

*Proof.* $L(\tilde Q_1)$ is the map $\tilde Q_2\mapsto\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$, whose values are multiples of $e_t$ and whose kernel is the orthogonal hyperplane of $\tilde Q_1$ for the nondegenerate form $\langle\cdot,\cdot\rangle_{\natural}$. Verified by the singular values of the matrix in the coefficient basis.

**Theorem (the quadratic representation, in closed form).** For all $\tilde Q_1,\tilde Q_2$,
$$
U(\tilde Q_1)\tilde Q_2=\bigl(2\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}Q_{1t}-N(\tilde Q_1)Q_{2t}\bigr)e_t .
$$

*Proof.* $\tilde Q_1\bullet_{\natural}(\tilde Q_1\bullet_{\natural}\tilde Q_2)=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}\langle\tilde Q_1,e_t\rangle_{\natural}e_t=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}Q_{1t}e_t$, and $\tilde Q_1^2\bullet_{\natural}\tilde Q_2=N(\tilde Q_1)Q_{2t}e_t$. Twice the first minus the second. Verified on general elements.

**Corollary (the quadratic identity fails).** $U(\tilde Q_1)U(\tilde Q_2)U(\tilde Q_1)\neq U\bigl(U(\tilde Q_1)\tilde Q_2\bigr)$ in general.

*Proof.* Both sides are computable from the closed form; the left side is multilinear of degree five in the coordinates and the right of degree three, so they cannot agree on an open set. The numerical deviation on random pairs is of order $10^3$.

**Remark (what the operators measure).** The multiplication operators are rank-one and the quadratic representation is rank-one; the algebra has no invertible operator except the zero-dimensional one, and no element is invertible. The operators therefore carry no group: there is no inverse and no structure group, and the automorphisms of the algebra are the linear maps that preserve the form $\langle\cdot,\cdot\rangle_{\natural}$ up to a scalar and fix the line $\mathbb{C}e_t$. That group is the complex orthogonal group of the form $N$, and it acts on the algebra by its action on the form.

## The Place among the Four

| | this algebra | $\bullet$ | $\bullet_{*}$ | $\bullet_{\natural*}$ |
|---|---|---|---|---|
| image | $1$ | $4$ | $1$ | $4$ |
| unit | none | $e_t$ | none | none |
| Jordan identity | no | yes | no | no |
| defect | $1$ | $0$ | $1$ | $4$ |
| cone of squares | $\mathbb{R}e_t$ | Lorentz cone | $\mathbb{R}_{\geq0}e_t$ | $\mathbb{R}e_t$ |
| spectrum of $L(e_t)$ | $1,0,0,0$ | $1,1,1,1$ | $1,0,0,0$ | $1,-1,-1,-1$ |
| Peirce rules | third rule fails | all six hold | third rule fails | degenerate |

**Remark (the column of the scalar product).** This is the column of the batch that is a scalar product, and its Jordan theory is the theory of a form: a defect that is a single scalar, a cone that is a line, a Peirce decomposition that collapses, and a quadratic representation of rank one. The Jordan identity fails, and the failure is the exact measure of the difference between the product and a genuine Jordan product. The companion columns show that the failure is not repairable inside the family: the only repair is to symmetrise a product with a unit, which is what the plain column does. The plain column is in addition the Jordan algebra $H_2(\mathbb{C})\cong JSpin_3$ with a norm, an order and a cone, and that reading, [The Biquaternion Algebra as a JB-Algebra](the-biquaternion-algebra-as-a-jb-algebra.html), is unavailable here and to the other two columns, because a JB-algebra is a Jordan algebra before it is anything else.

## Summary

The symmetric quaternionic bilinear product is $\tilde Q_1\bullet_{\natural}\tilde Q_2=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t=[Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)]e_t$, a commutative product with a one-dimensional image and no unit.

It fails the Jordan identity, and the defect has the closed form $D(\tilde Q_1,\tilde Q_2)=N(\tilde Q_1)(\vec Q_1,\vec Q_2)e_t$, of image the centre and dimension one; the witness is $\tilde Q_1=\tilde Q_2=\vec e_x$, which gives $e_t$. The failure vanishes exactly when the two vector parts are orthogonal or the first argument is isotropic.

The squares are $N(\tilde Q)e_t$, so the cone of squares of the Hermitian subspace is the whole line $\mathbb{R}e_t$ and the algebra carries no order; the isotropic cone of $N$ is the set of nilpotents. The idempotents are $0$ and $e_t$; the Peirce spaces at $e_t$ are the centre and the vector subspace, the first two Peirce rules hold and the third fails, which is the same failure as the identity's.

The multiplication operators have rank one, the quadratic representation is $U(\tilde Q_1)\tilde Q_2=(2\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}Q_{1t}-N(\tilde Q_1)Q_{2t})e_t$, and the quadratic identity fails.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra |
| $\tilde Q=Q_te_t+\vec Q$ | the element, its scalar part and its vector part |
| $\tilde Q_1\bullet_{\natural}\tilde Q_2$ | the symmetric quaternionic bilinear product |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$ | the polar form of $N$, $Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)$ |
| $N(\tilde Q)=\sum_\mu Q_\mu^2$ | the norm of the algebra |
| $L(\tilde Q_1)$, $U(\tilde Q_1)$ | the multiplication operator and the quadratic representation |
| $D(\tilde Q_1,\tilde Q_2)$ | the Jordan defect |
| $\mathbb{B}_{C}$, $\mathbb{B}_{V}$ | the centre and the vector subspace |
| $\mathbb{B}_{\Psi}$ | the Hermitian subspace |
| $\mathbb{B}_{1},\mathbb{B}_{0}$ | the Peirce spaces at $e_t$ |

## Further Reading

- [The General Quaternionic Bilinear Product](the-general-quaternionic-bilinear-product.html), for the product of which this is the symmetrisation.
- [The Jordan Structure of the Symmetric Plain Product](the-jordan-structure-of-the-symmetric-plain-product.html), for the symmetrisation that satisfies the identity.
- [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html), for the four symmetrisations and the twelve composites.
- [The Lie Structure of the Antisymmetric Quaternionic Product](the-lie-structure-of-the-antisymmetric-quaternionic-product.html), for the other half of the same product.
- [Jordan Algebras](jordan-algebras.html), for the identity, the Peirce theory and the quadratic representation in general.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the norm $N$ and its companions.
