# __The Realification and the Effect of the Change of Scalars__

## Introduction

The complex numbers carry two readings of one algebra: over $\mathbb{C}$, where the space has dimension one, and over $\mathbb{R}$, where the same space has dimension two. This article is the passage from the first reading to the second, the **realification**, and the effect of the change of scalars on the products and on the two forms. It is the **prototype** of the general construction of *The Realification and the Effect of the Change of Scalars*.

The space itself, its two scalar readings, the complex structure $J$ of multiplication by $i$, the criteria $TJ=JT$ and $SJ=-JS$ for the two kinds of real-linear map and their block shapes are those of *The Complex Numbers as a Vector Space over $\mathbb{R}$*, above this article in this category, and are recalled here only where the realification of the forms needs them. The two products are *The Two Products of the Complexoid Space*; the two forms and their algebraic norms are *The Two Forms and the Two Algebraic Norms of the Complexoid Space*, above this article in this category, and the realified signatures stated there, $(1,1)$ and $(2,0)$, are derived here from the two rules of the construction.

## The Two Scalar Interpretations and the Doubling of the Dimension

Read over itself, $\mathbb{C}$ is the one-dimensional complex space with basis $1$; read over $\mathbb{R}$, it is the two-dimensional real space with basis $1$, $i$, and the two coordinates are the real and imaginary parts,

$$
Q_1=q_1+iq'_1\longleftrightarrow (q_1,q'_1)\in\mathbb{R}^{2}.
$$

The passage is the **restriction of scalars**: the set of elements and the multiplication are the same, and only the field of scalars is restricted, from $\mathbb{C}$ to $\mathbb{R}$. The dimension doubles, $1$ becoming $2$, and the complex scalars, which were multiplications by elements, are replaced by the two real scalars in the two coordinates.

**Realification is not the inverse of complexification.** Complexifying the real line $\mathbb{R}$ gives $\mathbb{C}$ by tensoring with $\mathbb{C}$, but complexifying the realified plane $\mathbb{R}^{2}$ gives $\mathbb{C}^{2}$ and not $\mathbb{C}$; the object the realification forgets is not the field alone but the complex structure, and it is restored by hand, as follows.

## The Complex Structure and the Recovery of the Space

The **complex structure** of the realified space is the operator

$$
J(Q_1)=iQ_1,\qquad J(q_1,q'_1)=(-q'_1,q_1),
$$

which is $\mathbb{R}$-linear, is not $\mathbb{C}$-linear, and satisfies $J^{2}=-\operatorname{id}$. The map $J$ has no real eigenvalue, since $J(Q_1)=\lambda Q_1$ with $\lambda\in\mathbb{R}$ forces $Q_1=0$, so the only $J$-stable real subspaces are $\{0\}$ and the whole space; equivalently, the complex subspaces of the one-dimensional complex space are $\{0\}$ and $\mathbb{C}$. The two remarkable subspaces are not $J$-stable: $J$ exchanges them,

$$
J(\mathbb{R}_{\mathbb{C}})=i\mathbb{R}_{\mathbb{C}},\qquad J(i\mathbb{R}_{\mathbb{C}})=\mathbb{R}_{\mathbb{C}},
$$

and they are the two eigenspaces of the bar and not of $J$.

**Recovery.** Given the realified space together with $J$, the complex structure is restored by defining the product of a complex scalar $\lambda=a+ib$ with an element $Q_1$ as $aQ_1+bJ(Q_1)$; the space with this scalar multiplication is the complex space again, and multiplication by $i$ is $J$. Realification loses $J$ and restricts the scalars; the pair consisting of the realified space and its operator $J$ recovers both.

## The Interplay of the Complex Structure with the Two Products

The two products are real-bilinear after the realification. The complex structure is multiplication by an element of the algebra, so it commutes with the multiplication in both slots and anticommutes with the conjugation in the conjugated slot:

$$
\boxed{\;J(Q_1Q_2)=(JQ_1)Q_2=Q_1(JQ_2),\qquad J(Q_1\bar Q_2)=(JQ_1)\bar Q_2,\qquad Q_1\overline{(JQ_2)}=-J(Q_1\bar Q_2)\;}.
$$

The plain product $Q_1Q_2$ is therefore $J$-linear in both slots, and it is the realification of the complex-bilinear product of the algebra; the sesquilinear product $Q_1\bar Q_2$ is $J$-linear in the first slot and $J$-antilinear in the second, since the conjugation negates $J$. The two products are distinct real-bilinear operations, and the realification does not merge them; it is the complex structure that records how they differ.

## The Two Kinds of Real-Linear Map

A real-linear map $T$ of $\mathbb{C}$ is complex-linear exactly when it commutes with $J$, and a real-linear map $S$ is conjugate-linear exactly when it anticommutes with $J$:

$$
T(JQ_1)=J(TQ_1)\Longleftrightarrow TJ=JT,\qquad S(JQ_1)=-J(SQ_1)\Longleftrightarrow SJ=-JS.
$$

The bar is the model conjugate-linear map, and the multiplication by an element is the model complex-linear one. In the basis $1$, $i$, and with each complex entry replaced by its $2\times2$ real block, a complex-linear map of matrix $X$ has the **block shape** of a commuting map,

$$
\boxed{\;T=\begin{pmatrix}\Re X&-\Im X\\ \Im X&\Re X\end{pmatrix}\;},
$$

and a conjugate-linear map of the same formal matrix $X$ has the block shape of an anticommuting one,

$$
S=\begin{pmatrix}\Re X&\Im X\\ \Im X&-\Re X\end{pmatrix}.
$$

At $n=1$ the matrix $X$ is the complex number $Q_1=q_1+iq'_1$, and multiplication by $Q_1$ and the map $Q_2\mapsto Q_1\bar Q_2$ have the matrices

$$
\begin{pmatrix}q_1&-q'_1\\ q'_1&q_1\end{pmatrix},\qquad\begin{pmatrix}q_1&q'_1\\ q'_1&-q_1\end{pmatrix}.
$$

The first commutes with $J$ and has trace $2q_1$ and determinant $q_1^{2}+q'^2_1=\langle Q_1\rangle_{*}$; the second anticommutes with $J$ and has trace $0$ and determinant $-(q_1^{2}+q'^2_1)=-\langle Q_1\rangle_{*}$. The two kinds of real-linear map are therefore told apart by their commutation with $J$, and at $n=1$ by the vanishing of the trace and the sign of the determinant. The first matrix is the regular representation of the algebra, read in *The Matrix Element Representations of the Complex Numbers*, above this article in this category, where its determinant and trace are identified with the two algebraic norms.

## The Realification of the Two Forms

A form on the complex space, read on the realified space, is a form on a real space of twice the dimension, and its realified signature is given by one of two rules.

**A symmetric complex-bilinear form**, of rank $n$, realifies to the **split signature** $(n,n)$. The reason is that the complex structure flips the sign of the form, $\langle iQ_1,iQ_2\rangle=-\langle Q_1,Q_2\rangle$; on each complex line and its image under $J$ the realified form therefore takes opposite values, and the $n$ positive directions are balanced by $n$ negative ones.

**A Hermitian form**, of inertia $(n,m)$, realifies to the **doubled inertia** $(2n,2m)$. Its realification is the real part of the form, and the complex structure preserves that real part, $\langle iQ_1,iQ_2\rangle_{*}=\langle Q_1,Q_2\rangle_{*}$; on each complex line the real part is therefore read twice, once on the line and once on its image under $J$, and the inertia doubles. The conjugation in the second slot is what makes the difference, since it carries $\langle Q_1,iQ_2\rangle_{*}$ to $-i\langle Q_1,Q_2\rangle_{*}$ and so places the second copy with the sign that keeps the real part.

On the two forms of the complex space, of rank and inertia one, the rules give

$$
\boxed{\;\langle\cdot,\cdot\rangle\longrightarrow(1,1),\qquad \langle\cdot,\cdot\rangle_{*}\longrightarrow(2,0)\;},
$$

the signatures stated in *The Two Forms and the Two Algebraic Norms of the Complexoid Space*, above this article in this category. The realified Gram matrix of $\langle\cdot,\cdot\rangle$ is $\operatorname{diag}(1,-1)$, since the complex Gram matrix $[1]$ is real, and that of $\langle\cdot,\cdot\rangle_{*}$ is the identity $\mathrm{id}_2$. The form $\langle\cdot,\cdot\rangle$ is anisotropic over $\mathbb{C}$ and indefinite after realification; the two facts are read on different fields, the first on the complex values $Q_1^{2}$ and the second on their real parts $q_1^{2}-q'^2_1$.

## The Dictionary of the Complex Statements against the Real Ones

| the complex statement | the real statement |
|---|---|
| the space has dimension $1$ | the space has dimension $2$ |
| an element $Q_1=q_1+iq'_1$ | the pair $(q_1,q'_1)$ of real coordinates |
| the imaginary unit $i$ | the complex structure $J$, $J^{2}=-\operatorname{id}$ |
| multiplication by $Q_1$ | the matrix $\left(\begin{smallmatrix}q_1&-q'_1\\ q'_1&q_1\end{smallmatrix}\right)$, commuting with $J$ |
| the bar $\bar{\cdot}$ | the conjugate-linear maps, $SJ=-JS$ |
| a complex subspace, of complex dimension $m$ | a $J$-stable real subspace, of real dimension $2m$; here $\{0\}$ and $\mathbb{C}$ |
| a complex-linear map $T$ | the commutation $TJ=JT$ and the block shape of $T$ |
| the bilinear form $\langle\cdot,\cdot\rangle$ of rank $1$ | a form of split signature $(1,1)$ |
| the Hermitian form $\langle\cdot,\cdot\rangle_{*}$ of inertia $(1,0)$ | a form of signature $(2,0)$ |
| the automorphisms of $\mathbb{C}$ over itself, $\{1\}$ | the real-algebra automorphisms $\{1,\bar{\cdot}\}$ |
| the ideals, the idempotents, the zero divisors, the nilpotents, the units | unchanged by the change of scalars |

Two rows carry the substance of the dictionary. The row of the automorphisms: the bar is not complex-linear but is real-linear, so it appears as an automorphism only in the real reading, and the automorphism group grows from one element to two, the Galois twist of the change of scalars. The last row: the classes of element and the structure of the ring are unchanged, because $i$ is an element of the algebra and not an external scalar; passing to the real reading changes the field of coefficients and the dimension, not the algebra.

## The Trap of the Count of Operations

The realification doubles the dimension and leaves the two products distinct, so a reader who expects the count of operations to fall is looking in the wrong place. The trap is met one step earlier, on the **real subspace**: there the two products coincide, $Q_1\bar Q_2=Q_1Q_2$, because the bar fixes a real element, so a computation carried out on real elements sees one operation where the complex space has two. The count of two is recovered only by the imaginary elements, on which the two products are opposite (see *Remarkable Subspaces of the Complexoid and the Two Forms*, above this article in this category); the realification preserves that distinction and does not create it.

## Summary

The realification reads the one-dimensional complex space as the two-dimensional real space with basis $1$, $i$, restricting the scalars from $\mathbb{C}$ to $\mathbb{R}$ and doubling the dimension; the complex structure $J$ of multiplication by $i$ is $\mathbb{R}$-linear, not $\mathbb{C}$-linear, with $J^{2}=-\operatorname{id}$, no real eigenvalue, and the only $J$-stable real subspaces $\{0\}$ and $\mathbb{C}$, and the pair of the realified space and $J$ recovers the complex space. Realification is not the inverse of complexification; it is $J$ that is lost and $J$ that is restored. The two products stay distinct after the realification, and the complex structure records the difference by commuting with both slots of $Q_1Q_2$ and anticommuting with the conjugated slot of $Q_1\bar Q_2$. A symmetric complex-bilinear form of rank $n$ realifies to the split signature $(n,n)$ and a Hermitian form of inertia $(n,m)$ to $(2n,2m)$; on the two forms of the complex space this gives $(1,1)$ for $\langle\cdot,\cdot\rangle$ and $(2,0)$ for $\langle\cdot,\cdot\rangle_{*}$. The classes of element and the structure of the ring are unchanged, and the only count that falls is the count of the products on the real subspace, where they coincide.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{C}$ over $\mathbb{C}$ | the space of complex dimension $1$, basis $1$ |
| $\mathbb{C}$ over $\mathbb{R}$ | the realified space, real dimension $2$, basis $1$, $i$ |
| $Q_1=q_1+iq'_1$ | an element in the two coordinates |
| $J(Q_1)=iQ_1$ | the complex structure, $J^{2}=-\operatorname{id}$ |
| $TJ=JT$ | the criterion for a complex-linear real-linear map |
| $SJ=-JS$ | the criterion for a conjugate-linear real-linear map |
| $\left(\begin{smallmatrix}\Re X&-\Im X\\ \Im X&\Re X\end{smallmatrix}\right)$, $\left(\begin{smallmatrix}\Re X&\Im X\\ \Im X&-\Re X\end{smallmatrix}\right)$ | the two block shapes, commuting and anticommuting |
| $\langle Q_1,Q_2\rangle=Q_1Q_2$, $\langle Q_1,Q_2\rangle_{*}=Q_1\bar Q_2$ | the two forms, of rank and inertia one |
| $(1,1)$, $(2,0)$ | the realified signatures of $\langle\cdot,\cdot\rangle$ and of $\langle\cdot,\cdot\rangle_{*}$ |
| $\mathbb{R}_{\mathbb{C}}$, $i\mathbb{R}_{\mathbb{C}}$ | the two remarkable subspaces, exchanged by $J$ |

## Further Reading

- *The Complex Numbers as a Vector Space over $\mathbb{R}$*, above this article in this category, for the two scalar readings of $\mathbb{C}$, the complex structure $J$, the criteria $TJ=JT$ and $SJ=-JS$ and the block shapes.
- [The Two Forms and the Two Algebraic Norms of the Complexoid Space](the-two-forms-and-the-two-algebraic-norms-of-the-complexoid-space.html), above this article in this category, for the two forms whose realified signatures are derived here.
- *The Matrix Element Representations of the Complex Numbers*, above this article in this category, for the two matrices at $n=1$ read as element representations and for the identification of their determinant and trace with the algebraic norms.
- [Remarkable Subspaces of the Complexoid and the Two Forms](remarkable-subspaces-of-the-complexoid-and-the-two-forms.html), above this article in this category, for the coincidence of the two products on the real subspace.
- [The Realification and the Effect of the Change of Scalars](the-realification-and-the-effect-of-the-change-of-scalars.html), for the general construction, of which this article is the prototype.
- [Complexoid Subspaces](complexoid-subspaces.html) and [Complex Algebra](complex-algebra.html), for the two subspaces and the field of the algebra.
