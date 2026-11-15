# __The Lie Structure of the Antisymmetric Quaternionic Product__

## Introduction

The antisymmetrisation of $\tilde Q_1^{\natural}\tilde Q_2$ is
$$
\tilde Q_1\wedge_{\natural}\tilde Q_2=\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2-\tilde Q_2^{\natural}\tilde Q_1\bigr)=Q_{1t}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2 ,
$$
a bracket with no scalar part, an image of dimension three, and a defect of dimension three. It is alternating, and it is not a Lie bracket: the Jacobi identity fails. The failure is entirely a failure of the mixed part, because on the vector subspace the bracket is minus the cross product and the identity holds there.

This article reads the Lie structure of the bracket: the antisymmetrisation, the Jacobi identity and its failure, the defect and its span, the bracket table, the ideals and the radical, which does not exist, the Killing form and its non-invariance, the exponential and the versors, and the row of the bracket in the comparison of the four.

The setting is [The General Quaternionic Bilinear Product](the-general-quaternionic-bilinear-product.html), whose second half is this product, and [The Jordan Structure of the Symmetric Quaternionic Product](the-jordan-structure-of-the-symmetric-quaternionic-product.html), which reads the first half. The general theory is [Lie Algebras](lie-algebras-a-general-introduction.html), and the comparison of the four brackets is [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html).

## The Antisymmetrisation

**Definition.** The **antisymmetric quaternionic bilinear product** is
$$
\tilde Q_1\wedge_{\natural}\tilde Q_2=\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2-\tilde Q_2^{\natural}\tilde Q_1\bigr).
$$

**Theorem (the closed form).** For all $\tilde Q_1,\tilde Q_2$,
$$
\boxed{\;\tilde Q_1\wedge_{\natural}\tilde Q_2=Q_{1t}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2\;}
$$

*Proof.* In the general quaternionic bilinear product the scalar row $Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)$ is symmetric and the mixed part is $Q_{1t}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2$. Under the interchange of the arguments and the application of ${}^{\natural}$ the mixed part changes sign and the scalar row does not, so the half-difference is the mixed part. Verified exactly on the basis and on general elements.

**Corollary (the elementary properties).** The bracket is alternating, $\tilde Q\wedge_{\natural}\tilde Q=0$; it has no scalar part; its image is the vector subspace, of complex dimension $3$; and its restriction to the vector subspace is minus the cross product.

*Proof.* The alternation is the antisymmetry of the definition. The image is spanned by $\vec e_x\wedge_{\natural}\vec e_y=-\vec e_z$ and its companions, computed exactly. On the vector subspace the mixed part vanishes and the cross term remains with its sign.

**Remark (alternation is not Jacobi).** The bracket is alternating and it fails the Jacobi identity. The two properties are independent and the classical theorem that an alternating bracket is a Lie bracket is a theorem about a specific class of brackets, not a consequence of alternation. The example of this article is the smallest one inside the biquaternion algebra, and it is the reason the four brackets of the batch are not four Lie algebras.

**Remark (the three terms).** The bracket has three terms: the two mixed ones carry the scalar parts and the cross one carries the vector parts. The cross term is minus the cross product, and the mixed terms vanish on the vector subspace; the failure of the identity is carried by the mixed terms alone, as the next two sections show.

## The Jacobi Identity

**Theorem (the identity fails).** There are $\tilde Q_1,\tilde Q_2,\tilde Q_3$ with
$$
\bigl[\tilde Q_1,\tilde Q_2\bigr]_{\natural}\wedge_{\natural}\tilde Q_3+\bigl[\tilde Q_2,\tilde Q_3\bigr]_{\natural}\wedge_{\natural}\tilde Q_1+\bigl[\tilde Q_3,\tilde Q_1\bigr]_{\natural}\wedge_{\natural}\tilde Q_2\neq0 .
$$

*Proof.* Take $\tilde Q_1=e_t$, $\tilde Q_2=\vec e_x$, $\tilde Q_3=\vec e_y$. The three terms of the cyclic sum are
$$
[e_t,\vec e_x]_{\natural}\wedge_{\natural}\vec e_y=\vec e_x\wedge_{\natural}\vec e_y=-\vec e_z,\qquad
[\vec e_x,\vec e_y]_{\natural}\wedge_{\natural}e_t=(-\vec e_z)\wedge_{\natural}e_t=+\vec e_z,\qquad
[\vec e_y,e_t]_{\natural}\wedge_{\natural}\vec e_x=(-\vec e_y)\wedge_{\natural}\vec e_x=-\vec e_z,
$$
and the sum is $-\vec e_z$. Computed exactly.

**Proposition (the identity holds on the vector subspace).** For $\tilde Q_1,\tilde Q_2,\tilde Q_3\in\mathbb{B}_V$ the cyclic sum vanishes.

*Proof.* On the vector subspace the bracket is $-\vec Q_1\times\vec Q_2$; the cyclic sum of a cross product bracket is the negative of the cyclic sum of the cross product bracket, which vanishes by the Jacobi identity of $\mathfrak{so}(3,\mathbb{C})$. Verified on the three basis vectors.

**Remark (the failure is the mixed part).** The two statements together locate the failure exactly: it is produced when at least one argument has a nonzero scalar part. The three-dimensional defect is the span of the values obtained by inserting one scalar unit and two vector units, and it lies in the vector subspace. The defect is therefore a tensor of the mixed part, and it vanishes on the pure vectors.

## The Defect

**Theorem (the defect is three-dimensional).** The span of the values of
$$
J(\tilde Q_1,\tilde Q_2,\tilde Q_3)=\bigl[\tilde Q_1,\tilde Q_2\bigr]_{\natural}\wedge_{\natural}\tilde Q_3+\bigl[\tilde Q_2,\tilde Q_3\bigr]_{\natural}\wedge_{\natural}\tilde Q_1+\bigl[\tilde Q_3,\tilde Q_1\bigr]_{\natural}\wedge_{\natural}\tilde Q_2
$$
over all triples of the complex basis is three-dimensional, and it is the whole vector subspace.

*Proof.* The values at the triples with one scalar unit and two vector units are $\pm\vec e_k$, and the values at triples of three vector units vanish. The span of the whole set was computed from the singular values of the matrix of values: three nonzero singular values, equal to each other, and the left singular vectors are the three vector units. Computed exactly.

**Corollary (the defect has no scalar part).** Every value of $J$ is a vector, and the defect is contained in $\mathbb{B}_V$.

**Remark (the defect against the other three).** The four defects are $0,3,3,3$, and this is the first of the three ones. The plain bracket has none because it is a commutator in an associative algebra; the two sesquilinear brackets have three each, and their defects differ from this one in the direction of the failure rather than in its size. The sizes coincide because the mechanism coincides: a mixed part that does not cancel.

**Remark (the defect and the associator).** The bracket is not a commutator in an associative algebra, and the defect measures the distance. The candidate associative algebra is the plain product, and its commutator is the plain bracket, whose defect is zero. The two brackets differ by the mixed part, and the defect of this bracket is the failure of the mixed part to be a commutator. This is the exact sense in which the quaternionic bracket is not the commutator of the quaternionic product: the quaternionic product is not associative, so its commutator has no reason to satisfy an identity, and it does not.

## The Bracket on the Basis

**Proposition (the table).** In the coefficient basis,
$$
[e_t,\vec e_x]_{\natural}=\vec e_x,\quad [e_t,\vec e_y]_{\natural}=\vec e_y,\quad [e_t,\vec e_z]_{\natural}=\vec e_z,\quad [\vec e_x,\vec e_y]_{\natural}=-\vec e_z,
$$
with $[\vec e_y,\vec e_z]_{\natural}=-\vec e_x$, $[\vec e_z,\vec e_x]_{\natural}=-\vec e_y$, and the negatives in the reversed order.

*Proof.* $e_t^{\natural}=e_t$ and $\vec e_x^{\natural}=-\vec e_x$, so $e_t\wedge_{\natural}\vec e_x=\tfrac12(\vec e_x-(-\vec e_x))=\vec e_x$. The vector-vector brackets are minus the plain ones. Computed exactly.

| $\wedge_{\natural}$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $0$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
| $\vec e_x$ | $-\vec e_x$ | $0$ | $-\vec e_z$ | $\vec e_y$ |
| $\vec e_y$ | $-\vec e_y$ | $\vec e_z$ | $0$ | $-\vec e_x$ |
| $\vec e_z$ | $-\vec e_z$ | $-\vec e_y$ | $\vec e_x$ | $0$ |

**Remark (the reading of the table).** The table is the table of the affine algebra of the plane: the scalar unit acts on the vector subspace by the identity with a sign on the two sides, and the vector units act on each other by minus the cross product. The scalar line is not a centre, and the alteration of the scalar action is exactly what the Jordan article of the same product sees as the collapse of the Peirce theory.

**Corollary (the trace of the adjoint).** $\operatorname{tr}(\operatorname{ad}e_t)=3$ and $\operatorname{tr}(\operatorname{ad}\vec e_x)=0$.

*Proof.* The diagonal of the table: the three vector units on the first row and $-\vec e_k$ on the first column do not contribute to the trace, and the vector-vector block is anti-Hermitian. Computed exactly.

## The Ideals and the Radical

**Proposition (the ideals are the three).** The subspaces closed under the bracket with the whole algebra are $0$, $\mathbb{B}_V$ and $\mathbb{B}$.

*Proof.* $\mathbb{B}_V$ is closed: the bracket of a scalar unit with a vector is a vector, and the bracket of two vectors is a vector. The scalar line is not closed, since $[e_t,\vec e_x]_{\natural}=\vec e_x$. Any subspace containing an element with a nonzero scalar part contains $\vec e_x$ for some $x$ after subtracting a vector, and then contains $\vec e_k$ for all $k$ by bracketing with the vector units; it is everything. Verified by computing the invariant subspaces of the four adjoint matrices.

**Proposition (there is no radical).** The algebra is not a Lie algebra, so it has no radical in the sense of Lie theory; the trace form has radical $0$.

*Proof.* A radical is the maximal solvable ideal of a Lie algebra, and the notion presupposes the Jacobi identity. The radical of the trace form is computed in the next section and is zero. The statement of the proposition is a triviality, recorded so that the row of the four brackets is complete.

**Remark (the centre).** The centre is zero: no nonzero element brackets to zero against everything, since $[e_t,\vec e_x]_{\natural}=\vec e_x$ and $[\vec e_x,\vec e_t]_{\natural}=-\vec e_x$ are both nonzero. The centre is computed by solving the four linear systems, and the solution space is zero-dimensional.

## The Killing Form

**Definition.** $\kappa(\tilde Q_1,\tilde Q_2)=\operatorname{tr}\bigl(\operatorname{ad}\tilde Q_1\circ\operatorname{ad}\tilde Q_2\bigr)$, with $\operatorname{ad}$ the adjoint map of the bracket.

**Theorem (the form in the coefficient basis).** The matrix of $\kappa$ is $\operatorname{diag}(3,-2,-2,-2)$, that is
$$
\kappa(\tilde Q_1,\tilde Q_2)=3Q_{1t}Q_{2t}-2\bigl(\vec Q_1,\vec Q_2\bigr),
$$
nondegenerate.

*Proof.* The adjoint of $\vec e_x$ is minus the cross product matrix on $\mathbb{B}_V$ and zero on the scalar line, so its square has trace $-2$; the adjoint of $e_t$ is the identity on $\mathbb{B}_V$ and zero on the line, so its square has trace $3$. The mixed traces vanish. Computed exactly.

**Proposition (the form is not invariant).** There are $\tilde Q_1,\tilde Q_2,\tilde Q_3$ with
$$
\kappa\bigl(\tilde Q_1\wedge_{\natural}\tilde Q_2,\tilde Q_3\bigr)+\kappa\bigl(\tilde Q_2,\tilde Q_1\wedge_{\natural}\tilde Q_3\bigr)\neq0 .
$$

*Proof.* Take $(\tilde Q_1,\tilde Q_2,\tilde Q_3)=(e_t,\vec e_x,\vec e_x)$. Then $[e_t,\vec e_x]_{\natural}=\vec e_x$, and the sum of the two terms is $\kappa(\vec e_x,\vec e_x)+\kappa(\vec e_x,\vec e_x)=-2-2=-4$. Computed exactly, and the nine witnessing triples on the basis are all of this shape. The failure is a consequence of the failure of the Jacobi identity, of which the invariance is the integrated form.

**Remark (a nondegenerate form that is not the Killing form of anything).** The form is nondegenerate and symmetric, and it is not invariant. The invariance of the Killing form of a Lie algebra is proved from the Jacobi identity, and there is no such identity here; the form is the trace form of the adjoint representation of a non-Lie algebra, and it carries no cohomological information.

## The Exponential and the Versors

**Proposition (the adjoint of the scalar unit is the projection).** In the coefficient basis the adjoint of $e_t$ is
$$
\operatorname{ad}e_t=\operatorname{diag}(0,1,1,1),
$$
the projection onto the vector subspace, and
$$
\exp\bigl(t\operatorname{ad}e_t\bigr)=I+\bigl(e^{t}-1\bigr)P ,
$$
with $P$ the projection.

*Proof.* The bracket with $e_t$ is the identity on the vector subspace and zero on the line, by the table. A projection has $\exp(tP)=I+(e^t-1)P$, verified numerically.

**Proposition (the exponential is not an automorphism).** For $t\neq0$ the map $\exp(t\operatorname{ad}e_t)$ is not an automorphism of the bracket.

*Proof.* It multiplies the vector part by $e^t$ and leaves the scalar part alone, so it does not preserve the mixed part $Q_{1t}\vec Q_2-Q_{2t}\vec Q_1$, which is homogeneous of degree one in each scalar part. The numerical deviation on random triples is of order $10$. This is the general behaviour, and it is the third face of the failure of the Jacobi identity.

**Proposition (the versors act by automorphisms).** For every versor $\tilde U$, the map $\tilde Q\mapsto\tilde U\tilde Q\tilde U^{\natural}$ preserves the bracket.

*Proof.* The map preserves the plain product and commutes with ${}^{\natural}$, since ${}^{\natural}$ is an anti-automorphism and $\tilde U\tilde Q\tilde U^{\natural}$ conjugated is $\tilde U\tilde Q^{\natural}\tilde U^{\natural}$; the bracket is built from the product and the involution, so it is preserved. Verified on random versors and random pairs, with a deviation of zero.

**Remark (the two groups).** The bracket has two groups attached: the group of the versor conjugations, which acts by automorphisms, and the group generated by the exponentials of the adjoint maps, which does not. The first is the classical spin group of the plain algebra, of complex dimension three; the second is not a group of automorphisms at all, and its failure is the failure of the identity. The gap between the two is the Lie-theoretic content of the defect.

## The Place among the Four

| | this bracket | $\wedge$ | $\wedge_{*}$ | $\wedge_{\natural*}$ |
|---|---|---|---|---|
| value on $\mathbb{B}_V$ | $-\vec X\times\vec Y$ | $\vec X\times\vec Y$ | $-\vec X\times\vec Y$ | $\vec X\times\overline{\vec Y}$ |
| mixed part | $Q_{1t}\vec Q_2-Q_{2t}\vec Q_1$ | none | $-Q_{1t}\overline{\vec Q_2}+\overline{Q_{2t}}\vec Q_1$ | none |
| Jacobi | fails, defect $3$ | holds | fails, defect $3$ | fails, defect $3$ |
| centre | $0$ | $\mathbb{C}e_t$ | $0$ | $\mathbb{C}e_t$ |
| Killing form | $\operatorname{diag}(3,-2,-2,-2)$ | $\operatorname{diag}(0,-2,-2,-2)$ | $\operatorname{diag}(3,-2,-2,-2)$ | $\operatorname{diag}(0,-2,-2,-2)$ |
| invariant form | no | yes | no | no |
| $\exp(\operatorname{ad})$ automorphism | no | yes | no | no |

**Remark (the column with a mixed part and no centre).** This column has a mixed part and no centre, and the combination is what produces the defect: the mixed part supplies the failure. The plain bracket has no mixed part and a centre and its defect is zero; this bracket has a mixed part and its defect is three; the sesquilinear plain bracket has a mixed part and its defect is three; the sesquilinear quaternionic bracket has no mixed part and its defect is three as well, and its failure comes from the conjugate-linearity of its second slot instead. A mixed part is a sufficient cause of the failure and not a necessary one.

## Summary

The antisymmetric quaternionic bilinear product is $\tilde Q_1\wedge_{\natural}\tilde Q_2=Q_{1t}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2$, an alternating bracket with no scalar part and image the vector subspace.

It fails the Jacobi identity, with a defect of dimension three equal to the vector subspace; the witness is $(e_t,\vec e_x,\vec e_y)$, which gives $-\vec e_z$, and the identity holds on the vector subspace, where the bracket is minus the cross product. The failure is carried by the mixed part.

The ideals are $0$, $\mathbb{B}_V$ and $\mathbb{B}$, the centre is zero, and there is no radical because there is no Lie algebra. The Killing form is $\operatorname{diag}(3,-2,-2,-2)$, nondegenerate and not invariant. The adjoint of the scalar unit is the projection onto the vector subspace, its exponential is $I+(e^t-1)P$ and is not an automorphism, and the versor conjugations are automorphisms.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra |
| $\tilde Q=Q_te_t+\vec Q$ | the element, its scalar part and its vector part |
| $\tilde Q_1\wedge_{\natural}\tilde Q_2$ | the antisymmetric quaternionic bilinear product |
| ${}^{\natural}$ | the quaternion involution |
| $\operatorname{ad}\tilde Q$ | the adjoint map of the bracket |
| $\kappa$ | the trace form of the adjoint representation |
| $J$ | the Jacobi defect |
| $P$ | the projection onto the vector subspace |
| $\mathbb{B}_V$ | the vector subspace |
| $\tilde U$ versor | an element with $N(\tilde U)=1$ |

## Further Reading

- [The General Quaternionic Bilinear Product](the-general-quaternionic-bilinear-product.html), for the product of which this is the antisymmetrisation.
- [The Jordan Structure of the Symmetric Quaternionic Product](the-jordan-structure-of-the-symmetric-quaternionic-product.html), for the other half of the same product.
- [The Lie Structure of the Antisymmetric Plain Product](the-lie-structure-of-the-antisymmetric-plain-product.html), for the bracket that satisfies the identity.
- [The Lie Structure of the Antisymmetric Plain Sesquilinear Product](the-lie-structure-of-the-antisymmetric-plain-sesquilinear-product.html), for the companion bracket with the other mixed part.
- [Lie Algebras](lie-algebras-a-general-introduction.html), for the identity, the ideals and the Killing form in general.
- [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html), for the four brackets and the twelve composites.
