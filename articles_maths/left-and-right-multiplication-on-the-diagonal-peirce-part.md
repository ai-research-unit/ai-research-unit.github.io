# __Left and Right Multiplication on the Diagonal Peirce Part__

## Introduction

Left and right multiplication by an element $a$ are the operators $L_a(x)=ax$ and $R_a(x)=xa$. They commute, and their product is the sandwich $T_{a,b}$:

$$
L_aR_b=R_bL_a=T_{a,b}.
$$

An idempotent $e$ gives the two operators $L_e$ and $R_e$, and the Peirce decomposition of $A$ is the joint eigenspace decomposition of this commuting pair. The **diagonal Peirce part** is

$$
D=A_{00}\oplus A_{11}=eAe\oplus fAf, \qquad f=1-e,
$$

and it is exactly the centraliser of $e$: the elements on which $L_e$ and $R_e$ agree. The **off-diagonal part** is $N=A_{01}\oplus A_{10}$, and the commutator $L_e-R_e=\operatorname{ad}_e$ vanishes on $D$, acts as $+1$ on $A_{01}$ and as $-1$ on $A_{10}$, and satisfies

$$
\boxed{\;(L_e-R_e)^2=P_N,\qquad P_D=I-L_e-R_e+2L_eR_e\;},
$$

where $P_D$ and $P_N$ are the projections onto $D$ and $N$. The article proves these identities, computes the restrictions of $L_d$ and $R_d$ to the diagonal part for $d\in D$, and reads the diagonal part as the algebra $eAe\times fAf$ acting on itself by left and right multiplication.

The article is the diagonal companion of *Left and Right Multiplication*, *The Commutator Operator* and *The Sandwich Operators on the Peirce Components*. The Peirce decomposition is that of *Unital Algebras*, §*Idempotents and the Peirce Decomposition*; the centraliser theorem is *The Centraliser and the Diagonal Peirce Part*; the off-diagonal part is *Off-Diagonal Peirce Components and Noncentral Idempotents*; the derivations are *Derivations and the Peirce Decomposition*; and the two-sided multiplication is *The Sandwich Operator on an Algebra*. No form, involution or topology is used.

Throughout, $k$ is a field and $A$ is a unital associative $k$-algebra with $1\neq0$, not assumed commutative and not assumed finite-dimensional unless a statement says so. The idempotent is $e$, its complement is $f=1-e$, and the corners are $A_{ij}=e_iAe_j$ with $e_0=e$, $e_1=f$. The Peirce decomposition is $A=A_{00}\oplus A_{01}\oplus A_{10}\oplus A_{11}$, with the multiplication table $A_{ij}A_{kl}\subseteq\delta_{jk}A_{il}$. The diagonal part is $D=A_{00}\oplus A_{11}$ and the off-diagonal part is $N=A_{01}\oplus A_{10}$; the projections onto them are $P_D$ and $P_N$.

## Left and Right Multiplication

### Definitions and elementary identities

**Definition.** For $a\in A$, the **left multiplication** $L_a$ and the **right multiplication** $R_a$ are the $k$-linear operators

$$
L_a:A\to A,\quad x\mapsto ax, \qquad R_a:A\to A,\quad x\mapsto xa.
$$

They are the regular representations of $A$ on itself.

**Proposition.** For all $a,b\in A$:

**(a)** $L_{a+b}=L_a+L_b$ and $R_{a+b}=R_a+R_b$;

**(b)** $L_{ab}=L_aL_b$ and $R_{ab}=R_bR_a$;

**(c)** $L_aR_b=R_bL_a=T_{a,b}$;

**(d)** $L_1=R_1=\mathrm{id}_A$;

**(e)** $L_a=0$ exactly when $a=0$, and $R_a=0$ exactly when $a=0$.

*Proof.* (a), (b) and (c) are associativity: $L_{ab}(x)=(ab)x=a(bx)=L_aL_b(x)$, $R_{ab}(x)=x(ab)=(xa)b=R_bR_a(x)$, and $L_aR_b(x)=a(xb)=(ax)b=R_bL_a(x)$. (d) is the unit. (e) $L_a=0$ gives $a=L_a(1)=0$, and $R_a=0$ gives $a=R_a(1)=0$.

**Remark.** The left regular representation $a\mapsto L_a$ is an algebra homomorphism $A\to\operatorname{End}_k(A)$, and the right regular representation $a\mapsto R_a$ is an algebra anti-homomorphism. The two representations commute, and their product is the sandwich representation of the enveloping algebra $A\otimes A^{\mathrm{op}}$. The identities are those of *Left and Right Multiplication*; the article uses them without further proof.

### The operators of an idempotent

**Proposition.** Let $e$ be an idempotent and $f=1-e$.

**(a)** $L_e$ and $R_e$ are idempotent operators: $L_e^2=L_e$, $R_e^2=R_e$.

**(b)** $L_e$ and $R_e$ commute, and $L_eR_e=R_eL_e=P_e=T_{e,e}$.

**(c)** $L_e+L_f=\mathrm{id}_A$ and $R_e+R_f=\mathrm{id}_A$.

**(d)** The images and kernels are

$$
\boxed{\;\operatorname{im}L_e=eA, \quad \ker L_e=fA, \quad
\operatorname{im}R_e=Ae, \quad \ker R_e=Af\;}.
$$

**(e)** The image of $P_e=L_eR_e$ is the corner $eAe$, and its kernel is $eAf\oplus fAe\oplus fAf$.

*Proof.* (a) $L_e^2=L_{e^2}=L_e$ and $R_e^2=R_{e^2}=R_e$. (b) $L_eR_e=T_{e,e}=R_eL_e$. (c) $L_e+L_f=L_{e+f}=L_1=\mathrm{id}$, and similarly for $R$. (d) $\operatorname{im}L_e=\{ex:x\in A\}=eA$, and the Peirce decomposition gives $\ker L_e=\{x:ex=0\}=fA$; the right-hand statements are $\operatorname{im}R_e=Ae$ and $\ker R_e=Af$. (e) $P_e(x)=exe$ lies in $eAe$, and $P_e$ fixes $eAe$; its kernel is the sum of the other three corners.

**Remark (the two projections).** $L_e$ is the projection onto the right ideal $eA$ along $fA$, and $R_e$ is the projection onto the left ideal $Ae$ along $Af$. They are not the Peirce projections: the Peirce corner $A_{00}=eAe$ is the intersection of their images, and the Peirce projection onto it is $P_e=L_eR_e$, not $L_e$ or $R_e$. The four Peirce projections are the elementary sandwiches $E_{ij}=T_{e_i,e_j}$ of *The Sandwich Operators on the Peirce Components*.

### The joint eigenspaces

Because $L_e$ and $R_e$ commute and are idempotent, they are simultaneously diagonalisable, with eigenvalues in $\{0,1\}$. The joint eigenspaces are the four Peirce corners:

| Corner | $L_e$ | $R_e$ | $L_e-R_e$ | $L_e+R_e$ |
|---|---|---|---|---|
| $A_{00}=eAe$ | $1$ | $1$ | $0$ | $2$ |
| $A_{01}=eAf$ | $1$ | $0$ | $1$ | $1$ |
| $A_{10}=fAe$ | $0$ | $1$ | $-1$ | $1$ |
| $A_{11}=fAf$ | $0$ | $0$ | $0$ | $0$ |

*Proof.* For $x\in A_{ij}$, $L_e(x)=e x$ is nonzero only when $i=0$, and then equals $x$; $R_e(x)=x e$ is nonzero only when $j=0$, and then equals $x$. The table follows.

**Corollary.** The pair $(L_e,R_e)$ determines the Peirce decomposition: the corner $A_{ij}$ is the joint eigenspace with eigenvalues $(1-i,1-j)$, where $i,j\in\{0,1\}$. The diagonal part $D$ is the sum of the joint eigenspaces with pairs $(1,1)$ and $(0,0)$, and the off-diagonal part $N$ is the sum of the joint eigenspaces with pairs $(1,0)$ and $(0,1)$.

**Remark.** The table is the operator form of the Peirce decomposition. The diagonal corners are the two extremes $(1,1)$ and $(0,0)$, and the mixed corners are the two mixed pairs. The operator $L_e-R_e$ separates the diagonal from the off-diagonal, and the operator $L_e+R_e$ separates the two diagonal corners from each other only through the value $2$ versus $0$; in characteristic two the value $2$ is zero, and $L_e+R_e$ no longer distinguishes $A_{00}$ from $A_{11}$. The corner projections $P_e=L_eR_e$ and $P_f=L_fR_f$ distinguish them in every characteristic.

## The Diagonal Peirce Part

### Definition and the commutator identity

**Definition.** The **diagonal Peirce part** is $D=A_{00}\oplus A_{11}$, and the **off-diagonal part** is $N=A_{01}\oplus A_{10}$. The projections onto them are $P_D$ and $P_N=I-P_D$.

The diagonal part is the set of elements whose Peirce decomposition has no mixed component, and the off-diagonal part is the set of elements whose decomposition has only mixed components.

**Theorem.** The following hold.

**(a)** $D=\ker(L_e-R_e)=\ker(\operatorname{ad}_e)$, where $\operatorname{ad}_e=L_e-R_e$ is the commutator with $e$.

**(b)** $N=\operatorname{im}(\operatorname{ad}_e)$, and $\operatorname{ad}_e$ acts as $+1$ on $A_{01}$ and as $-1$ on $A_{10}$.

**(c)** $\operatorname{ad}_e^2=P_N$, and $P_D=I-L_e-R_e+2L_eR_e$.

**(d)** $D$ is a subalgebra with identity $1$, isomorphic to $A_{00}\times A_{11}$; $N$ is a $D$-bimodule, and $N^2\subseteq D$. Hence $A=D\oplus N$ is a $\mathbb{Z}/2$-graded algebra with even part $D$ and odd part $N$.

*Proof.* (a) For $a=\sum a_{ij}$, $e a=a_{00}+a_{01}$ and $a e=a_{00}+a_{10}$, so $(L_e-R_e)(a)=a_{01}-a_{10}$. This vanishes exactly when $a_{01}=a_{10}=0$, that is, when $a\in D$. (b) The same computation shows that the image is $N$, with $+1$ on $A_{01}$ and $-1$ on $A_{10}$. (c) On $D$, $\operatorname{ad}_e=0$; on $N$, $\operatorname{ad}_e^2=1$. Hence $\operatorname{ad}_e^2=P_N$. The formula for $P_D$ follows from $P_D=I-P_N$ and $P_N=(L_e-R_e)^2=L_e+R_e-2L_eR_e$, using $L_e^2=L_e$, $R_e^2=R_e$ and $L_eR_e=R_eL_e$. (d) $D$ is closed under multiplication because $A_{00}^2\subseteq A_{00}$, $A_{11}^2\subseteq A_{11}$ and the cross products $A_{00}A_{11}$, $A_{11}A_{00}$ vanish; it contains $1=e+f$. The map $D\to A_{00}\times A_{11}$, $d\mapsto(e d e,f d f)$, is an algebra isomorphism with inverse $(x,y)\mapsto x+y$. The bimodule and grading statements follow from the multiplication table: $D N\subseteq N$, $N D\subseteq N$, $N^2\subseteq D$.

**Corollary (the centraliser).** $D=C_A(e)$.

*Proof.* $a\in C_A(e)$ exactly when $ea=ae$, that is, when $\operatorname{ad}_e(a)=0$; by (a) this is $D$. The computation is the centraliser theorem of *The Centraliser and the Diagonal Peirce Part*.

**Remark (the meaning of the identities).** The commutator $\operatorname{ad}_e$ is a partial involution: it is zero on the diagonal part and squares to the identity on the off-diagonal part. The operator $P_N=(L_e-R_e)^2$ is the projection onto $N$, and $P_D=I-P_N$ is the projection onto the diagonal. The diagonal part is the kernel of the commutator, and the off-diagonal part is its image; the decomposition $A=D\oplus N$ is the eigenspace decomposition of $\operatorname{ad}_e$ with eigenvalues $0,\pm1$, with the two off-diagonal corners carrying the two signs. The identities are characteristic-free; in characteristic two the signs $+1$ and $-1$ coincide, and $\operatorname{ad}_e$ is the projection onto $N$.

### The diagonal operators

**Proposition.** Let $d=d_0+d_1\in D$ with $d_0\in A_{00}$, $d_1\in A_{11}$.

**(a)** $L_d$ and $R_d$ preserve each Peirce corner.

**(b)** Relative to the ordered corners $(A_{00},A_{01},A_{10},A_{11})$, the block matrices are

$$
\boxed{\;L_d=\operatorname{diag}(L_{d_0},L_{d_0},L_{d_1},L_{d_1}), \qquad
R_d=\operatorname{diag}(R_{d_0},R_{d_1},R_{d_0},R_{d_1})\;},
$$

where each entry is the left or right multiplication of the corresponding corner algebra.

**(c)** $L_d$ and $R_d$ preserve $D$ and $N$, and their restrictions to $D$ are the left and right regular representations of $D$; in particular the maps $d\mapsto L_d|_D$ and $d\mapsto R_d|_D$ are faithful.

**(d)** For $d,d'\in D$, the sandwich $T_{d,d'}$ preserves each corner and acts on $A_{ij}$ by the sandwich of the corner elements $d_i$ and $d'_j$.

*Proof.* (a) For $x\in A_{ij}$, $d x=(d_0+d_1)x$; the term $d_0x$ is nonzero only when $i=0$, and $d_1x$ only when $i=1$, so $dx\in A_{ij}$. The same for $xd$. (b) On $A_{00}$ and $A_{01}$, the left factor is $d_0$; on $A_{10}$ and $A_{11}$, it is $d_1$. On $A_{00}$ and $A_{10}$, the right factor is $d_0$; on $A_{01}$ and $A_{11}$, it is $d_1$. (c) The preservation is (a); the restrictions are the regular representations because $D$ is a subalgebra with the same multiplication. Faithfulness follows from $L_d(1)=d$ and $R_d(1)=d$. (d) is the corner computation $d_i x d'_j$ for $x\in A_{ij}$.

**Remark (the asymmetry).** The left multiplication $L_d$ uses $d_0$ on the left of the two corners with first index $0$, and $d_1$ on the left of the two corners with first index $1$; the right multiplication $R_d$ uses $d_0$ on the right of the two corners with second index $0$, and $d_1$ on the right of the two corners with second index $1$. The two block matrices are not the same, and they differ exactly on the mixed corners: on $A_{01}$, $L_d$ uses $d_0$ and $R_d$ uses $d_1$; on $A_{10}$, $L_d$ uses $d_1$ and $R_d$ uses $d_0$. The diagonal corners see the same factor on both sides.

### The compression of a general multiplication

For a general $a\in A$, the left multiplication does not preserve the corners, but its compression to $D$ has a clean form.

**Proposition.** Let $a=\sum a_{ij}\in A$, and let $P_D$ be the projection onto $D$ along $N$.

**(a)** $P_D L_a|_D=L_{a_{00}}\oplus L_{a_{11}}$ and $P_D R_a|_D=R_{a_{00}}\oplus R_{a_{11}}$.

**(b)** $P_N L_a|_D$ sends $A_{00}$ to $A_{10}$ by $x\mapsto a_{10}x$ and $A_{11}$ to $A_{01}$ by $x\mapsto a_{01}x$; $P_N R_a|_D$ sends $A_{00}$ to $A_{01}$ by $x\mapsto x a_{01}$ and $A_{11}$ to $A_{10}$ by $x\mapsto x a_{10}$.

*Proof.* For $x=x_0+x_1\in D$, $a x=a_{00}x_0+a_{01}x_1+a_{10}x_0+a_{11}x_1$. The first and last terms lie in $D$, and the middle two in $N$; the components are as stated. The right-hand computation is the same with $x a$.

**Corollary.** The diagonal compression of $L_a$ depends only on the diagonal part $a_{00}+a_{11}$ of $a$; the off-diagonal part of $a$ acts on $D$ only through the mixed compressions, and it maps $D$ to $N$.

**Remark.** The proposition is the operator form of the Peirce multiplication table. The diagonal part of $a$ acts on the diagonal part of $A$ by left multiplication, the off-diagonal part of $a$ maps the diagonal part to the off-diagonal part, and the mixed corners carry the two directions. The formula is the first block column of the full block matrix of $L_a$ relative to $A=D\oplus N$; the other columns are the same computation on $N$.

## Examples

### The matrix algebra $M_2(k)$

Let $e=E_{11}$, $f=E_{22}$, and use the corner-adapted basis $(E_{11},E_{12},E_{21},E_{22})$. The operators are diagonal in this basis:

$$
L_e=\operatorname{diag}(1,1,0,0), \qquad
R_e=\operatorname{diag}(1,0,1,0), \qquad
P_e=L_eR_e=\operatorname{diag}(1,0,0,0),
$$

$$
\operatorname{ad}_e=L_e-R_e=\operatorname{diag}(0,1,-1,0), \qquad
\operatorname{ad}_e^2=\operatorname{diag}(0,1,1,0)=P_N.
$$

The diagonal part is $D=kE_{11}\oplus kE_{22}$, the algebra of diagonal matrices; the off-diagonal part is $N=kE_{12}\oplus kE_{21}$. The centraliser of $e$ is $D$, and $\operatorname{ad}_e$ is the commutator with $e$. For $d=\operatorname{diag}(d_0,d_1)$, the diagonal operators are

$$
L_d=\operatorname{diag}(d_0,d_0,d_1,d_1), \qquad
R_d=\operatorname{diag}(d_0,d_1,d_0,d_1).
$$

The example is the model of the whole article: the two diagonal entries of $d$ act on the two rows and the two columns of the matrix, and the mixed corners see the row factor on the left and the column factor on the right.

### The split algebra $k\times k$

Let $A=k\times k$ and $e=(1,0)$, $f=(0,1)$. The mixed corners vanish, so $N=0$ and $D=A$. The operators are

$$
L_e=R_e=P_e=\operatorname{diag}(1,0)
$$

on the two coordinates, and $\operatorname{ad}_e=0$. The idempotent is central, the diagonal part is the whole algebra, and the Peirce decomposition is the product decomposition $A=A_{00}\times A_{11}$. The example is the extreme in which $L_e=R_e$ and the commutator vanishes identically.

### The upper triangular algebra

Let $A=T_2(k)$ and $e=E_{11}$. The corners are

$$
A_{00}=kE_{11}, \qquad A_{01}=kE_{12}, \qquad A_{10}=0, \qquad A_{11}=kE_{22}.
$$

The diagonal part is $D=kE_{11}\oplus kE_{22}$, the diagonal matrices; the off-diagonal part is $N=kE_{12}$. The commutator is

$$
\operatorname{ad}_e(E_{11})=0, \qquad \operatorname{ad}_e(E_{12})=E_{12}, \qquad \operatorname{ad}_e(E_{22})=0,
$$

so $\operatorname{ad}_e$ is the projection onto $N$, and $\operatorname{ad}_e^2=\operatorname{ad}_e=P_N$ on this algebra. The example is the degenerate case in which one mixed corner vanishes and the commutator has only the eigenvalue $+1$ on the off-diagonal part. The diagonal operators $L_d$ and $R_d$ preserve the three nonzero corners by the block formula of §*The diagonal operators*.

### The biquaternion algebra

Let $A=\mathbb{B}=M_2(\mathbb{C})$ and let $e=E_{11}$, $f=E_{22}$. The diagonal part is $D=\mathbb{C}e\oplus\mathbb{C}f\cong\mathbb{C}\times\mathbb{C}$; the off-diagonal part is $N=\mathbb{C}E_{12}\oplus\mathbb{C}E_{21}$. The commutator $\operatorname{ad}_e$ has eigenvalues $0,\pm1$, and its kernel is $D$, the centraliser of $e$. The example is the biquaternion case of *The Centraliser and the Diagonal Peirce Part* and *Off-Diagonal Peirce Components and Noncentral Idempotents*, read through the left and right multiplications; the diagonal part is the algebra of the two complex lines, and the off-diagonal part is the complement. The quaternion division algebra $\mathbb{H}$ itself has no nontrivial idempotent, so it has no such decomposition; the biquaternion algebra is the matrix model in which the idempotent exists.

## Summary

Left and right multiplication commute, and their product is the sandwich: $L_aR_b=R_bL_a=T_{a,b}$. For an idempotent $e$, the operators $L_e$ and $R_e$ are commuting idempotents whose joint eigenspaces are the four Peirce corners: $A_{00}$ with $(1,1)$, $A_{01}$ with $(1,0)$, $A_{10}$ with $(0,1)$, and $A_{11}$ with $(0,0)$. The diagonal Peirce part $D=A_{00}\oplus A_{11}$ is the kernel of the commutator $\operatorname{ad}_e=L_e-R_e$, the centraliser of $e$, and a subalgebra with identity $1$ isomorphic to $A_{00}\times A_{11}$. The off-diagonal part $N=A_{01}\oplus A_{10}$ is the image of $\operatorname{ad}_e$; the commutator acts as $+1$ on $A_{01}$ and $-1$ on $A_{10}$, and $\operatorname{ad}_e^2=P_N$, $P_D=I-L_e-R_e+2L_eR_e$. The decomposition $A=D\oplus N$ is a $\mathbb{Z}/2$-grading: $D$ is a subalgebra, $N$ is a $D$-bimodule, and $N^2\subseteq D$. For $d=d_0+d_1\in D$, the operators $L_d$ and $R_d$ preserve each corner and have block matrices $\operatorname{diag}(L_{d_0},L_{d_0},L_{d_1},L_{d_1})$ and $\operatorname{diag}(R_{d_0},R_{d_1},R_{d_0},R_{d_1})$; their restrictions to $D$ are the faithful left and right regular representations of $D$. The matrix algebra $M_2(k)$, the split algebra $k\times k$, the upper triangular algebra and the biquaternion algebra are the worked examples. The article uses no form, involution or topology.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_a,R_a$ | left and right multiplication by $a$ |
| $T_{a,b}=L_aR_b$ | the sandwich $x\mapsto axb$ |
| $e,f$ | idempotent and complement $f=1-e$ |
| $A_{ij}$ | the corner $e_iAe_j$, $e_0=e$, $e_1=f$ |
| $D=A_{00}\oplus A_{11}$ | the diagonal Peirce part |
| $N=A_{01}\oplus A_{10}$ | the off-diagonal part |
| $P_D,P_N$ | the projections onto $D$ and $N$ |
| $\operatorname{ad}_e=L_e-R_e$ | the commutator with $e$ |
| $P_e=L_eR_e$ | the projection onto $A_{00}$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce decomposition and the regular representations.
- Nathan Jacobson, *Basic Algebra II* (Freeman, 1989), for the left and right regular representations and the centraliser theorem.
- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, 1992), for the module-theoretic reading of the left and right multiplications.
- John Voight, *Quaternion Algebras* (Springer, 2021), for the biquaternion and split-quaternion examples and the absence of idempotents in the division quaternion algebra.
