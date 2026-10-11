# __The Remarkable Subspaces under the Six Operations__

## Introduction

The two remarkable subspaces of $\mathbb{H}$, the scalar line and the vector subspace, are read here against every form the six products carry, and the restriction of each form to them is tabulated. The article is a synthesis: it does not re-derive the forms, which are owned by the articles named in each row, and it does not re-derive the two subspaces, which are owned by *Introduction to the Remarkable Subspaces of the Quaternions*, above this article in this category. The two-form case of the table is treated in full in *Remarkable Subspaces and the Two Forms*, and the norm case in *Remarkable Subspaces and the Two Algebraic Norms*, both above this article in this category. What it owns is the restriction table over the six operations, the inertia, the isotropic elements, and the reason two subspaces suffice here where the biquaternion ladder needs six.

## The Two Subspaces

The scalar and vector subspaces of *Introduction to the Remarkable Subspaces of the Quaternions* are
$$
\mathbb{R}_{\mathbb{H}}=\{s e_0:s\in\mathbb{R}\} , \qquad \operatorname{Vect}(\mathbb{H})=\{\mathbf q=q_1e_1+q_2e_2+q_3e_3\} ,
$$
of dimensions $1$ and $3$, with $\mathbb{H}=\mathbb{R}_{\mathbb{H}}\oplus\operatorname{Vect}(\mathbb{H})$ and $\mathbb{R}_{\mathbb{H}}\cap\operatorname{Vect}(\mathbb{H})=\{0\}$. Their sign pattern under the conjugation is the one of *Introduction to the Remarkable Subspaces of the Quaternions*: the scalar line is the fixed space and the vector subspace the anti-fixed space, and the two subspaces are the whole list.

## The Five Forms of the Six Operations

The six products carry five named forms, of which four are distinct, because the trace form of the Jordan product coincides with the plain form. Writing $\tilde p,\tilde q$ for the elements,

| form | definition | owner |
|---|---|---|
| plain form $B$ | $B(\tilde p,\tilde q)=\operatorname{Sc}(\tilde p\tilde q)$ | *The 2 Forms over the Quaternion $\mathbb{R}$ Space* |
| quaternion form $N$ | $N(\tilde p,\tilde q)=\operatorname{Sc}(\tilde p^{\natural}\tilde q)=p_0q_0+\mathbf p\cdot\mathbf q$ | *The 2 Forms over the Quaternion $\mathbb{R}$ Space* |
| Jordan trace form $\tau$ | $\tau(\tilde p,\tilde q)=\operatorname{Sc}(\tilde p\bullet\tilde q)$ | *The Trace Form and the Invariance of the Symmetric Plain Algebra* |
| Killing form of the cross product $K$ | $K(\tilde p,\tilde q)=\operatorname{tr}(\operatorname{ad}_{\tilde p}\operatorname{ad}_{\tilde q})$ | *The Killing Form of the Antisymmetric Plain Algebra* |
| invariant form of the antisymmetrised quaternionic product $\varphi$ | $\varphi(\tilde p,\tilde q)=p_0q_0$, the unique invariant form of AQA | *The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra* |

The Jordan trace form equals the plain form, because $\operatorname{Sc}(\tilde p\bullet\tilde q)=\tfrac12(\operatorname{Sc}(\tilde p\tilde q)+\operatorname{Sc}(\tilde q\tilde p))=\operatorname{Sc}(\tilde p\tilde q)$ by the invariance of the scalar part under the cyclic permutation of a product. The antisymmetrisation kills the scalar part, so the two antisymmetric structures contribute no form by the scalar-part route: the values of the cross product and of the antisymmetrised quaternionic product are pure vectors, and the forms those structures carry instead are the Killing form of the cross product and the unique invariant form of the antisymmetrised quaternionic product, which is symmetric of rank one and not alternating.

## The Restriction Matrices

In the natural bases $(e_0)$ of the scalar line and $(e_1,e_2,e_3)$ of the vector subspace the restrictions of the four distinct forms are:

$$
B|_{\mathbb{R}_{\mathbb{H}}}=(1) ,\quad B|_{\operatorname{Vect}}=\operatorname{diag}(-1,-1,-1) ;\qquad
N|_{\mathbb{R}_{\mathbb{H}}}=(1) ,\quad N|_{\operatorname{Vect}}=\operatorname{diag}(1,1,1) ;
$$
$$
\tau|_{\mathbb{R}_{\mathbb{H}}}=\tau|_{\operatorname{Vect}}\ \text{as for } B ;\qquad
K|_{\mathbb{R}_{\mathbb{H}}}=(0) ,\quad K|_{\operatorname{Vect}}=\operatorname{diag}(-2,-2,-2) ;
$$
and $\varphi$, which reads the two scalar parts, has the rank-one matrix $\operatorname{diag}(1,0,0,0)$, that is $\varphi|_{\mathbb{R}_{\mathbb{H}}}=(1)$ and $\varphi|_{\operatorname{Vect}}=(0)$, by *The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra*. Both $B$ and $N$ are **orthogonal** for the decomposition, $B(e_0,e_k)=N(e_0,e_k)=0$, so their restriction matrices are block diagonal and there is no cross block; the Killing form and $\varphi$ are likewise block diagonal, the Killing form killing the scalar line, which is its radical, and $\varphi$ killing the vector subspace, which is its radical.

The **inertia** of each restriction is therefore read off the signs:

| form | on $\mathbb{R}_{\mathbb{H}}$ | on $\operatorname{Vect}(\mathbb{H})$ | on $\mathbb{H}$ |
|---|---|---|---|
| $B$ | $(1,0)$ | $(0,3)$ | $(1,3)$ |
| $\tau$ | $(1,0)$ | $(0,3)$ | $(1,3)$ |
| $N$ | $(1,0)$ | $(3,0)$ | $(4,0)$ |
| $K$ | $(0,0)$ | $(0,3)$ | $(0,3)$ |
| $\varphi$ | $(1,0)$ | $(0,0)$ | $(1,0)$ |

The plain family is indefinite, with the scalar line positive and the vector subspace negative; the quaternion family is definite, positive on both; the Killing form is negative definite on the vector subspace and zero on the scalar line; and $\varphi$ is positive on the scalar line and zero on the vector subspace, of rank one and degenerate. The two lines $(1,0)\perp(0,3)$ and $(1,0)\perp(3,0)$ of the menu are the inertia of $B$ and of $N$ read block by block.

## Isotropic Elements

An element is **isotropic** for a form when the form vanishes at that element with itself. For the plain form the scalar line and the vector subspace are each anisotropic, but the sum is not: $e_0+e_1$ gives $B(e_0+e_1,e_0+e_1)=1-1=0$, so the plain form has a null cone, of real dimension three, cut out by the single real equation $p_0^2=p_1^2+p_2^2+p_3^2$. For the quaternion form no nonzero element is isotropic, its positivity being total, $N(\tilde p,\tilde p)=\sum_\mu p_\mu^2$; the Jordan trace form is the plain form, so it has the same null cone, of dimension three; and for the Killing form the only isotropic elements are those of its radical, the scalar line. For $\varphi$ the isotropic elements are those with $x_0=0$, the vector subspace, which is at the same time its radical; a form of rank one carries no definite or indefinite sign pattern.

The **radical** is the anisotropic case's companion: $0$ for $B$, for $N$ and for $\tau$; the scalar line for $K$; and the vector subspace for $\varphi$. The radicals of the two forms of the two general products are computed in *The Two Pairings of the Quaternion Algebra*, below this article in this category.

## Why Two Subspaces Suffice

The biquaternion chapter needs six remarkable subspaces, because its isotropic cone cuts the space into null pieces and the split of the algebra is read block by block. Over $\mathbb{R}$ the cone of the plain form is not enough to split the space, because $\mathbb{H}$ has no zero divisor: the division property of *Norm and Invertibility in the General Plain Algebra* forbids the null pieces, and the only subspaces the conjugation singles out are the scalar line and the vector subspace. The reduction from six to two is the same reduction from four products to two that the synthesis of the block records, and it is the reason the restriction table has two rows of subspaces rather than six.

## Summary

The six products carry five named forms, of which four are distinct: the plain form $B$ of inertia $(1,3)$, coinciding with the Jordan trace form $\tau$; the quaternion form $N$ of inertia $(4,0)$; the Killing form $K$ of the cross product, of inertia $(0,3)$ with the scalar line as radical; and the invariant form $\varphi(\tilde p,\tilde q)=p_0q_0$ of the antisymmetrised quaternionic product, of rank one, reading the scalar line and vanishing on the vector subspace. Both $B$ and $N$ are orthogonal for the decomposition $\mathbb{H}=\mathbb{R}_{\mathbb{H}}\oplus\operatorname{Vect}(\mathbb{H})$, with the two blocks $(1,0)\perp(0,3)$ for the plain family and $(1,0)\perp(3,0)$ for the quaternion family. The isotropic elements are present for the indefinite forms $B$ and $\tau$, absent for the definite form $N$, and form the vector subspace for the degenerate $\varphi$, and the reason two subspaces suffice is the division property, which forbids the null split of the biquaternion ladder.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{R}_{\mathbb{H}}$, $\operatorname{Vect}(\mathbb{H})$ | the scalar line and the vector subspace |
| $B$, $N$, $\tau$, $K$, $\varphi$ | the plain, quaternion, Jordan trace, Killing and AQA invariant forms |
| $(1,0)\perp(0,3)$ | the inertia of $B$ and $\tau$ |
| $(1,0)\perp(3,0)$ | the inertia of $N$ |
| radical | the subspace annihilated by a form; the scalar line for $K$, the vector subspace for $\varphi$ |

## Further Reading

- *The 2 Forms over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-2-forms-over-the-quaternion-r-space.md`), above this article in this category.
- *Remarkable Subspaces and the Two Forms* (`articles_maths/remarkable-subspaces-and-the-two-forms.md`), above this article in this category, for the two-form case of the table.
- *Remarkable Subspaces and the Two Algebraic Norms* (`articles_maths/remarkable-subspaces-and-the-two-algebraic-norms.md`), above this article in this category, for the norm case.
- *The Trace Form and the Invariance of the Symmetric Plain Algebra* (`articles_maths/the-trace-form-and-the-invariance-of-the-symmetric-plain-algebra-of-quaternions.md`), above this article in this category.
- *The Killing Form of the Antisymmetric Plain Algebra* (`articles_maths/the-killing-form-of-the-antisymmetric-plain-algebra-of-quaternions.md`), above this article in this category.
- *The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra* (`articles_maths/the-invariant-bilinear-forms-of-the-antisymmetric-quaternionic-algebra-of-quaternions.md`), above this article in this category.
- *The Two Pairings of the Quaternion Algebra* (`articles_maths/the-two-pairings-of-the-quaternion-algebra.md`), below this article in this category.
