# __The Two Pairings of the Quaternion Algebra__

## Introduction

A pairing is the scalar part of a product, read as a function of two elements. The two general products therefore define two pairings, the plain form of signature $(1,3)$ and the quaternion form of signature $(4,0)$, and this article presents them side by side: their definitions, their Gram matrices, their polarisation, their relation to the two algebraic norms, and the comparison with the four pairings of the biquaternion algebra. The pairings themselves are *The 2 Forms over the Quaternion $\mathbb{R}$ Space*, the norms are *The 2 Algebraic Norms over the Quaternion $\mathbb{R}$ Space*, and the collapse from four to two is *The Two General Products and the Reason There Are Only Two*, all above this article in this category.

## The Two Pairings

**Definition.** For a product $\star$ on $\mathbb{H}$, the **pairing** it defines is
$$
\langle\tilde p,\tilde q\rangle_{\star}=\operatorname{Sc}(\tilde p\star\tilde q) , \qquad\text{equivalently}\qquad \operatorname{Sc}(\tilde p\star\tilde q)=\tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde p\star\tilde q)\bigr)
$$
in the matrix model of *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Quaternions*, above this article in this category. The two general products give the **plain pairing**
$$
B(\tilde p,\tilde q)=\operatorname{Sc}(\tilde p\tilde q)=p_0q_0-p_1q_1-p_2q_2-p_3q_3
$$
and the **quaternion pairing**
$$
N(\tilde p,\tilde q)=\operatorname{Sc}(\tilde p^{\natural}\tilde q)=p_0q_0+p_1q_1+p_2q_2+p_3q_3 .
$$
Both are symmetric and $\mathbb{R}$-bilinear, and the two agree on the scalar line and differ on the vector subspace, where their signs are opposite.

## Gram Matrices and Signatures

In the basis $(e_0,e_1,e_2,e_3)$ the Gram matrices are diagonal:
$$
[\,B\,]=\operatorname{diag}(1,-1,-1,-1) , \qquad [\,N\,]=\operatorname{diag}(1,1,1,1) .
$$
The plain pairing is the **Minkowski pairing** of signature $(1,3)$, with one positive and three negative directions; the quaternion pairing is the **Euclidean pairing** of signature $(4,0)$, positive definite. Both are **non-degenerate**, of radical $\{0\}$, since their matrices are invertible; the plain pairing has a non-trivial null cone and the quaternion pairing has none. The signs are what the two products transmit to their forms: the plain product carries $e_k^2=-e_0$ and the quaternion product, through the conjugation on its first slot, turns the three minuses into pluses.

The pairings restricted to the two remarkable subspaces, with their inertia, are tabulated in *The Remarkable Subspaces under the Six Operations*, above this article in this category.

## Polarisation

Each pairing is recovered from its quadratic form, its diagonal, by the polarisation identity
$$
B(\tilde p,\tilde q)=\tfrac12\bigl(Q_B(\tilde p+\tilde q)-Q_B(\tilde p)-Q_B(\tilde q)\bigr) , \qquad
N(\tilde p,\tilde q)=\tfrac12\bigl(Q_N(\tilde p+\tilde q)-Q_N(\tilde p)-Q_N(\tilde q)\bigr) ,
$$
with the diagonals
$$
Q_B(\tilde p)=B(\tilde p,\tilde p)=p_0^2-p_1^2-p_2^2-p_3^2 , \qquad
Q_N(\tilde p)=N(\tilde p,\tilde p)=p_0^2+p_1^2+p_2^2+p_3^2 .
$$
The polarisation is the general fact that a symmetric bilinear form over a field of characteristic not two is its diagonal's polarisation; over $\mathbb{R}$ this applies to both pairings, and the two quadratic forms are recovered from the two pairings in the same way.

## Relation to the Two Algebraic Norms

The **algebraic norms** of *The 2 Algebraic Norms over the Quaternion $\mathbb{R}$ Space* are read off the diagonals of the two pairings:
$$
N_P(\tilde p)=\tilde p^2 ,\quad \operatorname{Sc}\bigl(N_P(\tilde p)\bigr)=Q_B(\tilde p) \quad\text{(the plain norm, indefinite)} , \qquad
N_Q(\tilde p)=\tilde p^{\natural}\tilde p=N(\tilde p)e_0 \quad\text{(the quaternion norm, positive definite)} .
$$
The first is the square, read in the plain product, whose scalar coefficient is $Q_B$ and whose vector coefficient $2p_0\mathbf p$ is nonzero off the axes, and it is indefinite; the second is central and is exactly the diagonal of $N$, multiplicative, $N(\tilde p\tilde q)=N(\tilde p)N(\tilde q)$, and positive definite. The two norms are therefore not two more objects beside the pairings: the diagonals $Q_B$ and $Q_N$ are their scalar readings, and the one property that singles out the quaternion norm, multiplicativity, is the one that makes it the norm of the division algebra. The details are *The 2 Algebraic Norms over the Quaternion $\mathbb{R}$ Space*.

## Comparison with the Biquaternion Case

The biquaternion algebra carries **four** pairings, because its base ring $\mathbb{C}$ has a non-trivial involution: the general plain bilinear, the general quaternionic bilinear, the general plain sesquilinear (the Hermitian form) and the general quaternionic sesquilinear (the Krein form). Their Gram matrices carry the four sign patterns of the complex basis, and two of them, the sesquilinear pairings, have conjugate symmetry rather than symmetry. Over $\mathbb{R}$ the second slot of the general construction carries no involution, so the two sesquilinear pairings coincide with the two bilinear ones and only $B$ and $N$ survive. This is the collapse of *The Two General Products and the Reason There Are Only Two* read on the pairings; the four pairings of the complex rung and their Gram matrices are *The Four Pairings of the Biquaternion Algebra*.

## Summary

The two general products define two pairings: the plain pairing $B(\tilde p,\tilde q)=\operatorname{Sc}(\tilde p\tilde q)$ of signature $(1,3)$ and the quaternion pairing $N(\tilde p,\tilde q)=\operatorname{Sc}(\tilde p^{\natural}\tilde q)$ of signature $(4,0)$, non-degenerate and recovered from their diagonals by polarisation. Their diagonals are the two algebraic norms, the indefinite square and the multiplicative positive definite quaternion norm. The biquaternion chapter carries four pairings, the two sesquilinear ones being lost over $\mathbb{R}$ together with the second slot of the general construction; the four-to-two collapse of the pairings is the same collapse as that of the products.

## Summary of Notation

| symbol | meaning |
|---|---|
| $B$, $N$ | the plain and quaternion pairings |
| $\operatorname{diag}(1,-1,-1,-1)$ | the Gram matrix of $B$, signature $(1,3)$ |
| $\operatorname{diag}(1,1,1,1)$ | the Gram matrix of $N$, signature $(4,0)$ |
| $Q_B$, $Q_N$ | the diagonals, the two algebraic norms |
| Hermitian, Krein | the two sesquilinear pairings of the biquaternion rung |

## Further Reading

- *The 2 Forms over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-2-forms-over-the-quaternion-r-space.md`), above this article in this category.
- *The 2 Algebraic Norms over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-2-algebraic-norms-over-the-quaternion-r-space.md`), above this article in this category.
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the complex rung.
- *The Two Adjoints of the Two Algebras in Examples* (`articles_maths/the-two-adjoints-of-the-two-algebras-in-examples.md`), below this article in this category, for the adjoints these pairings define.
