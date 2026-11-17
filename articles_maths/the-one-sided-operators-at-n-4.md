# __The One-Sided Operators at $n=4$__

## Introduction

**The left multiplications $L_a$ and the right multiplications $R_a$ of the biquaternion algebra act on the four-dimensional coefficient space, each family is four-dimensional, the two commute, meet in the scalars and span dimension seven, the four matrices of each family are signed permutations of determinant one forming a quaternion group with their negatives, and the two families are stitched by $R^{\mathrm{axf}}=D(L^{\mathrm{axf}})^{\mathsf T}D$ with $D=\operatorname{diag}(1,-1,-1,-1)$.**

The article writes the two families as explicit $4\times4$ matrices, proves the two multiplication laws with their opposite orders, proves faithfulness, proves the stitch in which the transpose is the quaternion conjugation, identifies the eight signed permutations as $Q_8\subset SO(4)$, and reads the two families as the two Kronecker factors of the ambient endomorphism algebra.

It assumes *The Axis-Free Representation of $M_4(\mathbb{C})$* and *$M_4(\mathbb{C})$ Axis-Free Representation: Operators*. The model at order two is *The One-Sided Operators at $n=2$*; the two-sided construction is *The Two-Sided Operators and the Segre Cone at $n=4$*.

## The Two Families

**Definition.** For $a\in\mathbb{B}$ let $L_a$ be the operator $X\mapsto aX$ and $R_a$ the operator $X\mapsto Xa$ on $\mathbb{B}$, and write $\mathbb{B}_L=\{L_a\}$, $\mathbb{B}_R=\{R_a\}$.

**Proposition.** Each family is a complex vector space of dimension $4$, the maps $a\mapsto L_a$ and $a\mapsto R_a$ are linear and injective, and
$$
L_{ab}=L_aL_b,\qquad R_{ab}=R_bR_a.
$$

**Proof.** Linearity in $a$; injectivity because $L_a(e_t)=a$; and composing gives $L_aL_b(X)=abX=L_{ab}(X)$, while $R_aR_b(X)=Xba=R_{ba}(X)$.

**Corollary.** $\mathbb{B}_L$ is a subalgebra isomorphic to $\mathbb{B}$, and $\mathbb{B}_R$ is a subalgebra isomorphic to the opposite algebra $\mathbb{B}^{\mathrm{opp}}$.

**Proof.** The two multiplication laws, one direct and one reversed.

**Corollary.** $L_aR_b=R_bL_a$ for all $a,b$, so the two families commute.

**Proof.** $aXb=Xba$ as a product of three factors.

**The intersection and the sum.** $\mathbb{B}_L\cap\mathbb{B}_R=\mathbb{C}\mathrm I_4$ and $\dim(\mathbb{B}_L+\mathbb{B}_R)=7$.

**Proof.** $L_a=R_b$ forces $a=b$ by evaluation at $e_t$, and then $aX=Xa$ for all $X$, which forces $a$ to be a scalar; the dimension follows from $4+4-1$.

## The Matrices in the Axis-Free Frame

**Theorem.** In the coefficient basis $\mathcal{E}=(e_t,\vec e_x,\vec e_y,\vec e_z)$ each $L_a$ and each $R_a$ for an invertible element $a$ is a signed permutation matrix of determinant one, hence an orthogonal matrix in $SO(4)$.

**Proof.** Multiplication by an invertible element permutes the four basis elements up to signs, since the units form a group with $\vec e_k^{2}=-e_t$; a signed permutation has determinant $\pm1$, and the computation gives $+1$ for the four generators.

**Corollary.** The four left matrices and the four right matrices are eight of the sixteen two-sided matrices $T_{\mu\nu}$, and each is a signed permutation.

**Proof.** $T_{\mu t}=L_\mu$ and $T_{t\nu}=R_\nu$.

**Corollary.** The left matrices act on the coefficient vector by a signed permutation of the four coordinates, and the right matrices likewise, so both families lie in the group of signed permutations of the basis.

**Proof.** The matrix of the operator in the basis it permutes.

**The transposes.** The transpose of $L_a$ is $L_{a^{\natural}}$ and the transpose of $R_a$ is $R_{a^{\natural}}$, where $^{\natural}$ is the quaternion conjugation.

**Proof.** The transpose is the adjoint for the coefficient pairing $\sum q_\mu^2$, and conjugation reverses the order of a product; the explicit matrices confirm it entry by entry.

## The Stitch

**Theorem.** With $D=\operatorname{diag}(1,-1,-1,-1)$ in the coefficient basis,
$$
R^{\mathrm{axf}}=D\,(L^{\mathrm{axf}})^{\mathsf T}D .
$$

**Proof.** Both sides are signed permutations and the identity is checked on the four generators: the matrix of $L_a$ and the matrix of $R_a$ differ by the change of sign of the three spatial coordinates, which is the conjugation of the algebra.

**Corollary.** The two families are the same family read through $D$, so the left and the right structure are the two conjugates of one another under the coefficient form.

**Proof.** The stitch, read as $D L^{\mathsf T}D=R$.

**Corollary.** The transpose in the axis-free frame is the quaternion conjugation, so the plain adjoint of the algebra is the transpose of the matrix, as stated in the axis-free representation.

**Proof.** The transpose of $L_a$ is $L_{a^{\natural}}$, and $^{\natural}$ is the conjugation.

**The consequence for the two halves.** A two-sided operator is symmetric as a matrix exactly when the index pattern is symmetric, and this is why the trace pairing has the inertia $(10,6)$.

**Proof.** The sixteen $T_{\mu\nu}$ satisfy $T_{\mu\nu}^{\mathsf T}=\pm T_{\mu\nu}$ according to the symmetry of the pair, and the trace of the square is $+4$ or $-4$.

## The Group of the Four

**Theorem.** The eight matrices $\pm L_\mu$ and the eight $\pm R_\mu$ each form a group isomorphic to $Q_8$, of order $8$, contained in $SO(4)$.

**Proof.** The four units $e_t,\vec e_x,\vec e_y,\vec e_z$ and their negatives form the quaternion group, since $\vec e_k^{2}=-e_t$ and $\vec e_x\vec e_y=\vec e_z$; the left multiplication is an injective homomorphism, so the image is a copy of $Q_8$; each matrix has determinant one, and negation of a $4\times4$ matrix preserves the determinant.

**Corollary.** The two copies of $Q_8$ commute, meet in $\pm\mathrm I_4$, and their product is the group of order $32$ of the signed permutations.

**Proof.** The two families commute, the intersection of the two copies is $\pm\mathrm I_4$ since the only common elements are the scalars, and the product has $8\cdot8/2=32$ elements.

**Corollary.** The group of order $32$ is the central product $Q_8\circ Q_8$, and it is the finite shadow of $\mathrm{Spin}(4)=SU(2)\times SU(2)$.

**Proof.** The identification of the two factors and the covering of the rotor article.

**The orbit structure.** $Q_8$ acts on the coefficient space with the origin as the only fixed point and with orbits of eight elements off the origin, since $\pm L_\mu$ are distinct for distinct pairs.

**Proof.** A nonzero vector $v$ satisfies $av=v$ only for $a=e_t$; otherwise $av$ is another basis direction or its negative.

## The Multiplicative Laws and Faithfulness

**Proposition.** The map $a\mapsto L_a$ is an injective algebra homomorphism and $a\mapsto R_a$ is an injective anti-homomorphism; the images have dimension four and are closed under multiplication up to the reversed order.

**Proof.** The laws $L_{ab}=L_aL_b$ and $R_{ab}=R_bR_a$, and injectivity by evaluation at $e_t$.

**Corollary.** $L$ and $R$ are faithful representations of the algebra and of its opposite, and the kernel of each is zero.

**Proof.** Injectivity is faithfulness.

**Corollary.** The commutant of $\mathbb{B}_L$ inside $\operatorname{End}(\mathbb{B})$ is $\mathbb{B}_R$, and conversely.

**Proof.** A map commuting with all left multiplications is a right multiplication.

**The two-sided reading.** The product $L_aR_b$ is the operator $X\mapsto aXb$, which is the two-sided operator $T_{a,b}$; the sixteen $T_{\mu\nu}$ on the units are a basis of $M_4(\mathbb{C})$.

**Proof.** The definition and the basis theorem of the two-sided article.

## The Two Kronecker Factors

**Theorem.** In the Kronecker reading $M_4(\mathbb{C})\cong M_2(\mathbb{C})\otimes M_2(\mathbb{C})$ the family $\mathbb{B}_L$ is the first factor $M_2\otimes\mathrm I_2$ and the family $\mathbb{B}_R$ is the second factor $\mathrm I_2\otimes M_2$.

**Proof.** With $\mathbb{B}\cong M_2(\mathbb{C})$ acting on its two-dimensional module, the left multiplication is the first factor acting on the module index and the right multiplication the second, which is the content of the two displays $L(\tilde Q)=\mathrm I_2\otimes\mathsf M_2(\tilde Q)$ and $R(\tilde Q)=\mathsf M_2(\tilde Q)^{\mathsf T}\otimes\mathrm I_2$.

**Corollary.** The two families are subalgebras and not ideals, and their span has dimension seven while the algebra has dimension sixteen.

**Proof.** The two factors meet in the scalars, and a proper subalgebra of a simple algebra is not an ideal.

**Corollary.** The transposition in the second display is the reason the two families are stitched by $D$ and not by the identity: the right factor is the transpose of the matrix of the element.

**Proof.** The second display carries the transpose, and the transpose of the matrix of $a$ is the conjugation in the axis-free frame.

**The real slice.** Over $\mathbb{R}$ the same two families are real, the four matrices are real signed permutations, and the coefficients of an element are the four real coordinates.

**Proof.** The multiplication table has real structure constants and the coefficient basis is real.

## Summary

The left multiplications and the right multiplications of the biquaternion algebra give two four-dimensional families of operators on the coefficient space; they commute, meet in the scalars and span dimension seven. The left family is a copy of the algebra and the right family a copy of the opposite algebra, with the two multiplication laws in the two orders.

In the axis-free frame each family consists of signed permutations of determinant one, so both lie in $SO(4)$; the four units give a copy of $Q_8$, and the two copies commute and generate the group of order $32$. The two families are stitched by $D(L^{\mathrm{axf}})^{\mathsf T}D$, which is the statement that the transpose is the quaternion conjugation.

The two families are the two Kronecker factors of the ambient matrix algebra, subalgebras meeting in the scalars. The one-sided operators are the raw material; the two-sided operators are their products.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_a(X)=aX$ | the left multiplication |
| $R_a(X)=Xa$ | the right multiplication |
| $\mathbb{B}_L,\mathbb{B}_R$ | the two families, dimension $4$ each |
| $D=\operatorname{diag}(1,-1,-1,-1)$ | the stitch matrix |
| $Q_8$ | the quaternion group of the eight signed permutations |
| $L(\tilde Q)=\mathrm I_2\otimes\mathsf M_2(\tilde Q)$ | the left factor in the Kronecker reading |

## Further Reading

- [The Axis-Free Representation of $M_4(\mathbb{C})$](m4c-axis-free-representation.html), for the coefficient basis and the two families.
- [$M_4(\mathbb{C})$ Axis-Free Representation: Operators](m4c-axis-free-representation-operators.html), for the sixteen two-sided matrices and the trace pairing.
- [The Two-Sided Operators and the Segre Cone at $n=4$](the-two-sided-operators-and-the-segre-cone-at-n-4.html), for the products of the two families.
- [$\operatorname{End}(M_4(\mathbb{C}))$ as an Algebra: the Regular Representation](end-m4c-as-an-algebra-the-regular-representation.html), for the double centraliser.
- [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html), for the case at order two.
