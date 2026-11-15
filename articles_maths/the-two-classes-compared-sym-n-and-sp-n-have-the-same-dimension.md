# __The Two Classes Compared: $\operatorname{Sym}_n$ and $\mathfrak{sp}_n$ Have the Same Dimension__

## Introduction

**The transpose and the symplectic map fix spaces of the same dimension, $n(n+1)/2$, and the two spaces are not the same kind of object: one is a Jordan algebra, the other a Lie algebra, and no linear isomorphism carries the product of one to the product of the other.**

The article computes the two dimensions from the defining equations, proves the sign in the product rule of $\sigma_J$, counts how many commutators stay inside each fixed space, computes the signature of the trace form on each, and isolates the three invariants that separate the two classes. It assumes *The Involutions of the First Kind: Transpose and Symplectic* for the classification and *The Two Halves: Symmetric and Antisymmetric* for the Jordan structure. It supplies what the dimension count alone cannot.

Throughout $n$ is even and $J$ is the standard alternating matrix, the block-diagonal array of $n/2$ copies of $\begin{pmatrix}0&1\\ -1&0\end{pmatrix}$. Then

$$
J^{\mathsf T}=-J,\qquad J^{2}=-\mathrm{I},\qquad J^{-1}=-J.
$$

## The Two Maps

**The transpose and the symplectic map are the two involutions of the first kind over $\mathbb{R}$.** Define

$$
\sigma(X)=X^{\mathsf T},\qquad \sigma_J(X)=-JX^{\mathsf T}J^{-1}.
$$

Both are $\mathbb{R}$-linear, both reverse the order of a product, and both have order two.

**The symplectic map has order two.** Using $J^{-1}=J^{\mathsf T}=-J$,

$$
\sigma_J(\sigma_J(X))=-J\bigl(-JX^{\mathsf T}J^{-1}\bigr)^{\mathsf T}J^{-1}=J\,(J^{-1})^{\mathsf T}XJ^{\mathsf T}J^{-1}=-J^{2}X=X,
$$

since $(J^{-1})^{\mathsf T}J=J^{-1}J=\mathrm{I}$ and $J^{\mathsf T}J^{-1}=(-J)(-J)=-\mathrm{I}$. So $\sigma_J^{2}=\mathrm{id}$ and the algebra splits into a $+1$ space and a $-1$ space for $\sigma_J$.

**The two maps are not conjugate.** The transpose satisfies $\sigma(XY)=\sigma(Y)\sigma(X)$ and the symplectic map satisfies $\sigma_J(XY)=-\sigma_J(Y)\sigma_J(X)$. A conjugation preserves that sign, so the two classes are disjoint. The classification is the subject of *The Involutions of the First Kind: Transpose and Symplectic*; the comparison of the fixed spaces is the subject here.

## The Dimension Count

**The fixed space of $\sigma_J$ is the image of the symmetric matrices under $X\mapsto -JX$.** The equation $\sigma_J(X)=X$ is equivalent to $JX\in\operatorname{Sym}_n$. The map $S\mapsto -JS$ is invertible, so

$$
\{X:\sigma_J(X)=X\}=J^{-1}\operatorname{Sym}_n=\{X:JX\in\operatorname{Sym}_n\},
$$

and the dimension is that of $\operatorname{Sym}_n$, namely $n(n+1)/2$. The space is $\mathfrak{sp}_n$, the symplectic Lie algebra.

**The two dimensions agree at every even order.** Measured as the rank of the projection of the $n^{2}$ matrix units under $\tfrac12(X+\sigma_J(X))$, the dimension of $\mathfrak{sp}_n$ is $3$, $10$, $21$ at $n=2,4,6$. The dimension of $\operatorname{Sym}_n$ is $3$, $10$, $21$ at the same orders. Neither number separates the two classes.

**The two spaces are not equal, and their intersection is large.** The intersection is $\{S:SJ=-JS\}$, the symmetric matrices anticommuting with $J$. Measured by solving the two linear conditions together, its dimension is $2$, $6$, $12$ at $n=2,4,6$, which is $m(m+1)$ for $m=n/2$. Equal dimension does not mean equal space, and it does not mean disjoint spaces either.

**Definition.** $\mathfrak{sp}_n=\{X\in M_n(\mathbb{R}):JX\in\operatorname{Sym}_n\}$ and $\operatorname{Sym}_n=\{S:S^{\mathsf T}=S\}$.

## The Sign in the Product Rule

**The symplectic map reverses the product up to a sign, and the sign is $-1$.** For all $X,Y$,

$$
\sigma_J(XY)=-J\,(XY)^{\mathsf T}J^{-1}=-JY^{\mathsf T}X^{\mathsf T}J^{-1},
$$

while

$$
\sigma_J(Y)\sigma_J(X)=JY^{\mathsf T}J^{-1}JX^{\mathsf T}J^{-1}=JY^{\mathsf T}X^{\mathsf T}J^{-1}.
$$

The two right-hand sides differ by the sign, hence $\sigma_J(XY)=-\sigma_J(Y)\sigma_J(X)$. Measured on $100$ random pairs at each of $n=2,4,6$, the identity held in $100$ cases out of $100$.

**The mechanism is that the middle factors cancel.** The two minus signs of the two factors multiply to $+1$, and $J^{-1}J=\mathrm{I}$ cancels in the middle, so $\sigma_J(Y)\sigma_J(X)$ keeps a $+J$ where $\sigma_J(XY)$ has a $-J$. The plain transpose has no such factors, and its sign is $+1$.

**The sign decides which operation survives on the fixed space.** Reversing a product up to $-1$ turns the commutator into itself and the anticommutator into its negative. That is the content of the next section.

## One Space Is Closed under the Commutator

**Theorem.** $\mathfrak{sp}_n$ is closed under the commutator, and $\operatorname{Sym}_n$ is not.

*Proof.* Let $X,Y$ be fixed by $\sigma_J$. Then

$$
\sigma_J([X,Y])=\sigma_J(XY)-\sigma_J(YX)=-\sigma_J(Y)\sigma_J(X)+\sigma_J(X)\sigma_J(Y)=-YX+XY=[X,Y],
$$

so $[X,Y]\in\mathfrak{sp}_n$. For the transpose and symmetric $X,Y$,

$$
\sigma([X,Y])=\sigma(XY)-\sigma(YX)=YX-XY=-[X,Y],
$$

so $[X,Y]$ is anti-Hermitian, and it is nonzero for a generic pair.

**The measurement matches the proof.** On $100$ random pairs of elements of $\mathfrak{sp}_n$ at each of $n=2,4,6$, the commutator was fixed by $\sigma_J$ in $100$ cases out of $100$. On $100$ random pairs of symmetric matrices, the commutator was symmetric in $0$ cases out of $100$.

**The same sign puts the anticommutator on the other side.** For fixed $X,Y$,

$$
\sigma_J(XY+YX)=-(XY+YX).
$$

So the anticommutator of two elements of $\mathfrak{sp}_n$ lands in the $-1$ space of $\sigma_J$, of dimension $n(n-1)/2$. For the transpose the two roles are exchanged: the anticommutator of two symmetric matrices is symmetric, and the commutator is antisymmetric.

**So the two spaces carry dual structures.** $\operatorname{Sym}_n$ is a Jordan algebra of dimension $n(n+1)/2$ under $\circ$, and $\mathfrak{sp}_n$ is a Lie algebra of the same dimension under $[\,,\,]$. The dimensions coincide and the operations differ.

## The Trace Form on the Two Spaces

**The trace form is positive definite on $\operatorname{Sym}_n$.** $\operatorname{tr}(S^{2})=\sum_{i,j}S_{ij}^{2}$ for symmetric $S$, and the sum is nonzero for $S\ne0$. So the form has signature $(n(n+1)/2,0)$ there, and the restriction is an inner product.

**The trace form is indefinite on $\mathfrak{sp}_n$.** Write an element of $\mathfrak{sp}_n$ as $-JS$ with $S$ symmetric. Then

$$
\operatorname{tr}((-JS)^{2})=\operatorname{tr}(JSJS),
$$

and the sign of the right-hand side depends on $S$, because $J$ is antisymmetric. Measured on the basis $\{-JE^{(ij)}\mid i\le j\}$, where $E^{(ij)}$ runs over the standard symmetric basis, the Gram matrix of $\operatorname{tr}(XY)$ on $\mathfrak{sp}_n$ has signature

$$
(2,1)\ \text{at}\ n=2,\qquad (6,4)\ \text{at}\ n=4,\qquad (12,9)\ \text{at}\ n=6.
$$

Both signs occur as soon as $n\ge2$, so the restriction is indefinite. Its negative index is $1$, $4$, $9$ at $n=2,4,6$, which is $(n/2)^{2}$, and its positive index is $n(n+1)/2-(n/2)^{2}$, namely $2$, $6$, $12$.

**Definiteness is a real phenomenon.** Over $\mathbb{C}$ the two restrictions have complex values and no sign, so the statement that separates the two classes here has no content there. This is the third thing the real field adds, after the signature of a symmetric form and the two components of $\mathrm{GL}_n(\mathbb{R})$.

## The Three Invariants

**Three numbers and signs are available, and only one of them fails to separate.** They are:

- the dimension of the space: $n(n+1)/2$ for both;
- the dimension of the Lie hull, the Lie algebra generated inside $\mathfrak{gl}_n(\mathbb{R})$: $n^{2}$ for $\operatorname{Sym}_n$ and $n(n+1)/2$ for $\mathfrak{sp}_n$;
- the definiteness of the trace form: positive definite for $\operatorname{Sym}_n$ and indefinite for $\mathfrak{sp}_n$.

**The Lie hull of $\operatorname{Sym}_n$ is the whole algebra.** The commutator of two symmetric matrices is antisymmetric, and the commutators span the whole of $\operatorname{Skew}_n$: measured on the brackets of the standard symmetric basis, the span has dimension $1$, $3$, $6$ at $n=2,3,4$, which is $n(n-1)/2$ in each case. So the Lie algebra generated by $\operatorname{Sym}_n$ contains $\operatorname{Sym}_n$ and $\operatorname{Skew}_n$, hence is $\mathfrak{gl}_n(\mathbb{R})$ of dimension $n^{2}$.

**The Lie hull of $\mathfrak{sp}_n$ is $\mathfrak{sp}_n$ itself.** It is already a Lie subalgebra of dimension $n(n+1)/2$, so the Lie algebra it generates is itself. The two Lie hulls differ in dimension by $n(n-1)/2$.

**The dimension of the space is therefore the only invariant that agrees.** The comparison of the two classes is the comparison of the other two, and the negative result of the next section follows.

## No Linear Isomorphism Carries One Product to the Other

**Theorem.** There is no linear isomorphism $\varphi:\operatorname{Sym}_n\to\mathfrak{sp}_n$ and no nonzero scalar $c$ with

$$
\varphi(X\circ Y)=c\,[\varphi(X),\varphi(Y)]
$$

for all symmetric $X,Y$.

*Proof.* Take $X=Y$. Then $X\circ X=X^{2}$ and $[\varphi(X),\varphi(X)]=0$, so $\varphi(X^{2})=0$ for every $X$. Every symmetric matrix is a combination of squares, because

$$
S=\tfrac12\bigl((S+\mathrm{I})^{2}-S^{2}-\mathrm{I}\bigr),
$$

so $\varphi$ vanishes on a spanning set of $\operatorname{Sym}_n$, hence $\varphi=0$, which contradicts injectivity.

**The proof uses only the alternating law.** The bracket satisfies $[Z,Z]=0$ for every $Z$, and the Jordan product does not: $X\circ X=X^{2}$ is nonzero for an invertible $X$. The alternating law is the obstruction, and it is the Lie-theoretic shadow of the sign in the product rule.

**Measured on squares the same statement holds.** On $100$ random symmetric matrices at each of $n=2,3,4$ the squares span the whole of $\operatorname{Sym}_n$, of dimensions $3$, $6$, $10$. So the step that uses the identity above is not a formality on a thin set.

## The Case $n=2$

**At $n=2$ the symplectic Lie algebra is $\mathfrak{sl}_2(\mathbb{R})$.** An element of $\mathfrak{sp}_2$ is $X=-JS$ with $S$ symmetric, and

$$
\operatorname{tr}X=-\operatorname{tr}(JS)=0,
$$

because $JS=\begin{pmatrix}b&c\\ -a&-b\end{pmatrix}$ for $S=\begin{pmatrix}a&b\\ b&c\end{pmatrix}$ has zero trace. Both spaces are $3$-dimensional, and $\mathfrak{sp}_2=\mathfrak{sl}_2(\mathbb{R})$ has trace zero while $\operatorname{Sym}_2$ contains $\mathrm{I}$.

**The intersection is $2$-dimensional and the union is the algebra.** The trace-zero symmetric matrices form a plane inside both, so $\operatorname{Sym}_2\cap\mathfrak{sp}_2$ has dimension $2$ and $\operatorname{Sym}_2+\mathfrak{sp}_2$ has dimension $4$, the whole algebra. At this order the trace form is positive definite on $\operatorname{Sym}_2$ with signature $(3,0)$ and indefinite on $\mathfrak{sp}_2$ with signature $(2,1)$, which is the signature of the trace form on $\mathfrak{sl}_2(\mathbb{R})$.

**At $n=2$ the two classes are therefore easiest to tell apart.** The dimensions agree, the spaces overlap in a plane, and a single eigenvalue sign of the trace form decides which space is which. The general case keeps the same picture, with the intersection growing as $m(m+1)$.

## Summary

The transpose and the symplectic map $\sigma_J(X)=-JX^{\mathsf T}J^{-1}$ are the two involutions of the first kind of $M_n(\mathbb{R})$, and their fixed spaces $\operatorname{Sym}_n$ and $\mathfrak{sp}_n$ both have dimension $n(n+1)/2$, measured as $3$, $10$, $21$ at $n=2,4,6$. The symplectic map reverses products up to a sign, $\sigma_J(XY)=-\sigma_J(Y)\sigma_J(X)$, so its fixed space is closed under the commutator while $\operatorname{Sym}_n$ is not: $100$ of $100$ commutators stay in $\mathfrak{sp}_n$, and $0$ of $100$ commutators of symmetric matrices are symmetric. The trace form is positive definite on $\operatorname{Sym}_n$ and indefinite on $\mathfrak{sp}_n$ with signature $(2,1)$, $(6,4)$, $(12,9)$ at $n=2,4,6$. The three invariants are the dimension of the space, which agrees, the dimension of the Lie hull, which is $n^{2}$ against $n(n+1)/2$, and definiteness, which is positive against indefinite. The alternating law of the bracket forbids a linear isomorphism between the two products.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $J$ | the standard alternating matrix, $J^{\mathsf T}=-J$, $J^{2}=-\mathrm{I}$ |
| $\sigma(X)=X^{\mathsf T}$ | the transpose, an involution of the first kind with sign $+$ |
| $\sigma_J(X)=-JX^{\mathsf T}J^{-1}$ | the symplectic involution, of the first kind with sign $-$ |
| $\operatorname{Sym}_n$ | the fixed space of the transpose, a Jordan algebra of dimension $n(n+1)/2$ |
| $\mathfrak{sp}_n=J^{-1}\operatorname{Sym}_n$ | the fixed space of $\sigma_J$, a Lie algebra of dimension $n(n+1)/2$ |
| $X\circ Y=\tfrac12(XY+YX)$ | the anticommutator, closed on $\operatorname{Sym}_n$ |
| $[X,Y]=XY-YX$ | the commutator, closed on $\mathfrak{sp}_n$ |
| $\operatorname{tr}(XY)$ | the trace form, definite on $\operatorname{Sym}_n$ and indefinite on $\mathfrak{sp}_n$ |
| $m=n/2$ | half the order, the number of $2\times2$ blocks of $J$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the symplectic group and the matrices that satisfy $JX$ symmetric.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the two types of involution and their fixed spaces.
- [The Involutions of the First Kind: Transpose and Symplectic](the-involutions-of-the-first-kind-transpose-and-symplectic.html), for the classification of the two types.
- [The Two Halves: Symmetric and Antisymmetric](the-two-halves-symmetric-and-antisymmetric-over-r.html), for the Jordan structure of $\operatorname{Sym}_n$.
- [The Two Halves as Orthogonal Complements for the Trace Form](the-two-halves-as-orthogonal-complements-for-the-trace-form.html), for the signature of the trace form on the whole algebra.
