# __The Adjoint Operators of the Antisymmetric Quaternionic Algebra__

## Introduction

The antisymmetric quaternionic algebra of $\mathbb{H}$ carries the operation
$\tilde p\diamond\tilde q=\tfrac12(\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p)=p_0\mathbf q-q_0\mathbf p-\mathbf p\times\mathbf q$, which fails the Jacobi identity (*The Jacobi
Failure and the Associator Defect of the Antisymmetric Quaternionic Algebra*, below this article in
this category). This article reads its adjoint operators: the left multiplications by an element, their
matrix and invariants, the failure of the derivation property and its identity with the Jacobi failure,
the algebra the operators generate, the derivations of the block, and the comparison with the cross

The block's operators are a deformation of the cross-product operators: the trace is $3p_0$ instead of
$0$, the rank is three instead of two, the kernel is the **line** of the element instead of a plane, the
commutator of two operators deviates from the operator of the value by a term that is the operator form
of the Jacobi failure, and the operation has **no nonzero inner derivation**, all of its derivations
being outer.

**This is not the algebra $\mathbb{H}$.** The operators are read on the block, not on the associative
product. Throughout, the natural sign ${}^{\natural}$ is the quaternion conjugation, the bar is the
identity because $\mathbb{R}$ has no nontrivial involution, and the star coincides with the natural
sign and gives nothing new. The symbol $\diamond$ is reserved for this block.

The operation and its failure are *Introduction to the Antisymmetric Quaternionic Algebra of
Quaternions* and *The Jacobi Failure and the Associator Defect of the Antisymmetric Quaternionic
Algebra*, below this article in this category. The comparator is *The Adjoint Operators and the
chapter.

**Conventions.** The algebra is $\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$ and
$e_1^2=e_2^2=e_3^2=-e_0$; a generic element is $\tilde q=q_0e_0+\mathbf q$, the **centre** is
$\mathbb{R}_{\mathbb{H}}=\mathbb{R}e_0$ and the **vector subspace** is $\mathrm{Vect}(\mathbb{H})=\{\mathbf q\}$.
The **adjoint operator** is the left multiplication $L^{\diamond}_{\tilde p}\tilde q=\tilde p\diamond\tilde q$,
with matrix $M_{\tilde p}$ in the coefficient basis, and the **derivation** is an endomorphism $D$ with
$D(\tilde p\diamond\tilde q)=D\tilde p\diamond\tilde q+\tilde p\diamond D\tilde q$. The **cyclic sum**
is the left-nested one of *The Jacobi Failure and the Associator Defect of the Antisymmetric
Quaternionic Algebra*, below this article in this category.

## The Adjoint Operators

**Proposition.** The adjoint operator of $\tilde p$ is
$L^{\diamond}_{\tilde p}\tilde q=p_0\mathbf q-q_0\mathbf p-\mathbf p\times\mathbf q$, $\mathbb{R}$-linear,
and the map $\tilde p\mapsto L^{\diamond}_{\tilde p}$ is injective, since $L^{\diamond}_{\tilde p}e_0=-\mathbf p$.

**Proposition (the matrix).** In the basis $(e_0,e_1,e_2,e_3)$ the matrix is

$$
M_{\tilde p}=\begin{pmatrix}
0&0&0&0\\
-p_1&p_0&p_3&-p_2\\
-p_2&-p_3&p_0&p_1\\
-p_3&p_2&-p_1&p_0
\end{pmatrix},
$$

the first column being $-\mathbf p$ and the three-by-three block carrying $p_0\mathrm{I}_3-[\mathbf p]_\times$.

*Proof.* The columns are the coordinates of $\tilde p\diamond e_\nu$: at $\nu=0$ the value is $-\mathbf p$;
at $\nu=k$ the value is $p_0e_k-\mathbf p\times e_k$, whose coordinates are $p_0$ on the $k$-th vector
line and the cross terms of $\mathbf p\times e_k$ elsewhere.

**Theorem (the invariants).** The operator has

$$
\operatorname{Tr}M_{\tilde p}=3p_0,\qquad \det M_{\tilde p}=0,\qquad
\operatorname{rank}M_{\tilde p}=\begin{cases}3,&\tilde p\neq0,\\0,&\tilde p=0,\end{cases}
$$

the characteristic polynomial $\chi(t)=t(t-p_0)\bigl((t-p_0)^2+|\mathbf p|^2\bigr)$, the kernel the **line**
$\mathbb{R}\tilde p$, and the image the vector subspace $\mathrm{Vect}(\mathbb{H})$ for $\tilde p\neq0$.

*Proof.* The first row of $M_{\tilde p}$ is zero, so $t$ divides the characteristic polynomial, and the
three-by-three block is $p_0\mathrm{I}_3-[\mathbf p]_\times$, of determinant $p_0(p_0^2+|\mathbf p|^2)$
and trace $3p_0$; the displayed polynomial is the product, and its constant term, the determinant, is
zero. The kernel contains $\mathbb{R}\tilde p$ by alternation and the image lies in the vector subspace
because the values are pure; the rank is three off the origin and zero there, so the kernel is the line
and the image is the whole vector subspace. The trace is the sum of the three diagonal entries $p_0$ on
the vector lines.

**Remark (the kernel is the annihilator).** The kernel is exactly the line of the element, the
computation of *Zero Divisors of the Antisymmetric Quaternionic Algebra*, above this article in this
category; the rank three is the operator form of the total permissiveness of the zero divisors.

## The Derivation Property and Its Failure

**Theorem (the failure, parallel to the Jacobi failure).** The adjoint operators are not derivations, and
their failure is exactly the failure of the Jacobi identity: for all $\tilde p,\tilde q,\tilde r$,

$$
L^{\diamond}_{\tilde p}(\tilde q\diamond\tilde r)-\bigl(L^{\diamond}_{\tilde p}\tilde q\diamond\tilde r+\tilde q\diamond L^{\diamond}_{\tilde p}\tilde r\bigr)
=-\,J(\tilde p,\tilde q,\tilde r),
$$

so the derivation defect vanishes on exactly the triples on which the cyclic sum vanishes; equivalently
the homomorphism property fails with the same defect,

$$
\bigl[L^{\diamond}_{\tilde p},L^{\diamond}_{\tilde q}\bigr]-L^{\diamond}_{\tilde p\diamond\tilde q}=-\,J(\tilde p,\tilde q,\cdot),
\qquad\text{that is}\qquad
\bigl([L^{\diamond}_{\tilde p},L^{\diamond}_{\tilde q}]-L^{\diamond}_{\tilde p\diamond\tilde q}\bigr)\tilde r=-\,J(\tilde p,\tilde q,\tilde r).
$$

The defect is nonzero on $18$ of the $64$ basis triples, and the witness is $(e_0,e_1,e_2)$: there
$L^{\diamond}_{e_0}(e_1\diamond e_2)=-e_3$ against
$L^{\diamond}_{e_0}e_1\diamond e_2+e_1\diamond L^{\diamond}_{e_0}e_2=-e_3-e_3=-2e_3$, a defect $e_3$.

*Proof.* Expanding, the derivation defect is $p\diamond(q\diamond r)-(p\diamond q)\diamond r-q\diamond(p\diamond r)=-J(p,q,r)$
by the closed form of the cyclic sum, and the homomorphism defect is the same operator, $-J$, since it equals the derivation defect. The count and
the witness are the basis computation of *The Jacobi Failure and the Associator Defect of the
Antisymmetric Quaternionic Algebra*, below this article in this category.

**Corollary (the deviation of the commutator).** The commutator of two operators differs from the
operator of the value by the negative of the operator form of the cyclic sum,

$$
\bigl[L^{\diamond}_{\tilde p},L^{\diamond}_{\tilde q}\bigr]=L^{\diamond}_{\tilde p\diamond\tilde q}-J(\tilde p,\tilde q,\cdot),
$$

with $J(\tilde p,\tilde q,\cdot)$ the operator $r\mapsto -p_0(\mathbf q\times\mathbf r)+q_0(\mathbf p\times\mathbf r)-r_0(\mathbf p\times\mathbf q)$,
nonzero for general arguments; the block's adjoint map is therefore not a representation.

## The Derivation Algebra

**Theorem (the derivations are all outer).** The derivation algebra of the block is

$$
\operatorname{Der}(\diamond)=\{\text{the maps annihilating }e_0\text{ and acting on }\mathrm{Vect}(\mathbb{H})\text{ by skew maps}\},
$$

of real dimension three, and every derivation is **outer**: there is no nonzero inner derivation.

*Proof.* Let $D$ be the matrix of a general endomorphism and impose $D(\tilde p\diamond\tilde q)=D\tilde p\diamond\tilde q+\tilde p\diamond D\tilde q$
on the sixteen basis pairs. The system forces the first row and the first column of $D$ to vanish, so
$D(e_0)=0$ and $D$ preserves the vector subspace, and leaves the three-by-three vector block a general
skew matrix; its solution space is therefore the skew maps of the vector subspace, of dimension three.
For the inner derivations, $L^{\diamond}_{\tilde p}e_0=-\mathbf p$ vanishes exactly when $\mathbf p=0$,
and then $L^{\diamond}_{e_0}=\mathrm{diag}(0,1,1,1)$ is not a derivation, so the only inner derivation is
zero.

**Remark (the contrast with the Lie case).** The adjacent block $\mathrm{APA}$ has a three-dimensional
derivation algebra, all of it inner: its adjoint map is a representation and its image is the whole
derivation algebra $\mathfrak{so}(3)$. The block of this article has a three-dimensional derivation
algebra, all of it outer: the adjoint map is not a representation and its image contributes no
derivation. The two derivation algebras are the same algebra, reached in opposite ways.

**Remark (the automorphism group).** An automorphism of the bracket fixes $e_0$: the identity
$T(e_0\diamond\tilde u)=T(e_0)\diamond T\tilde u$ exhibits the left multiplication by $T(e_0)$ as a
rank-three idempotent, and by the matrix above $L^{\diamond}_{\tilde p}$ is a rank-three idempotent only
at $\tilde p=e_0$. It therefore preserves the vector subspace and the cross product on it; the
automorphism group is the group of linear maps of the vector subspace preserving the cross product, of
real dimension three, whose Lie algebra is the derivation algebra above. The structure group, with the
scalar multiplier free, is its product with $\mathbb{R}^{\times}$, of real dimension four.

## The Closure of the Operators

**Theorem (the associative algebra generated).** The four adjoint operators and their products span an
**associative** algebra of linear maps of real dimension **twelve** inside the sixteen-dimensional
algebra of all linear maps of $\mathbb{H}$; adjoined the identity, whose first row is not zero while
every product has first row zero, the algebra has dimension thirteen.

**Theorem (the Lie algebra generated).** The four adjoint operators and their commutators generate a
**Lie** algebra of real dimension **seven**.

*Proof.* Both dimensions are read from the span of the iterated products and brackets of the generators;
the associativity closure is the algebra generated by the four matrices, and no further products are
independent, the operators having first row zero and the products therefore reproducing a
twelve-dimensional subspace. The Lie closure is the span of the operators, of dimension four, and of
their brackets, of dimension six, the two meeting in a three-dimensional subspace; the sum is closed
under commutation and has dimension seven.

**Remark (the closure as the echo of the defect).** The quotient of the sixteen-dimensional algebra by
the twelve-dimensional one has dimension four, and it is the operator echo of the associativity defect
of the parent product.

## The Relation to the Adjoint Operators of the Cross Product

| | the cross product | the antisymmetric quaternionic block |
|---|---|---|
| the operator | $\operatorname{ad}_{\tilde p}=\operatorname{diag}(0,C_{\mathbf p})$ | $M_{\tilde p}$, first column $-\mathbf p$ |
| the trace | $0$ | $3p_0$ |
| the rank | $2$ off the centre | $3$ off the origin |
| the kernel | the plane $\mathbb{R}e_0\oplus\mathbb{R}\mathbf p$ | the line $\mathbb{R}\tilde p$ |
| the commutator formula | $\operatorname{ad}_{\tilde p\times\tilde q}=[\operatorname{ad}_{\tilde p},\operatorname{ad}_{\tilde q}]$ | $[L_{\tilde p},L_{\tilde q}]=L_{\tilde p\diamond\tilde q}-J(\tilde p,\tilde q,\cdot)$ |
| the derivations | three-dimensional, all inner | three-dimensional, all outer |
| the pure part | $\mathbf p\times\cdot$ | $-\mathbf p\times\cdot$ |

**Remark (the deformation).** On pure elements the block is the negative of the cross product, so the
operator of a pure element is the operator of $\mathrm{APA}$ with the sign reversed, a Lie bracket on
the vector subspace; for a general element the two mixed terms $p_0\mathbf q-q_0\mathbf p$ are added,
the trace $3p_0$ appears where it was zero, the kernel shrinks from a plane to the line of the element,
and the commutator acquires the deviation $J$, the operator form of the Jacobi failure.

## Summary

The adjoint operator of the antisymmetric quaternionic block is the left multiplication
$L^{\diamond}_{\tilde p}\tilde q=p_0\mathbf q-q_0\mathbf p-\mathbf p\times\mathbf q$, of matrix with
first column $-\mathbf p$ and vector block $p_0\mathrm{I}_3-[\mathbf p]_\times$, of trace $3p_0$,
determinant zero, rank three off the origin, characteristic polynomial
$t(t-p_0)\bigl((t-p_0)^2+|\mathbf p|^2\bigr)$, kernel the line $\mathbb{R}\tilde p$ and image the vector
subspace. The operators are not derivations: the derivation defect is $-J$ and the homomorphism defect
is $-J$, both zero exactly on the triples on which the cyclic sum vanishes, with the witness
$(e_0,e_1,e_2)$ giving a defect $e_3$; the commutator of two operators is the operator of the value
minus the operator form of the cyclic sum. The operators and their products span an associative algebra
of dimension twelve, thirteen with the identity, and generate a Lie algebra of dimension seven. The
derivations of the block are the skew maps of the vector subspace, of dimension three, and all are
outer, while the comparator $\mathrm{APA}$ has the same three-dimensional derivation algebra all of it
inner. The automorphism group is the group of linear maps of the vector subspace preserving the cross
product, of dimension three. Over $\mathbb{C}$ the operators and their closure agree, with the rank
drop on the isotropic cone.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L^{\diamond}_{\tilde p}\tilde q=\tilde p\diamond\tilde q$ | the adjoint operator |
| first column $-\mathbf p$, block $p_0\mathrm{I}_3-[\mathbf p]_\times$ | the matrix |
| $\operatorname{Tr}=3p_0$, rank $3$, kernel $\mathbb{R}\tilde p$ | the invariants |
| $L^{\diamond}_{\tilde p}(\tilde q\diamond\tilde r)-\dots=-J(\tilde p,\tilde q,\tilde r)$ | the derivation defect, the failure |
| $[L^{\diamond}_{\tilde p},L^{\diamond}_{\tilde q}]-L^{\diamond}_{\tilde p\diamond\tilde q}=-\,J(\tilde p,\tilde q,\cdot)$ | the homomorphism defect |
| $12$ and $7$ | the associative and Lie dimensions of the closure |
| the skew maps of the vector subspace | the derivations, three-dimensional, all outer |

## Further Reading

- *Introduction to the Antisymmetric Quaternionic Algebra of Quaternions*, for the product and its table.
- *The Jacobi Failure and the Associator Defect of the Antisymmetric Quaternionic Algebra*, below this article in this category, for the failure behind the derivation defect.
- *Zero Divisors of the Antisymmetric Quaternionic Algebra*, above this article in this category, for the annihilator that is the kernel.
- *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*, above this article in this category, for the comparator and its inner derivations.
- *The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra*, below this article in this category, for the operator trace form.
