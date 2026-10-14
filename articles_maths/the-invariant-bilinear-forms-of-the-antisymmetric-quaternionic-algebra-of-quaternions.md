# __The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra__

## Introduction

The antisymmetric quaternionic multiplication
$\tilde p\diamond\tilde q=\tfrac12(\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p)=p_0\vec q-q_0\vec p-\vec p\times\vec q$ is alternating and vector valued, and it fails the
Jacobi identity (*The Jacobi Failure and the Associator Defect of the Antisymmetric Quaternionic
Algebra*, below this article in this category). A Lie algebra carries its invariant bilinear forms, the
symmetric $\beta$ with $\beta([x,y],z)+\beta(y,[x,z])=0$, whose prototype is the Killing form; the block
of this article is an antisymmetrisation for which the Jacobi identity fails, so the classical theory
does not apply, and the question of its own invariant forms is well posed and is answered here.

The answer has three parts. The space of forms invariant under the block is **one-dimensional**,
spanned by the form $\varphi(\tilde p,\tilde q)=p_0q_0$ that reads the two scalar parts; the invariant
form is symmetric, its radical is the whole vector subspace, and there is no nonzero alternating
invariant form. The **trace form vanishes**, the values of the block having zero scalar part, so the
coefficient form of the block is zero. And the substitution that suggests itself in the absence of a
Jacobi identity, the trace form of the multiplication operators $\operatorname{Tr}(L_{\tilde p}L_{\tilde q})$,
is computed, is non-degenerate, and is **not invariant**, its failure being the same obstruction as the
Jacobi failure. The article closes with the comparison with the adjacent Lie case $\mathrm{APA}$, which
does carry a Killing form.

**This is not the algebra $\mathbb{H}$.** The forms are forms of the block, and the natural sign
${}^{\natural}$ is the quaternion conjugation; the bar is the identity, and the star coincides with the
natural sign and gives nothing new. The symbol $\diamond$ is reserved for this block.

The operation and the failure are *Introduction to the Antisymmetric Quaternionic Algebra of
Quaternions* and *The Jacobi Failure and the Associator Defect of the Antisymmetric Quaternionic
Algebra*, below this article in this category; the operators are *The Adjoint Operators of the
Antisymmetric Quaternionic Algebra*, below this article in this category. The comparator is *The Killing

**Conventions.** The algebra is $\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$ and
$e_1^2=e_2^2=e_3^2=-e_0$; a generic element is $\tilde q=q_0e_0+\vec q$, the **centre** is
$\mathbb{R}_{\mathbb{H}}=\mathbb{R}e_0$ and the **vector subspace** is
$\mathrm{Vect}(\mathbb{H})=\{\vec q\}$; $\vec p\cdot\vec q$ is the Euclidean dot product and
$L^{\diamond}_{\tilde p}$ is the left multiplication operator. The **quaternion form** is
$N(\tilde p,\tilde q)=p_0q_0+\vec p\cdot\vec q$.

## The Invariance Condition

**Definition.** An $\mathbb{R}$-bilinear form $\beta:\mathbb{H}\times\mathbb{H}\to\mathbb{R}$ is
**invariant under the block** if

$$
\beta(\tilde p\diamond\tilde q,\tilde r)+\beta(\tilde q,\tilde p\diamond\tilde r)=0
$$

for all $\tilde p,\tilde q,\tilde r$; equivalently, for a symmetric $\beta$, if
$\beta(\tilde p\diamond\tilde q,\tilde r)=\beta(\tilde p,\tilde q\diamond\tilde r)$ for all triples.
This is the classical invariance condition of a Lie algebra, $\beta([x,y],z)+\beta(y,[x,z])=0$, read
for the operation of the block.

**Proposition.** For a symmetric $\beta$ the second condition implies the first, for any alternating
operation, and for the block the two conditions are equivalent, both returning the same one-dimensional
space; the condition is $\mathbb{R}$-linear in $\beta$, so the invariant forms form a vector space and
split into a symmetric and an alternating part.

*Proof.* If $\beta(\tilde y,\tilde x\diamond\tilde z)=\beta(\tilde y\diamond\tilde x,\tilde z)$ then
$\beta(\tilde y,\tilde x\diamond\tilde z)=-\beta(\tilde x\diamond\tilde y,\tilde z)$ by the alternation,
which is the first condition. For the converse, the matrix of the left multiplication operator is
skew-symmetric with respect to the standard pairing only in the radical, and solving either condition
over the four basis operators gives the same solution, $G_{00}$ free and the other entries zero.

## The Space of Invariant Forms

**Theorem (the invariant forms).** The space of bilinear forms invariant under the block is
one-dimensional, spanned by

$$
\varphi(\tilde p,\tilde q)=p_0q_0 ,
$$

the product of the two scalar parts. Every invariant form is a multiple of $\varphi$.

*Proof.* Let $G_{\mu\nu}=\beta(e_\mu,e_\nu)$ be the Gram matrix in the coefficient basis, and let
$M_{\tilde p}$ be the matrix of the left multiplication, so that the coordinate vector of
$\tilde p\diamond e_\nu$ is the $\nu$-th column of $M_{\tilde p}$. Writing
$\beta(\tilde x,\tilde y)=x^{\mathsf T}Gy$, the condition at $e_\mu,e_\nu,e_\rho$ reads
$M_{e_\mu}^{\mathsf T}G+GM_{e_\mu}=0$, and the four basis elements generate it. Solving the $64$
equations $\beta(e_\mu\diamond e_\nu,e_\rho)+\beta(e_\nu,e_\mu\diamond e_\rho)=0$ over the $16$ entries
of $G$ gives $G_{00}=g$ free and $G_{\mu\nu}=0$ otherwise; the solution space is one-dimensional, with
basis $\varphi$.

**Remark (why the scalar form survives).** The operation has zero scalar part, so
$\varphi(\tilde p\diamond\tilde q,\tilde r)=(\tilde p\diamond\tilde q)_0r_0=0$ and the first term of the
condition vanishes for every triple, and the second vanishes for the same reason. The form $\varphi$ is
invariant for the trivial reason that both of its terms vanish, and it is the only form for which that
happens on the scalar slot. A form that reads a vector slot is not invariant, because the block moves
the scalar part into the vector part and the mixed terms then survive in the condition.

**Proposition (the Gram matrix and the rank).** The Gram matrix of $\varphi$ is
$\operatorname{diag}(1,0,0,0)$, of rank $1$.

*Proof.* $\varphi(e_\mu,e_\nu)=\delta_{\mu0}\delta_{\nu0}$ by the definition of the scalar part.

## The Trace Form Vanishes

**Proposition.** The coefficient form of the block vanishes identically,
$\mathrm{Sc}(\tilde p\diamond\tilde q)=0$ for all $\tilde p,\tilde q$, so the trace form of the block is
the zero form and is not an invariant form of the block.

*Proof.* The value is a pure vector, so its scalar part is zero; the scalar part of the value is the
coefficient of the block, and the bilinear form that reads it is the zero form, a multiple of $\varphi$.

## The Symmetric and the Alternating Parts

**Theorem.** The single invariant form $\varphi$ is **symmetric**, and there is **no nonzero
alternating invariant form**; the space of invariant forms is one dimension symmetric and zero
alternating.

*Proof.* $\varphi(\tilde p,\tilde q)=p_0q_0=\varphi(\tilde q,\tilde p)$ is symmetric. The solution of
the same system with the added antisymmetry $G^{\mathsf T}=-G$ is $G=0$, the solution space without the
added symmetry being one-dimensional and spanned by a symmetric element; so the only antisymmetric
invariant form is zero. The condition is preserved by the transposition of $\beta$, so the two searches
may be run separately.

## The Radical and the Degeneracy

**Theorem (the radical).** The radical of $\varphi$, the set of $\tilde x$ with
$\varphi(\tilde x,\tilde y)=0$ for all $\tilde y$, is the vector subspace $\mathrm{Vect}(\mathbb{H})$,
of real dimension three, and the isotropic elements of $\varphi$, those with
$\varphi(\tilde x,\tilde x)=0$, are the same set.

*Proof.* $\varphi(\tilde x,\tilde y)=x_0y_0$ vanishes for all $\tilde y$ exactly when $x_0=0$, and
$\varphi(\tilde x,\tilde x)=x_0^2$ vanishes exactly when $x_0=0$.

**Remark (the degeneracy is the image).** The form is as degenerate as it can be without being zero:
its rank is one, its radical is the three-dimensional image of the block, and the isotropic elements are
exactly the elements the block produces. The form reads the one-dimensional quotient
$\mathbb{H}/\mathrm{Vect}(\mathbb{H})$ and is non-degenerate there, being the pull-back of a
one-dimensional form along the scalar-part map. With respect to $\varphi$ the adjoint of a multiplication
operator is not determined, since $\varphi(L^{\diamond}_{\tilde p}\tilde x,\tilde y)=0$ for all arguments,
so every operator is adjoint to $0$ modulo the radical.

## The Operator Trace Form and Its Failure of Invariance

**Definition.** The **operator trace form** of the block is
$K(\tilde p,\tilde q)=\operatorname{Tr}(L^{\diamond}_{\tilde p}L^{\diamond}_{\tilde q})$, the trace of
the composition of the two left multiplication operators.

**Proposition (the operator trace form is non-degenerate).** For all $\tilde p,\tilde q$,

$$
K(\tilde p,\tilde q)=3p_0q_0-2\,\vec p\cdot\vec q ,
$$

with Gram matrix $\operatorname{diag}(3,-2,-2,-2)$, of rank four, hence non-degenerate.

*Proof.* The matrix of $L^{\diamond}_{\tilde p}$ is read off the table of the block; its diagonal entries
are $0,p_0,p_0,p_0$ on the scalar and the three vector lines, and the trace of the product is computed
entry by entry, the cross-product terms cancelling. The Gram matrix is diagonal with the displayed
entries.

**Proposition (it is not invariant).** The operator trace form is not invariant; the failure

$$
F(\tilde p,\tilde q,\tilde r)=K(\tilde p\diamond\tilde q,\tilde r)+K(\tilde q,\tilde p\diamond\tilde r)
=-4p_0\,(\vec q\cdot\vec r)+2q_0\,(\vec p\cdot\vec r)+2r_0\,(\vec p\cdot\vec q)
$$

does not vanish identically, and at $(\tilde p,\tilde q,\tilde r)=(e_0,e_1,e_1)$ it equals
$K(e_1,e_1)+K(e_1,e_1)=-2-2=-4$.

*Proof.* Insert the explicit form into the two terms and collect; the general expression is the one
displayed, and it is nonzero for a general triple.

**Remark (why no substitute for the Killing form).** The operator trace form is the natural substitute
for the Killing form: symmetric, non-degenerate and canonical. It fails the one property the theory
needs. This is the expected outcome of the absence of a Jacobi identity: the Killing form of a Lie
algebra is invariant because the Jacobi identity makes the adjoint representation a representation, and
here the adjoint map is not a representation, so the trace form of the operators is not invariant
either. The substitute computed here is a form of the **operators** and not an invariant form of the
**block**, and the only invariant form of the block remains the degenerate $\varphi$.

## The Comparison with the Killing Form of the Cross Product

**Remark (the comparator carries a Killing form).** The antisymmetric plain block
$\tilde p\times\tilde q=\vec p\times\vec q$ is a Lie algebra; it carries the Killing form
$\kappa(\tilde p,\tilde q)=\operatorname{Tr}(\operatorname{ad}_{\tilde p}\operatorname{ad}_{\tilde q})=-2\,\vec p\cdot\vec q$,
computed on the cross product and negative definite on the vector subspace, with the centre as radical
(*The Killing Form of the Antisymmetric Plain Algebra*). The block of this article has no such form:
its only invariant form is the degenerate $\varphi$, its coefficient form vanishes, and the trace form
of its operators is non-degenerate but not invariant. The comparison is the exact measure of the loss:
the Killing form exists for the cross product because the Jacobi identity holds, and it has no analogue
here because the Jacobi identity does not. On the vector subspace, where the block is the cross product
up to sign, both $\kappa$ and the operator trace form restrict to multiples of the same Euclidean form
$-\vec p\cdot\vec q$; the two differ only in the scalar factor, and neither is an invariant form
of the block.

## Summary

The antisymmetric quaternionic block has a degenerate invariant-form theory. The invariance condition
$\beta(\tilde p\diamond\tilde q,\tilde r)+\beta(\tilde q,\tilde p\diamond\tilde r)=0$ has a
one-dimensional solution space, spanned by the scalar-part form $\varphi(\tilde p,\tilde q)=p_0q_0$,
symmetric of Gram matrix $\operatorname{diag}(1,0,0,0)$ and rank one, with the vector subspace as
radical; there is no nonzero alternating invariant form. The coefficient form of the block vanishes,
the values having zero scalar part. The operator trace form
$K(\tilde p,\tilde q)=\operatorname{Tr}(L^{\diamond}_{\tilde p}L^{\diamond}_{\tilde q})=3p_0q_0-2\,\vec p\cdot\vec q$
is non-degenerate, of Gram matrix $\operatorname{diag}(3,-2,-2,-2)$, but is not invariant, with the
failure $-4p_0(\vec q\cdot\vec r)+2q_0(\vec p\cdot\vec r)+2r_0(\vec p\cdot\vec q)$;
the absence is the same obstruction as the Jacobi failure. The comparator, the cross product, carries
the Killing form $-2\,\vec p\cdot\vec q$, available because its Jacobi identity holds.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\beta(\tilde p\diamond\tilde q,\tilde r)+\beta(\tilde q,\tilde p\diamond\tilde r)=0$ | the invariance condition |
| $\varphi(\tilde p,\tilde q)=p_0q_0$, Gram $\operatorname{diag}(1,0,0,0)$ | the unique invariant form, symmetric, rank one |
| $\mathrm{Vect}(\mathbb{H})$ | the radical of $\varphi$ |
| $0$ | the alternating invariant forms |
| $\mathrm{Sc}(\tilde p\diamond\tilde q)=0$ | the vanishing of the coefficient form |
| $K(\tilde p,\tilde q)=3p_0q_0-2\,\vec p\cdot\vec q$, Gram $\operatorname{diag}(3,-2,-2,-2)$ | the operator trace form, non-degenerate, not invariant |
| $\kappa(\tilde p,\tilde q)=-2\,\vec p\cdot\vec q$ | the Killing form of the comparator |

## Further Reading

- *Introduction to the Antisymmetric Quaternionic Algebra of Quaternions*, for the product and its zero scalar part.
- *The Jacobi Failure and the Associator Defect of the Antisymmetric Quaternionic Algebra*, below this article in this category, for the obstruction behind the failure of invariance.
- *The Adjoint Operators of the Antisymmetric Quaternionic Algebra*, below this article in this category, for the multiplication operators and their traces.
- *The Killing Form of the Antisymmetric Plain Algebra*, above this article in this category, for the comparator's Killing form.
- *The 2 Forms over the Quaternion $\mathbb{R}$ Space*, for the forms of the parent and the space.
