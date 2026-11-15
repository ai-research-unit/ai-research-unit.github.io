# __The Two Forms and the Two Algebraic Norms of the Split-Complex Space__

## Introduction

The split-complex space carries two forms and two algebraic norms, one for each of its two products. This article writes the two forms on the coordinates, gives their Gram matrices, computes their realified signatures, and reads the two algebraic norms as the diagonals of the forms. It closes on the reversal: over the complex field the definite form is the sesquilinear one and its isotropic set is a point, and here the definite form is the plain one and the isotropic set is a pair of lines.

The claim is a claim about which form is definite. **The plain form is definite and the Hermitian form is indefinite**, the opposite of the complex field. One sign, $j^2=+1$, does it: the reflection $J$ preserves the plain form and reverses the Hermitian one, so the realification rules exchange places.

The two forms are built in *The Two Products of the Split-Complex Space*, which owns the products and their laws; the cone the Hermitian form defines is *The Hermitian Form, the Double Cone and the Reversed Cauchy-Schwarz Inequality*; the criterion of invertibility the norm gives is *Norm and Invertibility in the General Split-Complex Algebra*; the realified signatures are read against *Hermitian Forms over Algebras and Norms*.

## The Two Forms

**Definition.** A form of the space is the scalar part of a product of the space, so the space carries the **plain form** $P(A,C)=AC$ and the **Hermitian form** $H(A,C)=A\bar C$, and no third.

**Proposition (there is no third form).** Any reading of the two slots other than these two is a conjugate of one of them.

*Proof.* The space carries the two products $AC$ and $A\bar C$ (*The Two Products of the Split-Complex Space*), so it carries at most their two scalar parts. The bar in the first slot gives $\bar AC=\overline{A\bar C}$, the conjugate value of $H(A,C)$, and a form and its conjugate are one object with two signs.

## The Plain Form

### Symmetry and Bilinearity

**Proposition.** $P$ is symmetric and $\mathbb{C}_{\mathrm{spl}}$-bilinear, $P(A,C)=P(C,A)$, and linear in each slot over $\mathbb{C}_{\mathrm{spl}}$.

**Proof.** $P$ is the multiplication of a commutative ring, so it is symmetric, and a multiplication is linear in each slot over the ring.

### The Gram Matrix

Over the free module of rank one with the basis $1$, the Gram matrix of $P$ is the $1\times1$ matrix $[P(1,1)]=[1]$. Its realification has the Gram matrix on the basis $1,j$

$$
\bigl[\operatorname{Re}P\bigr]=\begin{pmatrix}1&0\\0&1\end{pmatrix} ,
$$

since $\operatorname{Re}P(1,1)=1$, $\operatorname{Re}P(1,j)=0$ and $\operatorname{Re}P(j,j)=1$.

### Definiteness and the Signature

**Theorem.** $\operatorname{Re}P$ is positive definite of signature $(2,0)$: $\operatorname{Re}P(A,A)=a^2+b^2$, which vanishes only at $A=0$.

**Proof.** $\operatorname{Re}P(A,A)$ is the real part of $A^2=(a^2+b^2)+2ab\,j$, that is $a^2+b^2$, a sum of two squares. The Gram matrix is the identity, so the signature is $(2,0)$.

### The Positive Set Is the Whole Plane

A definite form has no isotropic vector, so the set of $A$ with $\operatorname{Re}P(A,A)\ge0$ is the whole plane, the boundary of the set being empty. That is what "the positive set is the whole plane" means: the positivity of $P$ excludes nothing.

The image of the diagonal of $P$ is a smaller set. The values $P(A,A)=A^2$ fill the forward cone $a^2\ge b^2$ and not the plane, because the squaring is not onto (*The Square Map of the Split-Complex Space*). The two statements are not in conflict: the **positive set** of a definite form is the plane, and the **image of its diagonal map** is the cone. The first is a property of the form, the second of the square.

## The Hermitian Form

### Conjugate-Symmetry and Sesquilinearity

**Proposition.** $H$ is conjugate-symmetric and sesquilinear: $H(A,C)=\overline{H(C,A)}$, linear in the first slot and conjugate-linear in the second.

**Proof.** $H(C,A)=C\bar A=\overline{\bar C A}=\overline{A\bar C}$ by commutativity, and $H(A,\lambda C)=A\bar\lambda\bar C=\bar\lambda H(A,C)$.

### The Gram Matrix

The Gram matrix of $H$ over the free module of rank one is again $[H(1,1)]=[1]$, and the two forms therefore have the same single entry. The realification on the basis $1,j$ is

$$
\left[\operatorname{Re}H\right]=\begin{pmatrix}1&0\\0&-1\end{pmatrix} ,
$$

since $\operatorname{Re}H(1,1)=1$, $\operatorname{Re}H(1,j)=0$ and $\operatorname{Re}H(j,j)=-1$.

### The Signature

**Theorem.** $\operatorname{Re}H$ is indefinite of signature $(1,1)$: $\operatorname{Re}H(A,A)=a^2-b^2$, positive on the real line, negative on the split imaginary line and zero on the pair of null lines.

**Proof.** $\operatorname{Re}H(A,A)$ is the real part of $A\bar A=a^2-b^2$, which is already real. The Gram matrix has the eigenvalues $1$ and $-1$, so the signature is $(1,1)$; the form changes sign, so it is indefinite.

### The Isotropic Set

**Theorem.** The isotropic set of $H$ is the pair of null lines,

$$
\{A : H(A,A)=0\}=\mathbb{R}\Pi_+\cup\mathbb{R}\Pi_- .
$$

**Proof.** $H(A,A)=a^2-b^2$ vanishes exactly when $a^2=b^2$, that is $a=\pm b$, which is the union of the two lines spanned by $1+j$ and $1-j$.

The isotropic set is a pair of lines and not a point, it is closed under multiplication, and it consists of the zero divisors with the origin adjoined (*Zero Divisors of the Split-Complex Algebra*). The form is not definite: it is positive on the real line, negative on the split imaginary line, and zero on the two idempotent lines.

## The Two Algebraic Norms

### The Plain Norm

The **plain algebraic norm** is $P$ read at one argument,

$$
P(A)=A^2=(a^2+b^2)+2ab\,j ,
$$

$\mathbb{C}_{\mathrm{spl}}$-valued, multiplicative, anisotropic: $P(A)=0$ forces $a=b=0$, since $A^2=0$ reads $A_+^2=A_-^2=0$.

It is not a real-valued object and it carries no order and no modulus. It is multiplicative in the strong sense, $P(AC)=P(A)P(C)$, because $(AC)^2=A^2C^2$ in a commutative ring.

### The Hermitian Norm

The **Hermitian algebraic norm** is $H$ read at one argument,

$$
H(A)=A\bar A=a^2-b^2 ,
$$

real, multiplicative, indefinite. Its value is the real part of the form and the whole of the form, since $H(A,A)$ is real.

**Theorem.** $H(AC)=H(A)H(C)$ and $H(A)\neq0$ is the criterion of invertibility of $A$; the units are the elements off the null lines.

**Proof.** $H(AC)=(AC)\overline{(AC)}=A\bar A\,C\bar C$ by commutativity, and $A^{-1}=\bar A/H(A)$ when $H(A)\neq0$; the criterion is *Norm and Invertibility in the General Split-Complex Algebra*.

### Polarisation

The two norms polarise to the two forms:

$$
P(A+C)-P(A)-P(C)=2P(A,C), \qquad H(A+C)-H(A)-H(C)=2\operatorname{Re}H(A,C) .
$$

The second is the split bilinear form $g(A,C)=ac-bd$ of signature $(1,1)$, the polar form of the indefinite norm. The first polarises into a $\mathbb{C}_{\mathrm{spl}}$-valued form, which is the plain form again.

## The Reversal of the Complex Case

### The Definite Form Is the Sesquilinear One There

Over $\mathbb{C}$ the sesquilinear form $A\bar C$ is positive definite, its diagonal $A\bar A=\lvert A\rvert^2$ is the square of the modulus, and the plain form $AC$ realifies with signature $(1,1)$: the form $\operatorname{Re}(AC)$ is $ac-bd$ on the real and imaginary coordinates. So over $\mathbb{C}$ the definite form is the sesquilinear one, and here the definite form is the plain one. The two forms exchange their realified signatures.

**The reason.** The reflection $J$, the multiplication by the generator, preserves one form and reverses the other, and the sign of the square of the generator decides which is which:

$$
P(JA,JC)=+P(A,C), \qquad H(JA,JC)=-H(A,C) \quad\text{here},
$$

and the two signs are exchanged over $\mathbb{C}$, where $i^2=-1$. The realification rules attach the signature $(n,n)$ to the preserved form and the doubling to the reversed one, so the exchange of the signs is the exchange of the signatures.

### The Isotropic Set Is a Point There

Over $\mathbb{C}$ the isotropic set of the Hermitian form is the origin, since $A\bar A=0$ forces $A=0$; over $\mathbb{C}_{\mathrm{spl}}$ it is a pair of lines. The isotropic set of the plain form is the origin in both cases, the plain form being anisotropic in both. So the reversal is exact and total:

| | over $\mathbb{C}$ | over $\mathbb{C}_{\mathrm{spl}}$ |
|---|---|---|
| the plain form $P$ | $(1,1)$, indefinite | $(2,0)$, definite |
| the Hermitian form $H$ | $(2,0)$, definite | $(1,1)$, indefinite |
| the isotropic set of $H$ | the origin | two lines |
| the isotropic set of $P$ | the origin | the origin |

### The Two Norms Compared

Over $\mathbb{C}$ the norm $A\bar A$ is definite and gives the modulus, and the plain norm $A^2$ is complex-valued and fixes no order; here $H(A)=a^2-b^2$ is real and indefinite, and $P(A)=A^2$ is $\mathbb{C}_{\mathrm{spl}}$-valued. The arities agree and the characters are exchanged: over $\mathbb{C}$ the real norm is the definite one and it gives the modulus, while here the real norm is $H$ and it is indefinite, and no multiple of it is definite. That impossibility is *The Hermitian Form, the Double Cone and the Reversed Cauchy-Schwarz Inequality*, and it is the reason the ring has no modulus.

## Summary

The space carries two forms, the plain $P(A,C)=AC$ and the Hermitian $H(A,C)=A\bar C$, one for each product and no third. Both have the Gram matrix $[1]$ over the free module of rank one and are separated by symmetry, $P$ being symmetric and $H$ conjugate-symmetric.

$P$ realifies with signature $(2,0)$ and is positive definite, so its positive set is the whole plane; the image of its diagonal is the forward cone, because the square map is not onto. $H$ realifies with signature $(1,1)$ and is indefinite, with isotropic set the pair of null lines $\mathbb{R}\Pi_+\cup\mathbb{R}\Pi_-$, which is the set of zero divisors with the origin adjoined.

The two algebraic norms are $P(A)=A^2$, $\mathbb{C}_{\mathrm{spl}}$-valued and anisotropic, and $H(A)=A\bar A=a^2-b^2$, real and indefinite, and both are multiplicative. Over the complex field the two forms exchange their signatures and $H$ has the origin alone for its isotropic set; the reversal is caused by the sign of the square of the generator, which makes $J$ preserve $P$ and reverse $H$ here and the other way round over $\mathbb{C}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P(A,C)=AC$ | The plain form, symmetric, definite of signature $(2,0)$ |
| $H(A,C)=A\bar C$ | The Hermitian form, conjugate-symmetric, indefinite of signature $(1,1)$ |
| $P(A)=A^2$ | The plain algebraic norm, $\mathbb{C}_{\mathrm{spl}}$-valued, anisotropic |
| $H(A)=A\bar A=a^2-b^2$ | The Hermitian algebraic norm, real, indefinite |
| $\operatorname{Re}P$, $\operatorname{Re}H$ | The realifications, with Gram matrices $\mathrm{diag}(1,1)$ and $\mathrm{diag}(1,-1)$ |
| $g(A,C)=ac-bd$ | The polar form of $N$, of signature $(1,1)$ |
| $\mathbb{R}\Pi_+\cup\mathbb{R}\Pi_-$ | The isotropic set of $H$ |
| $J$ | The multiplication by $j$, preserving $P$ and reversing $H$ |

## Further Reading

- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for symmetric bilinear forms, signature and inertia in dimension two.
- János Bognár, *Indefinite Inner Product Spaces* (Springer, Ergebnisse der Mathematik 78, 1974), for indefinite forms, isotropic subspaces and the Krein form.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, Colloquium Publications 44, 1998), for forms over an algebra with an involution and the realification rules.
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for the trace and norm forms of an associative algebra and their polarization.
- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the two forms of the split plane and the two isotropic lines.
