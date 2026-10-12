# __The Two Metrics of the Split-Complex Numbers__

## Introduction

The split-complex space carries two distinguished forms (*The Two Forms and the Two Algebraic Norms of the Split-Complex Space*), and each of them induces a distance-like function on the one underlying plane. The **Euclidean metric** comes from the realification of the bilinear form $B$, and the **indefinite metric** from the realification of the Hermitian form $H$, whose diagonal is the norm $N(A)=a^{2}-a'^{2}$. This article defines both, computes their Gram matrices and signatures in the real basis $1$, $j$, reads their level sets and the null cone of the indefinite one, and identifies the group of linear maps preserving each. The two functions are then compared: they are the two real quadratic forms of a form pair, one definite and one indefinite, carried by one and the same space.

The word **metric** is used in the sense of the menu, for the quadratic function a form induces on the difference of two elements. Only the Euclidean one is a metric in the strict sense; the indefinite one is named a metric by the same convention, and the difference is stated where it occurs.

The article does not define the two forms, which are *The Two Forms and the Two Algebraic Norms of the Split-Complex Space*, nor the two algebraic norms $B(A)=A^{2}$ and $H(A)=A\bar A=N(A)$ that are their diagonals. The norm, its multiplicativity, the invertibility criterion, the group of units and the modulus $\rho$ are *Split-Complex Norm and Invertibility*, where the polarisation $g$ of the norm and the Euclidean form $\langle\cdot,\cdot\rangle$ are also defined; the topology is *Split-Complex Topology*. The hyperbolic rotations, the unit hyperbola and the classification of the maps preserving the form are *Hyperbolic Rotations*, below this article in this category. The group preserving the form, its algebraic name and its cover are *The Versors and the Orthogonal Group of the Split-Complex Numbers*, below this article in this category; the null quadric and its projectivity are *Split-Complex Null Quadric and Projective Geometry*, below this article in this category. The realification rule is *The Realification and the Effect of the Change of Scalars on the Split-Complex Numbers*.

**The split sign, stated once, because it decides the article.** On $\mathbb{C}$ the structure $J$ satisfies $J^{2}=-\mathrm{id}$, and there the Hermitian form is the definite one and gives the Euclidean metric, while the bilinear form is indefinite and gives the split metric. On $\mathbb{D}$ the structure satisfies $J^{2}=+\mathrm{id}$, and the roles are exchanged: the **bilinear** form $B=AC$ realifies to the definite Euclidean metric, and the **Hermitian** form $H=A\bar C$ realifies to the indefinite metric, whose diagonal is the split norm $N$ with its zero-divisor cone. The exchange is the two-dimensional instance of the rule of *The Realification and the Effect of the Change of Scalars on the Split-Complex Numbers*.

**Conventions.** The algebra is $\mathbb{D}=\mathbb{R}[x]/(x^{2}-1)$ over $\mathbb{R}$, with basis $1$, $j$ and $j^{2}=+1$; elements are $A=a+ja'$ and $C=c+jc'$ with real $a,a',c,c'$, and conjugation is $\bar A=a-ja'$. The global reading is bar $=$ the involution $j\mapsto-j$ and Hermitian star $=$ bar (*Conventions in Mathematics*). The letters $B$, $N$, $H$ and $K$ are reserved for the forms: $B(A,C)=AC$ is the general plain bilinear form and $H(A,C)=A\bar C$ the general plain sesquilinear or Hermitian form (*The Two Forms and the Two Algebraic Norms of the Split-Complex Space*). Elements are therefore written $A$ and $C$ and never $B$; the second element of the worked pair, $1-2j$, is written $C$ here.

## The Two Forms and Their Realifications

The two forms of the split-complex space are

$$
B(A,C)=AC, \qquad H(A,C)=A\bar C,
$$

the first the multiplication of the commutative ring, symmetric, and the second the derived operation of the algebra with its involution $j\mapsto-j$, conjugate-symmetric; both are $\mathbb{D}$-linear in the first slot and both have Gram matrix $[1]$ over $\mathbb{D}$ (*The Two Forms and the Two Algebraic Norms of the Split-Complex Space*). Their diagonals are the two algebraic norms,

$$
B(A,A)=A^{2}, \qquad H(A,A)=A\bar A=a^{2}-a'^{2}=N(A),
$$

the first $\mathbb{D}$-valued and anisotropic, vanishing only at the origin, the second real and indefinite, vanishing on the two null lines.

Both forms are $\mathbb{D}$-valued, and a real function is obtained from each by **realification**, the scalar part in the real basis $1$, $j$. With $A=a+ja'$ and $C=c+jc'$,

$$
\operatorname{Re}B(A,C)=ac+a'c', \qquad \operatorname{Re}H(A,C)=ac-a'c'.
$$

**Proposition (the two realified Gram matrices).** The realified forms have the Gram matrices

$$
[\operatorname{Re}B]=\mathrm{I}_{2}, \qquad [\operatorname{Re}H]=\operatorname{diag}(1,-1),
$$

of signatures $(2,0)$ and $(1,1)$.

*Proof.* The four values on the basis are $\operatorname{Re}B(1,1)=\operatorname{Re}B(j,j)=1$ and $\operatorname{Re}B(1,j)=0$, the last because $j^{2}=+1$ contributes no scalar part to $1\cdot j$; and $\operatorname{Re}H(1,1)=1$, $\operatorname{Re}H(j,j)=-1$, $\operatorname{Re}H(1,j)=0$, because $H(j,j)=j\bar j=-1$ and $H(1,j)=1\cdot\bar j=-j$ has scalar part zero. The two matrices are diagonal, and the signs of their diagonals give the signatures.

The realified $B$ is positive definite: it is the ordinary inner product of the plane, $\operatorname{Re}B(A,C)=ac+a'c'=\langle A,C\rangle$ in the notation of *Split-Complex Norm and Invertibility*. The realified $H$ is indefinite: it is the polarisation of the norm, $\operatorname{Re}H(A,C)=ac-a'c'=g(A,C)$, positive on the real direction $1$ and negative on the split imaginary direction $j$.

**Remark (the sign of the square of the structure decides the swap).** The realification carries the sign of the square of the structure that doubles the coordinate. When that structure squares to $-\mathrm{id}$, the two real blocks of a symmetric bilinear form carry opposite signs and the realified form is indefinite; this is the complex case, where $J^{2}=-\mathrm{id}$ and $B$ realifies to the signature $(1,1)$. Here $J^{2}=+\mathrm{id}$ and the two blocks carry the same sign, so $B$ realifies to $(2,0)$, and the indefinite realification is instead that of the Hermitian form $H$, whose diagonal $N$ carries the split sign. **This is the passage on which the present article and its complex counterpart are mirror images: the same two forms realify to the same two signatures, $(1,1)$ and $(2,0)$, but attached to the other form.**

## The Euclidean Metric

**Definition.** The **Euclidean metric** of the split-complex space is the quadratic function

$$
d_{B}^{2}(A,C)=\operatorname{Re}B(A-C,A-C)=(a-c)^{2}+(a'-c')^{2}.
$$

It is the diagonal of the realified bilinear form read on the difference $A-C$, and it is the square of the Euclidean norm of the difference, $\lVert A-C\rVert_{E}^{2}$ (*Split-Complex Norm and Invertibility*).

**Proposition (positive definiteness).** The Euclidean metric is real, non-negative, and vanishes exactly when $A=C$. Its Gram matrix is $\mathrm{I}_{2}$ and its signature is $(2,0)$; the only null difference is the zero difference.

*Proof.* The expression $(a-c)^{2}+(a'-c')^{2}$ is a sum of two squares of reals, hence non-negative and zero only when both differences vanish, that is when $A=C$. The Gram matrix was computed in the previous section.

**Proposition (it is a genuine distance).** The function $d_{B}(A,C)=\lVert A-C\rVert_{E}$ is symmetric, vanishes exactly on the diagonal, and satisfies the triangle inequality. These are the properties of the Euclidean norm of the difference (*Split-Complex Norm and Invertibility*), the norm that organises the plane of *Split-Complex Topology*.

The level sets are the circles: $d_{B}(A,C)=r$ is the Euclidean circle of radius $r$ about $C$. The form is definite, so there is no null cone beyond the point $A=C$.

**The group of maps preserving the form.** The $\mathbb{R}$-linear maps preserving the realified form are those whose matrix $M$ in the basis $1$, $j$ satisfies $M^{\mathsf T}M=\mathrm{I}_{2}$, that is the group $O(2)$. Its intersection with the $\mathbb{D}$-linear maps $A\mapsto uA$ is the four-element group $\{\pm1,\pm j\}$, since such a map preserves $\operatorname{Re}B$ exactly when $u^{2}=1$. That four-element group is also the shell of the plain algebraic norm, $\{A:A^{2}=\pm1\}$, and it is read again in *The Versors and the Orthogonal Group of the Split-Complex Numbers*, below this article in this category.

## The Indefinite Metric

**Definition.** The **indefinite metric** of the split-complex space is the quadratic function induced by the realified Hermitian form $H$,

$$
d_{H}^{2}(A,C)=\operatorname{Re}H(A-C,A-C)=N(A-C)=(a-c)^{2}-(a'-c')^{2}.
$$

It is the diagonal of the realified form read on the difference $A-C$, and it is the norm $N$ of the difference (*Split-Complex Norm and Invertibility*).

**Proposition (indefiniteness).** The indefinite metric is real and takes both signs. Its Gram matrix is $\operatorname{diag}(1,-1)$ and its signature is $(1,1)$; it is positive on the real direction and negative on the split imaginary one. It is therefore not a distance.

*Proof.* The value is the diagonal of the matrix $\operatorname{diag}(1,-1)$, a difference of two squares; on the difference $1$ it is $+1$ and on the difference $j$ it is $-1$. Since it changes sign, it is neither positive nor negative definite, and it cannot satisfy the axioms of a distance.

**The null cone.** The indefinite metric vanishes on the pairs whose separations satisfy $\lvert a-c\rvert=\lvert a'-c'\rvert$, that is

$$
d_{H}^{2}(A,C)=0 \iff a-c=\pm(a'-c').
$$

Through each point $C$ this is a pair of lines, of directions $1+j$ and $1-j$; the two directions are exchanged by conjugation, since $\overline{1+j}=1-j$. The null pair depends only on the difference, as does the metric itself, and through the origin it is the null cone of the norm, that is the zero-divisor set of the ring (*Split-Complex Zero Divisors*).

**The level sets.** For a constant $\kappa\neq0$ the equation $d_{H}^{2}(A,C)=\kappa$ is a hyperbola, the level set $\{N=\kappa\}$ translated by $C$; the two families $\kappa>0$ and $\kappa<0$ are exchanged by multiplication by $j$, and neither meets the null pair. The level $\kappa=1$ is the unit hyperbola, its level $\kappa=-1$ the conjugate hyperbola, both of *Hyperbolic Rotations*, below this article in this category. The indefinite metric is thus read by its null pair of lines and its two families of hyperbolas, in contrast with the circles of the Euclidean metric.

**The group of maps preserving the form.** The $\mathbb{R}$-linear maps preserving the realified form are those whose matrix $M$ in the basis $1$, $j$ satisfies

$$
M^{\mathsf T}\operatorname{diag}(1,-1)M=\operatorname{diag}(1,-1).
$$

Its identity component is the one-parameter group of **hyperbolic rotations**

$$
t\longmapsto\begin{pmatrix}\cosh t & \sinh t\\ \sinh t & \cosh t\end{pmatrix},
$$

which fixes the form and preserves its null pair as a set while moving it. The group has four components, and the $\mathbb{D}$-linear maps among its elements are the multiplications $A\mapsto uA$ with $N(u)=1$; the classification, the four components and the parametrisation are *Hyperbolic Rotations*, below this article in this category, and the group itself, its algebraic name and its cover are *The Versors and the Orthogonal Group of the Split-Complex Numbers*, below this article in this category.

## The Two Metrics Compared

The two metrics live on the same plane and are read from the two forms.

**Proposition (the two quadratics differ only in the sign of the square).** For all $A,C$,

$$
d_{B}^{2}(A,C)-d_{H}^{2}(A,C)=2(a'-c')^{2}, \qquad d_{B}^{2}(A,C)+d_{H}^{2}(A,C)=2(a-c)^{2}.
$$

*Proof.* Add and subtract the two coordinate expressions $(a-c)^{2}\pm(a'-c')^{2}$.

So each metric recovers one of the two squared coordinates from the pair, and the two differ by a positive term: the Euclidean metric is the sum, the indefinite metric the difference, of the two squared coordinate separations. In particular $d_{B}^{2}\geq d_{H}^{2}$ always, and the two agree exactly when the split imaginary separations vanish.

**Proposition (the forms are exchanged by conjugation in a slot).** For all $A,C$,

$$
\operatorname{Re}B(A,\bar C)=\operatorname{Re}H(A,C), \qquad \operatorname{Re}H(A,\bar C)=\operatorname{Re}B(A,C).
$$

*Proof.* $\operatorname{Re}B(A,\bar C)=\operatorname{Re}(A\bar C)=\operatorname{Re}H(A,C)$, and $\operatorname{Re}H(A,\bar C)=\operatorname{Re}(A\bar{\bar C})=\operatorname{Re}(AC)=\operatorname{Re}B(A,C)$, since $\bar{\bar C}=C$.

The two metrics are therefore the two readings of the two forms related by conjugation of the second argument.

**Proposition (multiplication by $j$ preserves one and reverses the other).** For the structure $J(A)=jA$,

$$
d_{B}^{2}(JA,JC)=d_{B}^{2}(A,C), \qquad d_{H}^{2}(JA,JC)=-d_{H}^{2}(A,C).
$$

*Proof.* In coordinates $J(a,a')=(a',a)$, since $j(a+ja')=a'+ja$; substituting gives $(a-c)^{2}+(a'-c')^{2}$ unchanged and $(a-c)^{2}-(a'-c')^{2}$ negated. Equivalently, the structure preserves the realified bilinear form and reverses the realified Hermitian form, the two-dimensional instance of the rule recorded in *The Realification and the Effect of the Change of Scalars on the Split-Complex Numbers*.

So multiplication by $j$ is a map preserving the Euclidean metric and reversing the sign of the indefinite one. The split complex structure is thus the operator that distinguishes the two metrics on the one space, exactly as the complex structure does on $\mathbb{C}$.

**Proposition (the two groups meet only in the centre).** The $\mathbb{D}$-linear maps preserving both realified forms are the two multiplications $\pm\mathrm{id}$.

*Proof.* A $\mathbb{D}$-linear map is $A\mapsto uA$. It preserves $\operatorname{Re}B$ exactly when $u^{2}=1$, since $\operatorname{Re}B(uA,uC)=\operatorname{Re}(u^{2}AC)$ and testing the two arguments $1$ and $j$ gives $p^{2}+q^{2}=1$ and $pq=0$ for $u=p+jq$. It preserves $\operatorname{Re}H$ exactly when $N(u)=1$, since $\operatorname{Re}H(uA,uC)=N(u)\operatorname{Re}H(A,C)$. Both conditions hold exactly for $u=\pm1$, because $\pm j$ satisfies the first and not the second.

So the definite group and the indefinite group of $\mathbb{D}$-linear maps share only the central pair: the Euclidean metric keeps the four elements $\{\pm1,\pm j\}$ and the indefinite metric keeps the hyperbola, and the two families meet only in $\{\pm1\}$. On $\mathbb{C}$ the two families are the circle and the pair $\{\pm1\}$; here they are the four-element group $\{\pm1,\pm j\}$ and the hyperbola, and the swap of their shapes is again the split sign.

**Remark (why the count is two and not three).** Accounts of the plane that count a third distance take the plain form $B$ to be the indefinite one, by analogy with the complex case, where the bilinear form is indeed indefinite; the analogy fails here. On $\mathbb{D}$ the plain form realifies to $\operatorname{Re}B(A,C)=ac+a'c'$ of signature $(2,0)$, which is the Euclidean metric itself, so the supposed third distance and the Euclidean metric coincide and the plane carries two. The split sign that moves the indefinite slot from the bilinear form to the Hermitian one is the reason, and it is the rule of *The Realification and the Effect of the Change of Scalars on the Split-Complex Numbers*.

**Remark (the realified signatures).** **The split-complex space carries a definite and an indefinite real form at once, and the split sign decides which form supplies which**: the definite slot is occupied by the bilinear form.

## Worked Example

For the worked pair $A=3+4j$ and $C=1-2j$, the difference is $A-C=2+6j$, so

$$
d_{B}^{2}(A,C)=2^{2}+6^{2}=40, \qquad d_{H}^{2}(A,C)=2^{2}-6^{2}=-32.
$$

The two identities of the comparison read $d_{B}^{2}-d_{H}^{2}=72=2\cdot6^{2}$ and $d_{B}^{2}+d_{H}^{2}=8=2\cdot2^{2}$. The Euclidean metric is positive on the separation $2+6j$, while the indefinite metric is negative on it; the two metrics disagree on its sign because the second is indefinite.

For the null pair, a difference on the line of direction $1+j$ is $A=t(1+j)$, and indeed

$$
d_{H}^{2}(t(1+j),0)=t^{2}-t^{2}=0
$$

for every real $t$; the same holds on the line of direction $1-j$. On those differences the Euclidean metric is $d_{B}^{2}=2t^{2}$, so the null lines of the indefinite metric are the directions on which its value vanishes while the Euclidean value stays positive.

## Summary

The one split-complex plane carries two real quadratic functions, one from each of the two forms, and the split sign decides which. The general plain bilinear form $B(A,C)=AC$ realifies to the Euclidean metric $d_{B}^{2}(A,C)=(a-c)^{2}+(a'-c')^{2}$, of Gram matrix $\mathrm{I}_{2}$ and signature $(2,0)$, positive definite, whose level sets are the circles, whose group of form-preserving $\mathbb{R}$-linear maps is $O(2)$ and whose genuine distance is the Euclidean norm of the difference. The general plain Hermitian form $H(A,C)=A\bar C$ realifies to the indefinite metric $d_{H}^{2}(A,C)=(a-c)^{2}-(a'-c')^{2}=N(A-C)$, of Gram matrix $\operatorname{diag}(1,-1)$ and signature $(1,1)$, indefinite, whose null set is the pair of lines $a-c=\pm(a'-c')$, the zero-divisor directions of the ring, whose nonzero level sets are the two families of hyperbolas, and whose group of form-preserving $\mathbb{R}$-linear maps has the hyperbolic rotations as identity component and four components in all.

The two metrics are the two readings of the two forms and satisfy $d_{B}^{2}-d_{H}^{2}=2(a'-c')^{2}$ and $d_{B}^{2}+d_{H}^{2}=2(a-c)^{2}$; the forms are exchanged by conjugation of the second slot, $\operatorname{Re}B(A,\bar C)=\operatorname{Re}H(A,C)$, and multiplication by $j$ preserves the Euclidean metric and reverses the indefinite one. The definite slot is on the bilinear form rather than the Hermitian one, and this exchange of the slots is the split sign $J^{2}=+\mathrm{id}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A=a+ja'$, $C=c+jc'$ | two elements of $\mathbb{D}$, with $a,a',c,c'\in\mathbb{R}$ |
| $\bar A=a-ja'$ | the conjugation, the involution $j\mapsto-j$ |
| $B(A,C)=AC$ | general plain bilinear form; Gram matrix $[1]$ over $\mathbb{D}$; diagonal $B(A)=A^{2}$, anisotropic |
| $H(A,C)=A\bar C$ | general plain Hermitian form; Gram matrix $[1]$ over $\mathbb{D}$; diagonal $H(A)=N(A)=a^{2}-a'^{2}$, indefinite |
| $\operatorname{Re}B(A,C)=ac+a'c'$ | the realified bilinear form, the Euclidean form $\langle A,C\rangle$; Gram matrix $\mathrm{I}_{2}$; signature $(2,0)$ |
| $\operatorname{Re}H(A,C)=ac-a'c'$ | the realified Hermitian form, the polarisation $g$; Gram matrix $\operatorname{diag}(1,-1)$; signature $(1,1)$ |
| $d_{B}^{2}(A,C)=\lVert A-C\rVert_{E}^{2}$ | Euclidean metric; positive definite; level sets the circles |
| $d_{H}^{2}(A,C)=N(A-C)$ | indefinite metric; signature $(1,1)$; level sets the hyperbolas |
| $a-c=\pm(a'-c')$ | the null pair of lines of the indefinite metric |
| $M^{\mathsf T}M=\mathrm{I}_{2}$ | the condition for preserving $\operatorname{Re}B$; the group $O(2)$ |
| $M^{\mathsf T}\operatorname{diag}(1,-1)M=\operatorname{diag}(1,-1)$ | the condition for preserving $\operatorname{Re}H$ |
| $J(A)=jA$ | the split complex structure, $J^{2}=+\mathrm{id}$; preserves $d_{B}^{2}$, reverses $d_{H}^{2}$ |
| $\{\pm1,\pm j\}$, $\{N=1\}$ | the $\mathbb{D}$-linear preservers of $d_{B}^{2}$ and of $d_{H}^{2}$ |

## Further Reading

- *The Two Forms and the Two Algebraic Norms of the Split-Complex Space* (`articles_maths/the-two-forms-and-the-two-algebraic-norms-of-the-split-complex-space.md`), for the two forms and the two algebraic norms whose diagonals are their squares.
- *The Realification and the Effect of the Change of Scalars on the Split-Complex Numbers* (`articles_maths/the-realification-and-the-effect-of-the-change-of-scalars-on-the-split-complex-numbers.md`), for the realification rules that give the signatures $(2,0)$ and $(1,1)$ and the sign of the structure.
- *Split-Complex Norm and Invertibility* (`articles_maths/split-complex-norm-and-invertibility.md`), for the norm, its polarisation $g$, the Euclidean form, the modulus and the group of units.
- *Split-Complex Topology* (`articles_maths/split-complex-topology.md`), for the Euclidean plane, its contractibility and the null cone as a removed pair of lines.
- *Hyperbolic Rotations* (`articles_maths/hyperbolic-rotations.md`), for the hyperbolic rotations, the unit hyperbola and the classification of the maps preserving the form.
- *The Versors and the Orthogonal Group of the Split-Complex Numbers* (`articles_maths/the-versors-and-the-orthogonal-group-of-the-split-complex-numbers.md`), for the group preserving the indefinite form, its algebraic name and its cover.
- *Split-Complex Null Quadric and Projective Geometry* (`articles_maths/split-complex-null-quadric-and-projective-geometry.md`), for the null cone of the indefinite metric read projectively.
- *Split-Complex Subspaces* (`articles_maths/split-complex-subspaces.md`), for the real and split imaginary subspaces on which the indefinite metric is definite of opposite signs.
- *The Two Metrics of the Complex Numbers* (`articles_maths/the-two-metrics-of-the-complex-numbers.md`), for the mirror image of the present pair, where the definite slot is on the Hermitian form.
- Werner Greub, *Linear Algebra*, 4th edition (Springer, 1981), for Gram matrices, inertia and the groups preserving a symmetric or Hermitian form.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd edition (Cambridge University Press, 2001), for the definite and indefinite forms of the plane and their groups.
