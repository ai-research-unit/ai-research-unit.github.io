
# __The Two Metrics of the Complex Numbers__

## Introduction

The complex space carries two distinguished forms (*The Two Forms and the Two Algebraic Norms of the Complexoid Space*), and each of them induces a distance-like function on the one underlying plane. The **Euclidean metric** comes from the definite Hermitian form $\langle\cdot,\cdot\rangle_{*}$, and the **split metric** from the realified bilinear form $\langle\cdot,\cdot\rangle$. This article defines both, computes their Gram matrices and signatures in the real basis $1$, $i$, reads their level sets and the null cone of the indefinite one, and identifies the group of linear maps preserving each. The two functions are then compared: they are the definite and the indefinite quadratic forms carried by the one plane.

The word **metric** is used in the sense of the menu, for the quadratic function a form induces on the difference of two elements. Only the Euclidean one is a metric in the strict sense; the split one is an indefinite quadratic function and is named a metric by the same convention, and the difference is stated where it occurs.

The article does not define the two forms, which are *The Two Forms and the Two Algebraic Norms of the Complexoid Space*, nor the two algebraic norms $Q_1^{2}$ and $\langle Q_1\rangle_{*}$ that are their diagonals. The modulus $\sqrt{\langle Q_1\rangle_{*}}=\sqrt{H(Q_1)}$, its multiplicativity, its triangle inequality, the invertibility criterion and the group of units are *Complex Norm and Invertibility*. The topology is *Complex Topology*; the reflections and the group of maps preserving the definite form are *Rotations and Reflections in the Complex Plane*, below this article in this category. The realification by which a complex form becomes a real bilinear form is the two-dimensional case of *The Realification and the Effect of the Change of Scalars*.

**Conventions.** The algebra is $\mathbb{C}$ over $\mathbb{R}$, with basis $1$, $i$ and $i^{2}=-1$; elements are $Q_1=q_1+iq'_1$ and $Q_2=q_2+iq'_2$ with real $q_1,q'_1,q_2,q'_2$, and conjugation is $\bar Q_1=q_1-iq'_1$. The global reading is bar $=$ complex conjugation and Hermitian star $=$ bar, the complex block reading $\mathbb{C}$ over $\mathbb{R}$ and calling complex conjugation its one nontrivial involution, beside the identity (*Complex Algebra*, *Complexoid Subspaces*, *Conventions in Mathematics*). The four general forms are written with brackets — $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\natural}$ the two bilinear, $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural*}$ the two sesquilinear; on $\mathbb{C}$ the two bilinear forms coincide and the two sesquilinear forms coincide, and the two forms read here are the plain bilinear form $\langle Q_1,Q_2\rangle=Q_1Q_2$ and the Hermitian form $\langle Q_1,Q_2\rangle_{*}=Q_1\bar Q_2$ (*The Two Forms and the Two Algebraic Norms of the Complexoid Space*). Elements are therefore written $Q_1$ and $Q_2$ and never $B$; the worked second element of the category, $1-2i$, is written $Q_2$ here.

## The Two Forms and Their Realifications

The two forms of the complex space are

$$
B(Q_1,Q_2)=Q_1Q_2, \qquad H(Q_1,Q_2)=Q_1\bar Q_2,
$$

the first the multiplication of the field, symmetric, and the second the derived operation of the algebra, conjugate-symmetric; the two products of the complex space are exactly these, $Q_1Q_2$ and $Q_1\bar Q_2$ (*The Two Products of the Complexoid Space*). Both are $\mathbb{C}$-linear in the first slot and both have Gram matrix $[1]$ over $\mathbb{C}$ (*The Two Forms and the Two Algebraic Norms of the Complexoid Space*). Their diagonals are the two algebraic norms,

$$
B(Q_1,Q_1)=Q_1^{2}, \qquad H(Q_1,Q_1)=Q_1\bar Q_1=\langle Q_1\rangle_{*},
$$

the first complex and anisotropic and the second real, positive definite and multiplicative. The form $\langle\cdot,\cdot\rangle$ is the two-dimensional case of the general plain bilinear form and $\langle\cdot,\cdot\rangle_{*}$ the case of the general plain sesquilinear form; the two bilinear forms coincide and the two sesquilinear forms coincide, so $B=\langle\cdot,\cdot\rangle_{\natural}$ and $H=\langle\cdot,\cdot\rangle_{\natural*}$, which is the reason the two diagonal norms are written $Q_1^{2}$ and $\langle Q_1\rangle_{*}$.

Both forms are complex-valued, and a real function is obtained from each by realification. In the real basis $1$, $i$, with $Q_1=q_1+iq'_1$ and $Q_2=q_2+iq'_2$,

$$
\operatorname{Re}B(Q_1,Q_2)=q_1q_2-q'_1q'_2, \qquad \operatorname{Re}H(Q_1,Q_2)=q_1q_2+q'_1q'_2.
$$

**Proposition (the two realified Gram matrices).** The realified forms have the Gram matrices

$$
[\operatorname{Re}B]=\operatorname{diag}(1,-1), \qquad [\operatorname{Re}H]=\mathrm{I}_{2},
$$

of signatures $(1,1)$ and $(2,0)$.

*Proof.* The four values on the basis are $\operatorname{Re}B(1,1)=1$, $\operatorname{Re}B(1,i)=0$, $\operatorname{Re}B(i,i)=-1$ and $\operatorname{Re}H(1,1)=\operatorname{Re}H(i,i)=1$, $\operatorname{Re}H(1,i)=0$. The two matrices are diagonal, and the signs of their diagonals give the signatures.

The realified Hermitian form is the ordinary inner product of the plane, $\operatorname{Re}H(Q_1,Q_2)=q_1q_2+q'_1q'_2$, and its diagonal is the real norm $\langle Q_1\rangle_{*}$. The realified $\langle\cdot,\cdot\rangle$ is indefinite: it is positive on the real direction $1$ and negative on the imaginary direction $i$. The two realifications are the scalar readings of the two complex forms, and the rules behind them — a symmetric bilinear form realifying to the split signature $(1,1)$ and a Hermitian form doubling its inertia to $(2,0)$ — are those of *The Realification and the Effect of the Change of Scalars*.

## The Euclidean Metric

**Definition.** The **Euclidean metric** of the complex space is the quadratic function

$$
d_{H}^{2}(Q_1,Q_2)=H(Q_1-Q_2,Q_1-Q_2)=\langle Q_1-Q_2\rangle_{*}=(q_1-q_2)^{2}+(q'_1-q'_2)^{2}.
$$

It is the diagonal of the definite form $\langle\cdot,\cdot\rangle_{*}$ read on the difference $Q_1-Q_2$; the modulus $\lvert\cdot\rvert$ and its multiplicativity are *Complex Norm and Invertibility*.

**Proposition (positive definiteness).** The Euclidean metric is real, non-negative, and vanishes exactly when $Q_1=Q_2$. Its Gram matrix is $\mathrm{I}_{2}$ and its signature is $(2,0)$; the only null difference is the zero difference.

*Proof.* The expression $(q_1-q_2)^{2}+(q'_1-q'_2)^{2}$ is a sum of two squares of reals, hence non-negative and zero only when both differences vanish, that is when $Q_1=Q_2$. The Gram matrix was computed in the previous section.

**Proposition (it is a genuine distance).** The function $d_{H}(Q_1,Q_2)=\sqrt{\langle Q_1-Q_2\rangle_{*}}$ is symmetric, vanishes exactly on the diagonal, and satisfies the triangle inequality. These are the properties of the modulus of *Complex Norm and Invertibility*, read on the difference.

The level sets are the circles: $d_{H}(Q_1,Q_2)=r$ is the circle of radius $r$ about $Q_2$. The form is definite, so there is no null cone beyond the point $Q_1=Q_2$.

**The group of maps preserving the form.** The $\mathbb{C}$-linear maps preserving $\langle\cdot,\cdot\rangle_{*}$ are the multiplications by the units of norm one, $Q\mapsto uQ$ with $\lvert u\rvert=1$; the identification of this group of multiplications with $\mathrm{SO}(2)$, together with the reading of the parameter, is *Rotations and Reflections in the Complex Plane*, below this article in this category. The full group of $\mathbb{R}$-linear maps preserving $H$ is the group $O(2)$, given by the matrix condition

$$
M^{\mathsf T}M=\mathrm{I}_{2}
$$

on the matrix of the map in the basis $1$, $i$. The maps of determinant $+1$ in it are exactly the multiplications $Q\mapsto uQ$ with $\lvert u\rvert=1$, and those of determinant $-1$ are exactly the reflections $Q\mapsto u\bar Q$ with $\lvert u\rvert=1$ (*Rotations and Reflections in the Complex Plane*, below this article in this category).

## The Split Metric

**Definition.** The **split metric** of the complex space is the quadratic function induced by the realified bilinear form $\langle\cdot,\cdot\rangle$,

$$
d_{B}^{2}(Q_1,Q_2)=\operatorname{Re}B(Q_1-Q_2,Q_1-Q_2)=\operatorname{Re}\bigl((Q_1-Q_2)^{2}\bigr)=(q_1-q_2)^{2}-(q'_1-q'_2)^{2}.
$$

It is the diagonal of the realified form read on the difference $Q_1-Q_2$.

**Proposition (indefiniteness).** The split metric is real and takes both signs. Its Gram matrix is $\operatorname{diag}(1,-1)$ and its signature is $(1,1)$; it is positive on the real direction and negative on the imaginary one. It is therefore not a distance.

*Proof.* The value is the diagonal of the matrix $\operatorname{diag}(1,-1)$, a difference of two squares; on $Q=1$ it is $+1$ and on $Q=i$ it is $-1$. Since it changes sign, it is neither positive nor negative definite, and it cannot satisfy the axioms of a distance.

**The null cone.** The split metric vanishes on the pairs whose separations satisfy $\lvert q_1-q_2\rvert=\lvert q'_1-q'_2\rvert$, that is

$$
d_{B}^{2}(Q_1,Q_2)=0 \iff q_1-q_2=\pm(q'_1-q'_2).
$$

Through each point $Q_2$ this is a pair of lines, of directions $1+i$ and $1-i$; the two directions are exchanged by conjugation, since $\overline{1+i}=1-i$. The null pair depends only on the difference, as does the metric itself.

**The level sets.** For a constant $\kappa\neq0$ the equation $d_{B}^{2}(Q_1,Q_2)=\kappa$ is a hyperbola; the two families $\kappa>0$ and $\kappa<0$ are exchanged by the multiplication by $i$, and neither meets the null pair. The split metric is thus read by its null pair of lines and its two families of hyperbolas, in contrast with the circles of the Euclidean metric.

**The group of maps preserving the form.** The $\mathbb{R}$-linear maps preserving the realified form are those whose matrix $M$ in the basis $1$, $i$ satisfies

$$
M^{\mathsf T}\operatorname{diag}(1,-1)M=\operatorname{diag}(1,-1),
$$

the group $O(1,1)$. Its subgroup whose elements fix the two null lines of $d_{B}^{2}$ separately consists of the matrices

$$
\begin{pmatrix}a & b\\ b & a\end{pmatrix}, \qquad a^{2}-b^{2}=1,
$$

each rescaling the direction $1+i$ by $a+b$ and the direction $1-i$ by $a-b$. The group is the split reading of the definite group of the previous section, and no map of the plane preserves the two realified forms at once except the four of the comparison below: the complex-linear ones among them are only the central pair $\pm1$.

## The Two Metrics Compared

The two metrics live on the same plane and are read from the two forms.

**Proposition (the two quadratics differ only in the sign of the square).** For all $Q_1,Q_2$,

$$
d_{H}^{2}(Q_1,Q_2)-d_{B}^{2}(Q_1,Q_2)=2(q'_1-q'_2)^{2}, \qquad d_{H}^{2}(Q_1,Q_2)+d_{B}^{2}(Q_1,Q_2)=2(q_1-q_2)^{2}.
$$

*Proof.* Add and subtract the two coordinate expressions $(q_1-q_2)^{2}\pm(q'_1-q'_2)^{2}$.

So each metric recovers one of the two squared coordinates from the pair, and the two differ by a positive term: the Euclidean metric is the sum, the split metric the difference, of the two squared coordinate separations. In particular $d_{H}^{2}\geq d_{B}^{2}$ always, and the two agree exactly when the imaginary separations vanish.

**Proposition (the forms are exchanged by conjugation in a slot).** For all $Q_1,Q_2$,

$$
H(Q_1,Q_2)=B(Q_1,\bar Q_2), \qquad B(Q_1,Q_2)=H(Q_1,\bar Q_2).
$$

*Proof.* $B(Q_1,\bar Q_2)=Q_1\bar Q_2=H(Q_1,Q_2)$, and $H(Q_1,\bar Q_2)=Q_1\overline{\bar Q_2}=Q_1Q_2=B(Q_1,Q_2)$.

The two metrics are therefore the two readings of the two forms related by conjugation of the second argument.

**Proposition (multiplication by $i$ preserves one and reverses the other).** For the complex structure $J(Q)=iQ$,

$$
d_{H}^{2}(JQ_1,JQ_2)=d_{H}^{2}(Q_1,Q_2), \qquad d_{B}^{2}(JQ_1,JQ_2)=-d_{B}^{2}(Q_1,Q_2).
$$

*Proof.* In coordinates $J(q_1,q'_1)=(-q'_1,q_1)$; substituting gives $(q_1-q_2)^{2}+(q'_1-q'_2)^{2}$ unchanged and $(q_1-q_2)^{2}-(q'_1-q'_2)^{2}$ negated. Equivalently, the realified Hermitian form is preserved by $J$ and the realified bilinear form is reversed, as the realification rules record.

So multiplication by $i$ preserves the Euclidean metric and reverses the split one. The complex structure is thus the operator that distinguishes the two metrics on the one space.

**Proposition (the elements common to the two groups).** The complex-linear maps preserving both realified forms are the two multiplications $\pm\mathrm{id}$. The full real-linear groups $O(2)$ and $O(1,1)$ meet in the four maps $\pm\mathrm{id}$ and $\pm\mathrm{conj}$, where $\mathrm{conj}(Q)=\bar Q$.

*Proof.* A $\mathbb{C}$-linear map is $Q\mapsto uQ$. It preserves $\operatorname{Re}H$ exactly when $\lvert u\rvert=1$, since $\operatorname{Re}H(uQ_1,uQ_2)=\lvert u\rvert^{2}\operatorname{Re}H(Q_1,Q_2)$. It preserves $\operatorname{Re}B$ exactly when $u^{2}=1$, since $\operatorname{Re}B(uQ_1,uQ_2)=\operatorname{Re}(u^{2}Q_1Q_2)$ and testing $Q_1=Q_2=1$ gives $\operatorname{Re}(u^{2})=1$ while testing $Q_1=1$, $Q_2=i$ gives $\operatorname{Im}(u^{2})=0$. Hence $u=\pm1$. For the full groups, a matrix that is orthogonal, $M^{\mathsf T}M=\mathrm{I}_{2}$, and preserves $\operatorname{diag}(1,-1)$ has orthogonal inverse and so commutes with $\operatorname{diag}(1,-1)$; since the two eigenvalues are distinct it preserves each eigenspace, hence is diagonal with entries $\pm1$. The four diagonal sign matrices are exactly $\pm\mathrm{id}$ and $\pm\mathrm{conj}$.

So the complex-linear coincidences are only the central pair, while the two real groups $O(2)$ and $O(1,1)$ share a Klein four group; neither group contains the other, and each enlarges the common pair in its own direction.

**Remark (the realified signatures).** The complex space carries a definite and an indefinite real form at once, and the pair $(1,1)$, $(2,0)$ is its realified signature pair.

## Worked Example

For the worked pair of the category, $Q_1=3+4i$ and $Q_2=1-2i$, the difference is $Q_1-Q_2=2+6i$, so

$$
d_{H}^{2}(Q_1,Q_2)=2^{2}+6^{2}=40, \qquad d_{B}^{2}(Q_1,Q_2)=2^{2}-6^{2}=-32.
$$

The two identities of the comparison read $d_{H}^{2}-d_{B}^{2}=72=2\cdot6^{2}$ and $d_{H}^{2}+d_{B}^{2}=8=2\cdot2^{2}$. The Euclidean metric is positive on the separation $2+6i$, while the split metric is negative on it; the two metrics disagree on its sign because the second is indefinite.

For the null pair, a difference on the line of direction $1+i$ is $Q=t(1+i)$, and indeed

$$
d_{B}^{2}(t(1+i),0)=t^{2}-t^{2}=0
$$

for every real $t$; the same holds on the line of direction $1-i$. On those differences the Euclidean metric is $d_{H}^{2}=2t^{2}$, so the null lines of the split metric are the directions on which the split value vanishes while the Euclidean value stays positive.

## Summary

The one complex plane carries two real quadratic functions, one from each of the two forms. The definite Hermitian form $\langle Q_1,Q_2\rangle_{*}=Q_1\bar Q_2$ gives the Euclidean metric $d_{H}^{2}(Q_1,Q_2)=(q_1-q_2)^{2}+(q'_1-q'_2)^{2}$, of Gram matrix $\mathrm{I}_{2}$ and signature $(2,0)$, positive definite, whose level sets are the circles, whose group of form-preserving $\mathbb{R}$-linear maps is $O(2)$ and whose genuine distance is the modulus of the difference. The realified plain bilinear form $\langle Q_1,Q_2\rangle=Q_1Q_2$ gives the split metric $d_{B}^{2}(Q_1,Q_2)=(q_1-q_2)^{2}-(q'_1-q'_2)^{2}$, of Gram matrix $\operatorname{diag}(1,-1)$ and signature $(1,1)$, indefinite, whose null set is the pair of lines $q_1-q_2=\pm(q'_1-q'_2)$, whose nonzero level sets are the two families of hyperbolas, and whose group of form-preserving $\mathbb{R}$-linear maps is $O(1,1)$, whose subgroup fixing the two null lines rescales them.

The two metrics are the two readings of the two forms and satisfy $d_{H}^{2}-d_{B}^{2}=2(q'_1-q'_2)^{2}$ and $d_{H}^{2}+d_{B}^{2}=2(q_1-q_2)^{2}$; the forms are exchanged by conjugation of the second slot, $\langle Q_1,Q_2\rangle_{*}=B(Q_1,\bar Q_2)$, and multiplication by $i$ preserves the Euclidean metric and reverses the split one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Q_1=q_1+iq'_1$, $Q_2=q_2+iq'_2$ | two elements of $\mathbb{C}$, with $q_1,q'_1,q_2,q'_2\in\mathbb{R}$ |
| $\bar Q_1=q_1-iq'_1$ | complex conjugation, the bar |
| $B(Q_1,Q_2)=Q_1Q_2$ | the plain bilinear form, $\langle\cdot,\cdot\rangle_{\natural}$; Gram matrix $[1]$ over $\mathbb{C}$ |
| $H(Q_1,Q_2)=Q_1\bar Q_2$ | the Hermitian form, $\langle\cdot,\cdot\rangle_{\natural*}$; Gram matrix $[1]$ over $\mathbb{C}$ |
| $\operatorname{Re}B(Q_1,Q_2)=q_1q_2-q'_1q'_2$ | the realified bilinear form; Gram matrix $\operatorname{diag}(1,-1)$; signature $(1,1)$ |
| $\operatorname{Re}H(Q_1,Q_2)=q_1q_2+q'_1q'_2$ | the realified Hermitian form; Gram matrix $\mathrm{I}_{2}$; signature $(2,0)$ |
| $d_{H}^{2}(Q_1,Q_2)=\langle Q_1-Q_2\rangle_{*}$ | Euclidean metric; positive definite; level sets the circles |
| $d_{B}^{2}(Q_1,Q_2)=\operatorname{Re}\bigl((Q_1-Q_2)^{2}\bigr)$ | split metric; indefinite; level sets the hyperbolas |
| $q_1-q_2=\pm(q'_1-q'_2)$ | the null pair of lines of the split metric |
| $M^{\mathsf T}M=\mathrm{I}_{2}$ | the condition for preserving $\operatorname{Re}H$; the group $O(2)$ |
| $M^{\mathsf T}\operatorname{diag}(1,-1)M=\operatorname{diag}(1,-1)$ | the condition for preserving $\operatorname{Re}B$; the group $O(1,1)$ |
| $J(Q)=iQ$ | the complex structure; preserves $d_{H}^{2}$, reverses $d_{B}^{2}$ |

## Further Reading

- [The Two Forms and the Two Algebraic Norms of the Complexoid Space](the-two-forms-and-the-two-algebraic-norms-of-the-complexoid-space.html), for the two forms and the two algebraic norms whose diagonals are their squares.
- [The Two Products of the Complexoid Space](the-two-products-of-the-complexoid-space.html), for the two products $Q_1Q_2$ and $Q_1\bar Q_2$ whose forms are realified here.
- [The Realification and the Effect of the Change of Scalars](the-realification-and-the-effect-of-the-change-of-scalars-on-the-complexoid.html), the complex article of that name, for the realification rules that give the signatures $(1,1)$ and $(2,0)$.
- [Complex Algebra](complex-algebra.html), for the algebra, its basis and its one nontrivial involution.
- [Complex Norm and Invertibility](complex-norm-and-invertibility.html), for the modulus, its multiplicativity, its triangle inequality and the group of units.
- [Rotations and Reflections in the Complex Plane](rotations-and-reflections-in-the-complex-plane.html), for the identification of the form-preserving multiplications with $\mathrm{SO}(2)$, the reflections and the group $O(2)$.
- [Complexoid Subspaces](complexoid-subspaces.html), for the real and imaginary subspaces on which the split metric is definite of opposite signs.
- [Remarkable Subspaces of the Complexoid and the Two Forms](remarkable-subspaces-of-the-complexoid-and-the-two-forms.html), for the restrictions of the two forms to the two subspaces.
- Werner Greub, *Linear Algebra*, 4th edition (Springer, 1981), for Gram matrices, inertia and the groups preserving a symmetric or Hermitian form.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd edition (Cambridge University Press, 2001), for the definite and indefinite forms of the plane and their groups.
