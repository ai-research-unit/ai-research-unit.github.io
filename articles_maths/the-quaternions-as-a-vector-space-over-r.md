# __The Quaternions as a Vector Space over $\mathbb{R}$__

## Introduction

The quaternion algebra $\mathbb{H}$ carries a vector space structure over $\mathbb{R}$, and this article reads it: the additive group, the real scalar action, the basis $e_0,e_1,e_2,e_3$, the coordinates, the real-linear endomorphism ring, and the two coordinate blocks that the algebra singles out. Nothing here uses the product except to record that the two structures agree, and no form appears. The element, the basis and the multiplication table are those of *Quaternion Algebra*, whose worked computations are *Worked Examples in the Quaternion Algebra*; the algebra reading of the same set is *Introduction to the General Plain Algebra of Quaternions*, below this article in this category, and the product is developed in *The Two General Products of the Quaternion $\mathbb{R}$ Space*, below this article in this category.

## The Additive Group and the Real Scalar Action

An element of $\mathbb{H}$ is a formal sum
$$
\tilde q=q_0e_0+q_1e_1+q_2e_2+q_3e_3 , \qquad q_0,q_1,q_2,q_3\in\mathbb{R},
$$
with the four units of *Quaternion Algebra*. The sum of two elements and the product by a real scalar are read coordinatewise,
$$
(\tilde p+\tilde q)_\mu=p_\mu+q_\mu , \qquad (\lambda \tilde q)_\mu=\lambda q_\mu , \qquad \lambda\in\mathbb{R},
$$
so that

- $(\mathbb{H},+)$ is the additive group $\mathbb{R}^4$, abelian, with zero $0$ and opposite $-\tilde q=(-q_0)e_0+\dots$;
- the real scalar action is the usual one of $\mathbb{R}$ on $\mathbb{R}^4$.

The product is $\mathbb{R}$-bilinear and the scalar action passes through it,
$$
\lambda(\tilde p\tilde q)=(\lambda \tilde p)\tilde q=\tilde p(\lambda \tilde q),
$$
because the product is built from sums and products of the coordinates. With this compatibility $\mathbb{H}$ is a real algebra of dimension four, and the two structures — the real vector space and the algebra — are the two readings of one set.

**Proposition (dimension and basis).** The four units $e_0,e_1,e_2,e_3$ are linearly independent over $\mathbb{R}$, and they span $\mathbb{H}$; hence $\dim_{\mathbb{R}}\mathbb{H}=4$ and $(e_0,e_1,e_2,e_3)$ is a basis. The four coordinates $q_0,\dots,q_3$ are the coordinates of $\tilde q$ in this basis and are unique.

**Proof.** A vanishing real combination $\sum_\mu\lambda_\mu e_\mu$ is the vanishing of the four real numbers $\lambda_\mu$, the units being the four coordinate directions; and every element is by definition a real combination of the four.

Two other coordinate conventions occur in the corpus and are named here only to fix the reading: the **combinations** $e_0\pm e_1$, $e_0\pm e_2$, $e_0\pm e_3$, used in the light-cone and root-of-minus-one computations, and the four half-integer coordinates of the Peirce decomposition. Neither changes the basis of this article. The coordinates always refer to the units $e_0,\dots,e_3$ unless a change of basis is stated; the elements themselves are those of *Quaternion Algebra*.

## The Real-Linear Endomorphisms

Because $\mathbb{H}$ is a real vector space, its real-linear endomorphisms form the ring $\operatorname{End}_{\mathbb{R}}(\mathbb{H})$, which is $\mathbb{R}$-linearly isomorphic to the matrix ring $M_4(\mathbb{R})$ once a basis is fixed. Two families of endomorphisms come from the product:

- the **left multiplication** $L_{\tilde p}:\mathbb{H}\to\mathbb{H}$, $L_{\tilde p}(\tilde r)=\tilde p\tilde r$;
- the **right multiplication** $R_{\tilde q}:\mathbb{H}\to\mathbb{H}$, $R_{\tilde q}(\tilde r)=\tilde r\tilde q$.

Both are real-linear, and the assignments $\tilde p\mapsto L_{\tilde p}$ and $\tilde q\mapsto R_{\tilde q}$ are injective, since $L_{\tilde p}(e_0)=\tilde p$ and $R_{\tilde q}(e_0)=\tilde q$. They are algebra embeddings with opposite multiplicativity,
$$
L_{\tilde p}L_{\tilde q}=L_{\tilde p\tilde q} , \qquad R_{\tilde p}R_{\tilde q}=R_{\tilde q\tilde p},
$$
the first from associativity $\tilde p(\tilde q\tilde r)=(\tilde p\tilde q)\tilde r$ and the second from $(\tilde r\tilde p)\tilde q=\tilde r(\tilde p\tilde q)$. The two images commute, $L_{\tilde p}R_{\tilde q}=R_{\tilde q}L_{\tilde p}$, both being the left and the right multiplication by fixed elements, and this is associativity again. The left regular representation $\tilde p\mapsto L_{\tilde p}$ is the quaternion algebra read as a four-dimensional subalgebra of $M_4(\mathbb{R})$; it is written $M_4(\mathbb{R})_L$ in the corpus and is the subject of *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{R})_L$ of Quaternions*, below this article in this category.

## The Scalar and Vector Subspaces

The coordinates cut $\mathbb{H}$ into two blocks, and the algebra singles these two blocks out:

- the **scalar subspace** (or **real line**) $\mathbb{R}_{\mathbb{H}}=\{\tilde q:q_1=q_2=q_3=0\}=\mathbb{R}e_0$, of dimension one;
- the **vector subspace** $\mathrm{Vect}(\mathbb{H})=\{\tilde q:q_0=0\}=\mathbb{R}e_1\oplus\mathbb{R}e_2\oplus\mathbb{R}e_3$, of dimension three, also written $\operatorname{Im}\mathbb{H}$.

The two are supplementary, $\mathbb{H}=\mathbb{R}_{\mathbb{H}}\oplus\mathrm{Vect}(\mathbb{H})$, and the decomposition of $\tilde q$ is the pair $(q_0,\mathbf q)$ with $\mathbf q=q_1e_1+q_2e_2+q_3e_3$. The two subspaces are the two fixed and anti-fixed spaces of the natural conjugation ${}^{\natural}$ in its coordinate form $\tilde q^{\natural}=q_0-\mathbf q$, and they are the two remarkable subspaces of the quaternion algebra. They are defined and developed in *Introduction to the Remarkable Subspaces of the Quaternions*, below this article in this category, and their comparison is *Comparison of the Remarkable Subspaces of the Quaternions*, below this article in this category. The word **scalar** is used for the real coordinate on $\mathbb{R}_{\mathbb{H}}$; the word **pure** is used for the elements of $\mathrm{Vect}(\mathbb{H})$.

## The Ladder of the Real Algebras

The three objects form a ladder of real algebras,
$$
\mathbb{R}\ \subset\ \mathbb{C}\ \subset\ \mathbb{H},
$$
in which each rung is a real vector space of dimension $1,2,4$ and the last is the division algebra $\mathbb{H}$.

**Warning (the bar on an element).** On an element of $\mathbb{H}$ the complex conjugation $\bar{\cdot}$ of the coefficients acts as the identity, because the coefficients are real. The conjugation that acts on $\mathbb{H}$ is the natural one ${}^{\natural}$, and it is ${}^{\natural}$ and never a bar that is written on an element here. The reading of the two conjugations is the one of *The Quaternions as a Vector Space over $\mathbb{C}$*, below this article in this category, and the involutions they obey are *The Group of Involutions of the Quaternions*, below this article in this category.

## Summary

The quaternion algebra is a four-dimensional real vector space on the basis $e_0,e_1,e_2,e_3$, with coordinatewise sum and real scalar action; the product is $\mathbb{R}$-bilinear and compatible with the scalars, so that $\mathbb{H}$ is a real algebra. The real-linear endomorphisms are $M_4(\mathbb{R})$, and the left and right multiplications embed $\mathbb{H}$ into it with $L_{\tilde p}L_{\tilde q}=L_{\tilde p\tilde q}$ and $R_{\tilde p}R_{\tilde q}=R_{\tilde q\tilde p}$. The coordinates cut out the scalar line $\mathbb{R}e_0$ and the vector subspace $\mathbb{R}e_1\oplus\mathbb{R}e_2\oplus\mathbb{R}e_3$, the two remarkable subspaces and the two eigenspaces of ${}^{\natural}$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{H}$ | the quaternion algebra, a four-dimensional real vector space |
| $\tilde q=q_0e_0+q_1e_1+\dots$ | the element and its four real coordinates |
| $\mathbb{R}_{\mathbb{H}}$ | the scalar subspace $\mathbb{R}e_0$, dimension one |
| $\mathrm{Vect}(\mathbb{H})$ | the vector subspace $\mathbb{R}e_1\oplus\mathbb{R}e_2\oplus\mathbb{R}e_3$, dimension three |
| $L_{\tilde p},R_{\tilde q}$ | the left and the right multiplication by $\tilde p$ and by $\tilde q$ |
| $M_4(\mathbb{R})_L$ | the image of $\tilde p\mapsto L_{\tilde p}$, the left regular representation |
| ${}^{\natural}$ | the natural conjugation $\tilde q\mapsto q_0-\mathbf q$ |

## Further Reading

- *Quaternion Algebra* (`articles_maths/quaternion-algebra.md`), for the element, the basis and the multiplication table read as an algebra.
- *The Quaternions as a Vector Space over $\mathbb{C}$* (`articles_maths/the-quaternions-as-a-vector-space-over-c.md`), below this article in this category, for the next rung and for the two distinct senses in which $\mathbb{H}$ is read over $\mathbb{C}$.
- *Introduction to the General Plain Algebra of Quaternions* (`articles_maths/introduction-to-the-general-plain-algebra-of-quaternions.md`), below this article in this category, for the same set read through the product.
