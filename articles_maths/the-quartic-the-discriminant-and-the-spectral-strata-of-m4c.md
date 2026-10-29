# __The Quartic, the Discriminant and the Spectral Strata of $M_4(\mathbb{C})$__

## Introduction

Every element $A\in M_4(\mathbb{C})$ has a characteristic polynomial of degree four,

$$
\chi_A(t)=\det(tI-A)=t^{4}-c_1t^{3}+c_2t^{2}-c_3t+c_4,
$$

with $c_1=\operatorname{tr}A$, $c_2$ the second elementary symmetric function of the eigenvalues, $c_3$ the third and $c_4=\det A$. The four roots, counted with multiplicity, are the eigenvalues. The **discriminant** $\Delta$ is the product of the squared differences of the roots,

$$
\Delta=\prod_{1\le i<j\le 4}(\lambda_i-\lambda_j)^{2}.
$$

It vanishes exactly when two eigenvalues coincide, so it is the polynomial that detects the collision of the spectrum. This article computes $\Delta$ in the coefficients, reduces the quartic to its depressed form and solves it by the resolvent cubic, describes the five spectral strata by the multiplicity pattern and their dimensions, and reads the discriminant locus as the hypersurface where the spectral projectors cease to depend holomorphically on $A$.

The article is the degree-four member of the family *The Cubic, the Discriminant and the Spectral Strata of $M_3(\mathbb{C})$* and *The Quintic and the Spectral Strata of $M_5(\mathbb{C})$*. The general spectral theory, the Jordan form and the Dunford calculus are *Spectral Theory and the Spectral Projectors of $M_4(\mathbb{C})$*; the root case $H^{4}=I$ is *Roots of Unity and the Lagrange Idempotents of $M_4(\mathbb{C})$*. Nothing of those articles is reproved here.

## The Characteristic Quartic

**Definition.** For $A\in M_4(\mathbb{C})$ the characteristic polynomial is $\chi_A(t)=\det(tI-A)$, and its coefficients are

$$
c_1=e_1,\qquad c_2=e_2,\qquad c_3=e_3,\qquad c_4=e_4,
$$

the elementary symmetric functions of the four eigenvalues.

**Proposition (Newton's identities).** With $p_k=\operatorname{tr}A^{k}$,

$$
c_1=p_1,\qquad
c_2=\tfrac12\bigl(p_1^{2}-p_2\bigr),\qquad
c_3=\tfrac16\bigl(p_1^{3}-3p_1p_2+2p_3\bigr),
$$

and

$$
c_4=\tfrac1{24}\bigl(p_1^{4}-6p_1^{2}p_2+3p_2^{2}+8p_1p_3-6p_4\bigr).
$$

**Proof.** Expand $p_k=\sum_i\lambda_i^{k}$ in the elementary symmetric functions by Newton's recursion $p_k-e_1p_{k-1}+e_2p_{k-2}-\cdots+(-1)^{k-1}e_{k-1}p_1+(-1)^{k}ke_k=0$ for $k\le 4$, and solve for $e_k$. The four formulas are the solutions at $k=1,2,3,4$. The trace of $A^{k}$ is the power sum of the eigenvalues, so the identities hold for the matrix.

**The degree.** The coefficient $c_k$ is a polynomial of degree $k$ in the entries. The determinant $c_4$ has $24$ terms, and $c_2$ and $c_3$ are the sums of the principal minors of order two and three.

**Cayley–Hamilton.** $\chi_A(A)=0$, so every power $A^{n}$ with $n\ge4$ is a linear combination of $I,A,A^{2},A^{3}$, and $\mathbb{C}[A]$ has dimension at most four. The dimension is four exactly when the minimal polynomial has degree four, that is, when $A$ is cyclic.

**The trace and the determinant of the roots.** By Vieta,

$$
\sum_i\lambda_i=c_1,\qquad
\sum_{i<j}\lambda_i\lambda_j=c_2,\qquad
\sum_{i<j<k}\lambda_i\lambda_j\lambda_k=c_3,\qquad
\lambda_1\lambda_2\lambda_3\lambda_4=c_4.
$$

## The Discriminant

**Definition.** For a monic quartic with roots $\lambda_1,\dots,\lambda_4$, the **discriminant** is $\Delta=\prod_{i<j}(\lambda_i-\lambda_j)^{2}$.

**The depressed form.** Put $t=y+c_1/4$. The quartic becomes

$$
y^{4}+py^{2}+qy+r,
$$

with

$$
p=c_2-\tfrac38c_1^{2},\qquad
q=-c_3+\tfrac12c_1c_2-\tfrac18c_1^{3},\qquad
r=c_4-\tfrac14c_1c_3+\tfrac1{16}c_1^{2}c_2-\tfrac3{256}c_1^{4}.
$$

The cubic term is removed by the shift, and the discriminant is unchanged, because differences of roots are unchanged.

**Theorem (the discriminant of the depressed quartic).**

$$
\Delta=256r^{3}-128p^{2}r^{2}+144pq^{2}r-27q^{4}+16p^{4}r-4p^{3}q^{2}.
$$

**Proof.** The discriminant is the resultant of the quartic and its derivative, divided by the leading coefficient; for the depressed quartic the resultant is a polynomial in $p,q,r$ that is homogeneous of weighted degree $12$ when $p,q,r$ carry the weights $1,2,3$. The six monomials displayed are the monomials of that weighted degree that occur, and their coefficients are fixed by evaluation at six convenient quartics: $y^{4}-1$, $y^{4}+1$, $(y^{2}-1)^{2}$, $(y-1)^{4}$, $y^{4}+y$ and $y^{4}+y^{2}$. Each evaluation is a direct computation of the root differences, and the resulting linear system has the displayed solution. Equivalently, the formula is the standard discriminant of a quartic, written in the depressed variables.

**The general form.** Substituting $p,q,r$ in the theorem gives $\Delta$ as a polynomial in $c_1,\dots,c_4$ of degree six. In the entries of $A$ it is homogeneous of degree twelve, because $c_k$ has degree $k$ and every monomial of the displayed polynomial has weighted degree twelve.

| Quartic | $p,q,r$ | $\Delta$ |
|---|---|---|
| $y^{4}-1$ | $0,0,-1$ | $-256$ |
| $y^{4}+1$ | $0,0,1$ | $256$ |
| $(y^{2}-1)^{2}$ | $-2,0,1$ | $0$ |
| $(y-1)^{4}$ | $0,0,0$ | $0$ |
| $y^{4}+y$ | $0,1,0$ | $-27$ |

**The root case.** For $H$ with $H^{4}=I$ and simple spectrum, $\chi_H(t)=t^{4}-1$, so $c_1=c_2=c_3=0$, $c_4=-1$, and $\Delta=-256$. The four roots are $1,-1,i,-i$; the six differences are $2$, $1-i$, $1+i$, $-1-i$, $-1+i$ and $2i$, and the product of their squares is $-256$. The quartic of this article is the deformation of $t^{4}-1$ in which the four roots move independently.

**The vanishing.** $\Delta=0$ exactly when two roots coincide, because a product of squares vanishes exactly when one factor vanishes. The discriminant is therefore the equation of the **discriminant locus**, the set of matrices with a repeated eigenvalue.

## The Resolvent Cubic

**Definition.** For roots $\lambda_1,\dots,\lambda_4$ put

$$
z_1=(\lambda_1+\lambda_2)(\lambda_3+\lambda_4),\qquad
z_2=(\lambda_1+\lambda_3)(\lambda_2+\lambda_4),\qquad
z_3=(\lambda_1+\lambda_4)(\lambda_2+\lambda_3).
$$

The three numbers $z_k$ are the roots of the **resolvent cubic**.

**Theorem (the resolvent in the coefficients).** The resolvent cubic is

$$
z^{3}-2c_2z^{2}+\bigl(c_2^{2}+c_1c_3-4c_4\bigr)z-\bigl(c_3^{2}-c_1c_2c_3+c_1^{2}c_4\bigr)=0.
$$

In the depressed variables, where $c_1=0$, $c_2=p$, $c_3=-q$ and $c_4=r$, it reads

$$
z^{3}-2pz^{2}+\bigl(p^{2}-4r\bigr)z+q^{2}=0.
$$

**Proof.** The sum $z_1+z_2+z_3$ is twice the second elementary symmetric function, hence $2c_2$. The sum of the pairwise products and the product are computed by expanding in the roots and collecting the elementary symmetric functions; the expansions give $c_2^{2}+c_1c_3-4c_4$ and $c_3^{2}-c_1c_2c_3+c_1^{2}c_4$. The depressed form follows by substituting $c_1=0$, $c_2=p$, $c_3=-q$, $c_4=r$.

**The Ferrari reduction.** Put $t=y+c_1/4$ and suppose the depressed quartic split as

$$
y^{4}+py^{2}+qy+r=(y^{2}+uy+v)(y^{2}-uy+w).
$$

Comparing coefficients gives $v+w-u^{2}=p$, $u(w-v)=q$ and $vw=r$. Eliminating $v$ and $w$ gives

$$
u^{2}\bigl(u^{4}+2pu^{2}+p^{2}-4r\bigr)=q^{2},
$$

that is, $z=u^{2}$ is a root of the resolvent cubic. Conversely, every root $z$ of the resolvent with a square root $u$ produces a factorisation.

**The four roots.** Let $z_1,z_2,z_3$ be the roots of the resolvent and let $u_k$ be square roots with $u_1^{2}=-z_1$, $u_2^{2}=-z_2$, $u_3^{2}=-z_3$, chosen so that

$$
u_1u_2u_3=-\Bigl(c_3-\tfrac12c_1c_2+\tfrac18c_1^{3}\Bigr),
$$

the third elementary symmetric function of the shifted roots. Then the four roots of the quartic are

$$
\lambda=\frac{c_1}{4}+\frac12\bigl(u_1+u_2+u_3\bigr),\qquad
\lambda=\frac{c_1}{4}+\frac12\bigl(u_1-u_2-u_3\bigr),
$$

and

$$
\lambda=\frac{c_1}{4}+\frac12\bigl(-u_1+u_2-u_3\bigr),\qquad
\lambda=\frac{c_1}{4}+\frac12\bigl(-u_1-u_2+u_3\bigr).
$$

**Why the sign condition.** With $y_k$ the shifted roots, whose sum is zero, put $u_1=y_1+y_2$, $u_2=y_1+y_3$ and $u_3=y_1+y_4$. Then $u_k^{2}=(y_1+y_j)^{2}=-z_k$ for the three pairings, and $u_1u_2u_3$ is the elementary symmetric function $e_3(y)$. The four linear combinations displayed recover $y_1,y_2,y_3,y_4$. An arbitrary choice of the three square roots changes the product by a sign and permutes the four values, so the set of four roots is unchanged only when the product is the prescribed one.

**Solvability by radicals.** The reduction solves the quartic by two square roots and one cube root: the resolvent is a cubic, solved by Cardano, and each of its roots contributes a square root. The Galois group of a general quartic is $S_4$, of order $24$, solvable; the resolvent cubic distinguishes the transitive subgroups: $S_4$ when the resolvent is irreducible with non-square discriminant, $A_4$ when it is irreducible with square discriminant, $V_4$ when it splits completely, and $C_4$ or $D_4$ in the remaining cases.

## The Spectral Strata

**Definition.** Two matrices have the same **spectral type** when their eigenvalues have the same multiplicities. The type is a partition of $4$, written $1^{4}$, $2\,1\,1$, $2\,2$, $3\,1$ or $4$.

**Theorem (the five strata).** The sets of matrices of each type are locally closed algebraic subvarieties of $M_4(\mathbb{C})$. Each contains an open dense orbit, of the following complex dimension.

| Type | Multiplicities | Dimension | Codimension | Discriminant locus |
|---|---|---|---|---|
| $1^{4}$ | $1,1,1,1$ | $16$ | $0$ | no |
| $2\,1\,1$ | $2,1,1$ | $15$ | $1$ | yes |
| $2\,2$ | $2,2$ | $14$ | $2$ | yes |
| $3\,1$ | $3,1$ | $14$ | $2$ | yes |
| $4$ | $4$ | $13$ | $3$ | yes |

**Proof.** A matrix of type $1^{4}$ is determined up to conjugation by its four distinct eigenvalues, and the centraliser of a diagonalisable matrix with distinct eigenvalues is the torus $(\mathbb{C}^{\times})^{4}$ of dimension $4$; the orbit has dimension $16-4=12$, and the four eigenvalues add the missing four parameters. For a repeated type, the open dense orbit is the non-derogatory one, with minimal polynomial of degree four and centraliser $\mathbb{C}[A]$ of dimension $4$; the orbit has dimension $12$, and the distinct eigenvalues add the missing parameters. For $2\,1\,1$ the representative $\operatorname{diag}(J_2(a),b,c)$ with $a,b,c$ distinct has centraliser $\mathbb{C}[J_2]\oplus\mathbb{C}\oplus\mathbb{C}$, of dimension $4$, so the orbit has dimension $12$; the three distinct eigenvalues add three parameters, giving $15$. For $2\,2$ the representative $\operatorname{diag}(J_2(a),J_2(b))$ has centraliser of dimension $4$ and orbit dimension $12$; the two distinct eigenvalues add two parameters, giving $14$. For $3\,1$ the representative $\operatorname{diag}(J_3(a),b)$ has centraliser of dimension $4$ and orbit dimension $12$; the two distinct eigenvalues add two parameters, giving $14$. For $4$ the representative $J_4(a)$ has centraliser $\mathbb{C}[J_4]$, of dimension $4$, the orbit has dimension $12$, and the single eigenvalue adds one parameter, giving $13$. The smaller Jordan refinements lie in the closure and have larger centralisers. Each defining condition is the vanishing of a polynomial (the discriminant or its derivatives), so each stratum is locally closed.

**The centraliser.** The open dense orbit of every type has centraliser of dimension exactly $4$, because its minimal polynomial has degree four. The other Jordan refinements have larger centralisers; the scalar matrices, whose centraliser is the whole algebra of dimension $16$, are the extreme case in the type $4$ stratum.

**The refinements.** Inside the stratum of a single eigenvalue $a$, the Jordan type refines the picture: the types $4$, $3\,1$, $2\,2$, $2\,1\,1$ and $1^{4}$ at the same $a$ are the nilpotent orbits of the nilpotent cone of $M_4$, shifted by $aI$. Their dimensions are $12$, $10$, $8$, $6$ and $0$ in the nilpotent cone; at fixed $a$ these are the dimensions of the submanifolds, and allowing $a$ to vary adds one to each, giving $13$, $11$, $9$, $7$ and $1$.

**The closures and the incidence.** The stratum $1^{4}$ is open and dense, and every other stratum lies in its closure. The stratum $4$ lies in the closure of $3\,1$, which lies in the closure of $2\,1\,1$; the stratum $4$ also lies in the closure of $2\,2$. Both $2\,1\,1$ and $2\,2$ lie in the closure of $1^{4}$, and $2\,2$ lies in the closure of $2\,1\,1$ (the collision of the two single eigenvalues), but not conversely. The discriminant locus is the union of the four repeated strata, a hypersurface of degree six in the coefficients and of degree twelve in the entries.

**The spectral projectors.** On the stratum $1^{4}$ the four eigenvalues are distinct and the Lagrange projectors

$$
P_k=\prod_{l\ne k}\frac{A-\lambda_lI}{\lambda_k-\lambda_l}
$$

are polynomial in $A$ and depend holomorphically on $A$. On the discriminant locus the Lagrange formula degenerates: at a double root the two projectors have no individual limit, and only their sum, the Dunford projector of the repeated eigenvalue, is continuous. The limit is *Spectral Theory and the Spectral Projectors of $M_4(\mathbb{C})$*, where the Dunford calculus is stated.

## Summary

The characteristic quartic $t^{4}-c_1t^{3}+c_2t^{2}-c_3t+c_4$ is computed from the traces by Newton's identities. The discriminant is a polynomial of degree six in the coefficients and twelve in the entries; in the depressed variables it is $256r^{3}-128p^{2}r^{2}+144pq^{2}r-27q^{4}+16p^{4}r-4p^{3}q^{2}$, and it vanishes exactly on the locus of a repeated eigenvalue. The resolvent cubic reduces the quartic to two square roots and one cube root, with the sign condition $u_1u_2u_3=e_3(y)$. The spectrum stratifies the algebra into five types, of dimensions $16$, $15$, $14$, $14$ and $13$, with centraliser dimension four on the open dense orbit of every type and a Jordan refinement inside every repeated type. The root of unity $H^{4}=I$ is the case $t^{4}-1$, of discriminant $-256$.

| Quantity | Value for $M_4(\mathbb{C})$ |
|---|---|
| Degree of the characteristic polynomial | $4$ |
| Degree of the discriminant in the coefficients | $6$ |
| Degree of the discriminant in the entries | $12$ |
| Simple spectrum dimension | $16$ complex, $32$ real |
| One double root | $15$ complex, $30$ real |
| Two double roots | $14$ complex, $28$ real |
| Triple root and a simple root | $14$ complex, $28$ real |
| Quadruple root | $13$ complex, $26$ real |
| Centraliser of a non-scalar matrix | $4$ |
| Centraliser of a scalar | $16$ |
| Discriminant of $t^{4}-1$ | $-256$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\chi_A(t)$ | the characteristic polynomial $\det(tI-A)$ |
| $c_1,c_2,c_3,c_4$ | the elementary symmetric functions of the spectrum, $c_1=\operatorname{tr}A$, $c_4=\det A$ |
| $p_k$ | the power sum $\operatorname{tr}A^{k}$ |
| $p,q,r$ | the coefficients of the depressed quartic $y^{4}+py^{2}+qy+r$ |
| $\Delta$ | the discriminant $\prod_{i<j}(\lambda_i-\lambda_j)^{2}$ |
| $z_1,z_2,z_3$ | the roots of the resolvent cubic |
| $u_1,u_2,u_3$ | the square roots with $u_k^{2}=-z_k$ and $u_1u_2u_3=e_3(y)$ |
| $J_k(a)$ | the Jordan block of size $k$ at $a$ |
| $P_k$ | a Lagrange spectral projector |

## Further Reading

- [Spectral Theory and the Spectral Projectors of $M_4(\mathbb{C})$](spectral-theory-and-the-spectral-projectors-of-m4c.html), for the Jordan form, the resolvent and the Dunford calculus.
- [The Cubic, the Discriminant and the Spectral Strata of $M_3(\mathbb{C})$](the-cubic-the-discriminant-and-the-spectral-strata-of-m3c.html), for the degree-three analogue.
- [The Quintic and the Spectral Strata of $M_5(\mathbb{C})$](the-quintic-and-the-spectral-strata-of-m5c.html), for the degree-five analogue and the strata of $M_5$.
- [Roots of Unity and the Lagrange Idempotents of $M_4(\mathbb{C})$](roots-of-unity-and-the-lagrange-idempotents-of-m4c.html), for the root case $H^{4}=I$.
- [The Element, the Coordinates and the Trace of $M_4(\mathbb{C})$](the-element-the-coordinates-and-the-trace-of-m4c.html), for the coordinates and the Jordan decomposition.
- [The Adjoint Action, the Orbits and the Flag Variety of $M_4(\mathbb{C})$](the-adjoint-action-the-orbits-and-the-flag-variety-of-m4c.html), for the orbit–stabiliser reading.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the characteristic polynomial, the resolvent and the Jordan form.
- Igor R. Shafarevich, *Basic Algebraic Geometry 1* (Springer, 2013), for the strata of matrices of given Jordan type.
