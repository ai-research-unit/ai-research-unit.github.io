# __The Krein Isometry Group and Its J-Contractions__

## Introduction

The isometries of the Krein form make up the **Krein isometry group** $U_{J}(\mathbb{B})$ of the biquaternion algebra, and its shape is the surprise of the indefinite theory: it is not compact, it is not the group $U(2)$ that the two-sided structure of the algebra might suggest, and it contains the Lorentz boosts of the Minkowski slices among its elements. This article determines the group, computes its dimension, identifies its centre and its maximal compact subgroup, lists the Krein isometries inside the algebra's own operator families, describes the spectrum of a Krein isometry and the one-parameter subgroups of boosts, and ends with the $J$-contractions and their defect operators. The group appears in *The Krein Cartan Decomposition of the Operator Algebra* as the fixed group of the Krein-adjoint involution and in *The Krein Level Sets and the Hyperbolic Structure* as the isometry group of the complex hyperbolic ball; the adjoint itself is *J-Self-Adjoint and J-Unitary Operators on the Biquaternion Algebra*.

**Conventions.** $\mathbb{B}$ is the biquaternion algebra; $\langle\tilde{Q},\tilde{Q}'\rangle=\sum_{\mu}\bar Q_{\mu}Q'_{\mu}$ is the Hermitian form (Gram matrix $\mathrm{I}_4$), $[\tilde{Q},\tilde{Q}']=\sum_{\mu}\varepsilon_{\mu}\bar Q_{\mu}Q'_{\mu}$ is the Krein form (Gram matrix $E=\mathrm{diag}(1,-1,-1,-1)$), $J={}^{\natural}$, and the Krein adjoint is $T^{\dagger}=JT^{*}J$. In the coefficient basis a $\mathbb{C}$-linear operator is a matrix $T$ and the Krein form is $[\tilde{Q},\tilde{Q}']=\tilde{Q}^{\mathsf T*}E\tilde{Q}'$, where $T^{\mathsf T*}$ is the conjugate transpose of the matrix or vector.

## The Group of Krein Isometries

**Definition.** An **isometry of the Krein form**, or a **Krein isometry**, or a **$J$-unitary operator**, is a $\mathbb{C}$-linear operator $T$ with $[\tilde{Q},\tilde{Q}']=[T\tilde{Q},T\tilde{Q}']$ for all $\tilde{Q},\tilde{Q}'$. The **Krein isometry group** is

$$
U_{J}(\mathbb{B})=\{T:T^{\dagger}T=\mathrm{id}\}=\{T:T^{\mathsf T*}ET=E\}.
$$

**Theorem (the group is $U(1,3)$).** In the coefficient basis the Krein isometry group is $U(1,3)$, the group of complex matrices preserving an indefinite Hermitian form of signature $(1,3)$. It has real dimension $16$, it is non-compact, its centre is the circle $U(1)$ of scalar matrices $c\cdot\mathrm{id}$ with $|c|=1$, and its maximal compact subgroup is $U(1)\times U(3)$, the group preserving the canonical fundamental decomposition $\mathbb{B}=\mathbb{C}_{\mathbb{B}}\perp_{K}\mathbb{V}_{\mathbb{B}}$.

**Proof.** The condition $T^{\mathsf T*}ET=E$ is the defining equation of the isometry group of the form with matrix $E=\mathrm{diag}(1,-1,-1,-1)$, of signature $(1,3)$ over $\mathbb{C}$, so the group is $U(1,3)$; its real dimension is $p^{2}+q^{2}+2pq=(p+q)^{2}=16$ for $p=1,q=3$. A group of this form is non-compact because it contains the boosts of the next sections. A matrix commutes with every $U(1,3)$ exactly when it is scalar, and the scalars that preserve the form are those of modulus $1$, giving the centre. The matrices preserving the two eigenspaces of the form, that is the decomposition $\mathbb{C}^{1}\oplus\mathbb{C}^{3}$, are block diagonal unitary in the two blocks, hence $U(1)\times U(3)$; by Cartan's theorem the fixed group of the Cartan involution is the maximal compact subgroup (*The Krein Cartan Decomposition of the Operator Algebra*).

**Theorem (the $J$-unitarity criterion).** A $\mathbb{C}$-linear operator is a Krein isometry if and only if $T^{*}JT=J$, that is $T^{\dagger}T=\mathrm{id}$; equivalently, if and only if $T^{*}=JT^{-1}J$, so that $T$ is invertible with $T^{-1}=T^{\dagger}$.

**Proof.** $[T\tilde{Q},T\tilde{Q}']=\langle JT\tilde{Q},T\tilde{Q}'\rangle=\langle\tilde{Q},T^{*}JT\tilde{Q}'\rangle$ while $[\tilde{Q},\tilde{Q}']=\langle\tilde{Q},J\tilde{Q}'\rangle$, so the preservation of the Krein form is $T^{*}JT=J$; multiplying by $J$ on the right gives $T^{\dagger}T=\mathrm{id}$.

## The Algebraic Krein Isometries

**Theorem (the isometries among the three families).** For a biquaternion $\tilde{Q}$,

$$
L_{\tilde{Q}}\ \text{is $J$-unitary}\iff\tilde{Q}\in S^{1}e_0,
\qquad
R_{\tilde{Q}}\ \text{is $J$-unitary}\iff\tilde{Q}\in S^{1}e_0,
\qquad
\Theta_{\tilde{Q}}\ \text{is $J$-unitary}\iff|N(\tilde{Q})|=1,
$$

where $S^{1}e_0$ is the circle of central phases.

**Proof.** $L_{\tilde{Q}}^{\dagger}L_{\tilde{Q}}=R_{\bar{\tilde{Q}}}L_{\tilde{Q}}$ is the operator $\tilde{P}\mapsto\tilde{Q}\tilde{P}\bar{\tilde{Q}}$, which is the identity exactly when $\tilde{Q}\bar{\tilde{Q}}=e_0$ and $\tilde{Q}$ is central, that is $\tilde{Q}\in S^{1}e_0$; the right case is symmetric. For the sandwich, $\Theta_{\tilde{Q}}^{\dagger}\Theta_{\tilde{Q}}=\Theta_{N(\tilde{Q})e_0}=|N(\tilde{Q})|^{2}\mathrm{id}$.

**Corollary (the algebraic subgroup).** The central phases and the sandwiches of norm one generate the compact subgroup

$$
U(1)\times PU(2)\cong U(1)\times SO(3),
$$

of real dimension $4$: the phases are the scalar isometries and the norm-one sandwiches are the inner automorphisms $\tilde{P}\mapsto\tilde{Q}\tilde{P}\tilde{Q}^{\dagger}$ of the algebra, which depend only on the class of $\tilde{Q}$ in $U(2)/U(1)=PU(2)\cong SO(3)$. The two families commute, and their only common element is the identity. This subgroup is far from the whole group, whose dimension is $16$.

**Proof.** The kernel of the map $\tilde{Q}\mapsto\Theta_{\tilde{Q}}$ is the centre of the algebra, so its image over the norm-one elements is $U(2)$ modulo its centre, which is $PU(2)\cong SO(3)$. The phases are central in the operator algebra, hence commute with the sandwiches; and $\Theta_{\tilde{Q}}$ is scalar only for $\tilde{Q}$ a scalar of modulus one, in which case $\Theta_{\tilde{Q}}=\mathrm{id}$.

## The Spectrum of a Krein Isometry

**Theorem (inversion symmetry; no confinement to the circle).** If $T$ is $J$-unitary then

$$
\lambda\in\mathrm{spec}(T)\iff\frac{1}{\bar\lambda}\in\mathrm{spec}(T),
$$

with the same multiplicity; the eigenvalues on the unit circle are paired by conjugation, and the eigenvalues off the circle occur in inverted pairs. The spectrum need not lie on the unit circle.

**Proof.** $T^{*}=JT^{-1}J$ makes $T^{*}$ similar to $T^{-1}$, so the characteristic polynomials of $T^{*}$ and of $T^{-1}$ agree, and $\mathrm{spec}(T^{*})=\overline{\mathrm{spec}(T)}$ while $\mathrm{spec}(T^{-1})=\{\lambda^{-1}\}$. The boost of the next section has the eigenvalues $e^{\pm t}$.

**Example.** The diagonal phases $L_{ce_0}$ with $c\in S^{1}$ have the single eigenvalue $c$ of multiplicity four, on the circle; the norm-one sandwiches have the eigenvalues $\lambda_i\bar\lambda_j$ of the conjugating unitary matrix, on the circle as well; the boosts leave the circle.

## The Boosts

**Definition.** On the Krein-orthogonal sum $\mathbb{C}e_0\perp_{K}\mathbb{C}e_1$ of a positive and a negative line, the **boost of parameter $t\in\mathbb{R}$** is the operator

$$
T_{t}e_0=\cosh t\,e_0+\sinh t\,e_1,\qquad
T_{t}e_1=\sinh t\,e_0+\cosh t\,e_1,\qquad
T_{t}=\mathrm{id}\ \text{on}\ \mathbb{C}e_2\perp_{K}\mathbb{C}e_3 .
$$

**Theorem (the boosts are Krein isometries).** Each $T_{t}$ is a Krein isometry, the assignment $t\mapsto T_{t}$ is a one-parameter subgroup of $U_{J}(\mathbb{B})$, and the spectrum is

$$
\mathrm{spec}(T_{t})=\{e^{t},e^{-t},1,1\},
$$

so the boosts are the elements of the group whose spectrum is real and off the unit circle. The restriction of $T_{t}$ to the Minkowski slice $\mathbb{H}_{\mathbb{B}}$ is the Lorentz boost of rapidity $t$ along the $e_1$ direction, that is of velocity $\tanh t$.

**Proof.** In the plane spanned by $e_0,e_1$ the form has the matrix $\mathrm{diag}(1,-1)$ and the matrix of $T_{t}$ is $\begin{pmatrix}\cosh t&\sinh t\\ \sinh t&\cosh t\end{pmatrix}$, whose columns have squares $\cosh^{2}t-\sinh^{2}t=1$, $-\cosh^{2}t+\sinh^{2}t=-1$ and scalar product $\cosh t\sinh t-\sinh t\cosh t=0$: the form is preserved, and the two remaining basis vectors are fixed in their own definite lines, so $T_{t}$ is an isometry. Additivity $T_{s}T_{t}=T_{s+t}$ is the addition formula for the hyperbolic functions, so the family is a one-parameter subgroup. The eigenvalues of the plane block are $e^{\pm t}$ and the two fixed directions contribute $1,1$. The fixed direction $e_{1}$ of the Minkowski slice is the boost axis, and the parameter is the rapidity.

**Corollary (the group is non-compact).** The boost family is unbounded in the operator norm as $t\to\infty$, so $U_{J}(\mathbb{B})$ is non-compact; the maximal compact subgroup $U(1)\times U(3)$ is exactly the part that fixes the canonical fundamental decomposition.

## The Actions of the Group

**Theorem (transitivity).** The group $U_{J}(\mathbb{B})$ acts transitively on the isotropic lines, on the positive definite lines and on the maximal totally isotropic subspaces of the Krein form; the stabiliser of the canonical positive line $\mathbb{C}e_0$ and of the canonical maximal isotropic subspace is $U(1)\times U(3)$ and the stabiliser of the isotropic line $\mathbb{C}(e_0+e_1)$ contains the boosts.

**Proof.** Transitivity on the isotropic and maximal isotropic subspaces is Witt's extension theorem (*Witt's Theorems*); transitivity on the positive definite lines follows or is read from the identification with the symmetric space $U(1,3)/(U(1)\times U(3))$ of *The Krein Level Sets and the Hyperbolic Structure*. An isometry mapping the canonical positive line onto itself preserves its Krein-orthogonal complement, hence the fundamental decomposition, so it lies in $U(1)\times U(3)$; and the boost fixes the direction of $e_0+e_1$ up to a scalar.

## The J-Contractions

**Definition.** A $\mathbb{C}$-linear operator is a **$J$-contraction** when $\mathrm{id}-T^{\dagger}T$ is in the $J$-positive cone $\mathcal{P}_{J}=J\cdot\{S\ge0\}$ of *Indefinite Positivity and the Krein Cone of the Biquaternion Algebra*; its **defect operator** is $\mathrm{id}-T^{\dagger}T$, and it is **strict** when the defect is invertible.

**Theorem (the model $J$-contraction and the invariance).** The Krein-orthogonal projection $\pi_{-}=\tfrac12(\mathrm{id}-J)$ onto the vector subspace is a $J$-contraction whose defect is the projection $\pi_{+}=\tfrac12(\mathrm{id}+J)$ onto the centre, a $J$-positive operator; and the set of $J$-contractions is invariant under $T\mapsto U^{\dagger}TU$ for $U$ a Krein isometry. The scalar multiplications are not $J$-contractions unless they are isometries.

**Proof.** $[\pi_{-}\tilde{Q},\pi_{-}\tilde{Q}]=-\|v\|_E^{2}$ while $[\tilde{Q},\tilde{Q}]=\|c\|_E^{2}-\|v\|_E^{2}$, so the difference is $-\|c\|_E^{2}\le0$ and $\pi_{-}$ is a contraction; $\pi_{-}^{\dagger}=\pi_{-}$ and $\pi_{-}^{2}=\pi_{-}$, so the defect is $\mathrm{id}-\pi_{-}=\pi_{+}$, which is $J$-positive because $\pi_{+}=J\pi_{+}$ with $\pi_{+}\ge0$ for $\langle\cdot,\cdot\rangle$. For the invariance, if $U$ is a Krein isometry then $(U^{\dagger}TU)^{\dagger}(U^{\dagger}TU)=U^{\dagger}T^{\dagger}TU$, and $U^{\dagger}$ conjugates $\mathcal{P}_{J}$ to itself because $(U^{\dagger}PU)^{\dagger}=U^{\dagger}P^{\dagger}U$ and $[U^{\dagger}PU\tilde{Q},\tilde{Q}]=[PU\tilde{Q},U\tilde{Q}]$. For a central scalar $\tilde{Q}=re_0$ the defect is $(1-r^{2})\mathrm{id}$ and $J(1-r^{2})\mathrm{id}=(1-r^{2})J$ is definite positive only for $r=1$, so the scalar multiplications are contractions only in the isometry case.

**Remark (the group as the boundary of the contractions).** The $J$-contractions of norm one among the central multiplications are exactly the scalar part of the group, and the strict $J$-contractions form the open part; in the geometry of *The Krein Level Sets and the Hyperbolic Structure* the corresponding points are the interior of the complex hyperbolic ball.

## Worked Examples

**The identity.** $\mathrm{id}=L_{e_0}$ is a $J$-unitary operator, in $U(1)\times U(3)$.

**$J$ itself.** $J={}^{\natural}$ is a Krein isometry, of spectrum $\{+1,-1\}$; it is the fundamental symmetry of the canonical decomposition.

**A phase.** $L_{ce_0}$ with $|c|=1$: a Krein isometry with the single eigenvalue $c$.

**A sandwich.** $\Theta_{e_1}$ with $|N(e_1)|=1$: a Krein isometry and an inner automorphism, of spectrum $\{+1,-1\}$.

**A boost.** $T_{t}$ with $t=1$: a Krein isometry of spectrum $\{e,e^{-1},1,1\}$, off the unit circle, realising the Lorentz boost of the Minkowski slice.

**A contraction.** $\pi_{-}=\tfrac12(\mathrm{id}-J)$, the projection onto the vector subspace: a $J$-contraction with defect $\pi_{+}$, the projection onto the centre.

**A non-isometry that is not a contraction.** $L_{2e_0}$: $\mathrm{id}-L^{\dagger}L=-3\,\mathrm{id}$, whose image under $J$ is $-3J$, not in the definite positive cone, so $L_{2e_0}$ is neither a contraction nor an isometry.

## Summary

The Krein isometry group $U_{J}(\mathbb{B})=\{T:T^{\mathsf T*}ET=E\}$ is $U(1,3)$: real dimension $16$, non-compact, centre the scalar phases $U(1)$, maximal compact subgroup $U(1)\times U(3)$. A Krein isometry is characterised by $T^{*}JT=J$, equivalently $T^{-1}=T^{\dagger}$. Inside the algebra's families the Krein isometries are the central phases $L_{\tilde{Q}}$, $\tilde{Q}\in S^{1}e_0$, and the norm-one sandwiches $\Theta_{\tilde{Q}}$, $|N(\tilde{Q})|=1$; together they form the compact subgroup $U(1)\times PU(2)\cong U(1)\times SO(3)$ of dimension $4$, the sandwiches acting as the inner automorphisms of the algebra. The spectrum of a Krein isometry is invariant under $\lambda\mapsto1/\bar\lambda$ and is not confined to the unit circle: the boosts $T_{t}$ have $e^{\pm t},1,1$ and are the one-parameter subgroups realising the Lorentz boosts of the Minkowski slices. The group acts transitively on the isotropic lines, on the positive lines and on the maximal isotropic subspaces. Finally the $J$-contractions, defined by the $J$-positivity of their defect, are invariant under conjugation by the group; their model is the projection onto the vector subspace, whose defect is the projection onto the centre, while a scalar multiplication is a contraction only when it is an isometry.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $U_{J}(\mathbb{B})=\{T:T^{\mathsf T*}ET=E\}$ | The Krein isometry group, $\cong U(1,3)$ |
| $16$ | Its real dimension; non-compact |
| $U(1)$ | Its centre, the scalar phases |
| $U(1)\times U(3)$ | Its maximal compact subgroup |
| $U(1)\times PU(2)\cong U(1)\times SO(3)$ | The Krein isometries among the algebra's families |
| $\lambda\leftrightarrow1/\bar\lambda$ | The symmetry of the spectrum |
| $T_{t}$, $\mathrm{spec}=\{e^{t},e^{-t},1,1\}$ | The boosts; non-compactness; the Lorentz boosts |
| $\mathrm{id}-T^{\dagger}T\in\mathcal{P}_{J}$ | $J$-contraction and defect |

## Further Reading

- *J-Self-Adjoint and J-Unitary Operators on the Biquaternion Algebra* (`articles_maths/j-self-adjoint-and-j-unitary-operators-on-the-biquaternion-algebra.md`), for the criteria in the algebra's families
- *J-Normal Operators and the Indefinite Spectral Theorem* (`articles_maths/j-normal-operators-and-the-indefinite-spectral-theorem.md`), for normality and the spectral symmetries
- *The Krein Cartan Decomposition of the Operator Algebra* (`articles_maths/the-krein-cartan-decomposition-of-the-operator-algebra.md`), for the Lie algebra $\mathfrak{u}(1,3)$ and the maximal compact subalgebra
- *The Krein Level Sets and the Hyperbolic Structure* (`articles_maths/the-krein-level-sets-and-the-hyperbolic-structure.md`), for the complex hyperbolic ball on which the group acts
- *Indefinite Positivity and the Krein Cone of the Biquaternion Algebra* (`articles_maths/indefinite-positivity-and-the-krein-cone-of-the-biquaternion-algebra.md`), for the $J$-positive cone used in the definition of the contractions
- *Biquaternion Rotations and Lorentz Transformations* (`articles_maths/biquaternion-rotations-and-lorentz-transformations.md`), for the Lorentz transformations realised by the boosts
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for the unitary group of an indefinite form, its maximal compact part and the contractions
