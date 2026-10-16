# __The Jacobi Failure and the Associator Defect of the Antisymmetric Quaternionic Algebra__

## Introduction

The antisymmetric quaternionic multiplication
$\tilde p\diamond\tilde q=\tfrac12(\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p)=p_0\vec q-q_0\vec p-\vec p\times\vec q$ is alternating, vector valued and without a unit,
and it fails the Jacobi identity (*Introduction to the Antisymmetric Quaternionic Algebra of
Quaternions*). This article does the failure in full: the cyclic sum and its closed form, the basis
computation and the witnesses, the criterion that relates the defect to the associator of the parent
quaternionic product, the derived bracket that remains a Lie bracket, and the comparison with the cross

The failure is one linear condition on the scalar parts of the triple: with the cross products as
coefficients, the cyclic sum vanishes exactly on a hyperplane of the scalar triple, and its witness is
the triple $(e_0,e_1,e_2)$, whose value is $-e_3$.

**This is not the algebra $\mathbb{H}$.** The defect is read on the parent product
$\tilde p^{\natural}\tilde q$, not on an associative product. Throughout, the natural sign
${}^{\natural}$ is the quaternion conjugation, the bar is the identity because $\mathbb{R}$ has no
nontrivial involution, and the star coincides with the natural sign and gives nothing new. The symbol
$\diamond$ is reserved for this block.

The operation and its table are *Introduction to the Antisymmetric Quaternionic Algebra of
Quaternions*; the criterion is *The Symmetric and Antisymmetric Parts of an Algebra Product*, and the
associator of the parent is *The Associator and the Ternary Product of the Quaternionic Product*. The
comparator, whose cyclic sum vanishes, is *The Lie Algebra of the Antisymmetric Plain Algebra*, above
*The Jacobi Failure and the Associator Defect of the Antisymmetric Quaternionic Algebra* of the

**Conventions.** The algebra is $\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$ and
$e_1^2=e_2^2=e_3^2=-e_0$; a generic element is $\tilde q=q_0e_0+\vec q$, the **vector subspace** is
$\mathrm{Vect}(\mathbb{H})=\{\vec q\}$ and $\vec p\times\vec q$ is the vector product. The
**cyclic sum** is the left-nested one,

$$
J(\tilde p,\tilde q,\tilde r)
=(\tilde p\diamond\tilde q)\diamond\tilde r
+(\tilde q\diamond\tilde r)\diamond\tilde p
+(\tilde r\diamond\tilde p)\diamond\tilde q ,
$$

and the block satisfies the Jacobi identity exactly when $J$ vanishes identically. The **associator**
of the parent product is
$[\tilde p,\tilde q,\tilde r]=(\tilde p^{\natural}\tilde q)^{\natural}\tilde r-\tilde p^{\natural}(\tilde q^{\natural}\tilde r)$.

## The Cyclic Sum and Its Closed Form

**Theorem (the closed form).** For all $\tilde p,\tilde q,\tilde r$,

$$
J(\tilde p,\tilde q,\tilde r)
=-p_0\,(\vec q\times\vec r)+q_0\,(\vec p\times\vec r)-r_0\,(\vec p\times\vec q).
$$

In particular $J$ is a pure vector for every triple, the scalar part of every cyclic sum is zero, and
$J$ is an $\mathbb{R}$-trilinear alternating map of its three arguments.

*Proof.* Insert the explicit form $\tilde a\diamond\tilde b=a_0\vec b-b_0\vec a-\vec a\times\vec b$
into the three terms. The first factor of each term is a value of the block and has zero scalar part, so
each term is $-c_0\tilde u-\tilde u\times\tilde c$ with $\tilde u$ the bracket of the first two
arguments; collecting the three terms, the double cross products collapse by the identity
$\vec q_a\times(\vec a\times\vec b)=\vec a(\vec q_a,\vec b)-\vec b(\vec q_a,\vec a)$
and the terms with the scalar product of vectors cancel in pairs, leaving the displayed expression.
Alternation follows from the antisymmetry of the cross product.

**Corollary (the vanishing condition).** The cyclic sum vanishes identically in the scalar triple
$(p_0,q_0,r_0)$ exactly when the three vector parts are pairwise parallel; otherwise the triples with
$J=0$ are those whose scalar triple lies in the hyperplane of the coefficients above.

*Proof.* The three coefficients of $p_0,q_0,r_0$ are the three cross products; a cross product vanishes
exactly when its factors are parallel.

## The Basis, the Witnesses and the Measure

**Proposition (the basis decides).** The cyclic sum is trilinear and alternating, so it vanishes
identically exactly when it vanishes on the triples of distinct basis elements, and on the basis

$$
J(e_\mu,e_\nu,e_\rho)=0\ \text{unless } \{\mu,\nu,\rho\}=\{0,j,k\}\ \text{with } j<k,\qquad
J(e_0,e_j,e_k)=-\,e_j\times e_k .
$$

There are three such unordered triples and eighteen ordered triples out of the sixty-four, and the
values are

$$
J(e_0,e_1,e_2)=-e_3,\qquad J(e_0,e_1,e_3)=e_2,\qquad J(e_0,e_2,e_3)=-e_1 ,
$$

the negatives of the three cross products.

*Proof.* Alternation kills the triples with a repeated argument, and a triple without the scalar unit
has all three scalar parts zero, so its cyclic sum vanishes by the closed form; the reduction to
$\{\mu,\nu,\rho\}=\{0,j,k\}$ and the values are the table of the block.

**Theorem (the witness).** At the triple $(e_0,e_1,e_2)$,

$$
J(e_0,e_1,e_2)=(e_0\diamond e_1)\diamond e_2+(e_1\diamond e_2)\diamond e_0+(e_2\diamond e_0)\diamond e_1
=e_1\diamond e_2+(-e_3)\diamond e_0+(-e_2)\diamond e_1=-e_3\neq0 ,
$$

so the block is not a Lie algebra; the minimal witnesses are $(e_0,e_1,e_2)$, $(e_0,e_1,e_3)$ and
$(e_0,e_2,e_3)$.

**Measure (the defect).** The cyclic sum is nonzero on $18$ of the $64$ basis triples; the parent
associator is nonzero on $24$ of the $64$. Both counts are recomputed from the table.

## The Associator Criterion

**Theorem (the criterion).** For an algebra $A$ of characteristic not two with antisymmetrisation
$A^{\wedge}$, the block satisfies the Jacobi identity exactly when the associator of $A$ satisfies the
cyclic identity, equivalently the Jacobi sum of the commutator is the signed sum of the six associators,

$$
[[x,y],z]+[[y,z],x]+[[z,x],y]=\sum_{\sigma\in S_3}\operatorname{sgn}(\sigma)\,[x_{\sigma(1)},x_{\sigma(2)},x_{\sigma(3)}] .
$$

*Proof.* This is *The Symmetric and Antisymmetric Parts of an Algebra Product*, proved there by
expanding the twelve monomials; it is general and is not redone here.

**Corollary (the criterion for the block).** For the antisymmetric quaternionic multiplication, half
the commutator and half the associator stand in the same relation,

$$
J(\tilde p,\tilde q,\tilde r)=\tfrac14\sum_{\sigma\in S_3}\operatorname{sgn}(\sigma)\,[\tilde p_{\sigma(1)},\tilde p_{\sigma(2)},\tilde p_{\sigma(3)}] ,
$$

with the associator taken in the parent product $\tilde p^{\natural}\tilde q$. The block is
Lie-admissible exactly when the parent product is; the parent is not associative, hence the failure.

*Proof.* The commutator of the parent product is $[\tilde p,\tilde q]_{\natural}=2(\tilde p\diamond\tilde q)$,
so the Jacobi sum of the commutator is four times $J$, and the theorem identifies it with the signed sum
of the six associators. The parent product is not associative, so its associator does not vanish
identically, and the criterion is not met.

## The Associator of the Quaternionic Product

**Theorem (the associator).** For the parent product the associator has the closed form

$$
[\tilde p,\tilde q,\tilde r]=\bigl(\tilde q^{\natural}\tilde p-\tilde p^{\natural}\tilde q^{\natural}\bigr)\tilde r ,
$$

and it is nonzero at $(e_1,e_0,e_0)$, where it equals $2e_1$, and at $24$ of the $64$ basis triples.

*Proof.* The closed form uses that ${}^{\natural}$ is an anti-automorphism of order two,
$(\tilde p^{\natural}\tilde q)^{\natural}=\tilde q^{\natural}\tilde p$, whence the associator is the
displayed product; it is verified on general elements and on the basis. The witness is the arithmetic
of the table, $(e_1^{\natural}e_0)^{\natural}e_0=e_1$ against $e_1^{\natural}(e_0^{\natural}e_0)=-e_1$.

**Computation (the criterion at the witness).** On the triple $(e_0,e_1,e_2)$ the six associators are

| ordering | $(\tilde p,\tilde q,\tilde r)$ | $(\tilde q,\tilde r,\tilde p)$ | $(\tilde r,\tilde p,\tilde q)$ | $(\tilde p,\tilde r,\tilde q)$ | $(\tilde q,\tilde p,\tilde r)$ | $(\tilde r,\tilde q,\tilde p)$ |
|---|---|---|---|---|---|---|
| the associator | $0$ | $0$ | $-2e_3$ | $0$ | $2e_3$ | $0$ |

the signed sum of the six is $-4e_3$, and its quarter is the cyclic sum $-e_3$ computed above.

*Proof.* For $(e_0,e_1,e_2)$ the parent product gives $e_0^{\natural}e_1=e_1$ and $e_1^{\natural}e_2=-e_3$,
so $(e_0^{\natural}e_1)^{\natural}e_2=e_1^{\natural}e_2=-e_3$ and $e_0^{\natural}(e_1^{\natural}e_2)=e_0^{\natural}(-e_3)=-e_3$,
and the two agree; the other orderings are the arithmetic of the table, the two survivors being those
that put $e_0$ in the middle slot, $(\tilde r,\tilde p,\tilde q)=(e_2,e_0,e_1)$ with $-2e_3$ and
$(\tilde q,\tilde p,\tilde r)=(e_1,e_0,e_2)$ with $2e_3$.

**Remark (why the defect is the whole failure).** The two nonzero associators are the two orderings with
$e_0$ in the middle slot, exchanged by the transposition of the outer arguments; the identity would hold
at this triple if they cancelled, and their two signs are the two signs of the transposition. It is the
conjugation in the first slot of the parent product that prevents the cancellation, and the defect of the
block is therefore the non-associativity of the parent alone.

## The Derived Bracket

**Proposition (the derived bracket is a Lie bracket).** The image of the block is the vector subspace,
$\mathbb{H}\diamond\mathbb{H}=\mathrm{Vect}(\mathbb{H})$, and it is closed under the operation. On it
the block is the negative of the cross product,

$$
\vec p\diamond\vec q=-\,\vec p\times\vec q ,
$$

which satisfies the Jacobi identity; the subalgebra $(\mathrm{Vect}(\mathbb{H}),\diamond)$ is therefore
a Lie algebra, isomorphic to the antisymmetric plain block and hence to $\mathfrak{so}(3)$.

*Proof.* The image is the vector subspace and the closure is read on the table,
$e_j\diamond e_k=-e_j\times e_k\in\mathrm{Vect}(\mathbb{H})$. On pure vectors the scalar factors of the
closed form all vanish, so $J$ vanishes identically there, and the remaining Lie axioms are alternation
and bilinearity; the negative of the cross product is the same bracket with every bracket reversed, and
it is the antisymmetric plain operation $\mathrm{APA}$ of *The Lie Algebra of the Antisymmetric Plain
Algebra*, above this article in this category, of structure $\mathfrak{so}(3)$.

**Remark (the failure is the scalar–vector interaction).** The block is a Lie bracket on
$\mathrm{Vect}(\mathbb{H})$ and not on $\mathbb{H}$: the derived bracket is the cross product and is
closed and Lie, and what the block adds to it is the two mixed terms $p_0\vec q-q_0\vec p$, which
carry the scalar part into the vector subspace and break the identity. The failure is thus the failure
of the extension, not of the derived bracket.

## Summary

The antisymmetric quaternionic block fails the Jacobi identity. Its cyclic sum is the pure vector
$J(\tilde p,\tilde q,\tilde r)=-p_0(\vec q\times\vec r)+q_0(\vec p\times\vec r)-r_0(\vec p\times\vec q)$,
linear in the scalar triple with the three cross products as coefficients; it vanishes identically in
the scalar triple exactly on the pairwise parallel vector parts, and it is nonzero on $18$ of the $64$
basis triples. The witness is $(e_0,e_1,e_2)$, of value $-e_3$, and the minimal witnesses are the three
triples $\{0,j,k\}$. The defect is exactly the associator defect of the parent product,
$J=\tfrac14\sum_\sigma\operatorname{sgn}(\sigma)\,[\tilde p_\sigma,\tilde q_\sigma,\tilde r_\sigma]$,
the associator having the closed form $(\tilde q^{\natural}\tilde p-\tilde p^{\natural}\tilde q^{\natural})\tilde r$
and nonzero on $24$ of the $64$ basis triples, with the witness $(e_1,e_0,e_0)=2e_1$. The derived
bracket remains a Lie bracket: on the vector subspace the block is the negative of the cross product,
of structure $\mathfrak{so}(3)$, and the failure is exactly the scalar–vector interaction the block adds
to it.
same way and has $\mathfrak{sl}(2,\mathbb{C})$ as derived algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $J(\tilde p,\tilde q,\tilde r)=(x\diamond y)\diamond z+(y\diamond z)\diamond x+(z\diamond x)\diamond y$ | the cyclic sum |
| $-p_0(\vec q\times\vec r)+q_0(\vec p\times\vec r)-r_0(\vec p\times\vec q)$ | the closed form |
| $J(e_0,e_1,e_2)=-e_3$ | the witness of the failure |
| $[\tilde p,\tilde q,\tilde r]=(\tilde p^{\natural}\tilde q)^{\natural}\tilde r-\tilde p^{\natural}(\tilde q^{\natural}\tilde r)$ | the associator of the parent |
| $(\tilde q^{\natural}\tilde p-\tilde p^{\natural}\tilde q^{\natural})\tilde r$ | the closed form of the associator |
| $J=\tfrac14\sum_\sigma\operatorname{sgn}(\sigma)\,[\tilde p_\sigma,\tilde q_\sigma,\tilde r_\sigma]$ | the criterion |
| $\vec p\diamond\vec q=-\vec p\times\vec q$ | the derived bracket, a Lie bracket of structure $\mathfrak{so}(3)$ |

## Further Reading

- *Introduction to the Antisymmetric Quaternionic Algebra of Quaternions*, for the product, its table and the announcement of the failure.
- *The Symmetric and Antisymmetric Parts of an Algebra Product*, for the associator criterion.
- *The Associator and the Ternary Product of the Quaternionic Product*, for the associator of the parent product.
- *The Lie Algebra of the Antisymmetric Plain Algebra*, above this article in this category, for the comparator and its structure.
- *The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra* and *The Adjoint Operators of the Antisymmetric Quaternionic Algebra*, both below this article in this category, for the form and the operators of the failing block.
