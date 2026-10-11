
# __The Two Metrics of the Complex Numbers__

## Introduction

The complex space carries two distinguished forms (*The Two Forms and the Two Algebraic Norms of the Complex Space*), and each of them induces a distance-like function on the one underlying plane. The **Euclidean metric** comes from the definite Hermitian form $H$, and the **split metric** from the realified bilinear form $B$. This article defines both, computes their Gram matrices and signatures in the real basis $1$, $i$, reads their level sets and the null cone of the indefinite one, and identifies the group of linear maps preserving each. The two functions are then compared: they are the definite and the indefinite quadratic forms carried by the one plane.

The word **metric** is used in the sense of the menu, for the quadratic function a form induces on the difference of two elements. Only the Euclidean one is a metric in the strict sense; the split one is an indefinite quadratic function and is named a metric by the same convention, and the difference is stated where it occurs.

The article does not define the two forms, which are *The Two Forms and the Two Algebraic Norms of the Complex Space*, nor the two algebraic norms $A^{2}$ and $\lvert A\rvert^{2}$ that are their diagonals. The modulus $\lvert A\rvert=\sqrt{H(A)}$, its multiplicativity, its triangle inequality, the invertibility criterion and the group of units are *Complex Norm and Invertibility*. The topology is *Complex Topology*; the reflections and the group of maps preserving the definite form are *Rotations and Reflections in the Complex Plane*, below this article in this category. The realification by which a complex form becomes a real bilinear form is the two-dimensional case of *The Realification and the Effect of the Change of Scalars*.

**Conventions.** The algebra is $\mathbb{C}$ over $\mathbb{R}$, with basis $1$, $i$ and $i^{2}=-1$; elements are $A=a+ia'$ and $C=c+ic'$ with real $a,a',c,c'$, and conjugation is $\bar A=a-ia'$. The global reading is bar $=$ complex conjugation, natural sign $=$ identity and Hermitian star $=$ bar, the complex block reading $\mathbb{C}$ over $\mathbb{R}$ and calling complex conjugation its one nontrivial involution, beside the identity (*Complex Algebra*, *Complex Subspaces*, *Conventions in Mathematics*). The letters $B$, $N$, $H$ and $K$ are the four general forms of the biquaternion method; on $\mathbb{C}$, which is the centre, the two bilinear forms coincide and the two sesquilinear forms coincide, and the two forms read here are the plain bilinear form $B(A,C)=AC$ and the Hermitian form $H(A,C)=A\bar C$ (*The Two Forms and the Two Algebraic Norms of the Complex Space*). Elements are therefore written $A$ and $C$ and never $B$; the worked second element of the category, $1-2i$, is written $C$ here.

## The Two Forms and Their Realifications

The two forms of the complex space are

$$
B(A,C)=AC, \qquad H(A,C)=A\bar C,
$$

the first the multiplication of the field, symmetric, and the second the derived operation of the algebra, conjugate-symmetric; the two products of the complex space are exactly these, $AC$ and $A\bar C$ (*The Two Products of the Complex Space*). Both are $\mathbb{C}$-linear in the first slot and both have Gram matrix $[1]$ over $\mathbb{C}$ (*The Two Forms and the Two Algebraic Norms of the Complex Space*). Their diagonals are the two algebraic norms,

$$
B(A,A)=A^{2}, \qquad H(A,A)=A\bar A=\lvert A\rvert^{2},
$$

the first complex and anisotropic and the second real, positive definite and multiplicative. The form $B$ is the two-dimensional case of the general plain bilinear form of the biquaternion method and $H$ the case of the general plain sesquilinear form; on the centre of $\mathbb{B}$ the plain and the quaternionic forms coincide, so $B=N$ and $H=K$ there, which is the reason the two diagonal norms are written $A^{2}$ and $\lvert A\rvert^{2}$.

Both forms are complex-valued, and a real function is obtained from each by realification. In the real basis $1$, $i$, with $A=a+ia'$ and $C=c+ic'$,

$$
\operatorname{Re}B(A,C)=ac-a'c', \qquad \operatorname{Re}H(A,C)=ac+a'c'.
$$

**Proposition (the two realified Gram matrices).** The realified forms have the Gram matrices

$$
[\operatorname{Re}B]=\operatorname{diag}(1,-1), \qquad [\operatorname{Re}H]=\mathrm{I}_{2},
$$

of signatures $(1,1)$ and $(2,0)$.

*Proof.* The four values on the basis are $\operatorname{Re}B(1,1)=1$, $\operatorname{Re}B(1,i)=0$, $\operatorname{Re}B(i,i)=-1$ and $\operatorname{Re}H(1,1)=\operatorname{Re}H(i,i)=1$, $\operatorname{Re}H(1,i)=0$. The two matrices are diagonal, and the signs of their diagonals give the signatures.

The realified Hermitian form is the ordinary inner product of the plane, $\operatorname{Re}H(A,C)=ac+a'c'$, and its diagonal is the real norm $\lvert A\rvert^{2}$. The realified $B$ is indefinite: it is positive on the real direction $1$ and negative on the imaginary direction $i$. The two realifications are the two scalar readings of one complex form, and the rules behind them — a symmetric bilinear form realifying to the split signature $(1,1)$ and a Hermitian form doubling its inertia to $(2,0)$ — are those of *The Realification and the Effect of the Change of Scalars*.

## The Euclidean Metric

**Definition.** The **Euclidean metric** of the complex space is the quadratic function

$$
d_{H}^{2}(A,C)=H(A-C,A-C)=\lvert A-C\rvert^{2}=(a-c)^{2}+(a'-c')^{2}.
$$

It is the diagonal of the definite form $H$ read on the difference $A-C$; the modulus $\lvert\cdot\rvert$ and its multiplicativity are *Complex Norm and Invertibility*.

**Proposition (positive definiteness).** The Euclidean metric is real, non-negative, and vanishes exactly when $A=C$. Its Gram matrix is $\mathrm{I}_{2}$ and its signature is $(2,0)$; the only null difference is the zero difference.

*Proof.* The expression $(a-c)^{2}+(a'-c')^{2}$ is a sum of two squares of reals, hence non-negative and zero only when both differences vanish, that is when $A=C$. The Gram matrix was computed in the previous section.

**Proposition (it is a genuine distance).** The function $d_{H}(A,C)=\lvert A-C\rvert$ is symmetric, vanishes exactly on the diagonal, and satisfies the triangle inequality. These are the properties of the modulus of *Complex Norm and Invertibility*, read on the difference.

The level sets are the circles: $d_{H}(A,C)=r$ is the circle of radius $r$ about $C$. The form is definite, so there is no null cone beyond the point $A=C$.

**The group of maps preserving the form.** The $\mathbb{C}$-linear maps preserving $H$ are the multiplications by the units of norm one, $A\mapsto uA$ with $\lvert u\rvert=1$; the identification of this group of multiplications with $\mathrm{SO}(2)$, together with the reading of the parameter, is *Rotations and Reflections in the Complex Plane*, below this article in this category. The full group of $\mathbb{R}$-linear maps preserving $H$ is the group $O(2)$, given by the matrix condition

$$
M^{\mathsf T}M=\mathrm{I}_{2}
$$

on the matrix of the map in the basis $1$, $i$. The maps of determinant $+1$ in it are exactly the multiplications $A\mapsto uA$ with $\lvert u\rvert=1$, and those of determinant $-1$ are exactly the reflections $A\mapsto u\bar A$ with $\lvert u\rvert=1$ (*Rotations and Reflections in the Complex Plane*, below this article in this category).

## The Split Metric

**Definition.** The **split metric** of the complex space is the quadratic function induced by the realified bilinear form $B$,

$$
d_{B}^{2}(A,C)=\operatorname{Re}B(A-C,A-C)=\operatorname{Re}\bigl((A-C)^{2}\bigr)=(a-c)^{2}-(a'-c')^{2}.
$$

It is the diagonal of the realified form read on the difference $A-C$.

**Proposition (indefiniteness).** The split metric is real and takes both signs. Its Gram matrix is $\operatorname{diag}(1,-1)$ and its signature is $(1,1)$; it is positive on the real direction and negative on the imaginary one. It is therefore not a distance.

*Proof.* The value is the diagonal of the matrix $\operatorname{diag}(1,-1)$, a difference of two squares; on $A=1$ it is $+1$ and on $A=i$ it is $-1$. Since it changes sign, it is neither positive nor negative definite, and it cannot satisfy the axioms of a distance.

**The null cone.** The split metric vanishes on the pairs whose separations satisfy $\lvert a-c\rvert=\lvert a'-c'\rvert$, that is

$$
d_{B}^{2}(A,C)=0 \iff a-c=\pm(a'-c').
$$

Through each point $C$ this is a pair of lines, of directions $1+i$ and $1-i$; the two directions are exchanged by conjugation, since $\overline{1+i}=1-i$. The null pair depends only on the difference, as does the metric itself.

**The level sets.** For a constant $\kappa\neq0$ the equation $d_{B}^{2}(A,C)=\kappa$ is a hyperbola; the two families $\kappa>0$ and $\kappa<0$ are exchanged by the multiplication by $i$, and neither meets the null pair. The split metric is thus read by its null pair of lines and its two families of hyperbolas, in contrast with the circles of the Euclidean metric.

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

**Proposition (the two quadratics differ only in the sign of the square).** For all $A,C$,

$$
d_{H}^{2}(A,C)-d_{B}^{2}(A,C)=2(a'-c')^{2}, \qquad d_{H}^{2}(A,C)+d_{B}^{2}(A,C)=2(a-c)^{2}.
$$

*Proof.* Add and subtract the two coordinate expressions $(a-c)^{2}\pm(a'-c')^{2}$.

So each metric recovers one of the two squared coordinates from the pair, and the two differ by a positive term: the Euclidean metric is the sum, the split metric the difference, of the two squared coordinate separations. In particular $d_{H}^{2}\geq d_{B}^{2}$ always, and the two agree exactly when the imaginary separations vanish.

**Proposition (the forms are exchanged by conjugation in a slot).** For all $A,C$,

$$
H(A,C)=B(A,\bar C), \qquad B(A,C)=H(A,\bar C).
$$

*Proof.* $B(A,\bar C)=A\bar C=H(A,C)$, and $H(A,\bar C)=A\overline{\bar C}=AC=B(A,C)$.

The two metrics are therefore the two readings of the two forms related by conjugation of the second argument.

**Proposition (multiplication by $i$ preserves one and reverses the other).** For the complex structure $J(A)=iA$,

$$
d_{H}^{2}(JA,JC)=d_{H}^{2}(A,C), \qquad d_{B}^{2}(JA,JC)=-d_{B}^{2}(A,C).
$$

*Proof.* In coordinates $J(a,a')=(-a',a)$; substituting gives $(a-c)^{2}+(a'-c')^{2}$ unchanged and $(a-c)^{2}-(a'-c')^{2}$ negated. Equivalently, the realified Hermitian form is preserved by $J$ and the realified bilinear form is reversed, as recorded in *The Realification of the Four Forms* for the general case.

So multiplication by $i$ preserves the Euclidean metric and reverses the split one. The complex structure is thus the operator that distinguishes the two metrics on the one space.

**Proposition (the elements common to the two groups).** The complex-linear maps preserving both realified forms are the two multiplications $\pm\mathrm{id}$. The full real-linear groups $O(2)$ and $O(1,1)$ meet in the four maps $\pm\mathrm{id}$ and $\pm\mathrm{conj}$, where $\mathrm{conj}(A)=\bar A$.

*Proof.* A $\mathbb{C}$-linear map is $A\mapsto uA$. It preserves $\operatorname{Re}H$ exactly when $\lvert u\rvert=1$, since $\operatorname{Re}H(uA,uC)=\lvert u\rvert^{2}\operatorname{Re}H(A,C)$. It preserves $\operatorname{Re}B$ exactly when $u^{2}=1$, since $\operatorname{Re}B(uA,uC)=\operatorname{Re}(u^{2}AC)$ and testing $A=C=1$ gives $\operatorname{Re}(u^{2})=1$ while testing $A=1$, $C=i$ gives $\operatorname{Im}(u^{2})=0$. Hence $u=\pm1$. For the full groups, a matrix that is orthogonal, $M^{\mathsf T}M=\mathrm{I}_{2}$, and preserves $\operatorname{diag}(1,-1)$ has orthogonal inverse and so commutes with $\operatorname{diag}(1,-1)$; since the two eigenvalues are distinct it preserves each eigenspace, hence is diagonal with entries $\pm1$. The four diagonal sign matrices are exactly $\pm\mathrm{id}$ and $\pm\mathrm{conj}$.

So the complex-linear coincidences are only the central pair, while the two real groups $O(2)$ and $O(1,1)$ share a Klein four group; neither group contains the other, and each enlarges the common pair in its own direction.

**Remark (the contrast with the biquaternion realification).** The same realification applied to the biquaternion algebra $\mathbb{B}$ gives the general plain bilinear form the split signature $(4,4)$ and the Hermitian form the definite signature $(8,0)$ (*The Realification of the Four Forms*). The pair $(1,1)$, $(2,0)$ of the complex space is the two-dimensional shadow of that pair, and the complex space carries a definite and an indefinite real form at once.

## Worked Example

For the worked pair of the category, $A=3+4i$ and $C=1-2i$, the difference is $A-C=2+6i$, so

$$
d_{H}^{2}(A,C)=2^{2}+6^{2}=40, \qquad d_{B}^{2}(A,C)=2^{2}-6^{2}=-32.
$$

The two identities of the comparison read $d_{H}^{2}-d_{B}^{2}=72=2\cdot6^{2}$ and $d_{H}^{2}+d_{B}^{2}=8=2\cdot2^{2}$. The Euclidean metric is positive on the separation $2+6i$, while the split metric is negative on it; the two metrics disagree on its sign because the second is indefinite.

For the null pair, a difference on the line of direction $1+i$ is $A=t(1+i)$, and indeed

$$
d_{B}^{2}(t(1+i),0)=t^{2}-t^{2}=0
$$

for every real $t$; the same holds on the line of direction $1-i$. On those differences the Euclidean metric is $d_{H}^{2}=2t^{2}$, so the null lines of the split metric are the directions on which the split value vanishes while the Euclidean value stays positive.

## Summary

The one complex plane carries two real quadratic functions, one from each of the two forms. The definite Hermitian form $H(A,C)=A\bar C$ gives the Euclidean metric $d_{H}^{2}(A,C)=(a-c)^{2}+(a'-c')^{2}$, of Gram matrix $\mathrm{I}_{2}$ and signature $(2,0)$, positive definite, whose level sets are the circles, whose group of form-preserving $\mathbb{R}$-linear maps is $O(2)$ and whose genuine distance is the modulus of the difference. The realified plain bilinear form $B(A,C)=AC$ gives the split metric $d_{B}^{2}(A,C)=(a-c)^{2}-(a'-c')^{2}$, of Gram matrix $\operatorname{diag}(1,-1)$ and signature $(1,1)$, indefinite, whose null set is the pair of lines $a-c=\pm(a'-c')$, whose nonzero level sets are the two families of hyperbolas, and whose group of form-preserving $\mathbb{R}$-linear maps is $O(1,1)$, whose subgroup fixing the two null lines rescales them.

The two metrics are the two readings of the two forms and satisfy $d_{H}^{2}-d_{B}^{2}=2(a'-c')^{2}$ and $d_{H}^{2}+d_{B}^{2}=2(a-c)^{2}$; the forms are exchanged by conjugation of the second slot, $H(A,C)=B(A,\bar C)$, and multiplication by $i$ preserves the Euclidean metric and reverses the split one. The pair $(1,1)$, $(2,0)$ is the two-dimensional shadow of the biquaternion pair $(4,4)$, $(8,0)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A=a+ia'$, $C=c+ic'$ | two elements of $\mathbb{C}$, with $a,a',c,c'\in\mathbb{R}$ |
| $\bar A=a-ia'$ | complex conjugation, the bar |
| $B(A,C)=AC$ | general plain bilinear form, $=N$; Gram matrix $[1]$ over $\mathbb{C}$ |
| $H(A,C)=A\bar C$ | Hermitian form, $=K$; Gram matrix $[1]$ over $\mathbb{C}$ |
| $\operatorname{Re}B(A,C)=ac-a'c'$ | the realified bilinear form; Gram matrix $\operatorname{diag}(1,-1)$; signature $(1,1)$ |
| $\operatorname{Re}H(A,C)=ac+a'c'$ | the realified Hermitian form; Gram matrix $\mathrm{I}_{2}$; signature $(2,0)$ |
| $d_{H}^{2}(A,C)=\lvert A-C\rvert^{2}$ | Euclidean metric; positive definite; level sets the circles |
| $d_{B}^{2}(A,C)=\operatorname{Re}\bigl((A-C)^{2}\bigr)$ | split metric; indefinite; level sets the hyperbolas |
| $a-c=\pm(a'-c')$ | the null pair of lines of the split metric |
| $M^{\mathsf T}M=\mathrm{I}_{2}$ | the condition for preserving $\operatorname{Re}H$; the group $O(2)$ |
| $M^{\mathsf T}\operatorname{diag}(1,-1)M=\operatorname{diag}(1,-1)$ | the condition for preserving $\operatorname{Re}B$; the group $O(1,1)$ |
| $J(A)=iA$ | the complex structure; preserves $d_{H}^{2}$, reverses $d_{B}^{2}$ |
| $(1,1),(2,0)$ | the two realified signatures, against $(4,4),(8,0)$ for $\mathbb{B}$ |

## Further Reading

- *The Two Forms and the Two Algebraic Norms of the Complex Space* (`articles_maths/the-two-forms-and-the-two-algebraic-norms-of-the-complex-space.md`), for the two forms and the two algebraic norms whose diagonals are their squares.
- *The Two Products of the Complex Space* (`articles_maths/the-two-products-of-the-complex-space.md`), for the two products $AC$ and $A\bar C$ whose forms are realified here.
- *The Realification and the Effect of the Change of Scalars* (`articles_maths/the-realification-and-the-effect-of-the-change-of-scalars-on-the-complex-numbers.md`), the complex article of that name, for the realification rules that give the signatures $(1,1)$ and $(2,0)$.
- *Complex Algebra* (`articles_maths/complex-algebra.md`), for the algebra, its basis and its one nontrivial involution.
- *The Realification of the Four Forms* (`articles_maths/the-realification-of-the-four-forms.md`), for the biquaternion signatures $(4,4)$ and $(8,0)$ of which the present pair is the two-dimensional shadow.
- *Complex Norm and Invertibility* (`articles_maths/complex-norm-and-invertibility.md`), for the modulus, its multiplicativity, its triangle inequality and the group of units.
- *Rotations and Reflections in the Complex Plane* (`articles_maths/rotations-and-reflections-in-the-complex-plane.md`), for the identification of the form-preserving multiplications with $\mathrm{SO}(2)$, the reflections and the group $O(2)$.
- *Complex Subspaces* (`articles_maths/complex-subspaces.md`), for the real and imaginary subspaces on which the split metric is definite of opposite signs.
- *Remarkable Subspaces of the Complex Numbers and the Two Forms* (`articles_maths/remarkable-subspaces-of-the-complex-numbers-and-the-two-forms.md`), for the restrictions of the two forms to the two subspaces.
- Werner Greub, *Linear Algebra*, 4th edition (Springer, 1981), for Gram matrices, inertia and the groups preserving a symmetric or Hermitian form.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd edition (Cambridge University Press, 2001), for the definite and indefinite forms of the plane and their groups.
